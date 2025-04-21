# Origin Access Control (OAC) with CloudFront and S3

This lesson walks through how to **secure an S3 bucket so that it can only be accessed via a CloudFront distribution** using **Origin Access Control (OAC)**, which is the **modern replacement for Origin Access Identity (OAI)**.

## Overview

- You will use previously created infrastructure:
  - A static website hosted in an **S3 bucket**.
  - A **CloudFront** distribution serving the content.
- The goal is to **restrict direct access to the S3 bucket**, forcing all requests to go through CloudFront.
- You must be logged into your **IAM Admin user** in the **Northern Virginia (us-east-1)** region.

## Initial Configuration

1. **Open AWS S3 Console**:

   - Find the `top-10-cats` bucket.
   - Verify public access:
     - Block Public Access: Disabled.
     - Bucket Policy: Allows `GetObject` for all principals.

2. **Check CloudFront Distribution**:
   - Note that direct access to the S3 website endpoint still works — **CloudFront is bypassed**.

## Securing Access with Origin Access Control

### Step 1: Modify the CloudFront Distribution

- Navigate to the **CloudFront console**.
- Select your distribution and go to the **"Origins"** tab.
- Edit the S3 origin:
  - Change **Origin Access** from `Public` to `Origin access control settings`.
  - Choose the option to **create a new OAC** if none exists.

### Step 2: Create a New Origin Access Control (OAC)

- Provide a **name** and **description**.
- Leave the default setting:  
  `Signing behavior: Always sign requests`.

> This ensures all CloudFront requests to S3 are signed and verified.

## Update the S3 Bucket Policy

Replace the existing bucket policy with one that allows only **CloudFront-signed requests**:

### Example Bucket Policy (Explained Line by Line)

```json
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Sid": "AllowCloudFrontServicePrincipalReadOnly",
      "Effect": "Allow",
      "Principal": {
        "Service": "cloudfront.amazonaws.com"
      },
      "Action": "s3:GetObject",
      "Resource": "arn:aws:s3:::top-10-cats/*",
      "Condition": {
        "StringEquals": {
          "AWS:SourceArn": "arn:aws:cloudfront::ACCOUNT_ID:distribution/DISTRIBUTION_ID"
        }
      }
    }
  ]
}
```

### Explanation

- `"Principal": {"Service": "cloudfront.amazonaws.com"}`  
  Allows CloudFront to act on behalf of the user.

- `"Action": "s3:GetObject"`  
  Grants permission to read objects from the bucket.

- `"Resource": "arn:aws:s3:::top-10-cats/*"`  
  Applies the permission to all objects in the bucket.

- `"Condition": { "StringEquals": { "AWS:SourceArn": "..." }}`  
  Restricts access to a **specific CloudFront distribution**.

## Validation

- **Direct S3 access** now returns a `403 Forbidden` error.
- **CloudFront URL** works — proves the access control is functioning correctly.

## Cleanup (Optional but Recommended)

### 1. Delete CloudFront Distribution

- Disable it first.
- Wait until it's fully disabled, then delete it.

### 2. Delete Origin Access Control

- Navigate to **Security > Origin Access** in the CloudFront console.
- Delete the OAC you created.

### 3. (If Previous Demo Was Done) Delete SSL Certificate

- Open **ACM (AWS Certificate Manager)**.
- Delete the certificate used for the alternate domain.

### 4. (If Previous Demo Was Done) Remove Route 53 Records

- Open **Route 53** > Hosted Zones.
- Delete:
  - The validation record from ACM.
  - The record pointing to CloudFront.

### 5. Delete CloudFormation Stack

- Open the **CloudFormation console**.
- Delete the stack from the first demo.

## Final Result

- S3 content is **only accessible via CloudFront**.
- OAC is properly configured to **secure static content delivery**.
- All test/demo resources are removed if cleanup was done.
