# WordPress Installation on AWS EC2

## Overview

This lesson demonstrates the manual installation of WordPress on an AWS EC2 instance. The purpose is to understand the challenges of manual deployment before transitioning to automated methods.

## Resources

- **1-Click Deployment**: [AWS CloudFormation Stack](https://console.aws.amazon.com/cloudformation/home?region=us-east-1#/stacks/create/review?templateURL=https://learn-cantrill-labs.s3.amazonaws.com/awscoursedemos/0006-aws-associate-ec2-wordpress-on-ec2/A4L_VPC_PUBLICINSTANCE_AL2023.yaml&stackName=WORDPRESS)
- **Lesson Commands**: [Download Commands](https://learn-cantrill-labs.s3.amazonaws.com/awscoursedemos/0006-aws-associate-ec2-wordpress-on-ec2/lesson_commands_AL2023.txt)
- **Blog Images**: [Download Images](https://learn-cantrill-labs.s3.amazonaws.com/awscoursedemos/0006-aws-associate-ec2-wordpress-on-ec2/blogimages.zip)

### **Learning Objectives**

- Understand a typical application stack installation.
- Deploy WordPress manually on AWS EC2.
- Recognize the limitations of manual installation.
- Prepare for automation and best practices.

## **Architecture Overview**

- Single EC2 instance with a **monolithic** architecture.
- WordPress application and database on the same instance.
- Deployed into a **public subnet** of a VPC.
- No high availability.

## **Steps to Set Up WordPress Manually**

### **1. Preparation**

1. Log into the AWS **management account**.
2. Select the **Northern Virginia region** (us-east-1).
3. Use the **one-click deployment** link to create the base infrastructure.
4. Wait for the stack to reach the `CREATE_COMPLETE` state.
5. Open the **lesson commands document** containing all required commands.

### **2. Connecting to EC2**

1. Navigate to **EC2 Dashboard**.
2. Locate the instance named `A4L-Public-EC2`.
3. Right-click on the instance and select **Connect**.
4. Use **EC2 Instance Connect** with `ec2-user`.

### **3. Setting Up Environment Variables**

Before installation, define essential variables:

```sh
DB_NAME='wordpress'
DB_USER='admin'
DB_PASSWORD='securepassword'
DB_ROOT_PASSWORD='rootpassword'
```

To verify variables:

```sh
echo $DB_NAME
```

### **4. Installing Required Software**

Install necessary packages using `dnf`:

```sh
sudo dnf install -y mariadb-server httpd wget
```

### **5. Starting Services**

Enable and start services to ensure persistence after a reboot:

```sh
sudo systemctl enable httpd mariadb
sudo systemctl start httpd mariadb
```

### **6. Configuring the Database**

Set the **root password** for MariaDB:

```sh
sudo mysqladmin -u root password "$DB_ROOT_PASSWORD"
```

### **7. Downloading and Extracting WordPress**

Move to the **web root directory** and download WordPress:

```sh
cd /var/www/html
sudo wget https://wordpress.org/latest.tar.gz
```

Extract and move files:

```sh
sudo tar -zxvf latest.tar.gz
sudo cp -r wordpress/* .
```

Cleanup unnecessary files:

```sh
sudo rm -rf wordpress latest.tar.gz
```

### **8. Next Steps**

- Configure WordPress (`wp-config.php` setup in the next part).
- Automate this setup using AWS services (e.g., **CloudFormation, Ansible, Terraform**).

## **Conclusion**

This lesson serves as a foundation to compare manual and automated installation methods. By understanding the complexity of manual deployment, we can better appreciate the benefits of automation in AWS.
