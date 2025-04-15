# Stage 3 – Add RDS and Update the Launch Template

## Architecture Overview

![alt text](./Images/image-19.png)

In this stage, we migrate the WordPress database from the EC2 instance to a dedicated **Amazon RDS** instance. This separation enables independent scaling of the application and the database layer and ensures data persistence even if the EC2 instance is terminated.

> **Key Benefits:**
>
> - Independent scalability of web server and database.
> - Data persistence across EC2 lifecycles.
> - Prerequisite for future scaling via ASG (Auto Scaling Group).

## Step-by-Step Implementation

### 1. **Create RDS Subnet Group**

A **DB Subnet Group** allows RDS to select subnets for placing database instances across multiple Availability Zones (AZs).

#### Steps:

- Go to **RDS Console → Subnet Groups → Create DB Subnet Group**
- Name: `wordpress-rds-subnet-group`
- Description: `RDS Subnet Group for WordPress`
- VPC: `A4L-VPC`
- Availability Zones: `us-east-1a`, `us-east-1b`, `us-east-1c`
- Subnets:
  - `10.16.16.0/20` (AZ A)
  - `10.16.80.0/20` (AZ B)
  - `10.16.14.0/20` (AZ C)

### 2. **Launch RDS Instance**

#### Steps:

- RDS Console → Databases → Create Database
- Choose **Standard Create**
- Engine: **MySQL**
- Version: Use version mentioned in lesson instructions
- Template: **Free Tier**
- DB Identifier: `a4lwordpress`
- Master Username/Password:
  - Get values from **SSM Parameter Store**
    - `/a4lwordpress/dbuser`
    - `/a4lwordpress/dbpassword`
- Instance type: `db.t3.micro`
- VPC: `A4L-VPC`
- Subnet Group: `wordpress-rds-subnet-group`
- Public Access: **No**
- Security Group: `a4lvpc-sg-database`
- AZ Preference: `us-east-1a`
- Initial DB Name:
  - From Parameter Store: `/a4lwordpress/dbname`

### 3. **Export Local MariaDB Data from EC2**

#### Connect to EC2 via Session Manager:

```bash
sudo bash
cd
clear
```

#### Load DB Parameters into Environment Variables:

```bash
export DBUSER=$(aws ssm get-parameter --name "/a4lwordpress/dbuser" --query "Parameter.Value" --output text)
export DBPASSWORD=$(aws ssm get-parameter --name "/a4lwordpress/dbpassword" --with-decryption --query "Parameter.Value" --output text)
export DBNAME=$(aws ssm get-parameter --name "/a4lwordpress/dbname" --query "Parameter.Value" --output text)
export DBENDPOINT=localhost
```

#### Export Database:

```bash
mysqldump -h $DBENDPOINT -u $DBUSER -p$DBPASSWORD $DBNAME > a4lwordpress.sql
```

### 4. **Update DB Endpoint Parameter in SSM**

> Important: Delete the old parameter and recreate it with the new RDS endpoint.

#### Steps:

- Copy RDS endpoint from console
- In **Systems Manager → Parameter Store**:
  - Delete: `/a4lwordpress/dbendpoint`
  - Recreate with:
    - Name: `/a4lwordpress/dbendpoint`
    - Type: `String`
    - Value: _RDS Endpoint_

### 5. **Import Data into RDS**

#### Reload Environment Variables:

```bash
export DBENDPOINT=$(aws ssm get-parameter --name "/a4lwordpress/dbendpoint" --query "Parameter.Value" --output text)
```

#### Import SQL Dump:

```bash
mysql -h $DBENDPOINT -u $DBUSER -p$DBPASSWORD $DBNAME < a4lwordpress.sql
```

### 6. **Reconfigure WordPress to Use RDS**

#### Update `wp-config.php` to use the RDS endpoint:

```bash
sed -i "s/localhost/$DBENDPOINT/" /var/www/html/wp-config.php
```

> This updates WordPress to use the new RDS backend instead of local MariaDB.

### 7. **Verify Migration**

- Open the WordPress site in a browser (using the EC2 public IP).
- Confirm that the blog and posts still load as expected.
- Data is now served from **RDS**, while media files remain on EC2 (`wp-content`).

### 8. **Update the Launch Template**

> Modify the launch template so that any new EC2 instances are preconfigured to use **RDS**, not MariaDB.

#### Steps:

- EC2 Console → Launch Templates → Select Template → Actions → Modify Template (Create new version)
- Description: `Single Server App Only`
- Expand **Advanced Details → User Data**

#### In the **User Data Script**, perform the following:

- **REMOVE**:
  ```bash
  systemctl enable mariadb
  systemctl start mariadb
  mysqladmin ...
  ```
- **REMOVE MariaDB DB setup block**:
  ```bash
  echo "CREATE DATABASE $DBNAME;"
  ...
  rm /tmp/db.setup
  ```

#### Finalize:

- Click **Create Template Version**

## Final Outcome

At the end of this stage:

- WordPress is running with **data hosted on Amazon RDS**
- The EC2 launch template is updated to reflect this new architecture
- We’re ready to scale using Auto Scaling in later stages

Let me know if you'd like this turned into a GitHub README, or if you want help with **Stage 4** next.
