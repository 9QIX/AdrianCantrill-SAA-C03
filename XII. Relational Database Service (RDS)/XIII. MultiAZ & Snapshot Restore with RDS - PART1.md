# RDS Snapshots & Multi-AZ Deployment

## Lesson Objective

This demo-based lesson covers the following:

- Understanding and configuring RDS Multi-AZ deployments
- Creating and restoring RDS snapshots
- Simulating failovers using AWS-managed RDS
- Understanding how WordPress (running on EC2) interacts with RDS

## One-Click Deployment

Deploy the infrastructure required for the demo using this CloudFormation stack:

**Deployment Link (N. Virginia region):**

```
https://us-east-1.console.aws.amazon.com/cloudformation/home?region=us-east-1#/stacks/quickcreate?templateURL=https://learn-cantrill-labs.s3.amazonaws.com/awscoursedemos/0035-aws-associate-rds-snapshot-and-multiaz/A4L_WORDPRESS_AND_RDS_AL2023.yaml&stackName=RDSMULTIAZSNAP&param_DBVersion=8.0.32
```

- Stack name: `RDSMULTIAZSNAP`
- Multi-AZ: Initially **set to false**
- Ensure you check the **Capabilities** box before clicking "Create Stack"
- Stack creation takes ~15 minutes

## WordPress Installation

After the stack is created:

1. Navigate to **EC2 > Running Instances**
2. Copy the **Public IPv4** of the `A4L-WordPress` instance
3. Access it via browser

### WordPress Setup

- **Site Title:** The Best Cats
- **Username:** `admin`
- **Password:** `animals4life`
- **Email:** `test@test.com`

After login:

1. Delete the "Hello World" post
2. Create a new post:

   - **Title:** The Best Cats Ever
   - **Block Type:** Gallery

3. Download the image set:
   ```
   https://learn-cantrill-labs.s3.amazonaws.com/awscoursedemos/0035-aws-associate-rds-snapshot-and-multiaz/blog_images.zip
   ```
4. Upload and insert the four images into the post
5. Publish the post

**Note:**

- Images are stored on the EC2 instance
- Post metadata (title, content, etc.) is stored in the RDS instance

## Creating RDS Snapshot

1. Go to **RDS > Databases**
2. Select the RDS instance from the deployment
3. Click **Actions > Take Snapshot**

### Snapshot Details

- Snapshot Name:  
  Format – `a4l-wordpress-with-cat-post-mysql-8032`  
  _(No dots in the version number)_

### Snapshot Behavior

- First snapshot: **full copy** of the DB (longer duration)
- Subsequent snapshots: **incremental** (only changed blocks)

**Retention Considerations:**

- Manual snapshots persist **beyond** the lifecycle of the RDS instance
- Must be deleted **manually** (or with your own automation)
- Useful for disaster recovery (DR) and long-term archiving

## Enabling Multi-AZ Deployment

Multi-AZ creates a **standby replica in another Availability Zone**, increasing durability and availability.

> **Note:** This incurs charges and is not part of the Free Tier.

### Steps:

1. Select your RDS instance
2. Click **Modify**
3. Change setting:
   - Availability & Durability: `Create a standby instance`
4. Scroll down and click **Continue**
5. Apply changes:
   - Choose `Apply Immediately` for the demo

### Behind the Scenes

- AWS takes a snapshot of the primary
- Restores it to a standby in another AZ
- Sets up **synchronous replication**
- Once ready, the DB becomes Multi-AZ

### Benefits:

- Automatic failover
- Backups occur on standby — less impact on performance
- Protection against AZ-level failures

## Simulating Failover

To simulate an AZ failure:

1. Select the RDS instance
2. Click **Actions > Reboot**
3. Select: `Reboot with failover`
4. Confirm the reboot

### What Happens:

- Failover is not immediate (usually **60–120 seconds**)
- The **RDS endpoint remains the same**, but now it points to the **standby**
- WordPress will temporarily show an error or load slowly during failover

### Testing:

- Go back to your blog post and refresh
- Page will load once failover completes

## Code Explanation (Snapshot Name)

Although no code is directly written in this lesson, here's a breakdown of the snapshot naming convention logic:

```bash
a4l-wordpress-with-cat-post-mysql-8032
```

| Segment         | Meaning                                      |
| --------------- | -------------------------------------------- |
| `a4l`           | Animals for Life (project naming convention) |
| `wordpress`     | Refers to the application using the DB       |
| `with-cat-post` | Indicates specific content in this snapshot  |
| `mysql`         | Database engine                              |
| `8032`          | Version of MySQL (8.0.32), no dots allowed   |

This structure helps in managing multiple snapshots across versions and content types.

## Summary

This lesson walks through a hands-on demo simulating:

- A production-like application setup using WordPress + RDS
- Manual snapshot creation and its role in DR
- Enabling Multi-AZ deployment for high availability
- Simulating failover to test resilience

## Key Takeaways

- **Snapshots** are critical for backups but must be **manually managed** if not automated
- **Multi-AZ** deployments provide resilience but incur additional costs
- **Failovers** are not instant, so **design for temporary disruption**
- RDS **endpoints remain static** across failovers, aiding in seamless recovery
