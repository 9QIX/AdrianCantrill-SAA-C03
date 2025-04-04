# Migrating WordPress Database from EC2 (MariaDB) to RDS

## Overview

This lesson covers the end-to-end process of migrating a WordPress site that uses a MariaDB database on an EC2 instance to Amazon RDS. It includes provisioning the RDS instance, securing connectivity, backing up and restoring data, and reconfiguring WordPress to use the new RDS database.

## Resources

- **CloudFormation One-Click Deployment**  
  [Launch Stack](https://console.aws.amazon.com/cloudformation/home?region=us-east-1#/stacks/create/review?templateURL=https://learn-cantrill-labs.s3.amazonaws.com/awscoursedemos/0015-aws-associate-rds-migrating-to-rds/A4L_WORDPRESS_AND_EC2DB_AL2023.yaml&stackName=MIGRATE2RDS)

- **Lesson Commands**  
  [lesson_commands.txt](https://learn-cantrill-labs.s3.amazonaws.com/awscoursedemos/0015-aws-associate-rds-migrating-to-rds/lesson_commands.txt)

- **Blog Images**  
  [blog_images.zip](https://learn-cantrill-labs.s3.amazonaws.com/awscoursedemos/0015-aws-associate-rds-migrating-to-rds/blog_images.zip)

## Key Concepts Covered

### 1. **Understanding RDS Configuration**

- Each RDS instance has an **endpoint** and **port**.
- Deployed within a **VPC** using a defined **subnet group**.
- Requires proper **security group rules** for EC2 instances to access it.

### 2. **Security Group Configuration**

1. Navigate to the RDS security group.
2. Add a new **inbound rule**:
   - **Type:** MySQL/Aurora
   - **Source:** EC2 instance security group from the WordPress stack
3. Save changes – this allows EC2-hosted WordPress to communicate with the RDS instance.

## Backup and Restore Process

### Step 1: Back Up the Existing EC2 MariaDB

```bash
mysqldump -h PRIVATEIPOFMARIADBINSTANCE -u a4lwordpress -p a4lwordpress > a4lwordpress.sql
```

**Explanation:**

- `mysqldump` — command to export a database.
- `-h PRIVATEIPOFMARIADBINSTANCE` — replace with private IP of the EC2 DB.
- `-u a4lwordpress` — database username.
- `-p` — prompts for password.
- `a4lwordpress` — database name.
- `> a4lwordpress.sql` — output redirected to a file.

### Step 2: Restore to the RDS Instance

```bash
mysql -h CNAMEOFRDSINSTANCE -u a4lwordpress -p a4lwordpress < a4lwordpress.sql
```

**Explanation:**

- `mysql` — command-line tool to import the SQL dump.
- `-h CNAMEOFRDSINSTANCE` — replace with RDS endpoint.
- `-u`, `-p`, and db name — same credentials used above.
- `< a4lwordpress.sql` — input from backup file.

## Step 3: Update WordPress Configuration

Navigate to WordPress directory:

```bash
cd /var/www/html
```

Edit the config:

```bash
sudo nano wp-config.php
```

Replace the DB host line:

**From:**

```php
define('DB_HOST', 'PRIVATEIPOFMARIADBINSTANCE');
```

**To:**

```php
define('DB_HOST', 'REPLACEME_WITH_RDSINSTANCEENDPOINTADDRESS');
```

Save and exit:

- `Ctrl + O` then `Enter` (write)
- `Ctrl + X` (exit)

## Step 4: Verification

1. Visit your WordPress site using the **public IP of the EC2 WordPress instance**.
2. If the site loads correctly, it's still functioning.
3. Stop the **original EC2 MariaDB instance**.
4. Refresh the WordPress site:
   - If it still loads, WordPress is now using the **RDS database**.

## Cleanup Steps

Because RDS was provisioned manually (outside of CloudFormation), you’ll need to manually delete resources:

### 1. **Delete RDS Instance**

- In the RDS Console:
  - Select DB instance → **Actions → Delete**
  - Opt out of final snapshot and backups
  - Type **`delete me`** to confirm

### 2. **Delete Subnet Group**

- Navigate to **RDS > Subnet Groups**
- Select the subnet group created earlier → **Delete**

### 3. **Delete Security Group**

- Go to **VPC Console > Security Groups**
- Delete the custom security group used for RDS

### 4. **Delete CloudFormation Stack**

- Navigate to **CloudFormation Console**
- Select the stack used in the 1-click deployment → **Delete**

## Summary of What You Learned

- Created and configured an **RDS instance** manually.
- Adjusted **VPC and security group settings** to allow EC2 access.
- **Backed up** a MariaDB EC2 database.
- **Restored** the backup into RDS.
- Updated WordPress config to point to RDS.
- Verified successful migration by shutting down the original database.
- Learned the importance of **automating infrastructure** using CloudFormation.
- Performed **manual cleanup** of AWS resources.

## What's Next?

In upcoming lessons, you will:

- Automate the creation of RDS.
- Learn more about backup, restore, and scaling.
- Enhance the WordPress architecture to make it **highly available and elastic**.
