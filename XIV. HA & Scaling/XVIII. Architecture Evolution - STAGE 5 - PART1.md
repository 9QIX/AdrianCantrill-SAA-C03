# Stage 5: Add an Application Load Balancer (ALB) and Auto Scaling Group (ASG)

**Objective**: Enhance the WordPress deployment by introducing elasticity using a Load Balancer and Auto Scaling Group. This enables automatic provisioning, health recovery, and decoupling traffic from individual instances.

## Architecture Overview

![alt text](./Images/image-21.png)

The infrastructure enhancement includes:

- **Application Load Balancer (ALB)** for routing HTTP traffic to WordPress instances.
- **Auto Scaling Group (ASG)** to scale instances based on load.
- **Launch Template** updated to:
  - Read the ALB DNS name from Parameter Store.
  - Update WordPress database with the ALB DNS.

Refer to the official [architecture diagram (PDF)](https://github.com/acantril/learn-cantrill-io-labs/blob/master/aws-elastic-wordpress-evolution/02_LABINSTRUCTIONS/STAGE5%20-%20ASG%20%26%20ALB.pdf) for a visual reference.

## Step-by-Step Breakdown

### 1. **Create the Load Balancer**

- Go to **EC2 Console > Load Balancers > Create Load Balancer**
- Select **Application Load Balancer**
- Name: `A4L-WordPress-ALB`
- Scheme: **Internet-facing**
- IP Address Type: **IPv4**
- **Select subnets** in 3 Availability Zones (1A, 1B, 1C), using public subnets:
  - `SN-HIF-PUB-A`, `SN-HIF-PUB-B`, `SN-HIF-PUB-C`
- **Security Group**: `A4LVPC-HIF-SG-LoadBalancer`
- **Listener settings**:
  - Protocol: HTTP
  - Port: 80
- **Target Group**:
  - Name: `A4L-WordPress-ALB-TG`
  - Target Type: Instances
  - Protocol: HTTP
  - Port: 80
  - VPC: `A4L-VPC`
  - Health Check Path: `/`
- **Do not register instances yet**
- Create the ALB and **copy its DNS name**.

### 2. **Add ALB DNS to Parameter Store**

Navigate to **Systems Manager > Parameter Store**:

- **Name**: `/A4L/WordPress/ALB/DNSNAME`
- **Description**: DNS name of the application load balancer for WordPress
- **Tier**: Standard
- **Type**: String
- **Value**: Paste the DNS name copied from the ALB

This allows EC2 instances to dynamically discover the ALB DNS.

### 3. **Update the Launch Template**

To ensure WordPress uses the ALB DNS as its **`siteurl`** and **`home`** URL:

#### a. Modify the Launch Template

- Go to **EC2 > Launch Templates**
- Select `WordPress Launch Template`
- Click **Actions > Modify Template (Create New Version)**
- **Template Description**:
  ```
  App only, uses EFS filesystem defined in /A4L/WordPress/EFSFSID, ALB home added to WP Database
  ```

#### b. Modify User Data

Under **Advanced Details > User Data**, locate the section starting with:

```bash
#!/bin/bash -xe
```

**Insert the following lines after this line**:

```bash
ALBDNSNAME=$(aws ssm get-parameters --region us-east-1 --names /A4L/WordPress/ALB/DNSNAME --query Parameters[0].Value)
ALBDNSNAME=`echo $ALBDNSNAME | sed -e 's/^"//' -e 's/"$//'`
```

These lines fetch the DNS name from Parameter Store and strip quotation marks.

#### c. At the bottom of the User Data, append this script:

```bash
cat >> /home/ec2-user/update_wp_ip.sh<< 'EOF'
#!/bin/bash
source <(php -r 'require("/var/www/html/wp-config.php"); echo("DB_NAME=".DB_NAME."; DB_USER=".DB_USER."; DB_PASSWORD=".DB_PASSWORD."; DB_HOST=".DB_HOST); ')
SQL_COMMAND="mysql -u $DB_USER -h $DB_HOST -p$DB_PASSWORD $DB_NAME -e"
OLD_URL=$(mysql -u $DB_USER -h $DB_HOST -p$DB_PASSWORD $DB_NAME -e 'select option_value from wp_options where option_name = "siteurl";' | grep http)

ALBDNSNAME=$(aws ssm get-parameters --region us-east-1 --names /A4L/WordPress/ALB/DNSNAME --query Parameters[0].Value)
ALBDNSNAME=`echo $ALBDNSNAME | sed -e 's/^"//' -e 's/"$//'`

$SQL_COMMAND "UPDATE wp_options SET option_value = replace(option_value, '$OLD_URL', 'http://$ALBDNSNAME') WHERE option_name = 'home' OR option_name = 'siteurl';"
$SQL_COMMAND "UPDATE wp_posts SET guid = replace(guid, '$OLD_URL','http://$ALBDNSNAME');"
$SQL_COMMAND "UPDATE wp_posts SET post_content = replace(post_content, '$OLD_URL', 'http://$ALBDNSNAME');"
$SQL_COMMAND "UPDATE wp_postmeta SET meta_value = replace(meta_value,'$OLD_URL','http://$ALBDNSNAME');"
EOF

chmod 755 /home/ec2-user/update_wp_ip.sh
echo "/home/ec2-user/update_wp_ip.sh" >> /etc/rc.local
/home/ec2-user/update_wp_ip.sh
```

### Script Explanation

#### Line by Line:

```bash
source <(php -r 'require("/var/www/html/wp-config.php"); echo("DB_NAME=".DB_NAME."; DB_USER=".DB_USER."; DB_PASSWORD=".DB_PASSWORD."; DB_HOST=".DB_HOST); ')
```

- Extracts DB credentials from WordPress `wp-config.php`

```bash
SQL_COMMAND="mysql -u $DB_USER -h $DB_HOST -p$DB_PASSWORD $DB_NAME -e"
```

- Defines reusable command for executing SQL on WordPress DB

```bash
OLD_URL=$(mysql -u $DB_USER -h $DB_HOST -p$DB_PASSWORD $DB_NAME -e 'select option_value from wp_options where option_name = "siteurl";' | grep http)
```

- Extracts the current WordPress site URL from the database

```bash
ALBDNSNAME=$(aws ssm get-parameters ...)
ALBDNSNAME=`echo $ALBDNSNAME | sed -e 's/^"//' -e 's/"$//'`
```

- Retrieves the DNS name of the ALB and formats it

```bash
$SQL_COMMAND "UPDATE wp_options SET option_value = replace(...) WHERE option_name = 'home' OR option_name = 'siteurl';"
```

- Replaces old IP-based URL with the ALB DNS in `wp_options`

Other similar SQL updates:

- Update GUID in `wp_posts`
- Update post content URLs
- Update postmeta values

```bash
chmod 755 ...
echo "... >> /etc/rc.local"
```

- Makes the script executable
- Ensures it runs on instance start

### 4. **Finalize Launch Template Version**

- Click **Create Template Version**
- Go back to **Launch Templates**
- Select the launch template, click **Actions > Set Default Version**
- Set **Version 4** as the default

## Summary

At this point:

- WordPress uses a **load balancer** for handling traffic
- **Instances scale automatically** based on demand
- ALB DNS is dynamically injected into the app via **SSM Parameter Store**
- WordPress database is **automatically updated** on launch to reflect correct URLs
