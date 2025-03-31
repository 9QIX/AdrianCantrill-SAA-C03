# EC2 Bootstrapping with User Data

## Overview

This lesson focuses on bootstrapping an Amazon EC2 instance using **user data**. The goal is to automatically configure an EC2 instance during provisioning without creating a custom Amazon Machine Image (AMI). The lesson demonstrates setting up a WordPress installation on Amazon Linux 2023.

## Key Concepts

1. **Bootstrapping vs Custom AMI**

   - A custom AMI includes pre-configured settings but lacks flexibility for changes at launch.
   - Bootstrapping uses scripts executed at launch, allowing dynamic configuration.

2. **User Data**
   - User data allows execution of a script at instance startup to install and configure software.
   - The script includes package installations, service configurations, and application setup.

## Resources

- **CloudFormation Templates:**

  - [One-Click Deployment](https://console.aws.amazon.com/cloudformation/home?region=us-east-1#/stacks/create/review?templateURL=https://learn-cantrill-labs.s3.amazonaws.com/awscoursedemos/0010-aws-associate-ec2-bootstrapping-with-userdata/A4L_VPC.yaml&stackName=BOOTSTRAP)
  - [Supplementary Deployment](https://console.aws.amazon.com/cloudformation/home?region=us-east-1#/stacks/create/review?templateURL=https://learn-cantrill-labs.s3.amazonaws.com/awscoursedemos/0010-aws-associate-ec2-bootstrapping-with-userdata/A4L_VPC_PUBLICINSTANCE_AL2023.yaml&stackName=BOOTSTRAPCFN)

- **User Data & Commands:**
  - [Userdata.txt](https://learn-cantrill-labs.s3.amazonaws.com/awscoursedemos/0010-aws-associate-ec2-bootstrapping-with-userdata/userdata_AL2023.txt)
  - [Lesson Commands](https://learn-cantrill-labs.s3.amazonaws.com/awscoursedemos/0010-aws-associate-ec2-bootstrapping-with-userdata/lesson_commands.txt)

## Bootstrapping Script Explanation

### **User Data Script**

```bash
#!/bin/bash -xe

# STEP 1 - Set Database Credentials
DBName='a4lwordpress'
DBUser='a4lwordpress'
DBPassword='4n1m4l$4L1f3'
DBRootPassword='4n1m4l$4L1f3'

# STEP 2 - Install Required Packages
dnf install wget php-mysqlnd httpd php-fpm php-mysqli mariadb105-server php-json php php-devel cowsay -y

# STEP 3 - Enable and Start Web & Database Servers
systemctl enable httpd
systemctl enable mariadb
systemctl start httpd
systemctl start mariadb

# STEP 4 - Configure MariaDB Root Password
mysqladmin -u root password $DBRootPassword

# STEP 5 - Install WordPress
wget http://wordpress.org/latest.tar.gz -P /var/www/html
cd /var/www/html
tar -zxvf latest.tar.gz
cp -rvf wordpress/* .
rm -R wordpress latest.tar.gz

# STEP 6 - Configure WordPress
cp ./wp-config-sample.php ./wp-config.php
sed -i "s/'database_name_here'/'$DBName'/g" wp-config.php
sed -i "s/'username_here'/'$DBUser'/g" wp-config.php
sed -i "s/'password_here'/'$DBPassword'/g" wp-config.php

# STEP 6a - Set Permissions
usermod -a -G apache ec2-user
chown -R ec2-user:apache /var/www
chmod 2775 /var/www
find /var/www -type d -exec chmod 2775 {} \;
find /var/www -type f -exec chmod 0664 {} \;

# STEP 7 - Create WordPress Database
cat <<EOF > /tmp/db.setup
CREATE DATABASE $DBName;
CREATE USER '$DBUser'@'localhost' IDENTIFIED BY '$DBPassword';
GRANT ALL ON $DBName.* TO '$DBUser'@'localhost';
FLUSH PRIVILEGES;
EOF
mysql -u root --password=$DBRootPassword < /tmp/db.setup
rm /tmp/db.setup

# STEP 8 - Customize Login Message
cat <<EOF > /etc/update-motd.d/40-cow
#!/bin/sh
cowsay "Amazon Linux 2023 AMI - Animals4Life"
EOF
chmod 755 /etc/update-motd.d/40-cow
update-motd
```

### **Explanation of Key Steps**

1. **Database Setup:**

   - Defines credentials and root password for MariaDB.
   - Stores them in shell variables for later use.

2. **Software Installation:**

   - Installs required packages (Apache, PHP, MariaDB, and utilities like `cowsay`).

3. **Service Management:**

   - Enables and starts Apache & MariaDB so they persist across reboots.

4. **WordPress Installation:**

   - Downloads WordPress from the official site.
   - Extracts and moves files to `/var/www/html`.

5. **Configuration:**

   - Updates `wp-config.php` with the database details.
   - Adjusts ownership and permissions for security.

6. **Database Initialization:**

   - Creates the WordPress database and user with appropriate permissions.

7. **Custom Login Message:**
   - Uses `cowsay` to display a custom login message upon SSH connection.

## **AWS Console Steps**

1. **Deploy the VPC**

   - Use the CloudFormation one-click deployment link to create the VPC.
   - Wait for stack creation to complete.

2. **Launch EC2 Instance**

   - Go to EC2 console and click "Launch Instance".
   - Select **Amazon Linux 2023** and a free-tier eligible instance type.
   - Use the Animals4Life VPC and public subnet.
   - Enable auto-assign public IP.
   - Attach the existing security group from CloudFormation.
   - Paste the **user data script** under "Advanced Details".
   - Click "Launch" and wait for the instance to reach a running state.

3. **Verify Installation**
   - Use **EC2 Instance Connect** to SSH into the instance.
   - The custom `cowsay` banner should appear.
   - Copy the **public IP** from the AWS console and open it in a browser.
   - The WordPress setup page should load.

## **Metadata Service Commands**

### Retrieve Instance Metadata

```bash
TOKEN=$(curl -X PUT "http://169.254.169.254/latest/api/token" -H "X-aws-ec2-metadata-token-ttl-seconds: 21600")
curl -H "X-aws-ec2-metadata-token: $TOKEN" -v http://169.254.169.254/latest/meta-data/
```

### Retrieve User Data

```bash
curl -H "X-aws-ec2-metadata-token: $TOKEN" -v http://169.254.169.254/latest/user-data/
```

## **Troubleshooting Logs**

1. **Check Cloud-Init Logs**
   ```bash
   sudo cat /var/log/cloud-init.log
   sudo cat /var/log/cloud-init-output.log
   ```
2. **Ensure Services are Running**
   ```bash
   systemctl status httpd
   systemctl status mariadb
   ```

## **Conclusion**

This lesson demonstrated how to bootstrap an EC2 instance using user data to automatically configure WordPress. This approach is more flexible than a pre-configured AMI and allows dynamic modifications at launch time.
