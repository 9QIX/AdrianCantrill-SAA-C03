# S3 Versioning Hands-On Demo

## Overview

This lesson provides a hands-on demonstration of using the versioning feature in Amazon S3. You'll learn how to enable versioning, manage object versions, and understand its implications on bucket management and costs.

## Prerequisites

1. **AWS Management Console Access:** Ensure you are logged into the management account with the region set to **Northern Virginia (us-east-1)**.
2. **Demo Files:** Download and extract the provided demo files from [this link](https://learn-cantrill-labs.s3.amazonaws.com/awscoursedemos/0046-aws-mixed-s3versioning/s3_versioning.zip).

## Steps to Perform

### 1. **Create an S3 Bucket**

- Go to the **S3 console**.
- Click on **Create Bucket**:
  - Enter a **unique bucket name** (e.g., `my-unique-bucket-name`).
  - Uncheck **Block all public access**.
  - Acknowledge the changes by checking the required box.
  - Enable **Bucket Versioning** under the versioning section.
- Click **Create Bucket**.

### 2. **Enable Static Website Hosting**

- Inside the bucket, navigate to **Properties** > **Static Website Hosting**.
- Edit the configuration:
  - Select **Host a static website**.
  - Set **Index Document** to `index.html`.
  - Set **Error Document** to `error.html`.
- Save the changes.

### 3. **Apply a Bucket Policy**

- Go to the **Permissions** tab > **Bucket Policy**.
- Use the following policy template:

  ```json
  {
    "Version": "2012-10-17",
    "Statement": [
      {
        "Sid": "PublicRead",
        "Effect": "Allow",
        "Principal": "*",
        "Action": ["s3:GetObject"],
        "Resource": ["arn:aws:s3:::examplebucket/*"]
      }
    ]
  }
  ```

- Replace `examplebucket` in the `Resource` ARN with your bucket's ARN.
- Save the policy.

### 4. **Upload Objects**

- In the **Objects** tab, upload files:
  - Add the file `index.html` from the `website` folder.
  - Add the folder `IMG` containing `winky.jpeg`.
- After upload, verify the structure:
  - Root contains `index.html` and `IMG/` folder.
  - Inside `IMG`, verify the file `winky.jpeg`.

### 5. **Test Static Website Hosting**

- Open the bucket's static website endpoint (URL available in **Properties**).
- Verify the website displays correctly.

## Exploring Versioning

### Upload a New Version

1. Upload a different version of `winky.jpeg` (e.g., `truffles.jpeg`).
2. Refresh the static website to confirm the new version is displayed.

### View Object Versions

- Enable the **Show Versions** toggle in the S3 console to view all versions of an object.
- Note the version IDs for each version.

### Delete an Object

- Delete `winky.jpeg`:
  - Adds a **delete marker**.
  - Toggle off **Show Versions** to confirm the object appears deleted.

### Restore Deleted Object

- Delete the **delete marker** to restore the object.

## Managing Costs with Versioning

- **Permanence:** All actions create versions or markers; nothing is truly deleted unless a specific version is permanently removed.
- **Cost Considerations:**
  - Versioning incurs additional costs as multiple versions of the same object are stored.
  - Suspended versioning prevents new versions but retains existing ones.

### Cleaning Up

1. Empty the bucket:
   - In the bucket's **Actions**, choose **Empty Bucket**.
   - Confirm by typing `permanently delete`.
2. Delete the bucket:
   - Select the bucket, choose **Delete Bucket**, and confirm.

## Key Takeaways

- Versioning ensures object data is never lost but requires thoughtful management to avoid unnecessary costs.
- Operations with objects are non-destructive (add new versions or markers), but operations with specific versions are permanent.
- Always plan the lifecycle and management strategy for versioned buckets to control costs effectively.
