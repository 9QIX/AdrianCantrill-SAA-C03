# Configuring S3 Cross-Region Replication (Demo)

This document outlines how to configure **S3 Cross-Region Replication** (CRR) using AWS S3 for disaster recovery of a static website. Below are the detailed steps and JSON templates used during the process.

## Overview

The purpose of this configuration is to replicate objects from a source bucket (in one AWS region) to a destination bucket (in another region). This ensures redundancy and enables disaster recovery for a static website hosted in Amazon S3.

### Prerequisites

1. Access to an AWS account.
2. Permissions to create and manage S3 buckets.
3. The following regions will be used in this demo:
   - Source Bucket: `us-east-1 (N. Virginia)`
   - Destination Bucket: `us-west-1 (N. California)`
4. Download website [files](https://learn-cantrill-labs.s3.amazonaws.com/awscoursedemos/0053-aws-mixed-s3-replication/replication.zip).

## Step-by-Step Guide

### 1. Create the Source Bucket

1. **Navigate to the S3 Console**:
   - Create a new bucket, e.g., `source-bucket-<initials>-<random-number>`.
   - Ensure the region is set to `us-east-1`.
2. **Enable Static Website Hosting**:

   - Navigate to **Properties** → **Static Website Hosting** → Enable it.
   - Use `index.html` as the **Index Document** and **Error Document**.

3. **Allow Public Access**:

   - Update the bucket's **Block Public Access** settings by unchecking "Block all public access."
   - Confirm the changes.

4. **Set a Bucket Policy**:
   Use the following JSON template to allow public access:

   ```json
   {
     "Version": "2012-10-17",
     "Statement": [
       {
         "Effect": "Allow",
         "Principal": "*",
         "Action": "s3:GetObject",
         "Resource": "arn:aws:s3:::source-bucket-<your-bucket-name>/*"
       }
     ]
   }
   ```

   - Replace `<your-bucket-name>` with your source bucket's ARN.

### 2. Create the Destination Bucket

1. **Create a New Bucket**:

   - Name it, e.g., `destination-bucket-<initials>-<random-number>`.
   - Set the region to `us-west-1`.

2. **Enable Static Website Hosting**:

   - Similar to the source bucket, enable static website hosting and use `index.html` for the **Index Document** and **Error Document**.

3. **Set a Bucket Policy**:
   Use the following JSON template:

   ```json
   {
     "Version": "2012-10-17",
     "Statement": [
       {
         "Effect": "Allow",
         "Principal": "*",
         "Action": "s3:GetObject",
         "Resource": "arn:aws:s3:::destination-bucket-<your-bucket-name>/*"
       }
     ]
   }
   ```

   - Replace `<your-bucket-name>` with your destination bucket's ARN.

### 3. Enable Cross-Region Replication

1. **Enable Bucket Versioning**:

   - Navigate to the **Source Bucket** → **Management Tab** → **Replication Rules** → Enable versioning for both buckets.

2. **Create a Replication Rule**:
   - Name it, e.g., `Static Website DR`.
   - Apply it to all objects in the source bucket.
   - Select the destination bucket in your account.
3. **Assign Permissions Using an IAM Role**:
   - AWS creates an IAM role for the replication rule. Ensure that the role has permissions to:
     - Read from the source bucket.
     - Write to the destination bucket.

## Key JSON: IAM Role Policy for Replication

Below is the JSON policy automatically created for the IAM role:

```json
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Action": ["s3:GetReplicationConfiguration", "s3:ListBucket", "s3:GetObjectVersion", "s3:GetObjectVersionAcl"],
      "Resource": "arn:aws:s3:::source-bucket-<your-bucket-name>"
    },
    {
      "Effect": "Allow",
      "Action": ["s3:ReplicateObject", "s3:ReplicateDelete", "s3:ReplicateTags", "s3:GetObjectVersionTagging"],
      "Resource": "arn:aws:s3:::destination-bucket-<your-bucket-name>/*"
    }
  ]
}
```

- **Explanation**:
  - **`s3:GetReplicationConfiguration`**: Allows reading replication configurations from the source bucket.
  - **`s3:ListBucket`**: Lists objects in the source bucket.
  - **`s3:GetObjectVersion` & `s3:GetObjectVersionAcl`**: Access object versions and their ACLs in the source bucket.
  - **`s3:ReplicateObject`**: Enables replicating objects to the destination bucket.
  - **`s3:ReplicateDelete`**: Allows replicating delete markers to the destination bucket.
  - **`s3:ReplicateTags`**: Replicates object tags.
  - **`s3:GetObjectVersionTagging`**: Reads tags from object versions in the source bucket.

### 4. Testing Replication

1. **Upload Objects to the Source Bucket**:

   - Add `index.html` and an image (e.g., `aotm.jpg`) to the source bucket.

2. **Check the Destination Bucket**:

   - Objects will be replicated automatically to the destination bucket. Replication may take several minutes.

3. **Verify Static Website Accessibility**:
   - Open the static website endpoints for both the source and destination buckets to confirm functionality.

## Additional Considerations

- **Replication SLA (Optional)**:
  - Enable Replication Time Control (RTC) for guaranteed replication within 15 minutes. This incurs additional costs.
- **Delete Marker Replication**:

  - By default, S3 replication does not replicate delete markers. Enable this option if needed.

- **Replication for Existing Objects**:
  - Existing objects in the source bucket are not replicated unless explicitly enabled.
