# AWS RDS Provisioning & Migration

This lesson walks through how to provision an Amazon RDS instance and migrate data from a self-managed MariaDB (on EC2) to RDS. It is part of a series of demos in which a simple WordPress application is used to demonstrate evolving database architectures on AWS.

## Overview

You will learn to:

- Provision an Amazon RDS database (MySQL Community Edition)
- Migrate a WordPress blog’s data from EC2-hosted MariaDB to RDS
- Configure networking and security via subnet groups and VPC security groups
- Understand infrastructure deployed by CloudFormation for the demo

## Prerequisites

- Logged into the **AWS Management Account**
- Use the **Northern Virginia (us-east-1)** region
- Launch infrastructure via the **one-click CloudFormation stack** (linked in lesson)
- Open the **lesson commands document** (linked in lesson) for terminal commands

## Initial Setup

1. **Launch CloudFormation Stack**  
   Use the one-click link. Stack name is prefilled (`migrate-to-rds`).  
   Just check the _capabilities_ checkbox and click **Create Stack**.

2. **Wait for "CREATE_COMPLETE"**  
   This will provision:
   - EC2 Instance: `a4l-wordpress` (WordPress + Apache)
   - EC2 Instance: `a4l-db-wordpress` (MariaDB)

## Create & Configure WordPress Blog

1. **Open WordPress Setup**

   - Copy the **public IPv4** of `a4l-wordpress`
   - Open in browser (http, **not** https)

2. **Setup Form**

   - Site title: `The Best Cats`
   - Username: `admin`
   - Password: from CloudFormation `Parameters` tab (`animals4life` password)
   - Email: `test@test.com`

3. **Create Blog Post**
   - Login > Posts > Trash default post
   - Create new post:
     - Title: `The Best Cats Ever`
     - Add Gallery Block
     - Upload 4 images (from downloadable zip)
     - Publish the post

This data is now stored on the **EC2-hosted MariaDB** instance.

## Provisioning RDS Instance

### Step 1: Create a Subnet Group

RDS uses **DB subnet groups** to determine which subnets it can launch databases into.

1. Go to RDS > **Subnet Groups**
2. Create DB Subnet Group:
   - Name & Description: `a4l-sn-group`
   - VPC: `a4l-vpc1`
   - Availability Zones: `us-east-1a`, `us-east-1b`, `us-east-1c`
   - Subnets:
     - Find subnets with CIDRs ending in `.16`, `.80`, `.144`
     - These match `SN-DBA`, `SN-DBB`, `SN-DBC`

> ✅ **Note**: Use VPC Console to confirm subnet CIDRs if needed.

### Step 2: Launch RDS Instance

Go to RDS > Databases > Create Database

#### Engine & Template

- Engine: **MySQL** (Community Edition)
- Template: **Free Tier**

#### Configuration

- DB Identifier: `a4l-wordpress`
- Master Username: `a4l-wordpress`
- Password: Same `animals4life` password

#### DB Instance Class

- Type: `db.t3.micro` (or free-tier equivalent)

#### Storage

- Allocated: `20 GB`
- Disable auto-scaling

#### Connectivity

- VPC: `a4l-vpc1`
- DB Subnet Group: `a4l-sn-group`
- Public Access: **No**
- Security Group: Use existing (or create new) that allows MySQL access from WordPress instance

> 🔒 Security: WordPress EC2 instance must be able to access RDS on port `3306`. Ensure the security group allows this.

## Key AWS Concepts Explained

### CloudFormation

Used to launch all demo infrastructure with a single click. Deploys:

- EC2 (MariaDB)
- EC2 (WordPress)
- Networking components

### Subnet Groups

- Inform RDS which subnets it may use within a VPC.
- Required for multi-AZ deployments, read replicas, or Aurora clusters.

### RDS Engine Types

- **MySQL**: Used in demo
- **Aurora**: AWS’s own engine (MySQL/Postgres compatible)
- **Oracle/MSSQL**: Commercial engines (license required)

### Templates

- **Production**, **Dev/Test**, **Free Tier**
- Adjust available instance types and features (e.g. Multi-AZ)

## Notes on Versions & Compatibility

- RDS engine versions may change.
- Always refer to the **lesson description** for the recommended version.
- Aurora snapshots & imports may require specific version compatibility.

## Summary

You have:

- Deployed a WordPress app with a MariaDB backend
- Created a sample blog post
- Prepared the environment for migrating the data to Amazon RDS

Next steps (in upcoming lessons) will include:

- Database migration commands
- Backups, restores
- Adding high availability with Multi-AZ
