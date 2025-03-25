# Learn Cantrill.io AWS SA C03 - WordPress Deployment on EC2

## Resources

- **1-Click Deployment**: [AWS CloudFormation Stack](https://console.aws.amazon.com/cloudformation/home?region=us-east-1#/stacks/create/review?templateURL=https://learn-cantrill-labs.s3.amazonaws.com/awscoursedemos/0006-aws-associate-ec2-wordpress-on-ec2/A4L_VPC_PUBLICINSTANCE_AL2023.yaml&stackName=WORDPRESS)
- **Lesson Commands**: [Lesson Commands File](https://learn-cantrill-labs.s3.amazonaws.com/awscoursedemos/0006-aws-associate-ec2-wordpress-on-ec2/lesson_commands_AL2023.txt)
- **Blog Images**: [Blog Images Zip](https://learn-cantrill-labs.s3.amazonaws.com/awscoursedemos/0006-aws-associate-ec2-wordpress-on-ec2/blogimages.zip)

## Overview

This lesson details the manual installation of WordPress on an AWS EC2 instance. It covers setting up the WordPress configuration, configuring the database, and verifying the setup. The lesson emphasizes the drawbacks of manual installation and introduces automation concepts for future lessons.

## Step 6 - Configure WordPress

### Commands:

```bash
sudo cp ./wp-config-sample.php ./wp-config.php
sudo sed -i "s/'database_name_here'/'$DBName'/g" wp-config.php
sudo sed -i "s/'username_here'/'$DBUser'/g" wp-config.php
sudo sed -i "s/'password_here'/'$DBPassword'/g" wp-config.php
sudo chown apache:apache * -R
```

### Explanation:

1. **Copy the sample configuration file:**

   ```bash
   sudo cp ./wp-config-sample.php ./wp-config.php
   ```

   - Copies `wp-config-sample.php` to `wp-config.php`, making it the active configuration file for WordPress.

2. **Modify the configuration file:**

   ```bash
   sudo sed -i "s/'database_name_here'/'$DBName'/g" wp-config.php
   ```

   - Replaces `'database_name_here'` with the actual database name stored in `$DBName`.
   - The `-i` flag modifies the file in place.

   ```bash
   sudo sed -i "s/'username_here'/'$DBUser'/g" wp-config.php
   ```

   - Replaces `'username_here'` with the actual database username stored in `$DBUser`.

   ```bash
   sudo sed -i "s/'password_here'/'$DBPassword'/g" wp-config.php
   ```

   - Replaces `'password_here'` with the actual database password stored in `$DBPassword`.

3. **Set file ownership to Apache:**
   ```bash
   sudo chown apache:apache * -R
   ```
   - Changes ownership of all files in the directory to the Apache web server user and group.
   - Ensures that the web server has proper permissions to access and modify files.

## Step 7 - Create WordPress Database

### Commands:

```bash
echo "CREATE DATABASE $DBName;" >> /tmp/db.setup
echo "CREATE USER '$DBUser'@'localhost' IDENTIFIED BY '$DBPassword';" >> /tmp/db.setup
echo "GRANT ALL ON $DBName.* TO '$DBUser'@'localhost';" >> /tmp/db.setup
echo "FLUSH PRIVILEGES;" >> /tmp/db.setup
mysql -u root --password=$DBRootPassword < /tmp/db.setup
sudo rm /tmp/db.setup
```

### Explanation:

1. **Create a temporary database setup script:**

   ```bash
   echo "CREATE DATABASE $DBName;" >> /tmp/db.setup
   ```

   - Appends the SQL command to create the database to `/tmp/db.setup`.

2. **Create a new database user:**

   ```bash
   echo "CREATE USER '$DBUser'@'localhost' IDENTIFIED BY '$DBPassword';" >> /tmp/db.setup
   ```

   - Creates a new MySQL user with the specified credentials.

3. **Grant privileges to the new user:**

   ```bash
   echo "GRANT ALL ON $DBName.* TO '$DBUser'@'localhost';" >> /tmp/db.setup
   ```

   - Grants all permissions on the WordPress database to the new user.

4. **Flush privileges to apply changes:**

   ```bash
   echo "FLUSH PRIVILEGES;" >> /tmp/db.setup
   ```

   - Ensures that the privilege changes take effect.

5. **Execute the setup script:**

   ```bash
   mysql -u root --password=$DBRootPassword < /tmp/db.setup
   ```

   - Runs the SQL commands in `/tmp/db.setup` using the root database user.

6. **Remove the setup script:**
   ```bash
   sudo rm /tmp/db.setup
   ```
   - Deletes the setup file for security reasons.

## Step 8 - Access WordPress

- Navigate to `http://your_instance_public_ipv4_ip` in a web browser.
- The WordPress installation wizard should appear.

### Installation Steps:

1. Choose **English (United States)**.
2. Enter a **blog title** (e.g., "All the Cats").
3. Set the **admin username** to `admin`.
4. Copy and save the **generated password**.
5. Provide an **email address** (e.g., `test@test.com`).
6. Click **Install WordPress**.
7. Log in using the **admin** username and the copied password.

### Verify Installation:

- Click **"All the Cats"** at the top.
- Click **"Visit Site"** to confirm the WordPress blog is live.

## Conclusion

This lesson covered manually installing WordPress on an EC2 instance, configuring the database, and setting up the application. It demonstrated how manual deployment is error-prone and time-consuming, highlighting the need for automation.

### Next Steps:

- **Automation with AWS CloudFormation:** Future lessons will introduce automated deployment using AWS CloudFormation and other infrastructure as code tools.
- **Amazon Machine Images (AMI):** The course will guide the creation of pre-configured AMIs for faster deployment.
- **Further AWS services:** The course will explore scalable and efficient AWS architectures beyond a single EC2 instance.

To clean up resources, navigate to the AWS Console, go to **CloudFormation**, select the **WordPress stack**, and delete it.

## Final Thoughts

This lesson provided hands-on experience with setting up WordPress manually, understanding Linux commands, MySQL database management, and AWS EC2 configurations. Future lessons will transition to automated deployments to streamline infrastructure management.
