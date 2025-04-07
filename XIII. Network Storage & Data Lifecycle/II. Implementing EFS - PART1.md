# Implementing EFS on EC2 (Part 1)

## Overview

This lesson walks through a **hands-on demo** of **Amazon Elastic File System (EFS)**, giving practical experience in provisioning infrastructure, creating an EFS file system, setting network configurations, and preparing mount targets.

## Prerequisites & Setup

### Resources

[1-Click Deployement](https://console.aws.amazon.com/cloudformation/home?region=us-east-1#/stacks/create/review?templateURL=https://learn-cantrill-labs.s3.amazonaws.com/awscoursedemos/0019-aws-associate-storage-implementing-efs/A4L_TWO_EFS_EC2_AL2023.yaml&stackName=IMPLEMENTINGEFS)

### 1. AWS Management Account

- Ensure you're logged into the **Management (General) AWS Account**.
- Region: **US East (N. Virginia)**.

### 2. Launch Stack

- Use the **One-Click CloudFormation Deployment** link provided in the course.
- Go to the **Quick Create Stack** screen.
- Scroll down, **check the Capabilities box**, and click **Create Stack**.

### 3. Open Command Reference

- Open the provided **Lesson Commands Document** in a new tab for CLI references (placeholders like `FileSystemID` will be filled in during the lesson).

## Infrastructure Provisioned

After the stack reaches **Create Complete**:

- A VPC named `animals-for-life` is created.
- Two EC2 instances are deployed:
  - `a4l-efs-instance-a`
  - `a4l-efs-instance-b`

These instances will later mount the EFS file system for demonstration.

## EFS Console & File System Creation

### Navigate to EFS Console

- Open the EFS service in a **new tab**.
- Keep the EC2 tab open for later access.

### Create File System (Initial Setup)

You have two options:

- **Simple Wizard** (limited customization)
- **Customize** (recommended for full control)

### Customizing EFS

#### File System Basics

- **Name**: `a4l-efs`
- **VPC**: `animals-for-life`

#### Storage Class

- **Standard** (multi-AZ replication for high durability)
- **One Zone** (single AZ – for dev/test environments)

> In this demo, choose **Standard** to simulate production-ready configuration.

#### Backup

- AWS Backup integration (enabled/disabled)
- For this demo: **Disable backups**

#### Lifecycle Management

Move unused files to Infrequent Access (IA) storage:

- Files **not accessed for 30 days** → IA
- Files **accessed again** → back to Standard

> Select **"Transition out on first access"** to automatically bring files back to Standard.

#### Throughput & Performance

- **Throughput Mode**: `Bursting` (automatic scaling with usage)
- **Performance Mode**: `General Purpose` (default, for most cases)
  - Use `Max IO` only for high-performance parallel workloads

#### Encryption

- EFS supports **encryption at rest** using **KMS**.
- In production: Enable it and assign a KMS key.
- For this demo: **Disable encryption**

> Permissions are needed on both EFS and the KMS key when encryption is enabled.

#### Tags

- Skip tagging for demo purposes.

Click **Next** to continue.

## Network Configuration (Mount Targets)

### Mount Targets by AZ

Best practice: Create mount targets in **each AZ** where the service is consumed.

In this demo:

- **AZs**: `us-east-1a`, `us-east-1b`, `us-east-1c`
- **Subnets**:
  - `us-east-1a` → `app-a`
  - `us-east-1b` → `app-b`
  - `us-east-1c` → `app-c`

### Security Groups

- Remove default security group associations.
- Assign **`instance security group`** (provisioned by CloudFormation).
  - This SG allows communication between instances and mount targets.

Assign it to **all three** mount targets.

## File System Policies (Optional)

Options (disabled in this demo but useful in production):

- Prevent root access
- Enforce read-only access
- Prevent anonymous access
- Enforce **encryption in transit**

For this demo: **Skip all policy configurations**.

## Final Steps

### Review & Create

- Review all configurations.
- Click **Create** to provision the file system and mount targets.

### Wait for Mount Targets

- Navigate to the file system details → **Network** tab.
- Wait for **all three mount targets** to show as **"Available"**.

## What's Next?

This concludes **Part 1** of the EFS demo.

Once all mount targets are ready, proceed to **Part 2**, where you'll:

- Mount EFS to EC2 instances
- Interact with the shared file system
- Execute commands to demonstrate networked file access
