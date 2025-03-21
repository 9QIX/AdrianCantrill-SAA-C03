# EC2 Instance Connect vs SSH

## Overview

This lesson provides a practical demonstration of two different methods for connecting to an EC2 instance:

- **EC2 Instance Connect**
- **SSH with a local client**

Both methods are used to establish remote access to EC2 instances, whether using IPv4 or IPv6.

## Prerequisites

- Logged in as an IAM admin user in the AWS management account
- AWS region set to **Northern Virginia (us-east-1)**
- A key pair named **A4L.pem** (or an existing key pair)

## 1-Click Deployment

A CloudFormation stack is provided for quick deployment. Use the following link to create the stack:

[CloudFormation Quick Create](https://us-east-1.console.aws.amazon.com/cloudformation/home?region=us-east-1#/stacks/quickcreate?templateURL=https://learn-cantrill-labs.s3.amazonaws.com/awscoursedemos/0021-aws-associate-ec2-instance-connect-vs-ssh/A4L_VPC_PUBLICINSTANCE_AL2023.yaml&stackName=EC2INSTANCECONNECTvsSSH)

After deployment, an EC2 instance will be available with public access.

## Connecting to EC2 Using SSH

1. **Locate Your Private Key:** Ensure you have the private key (`A4L.pem`).
2. **Set Key Permissions:** Run the following command to restrict access to the key file:
   ```sh
   chmod 400 A4L.pem
   ```
3. **Connect Using SSH:** Use the provided public DNS of the instance:
   ```sh
   ssh -i "A4L.pem" ec2-user@ec2-3-92-32-119.compute-1.amazonaws.com
   ```
4. **Verify SSH Connection:** If prompted, confirm the connection by typing `yes`.

## Security Group Rules

### **Inbound Rules**

| Rule ID               | Port | Protocol | Source    | Description     |
| --------------------- | ---- | -------- | --------- | --------------- |
| sgr-0282019bc9954bcda | 22   | TCP      | 0.0.0.0/0 | Allow SSH IPv4  |
| sgr-0a4646b91669ad6f5 | 80   | TCP      | 0.0.0.0/0 | Allow HTTP IPv4 |
| sgr-09ba1978a7d41af80 | 22   | TCP      | ::/0      | Allow SSH IPv6  |

### **Outbound Rules**

| Rule ID               | Port | Protocol | Destination |
| --------------------- | ---- | -------- | ----------- |
| sgr-09389b3d5736b3544 | All  | All      | ::/0        |
| sgr-03001beb0129b3b8f | All  | All      | 0.0.0.0/0   |

## Connecting Using EC2 Instance Connect

1. Go to **EC2 Console** > **Instances**.
2. Select the instance and click **Connect**.
3. Choose **EC2 Instance Connect** and click **Connect**.
4. A terminal session will open in the browser.

### Key Differences from SSH

- Does not require a key pair.
- Uses **AWS IAM permissions** instead of local credentials.
- More secure for managed access.

## Adjusting Security Group for Restricted SSH Access

To restrict SSH access:

1. Go to **EC2 Console** > **Instances** > **Security**.
2. Edit the inbound rule for SSH (`port 22`):
   - Remove `0.0.0.0/0`.
   - Set **Source** to `My IP`.
3. Save the rule and test connectivity.

## Summary of Findings

- **SSH with a key pair** provides traditional access but requires key management.
- **EC2 Instance Connect** simplifies access, removing key pair dependency.
- Adjusting security groups helps secure remote access by restricting SSH to specific IPs.
- For production, **EC2 Instance Connect** is preferred due to security and ease of access management.
