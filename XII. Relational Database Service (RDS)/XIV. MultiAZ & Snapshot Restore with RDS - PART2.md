# RDS Snapshot Recovery and Application Repointing

## Overview

This lesson demonstrates **how to recover from data corruption** in a typical AWS RDS setup using **manual snapshots**, by restoring a database and **repointing the WordPress application** to the new instance.

## Key Concepts Covered

- Manual snapshots in RDS
- Restoring from a snapshot
- Understanding RDS behavior: creates new instances on restore
- Updating applications to use the new RDS instance
- Cleaning up AWS resources post-demo

## 1-Click Deployment Setup

You can deploy the lab resources using the following CloudFormation Stack:

**CloudFormation URL:**  
[Deploy Lab Stack](https://us-east-1.console.aws.amazon.com/cloudformation/home?region=us-east-1#/stacks/quickcreate?templateURL=https://learn-cantrill-labs.s3.amazonaws.com/awscoursedemos/0035-aws-associate-rds-snapshot-and-multiaz/A4L_WORDPRESS_AND_RDS_AL2023.yaml&stackName=RDSMULTIAZSNAP&param_DBVersion=8.0.32)

**Blog Images:**  
[Download blog_images.zip](https://learn-cantrill-labs.s3.amazonaws.com/awscoursedemos/0035-aws-associate-rds-snapshot-and-multiaz/blog_images.zip)

## Step-by-Step Demo Summary

### Simulating Data Corruption

1. Modify a WordPress blog post's title (e.g., change "The Best Cats Ever" to "Not The Best Cats Ever").
2. Save the post — this simulates **data corruption** in the database.

### Manual Snapshot Restoration

1. Navigate to the **RDS Console > Snapshots**.
2. Select the **manual snapshot** previously created.
3. Click **Actions > Restore Snapshot**.
4. Key Settings:
   - **DB Engine:** MySQL Community
   - **DB Identifier:** `a4l-wordpress-restore`
   - **Deployment:** Single-AZ (for demo purposes)
   - **Instance Type:** Choose from `t2.micro` or `t3.micro`
   - **VPC/Subnet Group:** Use the same as initial deployment
   - **Public Access:** No
   - **Security Group:** Use `rds-multiaz-snap-rds` (not the instance SG)
5. Click **Restore DB Instance**.

> ⚠️ Important: Restoring from a snapshot creates a **brand new RDS instance** with a new **endpoint DNS name**.

### Repointing WordPress to Restored DB

Once the new DB instance is in **Available** state:

1. Go to **EC2 > Instances > a4l-wordpress**.
2. Click **Connect > EC2 Instance Connect**.
3. Access the WordPress root directory:
   ```bash
   cd /var/www/html
   ls -la
   ```
4. Edit the WordPress config:
   ```bash
   nano wp-config.php
   ```
5. Find the line:

   ```php
   define('DB_HOST', 'old-database-endpoint');
   ```

   Replace `old-database-endpoint` with the **new endpoint** from the restored RDS instance.

6. Save and exit:

   ```bash
   Ctrl+O  # Write changes
   Enter   # Confirm
   Ctrl+X  # Exit editor
   ```

7. Refresh the WordPress site — the post should now reflect the **original correct data** from the restored snapshot.

### Key Code Explanation

#### wp-config.php line (before and after)

```php
// Before
define('DB_HOST', 'a4l-wordpress.randomhash.us-east-1.rds.amazonaws.com');

// After
define('DB_HOST', 'a4l-wordpress-restore.randomhash.us-east-1.rds.amazonaws.com');
```

#### Explanation

- `define('DB_HOST', ...)`: This line tells WordPress where to find the database.
- By updating it with the **restored RDS endpoint**, we point the app to the version with uncorrupted data.

## Cleanup Process

1. **Delete Restored RDS Instance:**

   - Go to **RDS > Databases**
   - Select `a4l-wordpress-restore`
   - Click **Actions > Delete**
   - Choose:
     - Do not create final snapshot
     - Do not retain automated backups
     - Acknowledge by typing `delete me`
   - Click **Delete**

2. **Verify Snapshots:**

   - System snapshots tied to deleted instance are removed automatically.
   - **Manual snapshot** (with the original data) is retained for future use.

3. **Delete CloudFormation Stack:**
   - Go to **CloudFormation > Stacks**
   - Select `rds-multiaz-snap`
   - Click **Delete**
   - Confirm

## Key Takeaways

- **Normal RDS snapshot restores always create a new instance**. There's no in-place restore for MySQL (unlike Aurora).
- You must **manually update application configuration** to use the new RDS endpoint.
- Snapshots can be used as a **robust disaster recovery mechanism** in production environments.
- Hands-on practice is crucial to understand real-world AWS database recovery scenarios.

## Additional Notes

- Different RDS engines (Oracle, MSSQL, Aurora, PostgreSQL) have **different feature sets**.
- **Aurora** does support _in-place restores_ and will be covered in another section.
- Manual snapshots are retained even after instance deletion, unlike automated ones.
