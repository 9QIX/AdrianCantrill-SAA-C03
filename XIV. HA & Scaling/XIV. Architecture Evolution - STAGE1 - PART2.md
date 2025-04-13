# **Stage 1: Manual WordPress Installation on EC2**

### **Overview**

This stage demonstrates a **manual installation of WordPress** on a single EC2 instance using Amazon Linux 2023 (AL2023). The aim is to understand the complexities and pain points of manual deployment, which will be automated in later stages.

### **1. CloudFormation Launch (Pre-Step)**

Deploy a foundational VPC and EC2 environment using a one-click CloudFormation stack:

- [**CloudFormation Stack Link**](https://console.aws.amazon.com/cloudformation/home?region=us-east-1#/stacks/quickcreate?templateURL=https://learn-cantrill-labs.s3.amazonaws.com/aws-elastic-wordpress-evolution/A4LVPC.yaml&stackName=A4LVPC)

### **2. Connect to EC2 Instance**

Use **Session Manager** to connect without SSH keys:

```bash
sudo bash   # Elevate privileges
cd          # Navigate to home
clear       # Clean screen for clarity
```

### **3. Set Environment Variables from SSM Parameter Store**

These parameters (like DB credentials) are securely stored in AWS SSM and fetched as shell environment variables.

```bash
DBPassword=$(aws ssm get-parameters --region us-east-1 --names /A4L/Wordpress/DBPassword --with-decryption --query Parameters[0].Value)
DBPassword=`echo $DBPassword | sed -e 's/^"//' -e 's/"$//'`

DBRootPassword=$(aws ssm get-parameters --region us-east-1 --names /A4L/Wordpress/DBRootPassword --with-decryption --query Parameters[0].Value)
DBRootPassword=`echo $DBRootPassword | sed -e 's/^"//' -e 's/"$//'`

DBUser=$(aws ssm get-parameters --region us-east-1 --names /A4L/Wordpress/DBUser --query Parameters[0].Value)
DBUser=`echo $DBUser | sed -e 's/^"//' -e 's/"$//'`

DBName=$(aws ssm get-parameters --region us-east-1 --names /A4L/Wordpress/DBName --query Parameters[0].Value)
DBName=`echo $DBName | sed -e 's/^"//' -e 's/"$//'`

DBEndpoint=$(aws ssm get-parameters --region us-east-1 --names /A4L/Wordpress/DBEndpoint --query Parameters[0].Value)
DBEndpoint=`echo $DBEndpoint | sed -e 's/^"//' -e 's/"$//'`
```

**Explanation:**

- `aws ssm get-parameters` retrieves the values securely.
- `sed` is used to strip quotation marks for clean variable use.

### **4. Update OS & Install Prerequisites**

```bash
sudo dnf -y update
```

```bash
sudo dnf install wget php-mysqlnd httpd php-fpm php-mysqli mariadb105-server php-json php php-devel stress -y
```

**Explanation:**

- Installs **Apache**, **PHP**, **MariaDB**, and other libraries necessary for WordPress.

### **5. Enable & Start Web and DB Services**

```bash
sudo systemctl enable httpd
sudo systemctl enable mariadb
sudo systemctl start httpd
sudo systemctl start mariadb
```

**Explanation:**

- Enables services on boot.
- Starts them immediately.

### **6. Set MariaDB Root Password**

```bash
sudo mysqladmin -u root password $DBRootPassword
```

### **7. Download and Install WordPress**

```bash
sudo wget http://wordpress.org/latest.tar.gz -P /var/www/html
cd /var/www/html
sudo tar -zxvf latest.tar.gz
sudo cp -rvf wordpress/* .
sudo rm -R wordpress
sudo rm latest.tar.gz
```

**Explanation:**

- Downloads latest WordPress.
- Extracts and moves it to Apache’s root folder.

### **8. Configure WordPress**

```bash
sudo cp ./wp-config-sample.php ./wp-config.php
sudo sed -i "s/'database_name_here'/'$DBName'/g" wp-config.php
sudo sed -i "s/'username_here'/'$DBUser'/g" wp-config.php
sudo sed -i "s/'password_here'/'$DBPassword'/g" wp-config.php
```

**Explanation:**

- Prepares `wp-config.php` by replacing placeholders with real DB values.

### **9. Fix File System Permissions**

```bash
sudo usermod -a -G apache ec2-user
sudo chown -R ec2-user:apache /var/www
sudo chmod 2775 /var/www
sudo find /var/www -type d -exec chmod 2775 {} \;
sudo find /var/www -type f -exec chmod 0664 {} \;
```

**Explanation:**

- Ensures Apache can read/write web files.
- Prevents permission issues during uploads.

### **10. Create Database & WordPress User**

```bash
sudo echo "CREATE DATABASE $DBName;" >> /tmp/db.setup
sudo echo "CREATE USER '$DBUser'@'localhost' IDENTIFIED BY '$DBPassword';" >> /tmp/db.setup
sudo echo "GRANT ALL ON $DBName.* TO '$DBUser'@'localhost';" >> /tmp/db.setup
sudo echo "FLUSH PRIVILEGES;" >> /tmp/db.setup

sudo mysql -u root --password=$DBRootPassword < /tmp/db.setup
sudo rm /tmp/db.setup
```

**Explanation:**

- Creates DB and user.
- Grants necessary permissions.
- Executes SQL script through MariaDB CLI.

### **11. WordPress Initial Setup (Browser)**

1. Copy EC2 **Public IPv4 Address**.
2. Paste into browser (use **HTTP**, not HTTPS).
3. Complete WordPress setup wizard:
   - **Site Title:** Categoram
   - **Username:** admin
   - **Password:** animalsforlife
   - **Email:** dummy address
4. Click **Install WordPress**.
5. Log in using the credentials.

### **12. Create a Sample Post**

- Go to **Posts > Add New**
- Title: `Best Animals!`
- Add a **Gallery block**, upload images (cat, dog, etc.)
- Publish post
- View post

**Note:** Images are stored in `/wp-content/uploads`, metadata in MariaDB.

### **13. Architecture Limitations (Important)**

- **Manual Setup**: Tedious and error-prone.
- **Single Instance**: No decoupling of DB and app.
- **Local Storage**:
  - Images stored on instance (can't scale).
  - DB stored locally (risk of data loss).
- **No Load Balancing**: Public IP directly mapped to EC2 instance.
- **WordPress stores hardcoded IP**:
  - IP address saved in DB.
  - After EC2 stop/start (IP change), app fails to load.

### **14. Demonstrate IP Limitation**

- Stop instance → Public IP is lost.
- Start instance → New IP assigned.
- WordPress fails to load due to IP mismatch in DB.

### **15. Next Steps**

In **Stage 2**, this entire process will be **automated** using AWS services (like CloudFormation, Elastic Beanstalk, RDS, etc.).

### **References**

- [Lab Instructions – Stage 1](https://github.com/acantril/learn-cantrill-io-labs/blob/master/aws-elastic-wordpress-evolution/02_LABINSTRUCTIONS/STAGE1%20-%20Setup%20and%20Manual%20wordpress%20build.md)
- [Stage 1 Architecture (PDF)](https://github.com/acantril/learn-cantrill-io-labs/blob/master/aws-elastic-wordpress-evolution/02_LABINSTRUCTIONS/STAGE1%20-%20SINGLE%20SERVER%20MANUAL.pdf)
