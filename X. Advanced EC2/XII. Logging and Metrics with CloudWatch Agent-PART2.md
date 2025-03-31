# CloudWatch Agent Setup - PART 2

## Overview

This guide covers the setup and configuration of Amazon CloudWatch Agent on an EC2 instance using AWS Systems Manager (SSM) and IAM roles. The process includes installing the agent, configuring it for log and metric collection, and verifying its functionality in CloudWatch.

## Prerequisites

- AWS account with necessary permissions
- EC2 instance (Amazon Linux 2023)
- IAM Role with required policies
- AWS CLI installed and configured

## Step 1: Install CloudWatch Agent

Run the following command to install the CloudWatch agent on the EC2 instance:

```sh
sudo dnf install amazon-cloudwatch-agent
```

## Step 2: Create an IAM Role

1. Navigate to IAM in the AWS Console.
2. Create a new IAM role with type **EC2 Role**.
3. Attach the following managed policies:
   - `CloudWatchAgentServerPolicy`
   - `AmazonSSMFullAccess`
4. Name the role `CloudWatchRole`.
5. Attach the role to the EC2 instance.

### IAM Role JSON Definition

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

## Step 3: Configure CloudWatch Agent

Run the configuration wizard:

```sh
sudo /opt/aws/amazon-cloudwatch-agent/bin/amazon-cloudwatch-agent-config-wizard
```

- Accept all defaults until **default metrics**.
- Choose **advanced** metrics collection.
- Specify log files to monitor:
  1. `/var/log/secure`
  2. `/var/log/httpd/access_log`
  3. `/var/log/httpd/error_log`
- Accept **default instance ID** and **default retention option**.
- Save the configuration to SSM (default name).
- Configuration file location: `/opt/aws/amazon-cloudwatch-agent/bin/config.json`.

## Step 4: Fix Missing Dependencies

Before starting the agent, create necessary files:

```sh
sudo mkdir -p /usr/share/collectd/
sudo touch /usr/share/collectd/types.db
```

## Step 5: Start CloudWatch Agent

Fetch the stored configuration and start the agent:

```sh
sudo /opt/aws/amazon-cloudwatch-agent/bin/amazon-cloudwatch-agent-ctl -a fetch-config -m ec2 -c ssm:AmazonCloudWatch-linux -s
```

## Step 6: Verify Logs in CloudWatch

1. Open **AWS Console** → **CloudWatch**.
2. Navigate to **Log Groups**.
3. Look for:
   - `/var/log/secure`
   - `/var/log/httpd/access_log`
   - `/var/log/httpd/error_log`
4. Open logs and verify entries.
5. If logs are missing:
   - Visit the EC2 instance in AWS Console.
   - Copy the **public IPv4 address**.
   - Open it in a browser to generate access logs.
   - Refresh CloudWatch Logs.

## Step 7: Monitor Metrics in CloudWatch

1. Navigate to **CloudWatch** → **Metrics**.
2. Look for the **CWAgent namespace**.
3. Select relevant metrics:
   - CPU Utilization
   - Disk Read/Write Operations
   - Network Traffic
4. Visualize the collected metrics.

## Step 8: Cleanup

To remove all resources created:

1. **Detach IAM Role**:
   - Go to **EC2 Console** → Select Instance → Security → Modify IAM Role → Remove `CloudWatchRole`.
2. **Delete IAM Role**:
   - Go to **IAM Console** → Roles → Delete `CloudWatchRole`.
3. **Delete CloudWatch Log Groups**:
   - Remove logs for `/var/log/secure`, `/var/log/httpd/access_log`, `/var/log/httpd/error_log`.
4. **Delete CloudFormation Stack**:
   - Navigate to **CloudFormation Console**.
   - Delete the `CWAGENT` stack.
5. **Leave SSM Parameter Store value** (can be used in future lessons).

## Additional Resources

- [1-Click Deployment](https://console.aws.amazon.com/cloudformation/home?region=us-east-1#/stacks/create/review?templateURL=https://learn-cantrill-labs.s3.amazonaws.com/awscoursedemos/0013-aws-associate-ec2-cwagent/A4L_VPC_PUBLIC_Wordpress_AL2023.yaml&stackName=CWAGENT)
- [Lesson Commands](https://learn-cantrill-labs.s3.amazonaws.com/awscoursedemos/0013-aws-associate-ec2-cwagent/lesson_commands_AL2023.txt)

---

This guide provides step-by-step instructions for configuring CloudWatch Agent on an EC2 instance, monitoring logs and metrics, and properly cleaning up resources afterward. Ensure all steps are completed for a successful implementation.
