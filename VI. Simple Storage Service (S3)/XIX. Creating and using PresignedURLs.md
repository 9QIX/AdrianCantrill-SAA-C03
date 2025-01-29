# AWS S3 Pre-Signed URLs Demo

## Overview

This lesson provides a hands-on demonstration of AWS S3 pre-signed URLs, which are used to grant temporary access to objects in an S3 bucket. The access credentials are embedded within the URL, making it possible to share objects securely for a limited time.

## Steps to Implement

### 1. Setting Up the S3 Bucket

1. **Log in to AWS** as the IAM admin user.
2. **Select the Northern Virginia (us-east-1) region.**
3. **Search for "S3" in the AWS console** and open it in a new tab.
4. **Create a new S3 bucket:**
   - Name: `animals-for-life-media-<random-string>` (S3 bucket names must be unique).
   - Region: `us-east-1`.
   - Leave other settings as default.
5. **Upload an object to the bucket:**
   - Download the sample image: [all5.jpg](https://learn-cantrill-labs.s3.amazonaws.com/awscoursedemos/0032-aws-s3-presignedURL/all5.jpg).
   - Upload `all5.jpg` to the bucket.

### 2. Accessing the Object

- **Method 1: Using the AWS Console**
  - Click the uploaded object and select `Open`. This generates a URL with authentication credentials.
- **Method 2: Using the Object URL**
  - Copy the object URL and paste it into a new browser tab.
  - Results in an `Access Denied` error because public access is not allowed.

### 3. Generating a Pre-Signed URL

- Open **AWS CloudShell** (icon in the AWS console).
- Run the following AWS CLI command to generate a pre-signed URL valid for 3 minutes (180 seconds):

  ```sh
  aws s3 presign s3://animals-for-life-media-<random-string>/all5.jpg --expires-in 180
  ```

- Copy the generated URL and open it in a new browser tab. The image should be accessible.
- After 180 seconds, refreshing the URL will result in an `Access Denied` error.

### 4. Extending Pre-Signed URL Expiration

- Generate a new pre-signed URL with a longer expiration time:

  ```sh
  aws s3 presign s3://animals-for-life-media-<random-string>/all5.jpg --expires-in 604800
  ```

- This URL is valid for **7 days (604,800 seconds)**.

### 5. Testing IAM Policies with Pre-Signed URLs

#### Denying S3 Access to IAM Admin User

- Open **IAM** in the AWS console.
- Select `Users` > `IAM Admin User` > `Permissions`.
- Attach an inline policy with the following JSON:

  ```json
  {
    "Version": "2012-10-17",
    "Statement": [
      {
        "Sid": "VisualEditor0",
        "Effect": "Deny",
        "Action": "s3:*",
        "Resource": "*"
      }
    ]
  }
  ```

- Name the policy `DenyS3` and attach it.
- Running `aws s3 ls` in CloudShell should now return `Access Denied`.
- Refreshing the previously generated pre-signed URL also results in `Access Denied`.

#### Removing the Deny Policy

- Remove the `DenyS3` policy from the IAM admin user.
- Running `aws s3 ls` should now work again.
- Refreshing the pre-signed URL now grants access to the object.

### 6. Generating a Pre-Signed URL for a Non-Existent Object

- Run the following command for an object that doesn’t exist:

  ```sh
  aws s3 presign s3://animals-for-life-media-<random-string>/nonexistent.jpg --expires-in 180
  ```

- A URL will still be generated, but accessing it results in an `Access Denied` or `NoSuchKey` error.

## Key Takeaways

1. **Pre-signed URLs grant temporary access** to S3 objects based on the permissions of the identity generating them.
2. **IAM permissions impact pre-signed URLs.** If the generating user loses access, the URL also loses access.
3. **You can generate pre-signed URLs for non-existent objects,** but they will not work unless the object is later uploaded.
4. **Using CloudShell provides a quick way** to interact with AWS CLI without setting up an EC2 instance.

## Conclusion

AWS S3 pre-signed URLs are a powerful way to share objects securely for a limited time. Understanding how they interact with IAM policies and permissions is essential for architects and developers working with AWS S3.
