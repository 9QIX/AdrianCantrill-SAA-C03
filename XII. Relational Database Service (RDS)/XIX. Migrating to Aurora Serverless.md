# Migrating Aurora Provisioned Snapshot to Aurora Serverless

This demo lesson walks through how to **restore a snapshot** taken from an **Aurora (Provisioned)** database into an **Aurora Serverless** cluster. It highlights both **automated** and **manual** approaches, introduces Aurora Serverless capacity scaling, and shows how it can optimize cost through **auto-pausing**.

## Prerequisites

- Be logged into the **General AWS account** (management account).
- AWS Region must be **us-east-1 (N. Virginia)**.
- You need a previously created **Aurora Provisioned snapshot** (from an earlier demo).

## 1. One-Click Deployment via CloudFormation

1. **Launch the One-Click Stack:**

   - Use the provided CloudFormation deployment link.
   - Copy the snapshot name (not ARN) of the relevant Aurora Provisioned DB.

2. **Find Snapshot:**

   - Go to **RDS > Snapshots**.
   - Use the snapshot named:  
     `a4l-wordpress-aurora-with-cat-post`

3. **Configure CloudFormation:**
   - Paste the snapshot name into the template input.
   - Acknowledge capabilities.
   - Click **Create Stack**.
   - This process can take up to **45 minutes**.

## 2. Manual Restore of Aurora Snapshot to Serverless

1. In RDS console, go to the **snapshot** and choose:

   - **Actions > Restore Snapshot**

2. **Configure Restore Settings:**
   - **Engine Compatibility:** Only MySQL-compatible engines will be shown.
   - **Capacity Type:** Change from _Provisioned_ to _Serverless_.
   - **Version:** Must match (e.g., `2.07.1`).
   - **DB Identifier:** Give a new name (e.g., `a4l-wordpress-serverless`).
   - **Connectivity:**
     - Select VPC (e.g., `animals4life-vpc`).
     - Provide a **DB subnet group**.
     - Assign a **security group** for access control.
   - **Additional Configuration:**
     - Includes setting up **data API access** for lightweight, connectionless access (useful for Lambda apps).
     - Set encryption and backup options.

## 3. Aurora Serverless Concepts

### Aurora Capacity Units (ACUs)

- Aurora Serverless scales based on **ACUs**.
- You can define:
  - **Minimum Capacity**
  - **Maximum Capacity**
- Aurora will **auto-scale** between these based on actual load.

### Pause on Inactivity

- You can configure the cluster to **pause** after a certain number of **idle minutes**.
- During pause:
  - **Compute cost** drops to zero.
  - The database remains available but incurs **no compute billing**.

```bash
# Example Settings:
Min ACU = 1
Max ACU = 2
Pause After = 5 minutes of inactivity
```

## 4. Application Verification (WordPress)

1. Locate the **EC2 WordPress instance** from a previous deployment.
2. Open its **IPv4 Public Address** in a browser.
3. Confirm that the WordPress site and post ("Best Cats Ever") still exist.
4. Note: **Media files are missing** because they are stored on the instance's local file system, not in the database.

## 5. Auto-Scaling & Pause Demo

- Initially, after restore, the cluster will use **2 ACUs** due to load.
- Over time:
  - Drops to **1 ACU**.
  - Then **0 ACUs** after inactivity (5 minutes in this demo).
- You can verify this by:
  - Checking **RDS Monitoring**.
  - Watching CPU utilization drop.
  - Seeing connection count reduce to 0.

> Aurora Serverless will resume when traffic returns. You may notice a slight **delay** or **WordPress error** if the resume process takes too long.

## 6. Clean Up Resources

To avoid ongoing charges:

1. Go to the **CloudFormation console**.
2. Select the **Aurora Serverless Stack**.
3. Click **Delete > Delete Stack**.
4. This will remove all provisioned resources.

## Summary

### What You Learned

- How to restore a **snapshot** from Aurora Provisioned to **Aurora Serverless**.
- Aurora Serverless concepts: **ACUs**, **auto-scaling**, **pause-on-inactivity**.
- Cost optimization with auto-pause.
- Limitations of file system media when decoupling database from EC2.
- Foundation for upcoming **EFS** integration.

## Coming Up Next

The next section will solve the issue of media files being lost due to local EC2 storage by introducing **Amazon EFS (Elastic File System)** for **shared, persistent storage**.
