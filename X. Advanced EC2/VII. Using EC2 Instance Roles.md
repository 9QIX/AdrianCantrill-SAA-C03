# Using EC2 Instance Roles Demo

## Overview

This document provides a comprehensive summary of the lesson on AWS EC2 instance roles, IAM roles, and temporary security credentials. It also includes detailed explanations of relevant AWS CLI commands and JSON policy documents.

## 1-Click Deployment

To quickly deploy the necessary AWS infrastructure for this lesson, use the following CloudFormation link:

[1-Click Deployment](https://console.aws.amazon.com/cloudformation/home?region=us-east-1#/stacks/create/review?templateURL=https://learn-cantrill-labs.s3.amazonaws.com/awscoursedemos/0011-aws-associate-ec2-instance-role/A4L_VPC_PUBLICINSTANCE_ROLEDEMO.yaml&stackName=IAMROLEDEMO)

This will create:

- A VPC
- An EC2 instance
- An S3 bucket

## AWS IAM Instance Roles

An **instance role** is an IAM role that an EC2 instance can assume. It allows the instance to obtain temporary security credentials.

### JSON IAM Role Policy

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

#### Explanation:

- **Effect**: `Allow` - Grants permission for the action.
- **Action**: `sts:AssumeRole` - Allows the EC2 service to assume the role.
- **Principal**: Specifies `ec2.amazonaws.com` as the trusted entity.

## Accessing EC2 Instance Metadata

You can retrieve instance metadata using the following command:

```sh
curl http://169.254.169.254/latest/meta-data/iam/security-credentials/
```

### Example Output:

```
a4linstancerole
```

This confirms that the role `a4linstancerole` is associated with the instance.

### Retrieving Temporary Credentials

```sh
curl http://169.254.169.254/latest/meta-data/iam/security-credentials/a4linstancerole
```

#### Example Output:

```json
{
  "Code": "Success",
  "LastUpdated": "2025-03-31T09:06:59Z",
  "Type": "AWS-HMAC",
  "AccessKeyId": "ASIAUZPNLGF6EEXEFFOU",
  "SecretAccessKey": "<hidden>",
  "Token": "<hidden>",
  "Expiration": "2025-03-31T15:42:31Z"
}
```

#### Explanation:

- **AccessKeyId & SecretAccessKey**: Temporary credentials used to authenticate AWS API requests.
- **Token**: Session token required for authentication.
- **Expiration**: Credentials have a limited validity period.

## Listing S3 Buckets

```sh
aws s3 ls
```

#### Example Output:

```
2025-03-31 08:57:26 iamroledemo-s3bucket-wcxouaslb1ry
```

This confirms that the EC2 instance, via its IAM role, can list S3 buckets.

## AWS CLI Credential Precedence

Credentials can be configured in multiple ways. The AWS CLI follows this order of precedence:

1. **Command Line Options**: Overrides all other configurations (e.g., `--region`, `--output`, `--profile`).
2. **Environment Variables**: Stored in system variables.
3. **Assume Role**: IAM role assumed by `aws configure` or `aws sts assume-role`.
4. **AWS IAM Identity Center (SSO)**: Configured with `aws configure sso`.
5. **Credentials File**: Located at `~/.aws/credentials`.
6. **Configuration File**: Located at `~/.aws/config`.
7. **Container Credentials**: Assigned to Amazon ECS tasks.
8. **EC2 Instance Profile Credentials**: Provided through EC2 metadata service.

## Attaching an IAM Role to an EC2 Instance

1. Navigate to the **AWS EC2 Console**.
2. Select the **EC2 instance**.
3. Click on **Security** → **Modify IAM Role**.
4. Select the role **a4linstancerole**.
5. Click **Save**.
6. Confirm that the role is attached in the **Security** tab.

## Using IAM Roles for Secure Authentication

Instead of manually configuring credentials, EC2 instance roles allow applications running on an instance to authenticate securely using the metadata service. This eliminates the need for long-term access keys.

## Key Takeaways

- **IAM roles** provide temporary credentials for EC2 instances.
- **Metadata service** allows retrieval of IAM credentials.
- **Best practice**: Use instance roles instead of hardcoding credentials.
- **AWS CLI follows a specific precedence order** when choosing credentials.

For more details, refer to the [AWS CLI Credential Configuration Guide](https://docs.aws.amazon.com/cli/latest/userguide/cli-configure-quickstart.html#cli-configure-quickstart-precedence).
