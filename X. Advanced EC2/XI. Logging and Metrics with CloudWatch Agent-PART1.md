# CloudWatch Agent Setup - PART 1

## Overview

This guide covers the installation and configuration of the Amazon CloudWatch agent on an EC2 instance. The goal is to capture and inject log data from three different log files into CloudWatch Logs while also providing access to additional system metrics.

## Prerequisites

- AWS account with appropriate permissions
- EC2 instance running Amazon Linux 2023
- IAM role with required policies
- CloudFormation stack deployment

## Step 1: Deploy Infrastructure

### 1-Click Deployment

Use the following CloudFormation stack deployment link:
[CloudFormation Stack Deployment](https://console.aws.amazon.com/cloudformation/home?region=us-east-1#/stacks/create/review?templateURL=https://learn-cantrill-labs.s3.amazonaws.com/awscoursedemos/0013-aws-associate-ec2-cwagent/A4L_VPC_PUBLIC_Wordpress_AL2023.yaml&stackName=CWAGENT)

Wait for the stack to reach the `CREATE_COMPLETE` status before proceeding.

## Step 2: Connect to EC2 Instance

1. Navigate to **EC2 Console** → Click **Instances** → Locate the instance named `A4L_WordPress`.
2. Select the instance → Click **Connect**.
3. Use **EC2 Instance Connect** with the username `ec2-user`.
4. Verify connection by checking for the Animals for Life custom login banner.

## Step 3: Install CloudWatch Agent

Execute the following command to install the CloudWatch agent:

```sh
sudo dnf install amazon-cloudwatch-agent
```

This installs the agent but does not start it.

## Step 4: Create and Attach IAM Role

### Create IAM Role

1. Navigate to **IAM Console** → Click **Roles** → **Create Role**.
2. Select **AWS Service** → Choose **EC2** → Click **Next**.
3. Attach the following managed policies:
   - `CloudWatchAgentServerPolicy`
   - `AmazonSSMFullAccess`
4. Name the role `CloudWatchRole` and click **Create Role**.

### Attach IAM Role to EC2 Instance

1. Go to **EC2 Console** → Select the instance.
2. Click **Security** → **Modify IAM Role**.
3. Select `CloudWatchRole` → Click **Update IAM Role**.

## Step 5: Configure CloudWatch Agent

Run the configuration wizard:

```sh
sudo /opt/aws/amazon-cloudwatch-agent/bin/amazon-cloudwatch-agent-config-wizard
```

Accept default values until **default metrics**, then choose `Advanced` (option 3).

### Log File Configuration

| Log File Path               | Log Group Name              | Log Stream Name |
| --------------------------- | --------------------------- | --------------- |
| `/var/log/secure`           | `/var/log/secure`           | Instance ID     |
| `/var/log/httpd/access_log` | `/var/log/httpd/access_log` | Instance ID     |
| `/var/log/httpd/error_log`  | `/var/log/httpd/error_log`  | Instance ID     |

Store the configuration in **SSM Parameter Store** with the default name `AmazonCloudWatch-linux`.

The configuration file is stored at:

```sh
/opt/aws/amazon-cloudwatch-agent/bin/config.json
```

## Step 6: Fix Common Issues

Run the following commands to ensure the agent starts correctly:

```sh
sudo mkdir -p /usr/share/collectd/
sudo touch /usr/share/collectd/types.db
```

## Step 7: Load Configuration and Start Agent

```sh
sudo /opt/aws/amazon-cloudwatch-agent/bin/amazon-cloudwatch-agent-ctl -a fetch-config -m ec2 -c ssm:AmazonCloudWatch-linux -s
```

## Step 8: Cleanup

### Delete Resources

1. Delete the CloudFormation stack.
2. Optionally leave the SSM Parameter Store value.
3. Delete the CloudWatch log groups for:
   - `/var/log/secure`
   - `/var/log/httpd/access_log`
   - `/var/log/httpd/error_log`
4. Remove the `CloudWatchRole` IAM role.

## IAM Role JSON Definition

```json
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Action": ["sts:AssumeRole"],
      "Principal": {
        "Service": ["ec2.amazonaws.com"]
      }
    }
  ]
}
```

## Additional Resources

- [Lesson Commands](https://learn-cantrill-labs.s3.amazonaws.com/awscoursedemos/0013-aws-associate-ec2-cwagent/lesson_commands_AL2023.txt)
- [AWS CloudWatch Documentation](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/WhatIsCloudWatch.html)
