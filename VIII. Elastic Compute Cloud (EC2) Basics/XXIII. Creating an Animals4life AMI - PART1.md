# Creating an Animals4life AMI - PART1

## Overview

This lesson covers the process of manually installing WordPress on an Amazon EC2 instance running Amazon Linux 2023. It also includes creating an Amazon Machine Image (AMI) with a pre-configured WordPress installation and a customized login banner.

## Prerequisites

- AWS Account with appropriate permissions.
- AWS region set to **us-east-1 (Northern Virginia)**.
- Access to the AWS Management Console.
- Basic familiarity with Linux command-line operations.

## One-Click Deployment

To quickly deploy the required AWS infrastructure, use the following CloudFormation template:

[1-Click Deployment](https://console.aws.amazon.com/cloudformation/home?region=us-east-1#/stacks/create/review?templateURL=https://learn-cantrill-labs.s3.amazonaws.com/awscoursedemos/0007-aws-associate-ec2-ami-demo/A4L_VPC_PUBLICINSTANCE_AL2023.yaml&stackName=AMIDEMO)

## Steps to Install and Configure WordPress

### Step 1: Set Authentication Variables

Define environment variables to be used throughout the installation.

```sh
DBName='a4lwordpress'
DBUser='a4lwordpress'
DBPassword='4n1m4l$L1f3'
DBRootPassword='4n1m4l$L1f3'
```

### Step 2: Install System Software

Install required packages including MariaDB, Apache, and PHP.

```sh
sudo dnf install wget php-mysqlnd httpd php-fpm php-mysqli mariadb105-server php-json php php-devel -y
```

### Step 3: Enable and Start Web & Database Services

```sh
sudo systemctl enable httpd
sudo systemctl enable mariadb
sudo systemctl start httpd
sudo systemctl start mariadb
```

### Step 4: Set MariaDB Root Password

```sh
sudo mysqladmin -u root password $DBRootPassword
```

### Step 5: Download and Extract WordPress

```sh
sudo wget http://wordpress.org/latest.tar.gz -P /var/www/html
cd /var/www/html
sudo tar -zxvf latest.tar.gz
sudo cp -rvf wordpress/* .
sudo rm -R wordpress
sudo rm latest.tar.gz
```

### Step 6: Configure WordPress

```sh
sudo cp ./wp-config-sample.php ./wp-config.php
sudo sed -i "s/'database_name_here'/'$DBName'/g" wp-config.php
sudo sed -i "s/'username_here'/'$DBUser'/g" wp-config.php
sudo sed -i "s/'password_here'/'$DBPassword'/g" wp-config.php
sudo chown apache:apache * -R
```

### Step 7: Create WordPress Database and User

```sh
echo "CREATE DATABASE $DBName;" >> /tmp/db.setup
echo "CREATE USER '$DBUser'@'localhost' IDENTIFIED BY '$DBPassword';" >> /tmp/db.setup
echo "GRANT ALL ON $DBName.* TO '$DBUser'@'localhost';" >> /tmp/db.setup
echo "FLUSH PRIVILEGES;" >> /tmp/db.setup
mysql -u root --password=$DBRootPassword < /tmp/db.setup
sudo rm /tmp/db.setup
```

### Step 8: Access WordPress Installation Page

Open a browser and navigate to:

```
http://your_instance_public_ipv4_ip
```

You should see the WordPress installation page. Do not proceed with the installation yet.

### Step 9: Customize Login Banner with Cowsay

Install **cowsay** for a custom login message.

```sh
sudo dnf install -y cowsay
cowsay "oh hi"
```

Create a custom message for users logging into the instance:

```sh
sudo nano /etc/update-motd.d/40-cow
```

Add the following content:

```sh
#!/bin/sh
cowsay "Amazon Linux 2023 AMI - Animals4Life"
```

Set permissions and apply the changes:

```sh
sudo chmod 755 /etc/update-motd.d/40-cow
sudo update-motd
sudo reboot
```

After reboot, log in again to see the new login banner.

## Creating an Amazon Machine Image (AMI)

### Step 1: Navigate to EC2 in AWS Console

1. Go to **EC2 Dashboard**.
2. Select the running **A4L Public EC2 instance**.
3. Click on **Actions > Image and Templates > Create Image**.
4. Provide a name and description.
5. Click **Create Image**.

### Step 2: Verify the AMI

1. Navigate to **AMIs** in the EC2 Dashboard.
2. Locate the newly created AMI and verify its status.

## Summary

This guide covered setting up an EC2 instance, installing WordPress, configuring the database, setting up a custom login banner, and creating an AMI for reuse.

### Additional Resources

- [Lesson Commands](https://learn-cantrill-labs.s3.amazonaws.com/awscoursedemos/0007-aws-associate-ec2-ami-demo/lesson_commands_AL2023.txt)
