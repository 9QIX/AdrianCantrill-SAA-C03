# S3 Multi-Region Access Points Mini Project

## Overview

This mini-project focuses on creating and configuring **Amazon S3 Multi-Region Access Points (MRAP)**. MRAP allows you to create a single global endpoint that routes requests to the closest S3 bucket across multiple AWS regions. This setup is useful for improving latency and ensuring high availability for globally distributed applications.

The project involves:

1. Creating S3 buckets in two different AWS regions.
2. Configuring a Multi-Region Access Point.
3. Setting up replication between the buckets.
4. Testing the MRAP by uploading and downloading files from different regions.
5. Cleaning up the resources after the project.

## Prerequisites

- An AWS account with **admin permissions**.
- Two different AWS regions selected for the project (e.g., `ap-southeast-2` for Sydney and `ca-central-1` for Canada).
- GitHub Link: [S3 Multi-Region Access Points](https://github.com/acantril/learn-cantrill-io-labs/blob/master/00-aws-simple-demos/aws-s3-multi-region-access-point/Readme.md)

## Step-by-Step Instructions

### Step 1: Create S3 Buckets

1. **Navigate to the S3 Console**:

   - Go to the [S3 Console](https://s3.console.aws.amazon.com/s3/buckets).
   - Click on **Create Bucket**.

2. **Create the First Bucket**:

   - **Bucket Name**: Use a consistent naming convention, e.g., `multi-region-demo-sydney-<random-number>`.
   - **Region**: Select `ap-southeast-2` (Sydney).
   - **Bucket Versioning**: Enable versioning.
   - Leave other settings as default and click **Create Bucket**.

3. **Create the Second Bucket**:
   - **Bucket Name**: Use a similar naming convention, e.g., `multi-region-demo-canada-<random-number>`.
   - **Region**: Select `ca-central-1` (Canada).
   - **Bucket Versioning**: Enable versioning.
   - Leave other settings as default and click **Create Bucket**.

### Step 2: Create Multi-Region Access Point

1. **Navigate to Multi-Region Access Points**:

   - In the S3 Console, go to the **Multi-Region Access Points** section.
   - Click **Create Multi-Region Access Point**.

2. **Configure the Access Point**:

   - **Name**: Choose a unique name (e.g., `critical-cat-data`).
   - **Add Buckets**: Select the two buckets created earlier (Sydney and Canada).
   - Click **Create Multi-Region Access Point**.

3. **Wait for Creation**:
   - The creation process can take up to 24 hours but typically completes in 10-30 minutes.
   - Ensure the status changes to **Ready** before proceeding.

### Step 3: Configure Replication Between Buckets

1. **Navigate to Replication and Failover**:

   - Go to the **Multi-Region Access Points** section.
   - Select the access point you created and go to the **Replication and Failover** tab.

2. **Create Replication Rules**:

   - Click **Create Replication Rules**.
   - Select **Replicate objects among all specified buckets**.
   - Choose both buckets (Sydney and Canada).
   - **Scope**: Apply to all objects in the bucket.
   - Enable **Replication Metrics and Notifications** and **Replica Modification Sync**.
   - Click **Create Replication Rules**.

3. **Verify Replication**:
   - The graphical representation should show two-way replication between the buckets.

### Step 4: Test the Multi-Region Access Point

1. **Generate Test Files**:

   - Use AWS CloudShell to create test files in different regions.
   - Example command to create a 10MB file:
     ```bash
     dd if=/dev/urandom of=test1.file bs=1M count=10
     ```

2. **Upload Files to MRAP**:

   - Use the following command to upload the file to the MRAP:
     ```bash
     aws s3 cp test1.file s3://arn:aws:s3::<account-id>:accesspoint/<mrap-alias>/
     ```
   - Replace `<account-id>` and `<mrap-alias>` with your MRAP ARN.

3. **Verify File Replication**:

   - Check the buckets in both regions to ensure the file is replicated.
   - Note: Replication may take a few minutes.

4. **Test from Different Regions**:
   - Repeat the process from regions closer to each bucket (e.g., Tokyo for Sydney and Ohio for Canada).
   - Observe which bucket receives the file first and how replication behaves.

### Step 5: Clean Up Resources

1. **Delete the Multi-Region Access Point**:

   - Go to the **Multi-Region Access Points** section.
   - Select the access point and click **Delete**.
   - Confirm by typing the access point name.

2. **Empty and Delete Buckets**:
   - Go to the **Buckets** section.
   - Select each bucket, click **Empty**, and confirm by typing `permanently delete`.
   - After emptying, delete the buckets by clicking **Delete** and confirming the bucket name.

## Key Learnings

- **Multi-Region Access Points** provide a single global endpoint for S3 buckets in multiple regions.
- **Replication** ensures data consistency across buckets but may introduce latency.
- **Testing from different regions** helps understand how MRAP routes requests to the closest bucket.
- **Replication Time Control (RTC)** can reduce replication latency but incurs additional costs.

## Code Explanation

### Generating a Test File

```bash
dd if=/dev/urandom of=test1.file bs=1M count=10
```

- **`dd`**: Command to convert and copy files.
- **`if=/dev/urandom`**: Input file (random data generator).
- **`of=test1.file`**: Output file name.
- **`bs=1M`**: Block size (1MB).
- **`count=10`**: Number of blocks (creates a 10MB file).

### Uploading a File to MRAP

```bash
aws s3 cp test1.file s3://arn:aws:s3::<account-id>:accesspoint/<mrap-alias>/
```

- **`aws s3 cp`**: AWS CLI command to copy files to S3.
- **`test1.file`**: Local file to upload.
- **`s3://arn:aws:s3::<account-id>:accesspoint/<mrap-alias>/`**: MRAP ARN where the file will be uploaded.

### Downloading a File from MRAP

```bash
aws s3 cp s3://arn:aws:s3::<account-id>:accesspoint/<mrap-alias>/test1.file .
```

- **`.`**: Current directory (downloads the file to the local machine).

## Conclusion

This project provides hands-on experience with S3 Multi-Region Access Points and replication. It highlights the benefits of using MRAP for global applications and the importance of understanding replication latency. By following these steps, you can effectively configure and test a globally distributed S3 setup.

For more details, refer to the [AWS S3 Documentation](https://docs.aws.amazon.com/AmazonS3/latest/userguide/MultiRegionAccessPoints.html).

Check for the GitHub Documentation by Adrian:
