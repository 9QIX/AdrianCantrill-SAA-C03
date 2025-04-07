# AWS Backup

## Overview

**AWS Backup** is a **fully managed backup and restore service** that centralizes and automates data protection across AWS services, both in-cloud and on-premises (via AWS Storage Gateway).

It provides centralized configuration, backup lifecycle management, compliance enforcement, and point-in-time recovery capabilities. This service is often covered at a foundational level in AWS certification exams like the Solutions ct Associate (SAA-C03).

## Key Features of AWS Backup

### 1. **Centralized Backup Management**

- **Supports multiple AWS services**: RDS, DynamoDB, EBS, EFS, S3, FSx, Aurora, Neptune, and DocumentDB.
- **Cross-region and cross-account backups**: Can be configured via AWS Organizations and Control Tower.
- **Backup consolidation**: Replace service-specific backup scripts with centralized backup policies.

### 2. **Automation & Monitoring**

- Create and apply **backup plans**.
- Use **lifecycle rules** for transitioning to cold storage and retention management.
- Enables **auditing and compliance reporting**.

## Core Components of AWS Backup

### 1. **Backup Plan**

A blueprint defining **how and when** to back up resources.

- **Frequency Options**: Hourly, daily, weekly, monthly, or via cron expressions.
- **Backup Window**: Defines the start time and duration.
- **Lifecycle Policies**:
  - Transition to **cold storage** (minimum 90 days).
  - **Expiration** of backups.
- **Continuous Backups**:
  - Enables **point-in-time restore** (PITR) for supported services.
- **Cross-region Copy**:
  - Copies backups to other regions for disaster recovery.
- **Backup Vault Association**: Specifies where backups are stored.

### 2. **Backup Resources**

Defines **what** is being backed up:

- E.g., S3 bucket, RDS database, EBS volume, etc.

### 3. **Backup Vaults**

The **destination storage** for all backups.

- By default, vaults are **read-write**.
- Optionally enable **Vault Lock**:
  - WORM (Write Once Read Many) mode.
  - 72-hour cool-off period.
  - Once active, **even AWS can't delete** content.
  - Ideal for compliance and regulatory needs.
  - Retention settings still apply.

## On-Demand Backups & PITR

- **Manual backups**: Can be triggered anytime.
- **Point-in-Time Recovery**:
  - Supported for services like S3, RDS.
  - Allows restoring to an exact time within the retention window.

## Supporting AWS Services

### Object Storage

#### Amazon S3

- Stores data from web, mobile apps, IoT, etc.
- **Query-in-place** feature for analytics without data movement.
- **Transfer Acceleration** for global uploads.

#### Amazon S3 Glacier & Glacier Deep Archive

| Tier                 | Use Case                       | Cost (USD/GB/month) | Notes                |
| -------------------- | ------------------------------ | ------------------- | -------------------- |
| Glacier              | Regular archive                | ~$0.004             | Retrieval in minutes |
| Glacier Deep Archive | Rare access, long-term storage | ~$0.00099           | Lowest-cost option   |

### Hybrid Storage

#### AWS Storage Gateway

Connects on-premises apps to AWS storage.

- **Modes**:
  - File Gateway → S3 (NFS/SMB)
  - Volume Gateway → EBS (iSCSI)
  - Tape Gateway → S3/Glacier (for backup archiving)

### Block Storage

#### Amazon EBS (Elastic Block Store)

- Persistent storage for EC2.
- Supports **snapshots** for backups.
- **Automatically replicated** for fault tolerance.
- Pay-per-provisioned GB.

### File Storage

#### Amazon EFS (Elastic File System)

- Scalable file system for EC2 instances.
- Shared access across instances.
- Supports **automatic backup scheduling**.

### Data Transfer Services

#### AWS Snowball

- **Physical device** for data transfer to AWS.
- **Tamper-proof, encrypted**.
- Cost-effective for petabyte-scale migration.

#### AWS Snowball Edge

- Snowball with **compute + storage**.
- Supports **local processing** in disconnected environments.

#### AWS Snowmobile

- **Exabyte-scale transfer** via 45-ft truck.
- Physical transport of up to 100 PB.
- **High-security layers** including 24/7 surveillance, GPS, etc.

### Streaming & Migration Tools

#### Amazon Kinesis Firehose

- Ingests and delivers **streaming data** to S3, Redshift, Elasticsearch, or Splunk.
- **Auto-scaling**, **encryption**, **transformation**, and **compression**.

#### AWS Migration Hub

- Unified dashboard to track **application migration**.
- Tracks migrations from multiple AWS and partner tools.

#### AWS Database Migration Service (DMS)

- **Minimal downtime** migrations.
- Supports most commercial & open-source DBs.
- **Free for 6 months** when migrating to select AWS DBs.

## Compliance & Retention Best Practices

- Use **Vault Lock** for regulatory compliance.
- Define **retention windows** carefully.
- Use **cross-region** copies for disaster recovery.

## Exam & Real-World Relevance

- **AWS Backup** is a **foundational topic** in AWS certification (especially SAA-C03).
- Understand **basic configurations**, **backup plans**, and **vault management**.
- **Deep dive** security, auditing, and scripting are **not typically required** unless stated in specialized courses.

## Final Thoughts

- AWS Backup simplifies backup orchestration across AWS and hybrid environments.
- Great for ensuring **business continuity**, **data durability**, and **compliance**.
- Always refer to [AWS Backup Documentation](https://docs.aws.amazon.com/aws-backup/) for the **most current features and support**.
