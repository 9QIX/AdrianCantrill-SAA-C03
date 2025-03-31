# AWS Solutions Architect - Associate (SAA-C03) - Learn Cantrill.io Summary

## Lesson: EC2 Bootstrapping with User Data

### Overview

This lesson covers how to use **EC2 User Data** to automate instance configuration during launch. The lesson demonstrates both **manual user data** entry and **CloudFormation automation** to bootstrap an EC2 instance with WordPress installed.

## Resources

- **1-Click Deployment:** [CloudFormation Stack](https://console.aws.amazon.com/cloudformation/home?region=us-east-1#/stacks/create/review?templateURL=https://learn-cantrill-labs.s3.amazonaws.com/awscoursedemos/0010-aws-associate-ec2-bootstrapping-with-userdata/A4L_VPC.yaml&stackName=BOOTSTRAP)
- **User Data Script:** [userdata.txt](https://learn-cantrill-labs.s3.amazonaws.com/awscoursedemos/0010-aws-associate-ec2-bootstrapping-with-userdata/userdata_AL2023.txt)
- **Lesson Commands:** [lesson_commands.txt](https://learn-cantrill-labs.s3.amazonaws.com/awscoursedemos/0010-aws-associate-ec2-bootstrapping-with-userdata/lesson_commands.txt)
- **Supplementary 1-Click Deployment (CloudFormation - Part 2):** [CloudFormation Stack](https://console.aws.amazon.com/cloudformation/home?region=us-east-1#/stacks/create/review?templateURL=https://learn-cantrill-labs.s3.amazonaws.com/awscoursedemos/0010-aws-associate-ec2-bootstrapping-with-userdata/A4L_VPC_PUBLICINSTANCE_AL2023.yaml&stackName=BOOTSTRAPCFN)

## Steps to Automate EC2 Configuration with User Data

### 1. Define Database Credentials

```bash
DBName='a4lwordpress'
DBUser='a4lwordpress'
DBPassword='4n1m4l$4L1f3'
DBRootPassword='4n1m4l$4L1f3'
```

- These variables store database credentials used later in the script.

### 2. Install Required Software Packages

```bash
dnf install wget php-mysqlnd httpd php-fpm php-mysqli mariadb105-server php-json php php-devel cowsay -y
```

- **dnf install**: Installs necessary packages, including:
  - Apache Web Server (`httpd`)
  - MariaDB (`mariadb105-server`)
  - PHP and required extensions
  - `cowsay` (for fun login banner)

### 3. Enable and Start Services

```bash
systemctl enable httpd
systemctl enable mariadb
systemctl start httpd
systemctl start mariadb
```

- Ensures that **Apache** and **MariaDB** start automatically on boot.

### 4. Set Database Root Password

```bash
mysqladmin -u root password $DBRootPassword
```

- Sets the root password for MariaDB.

### 5. Download and Install WordPress

```bash
wget http://wordpress.org/latest.tar.gz -P /var/www/html
cd /var/www/html
tar -zxvf latest.tar.gz
cp -rvf wordpress/* .
rm -R wordpress
rm latest.tar.gz
```

- Downloads and extracts WordPress files into `/var/www/html`.

### 6. Configure WordPress

```bash
cp ./wp-config-sample.php ./wp-config.php
sed -i "s/'database_name_here'/'$DBName'/g" wp-config.php
sed -i "s/'username_here'/'$DBUser'/g" wp-config.php
sed -i "s/'password_here'/'$DBPassword'/g" wp-config.php
```

- Copies **wp-config-sample.php** to **wp-config.php** and updates database credentials.

### 7. Set Permissions

```bash
usermod -a -G apache ec2-user
chown -R ec2-user:apache /var/www
chmod 2775 /var/www
find /var/www -type d -exec chmod 2775 {} \;
find /var/www -type f -exec chmod 0664 {} \;
```

- Grants the `ec2-user` permission to manage web files.

### 8. Create WordPress Database

```bash
echo "CREATE DATABASE $DBName;" >> /tmp/db.setup
echo "CREATE USER '$DBUser'@'localhost' IDENTIFIED BY '$DBPassword';" >> /tmp/db.setup
echo "GRANT ALL ON $DBName.* TO '$DBUser'@'localhost';" >> /tmp/db.setup
echo "FLUSH PRIVILEGES;" >> /tmp/db.setup
mysql -u root --password=$DBRootPassword < /tmp/db.setup
sudo rm /tmp/db.setup
```

- Creates the WordPress database, user, and grants permissions.

### 9. Custom Login Banner (Cowsay)

```bash
echo "#!/bin/sh" > /etc/update-motd.d/40-cow
echo 'cowsay "Amazon Linux 2023 AMI - Animals4Life"' >> /etc/update-motd.d/40-cow
chmod 755 /etc/update-motd.d/40-cow
update-motd
```

- Adds a **cowsay** message to appear when users log into the instance.

## CloudFormation Integration

### Automating EC2 with CloudFormation

- Instead of manually adding user data, **CloudFormation** can launch EC2 instances with user data encoded in **Base64**.
- The template automates the deployment process and removes manual setup.

### Accessing Instance Metadata

```bash
TOKEN=`curl -X PUT "http://169.254.169.254/latest/api/token" -H "X-aws-ec2-metadata-token-ttl-seconds: 21600"`
curl -H "X-aws-ec2-metadata-token: $TOKEN" -v http://169.254.169.254/latest/meta-data/
curl -H "X-aws-ec2-metadata-token: $TOKEN" -v http://169.254.169.254/latest/user-data/
```

- Retrieves EC2 instance metadata securely using a token.

## Cleanup Steps

1. **Terminate Manual EC2 Instance**
   - In the EC2 console, locate **a4l-manual WordPress**, right-click and select **Terminate**.
2. **Delete CloudFormation Stacks**
   - In the CloudFormation console, delete **bootstrap-cfn** and **bootstrap** stacks.

## Summary

- **Manual Bootstrapping:** Used EC2 **User Data** to install WordPress during instance launch.
- **CloudFormation Automation:** Used **Base64-encoded** user data for instance provisioning.
- **Best Practices:**
  - Automate infrastructure provisioning using **CloudFormation**.
  - Securely retrieve instance metadata.
  - Cleanup resources to avoid unnecessary costs.

This lesson provides a strong foundation in **EC2 bootstrapping** and **CloudFormation automation** for deploying AWS infrastructure efficiently.
