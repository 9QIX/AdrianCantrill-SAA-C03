# Learn Cantrill AWS S3 Object Encryption Demo

This detailed walkthrough demonstrates how to handle server-side encryption in Amazon S3, using different encryption types. The goal is to familiarize users with the practical implementation of encryption and permissions in AWS.

## Resources

- [Download the files used in this lesson](https://learn-cantrill-labs.s3.amazonaws.com/awscoursedemos/0043-aws-mixed-s3-object-encryption/object_encryption.zip)

## Overview

We will:

1. Create an S3 bucket and upload objects with different server-side encryption (SSE) methods.
2. Experiment with IAM permissions and restrictions for encryption key usage.
3. Demonstrate default encryption settings for an S3 bucket.

## Steps to Follow

### 1. Create an S3 Bucket

- Log into the AWS Console as an IAM admin user.
- Ensure the region is set to **US East (Northern Virginia)**.
- Navigate to the S3 console and create a bucket with a unique name (e.g., `catpics-<random-text>`).
- Leave the default settings and click **Create Bucket**.

### 2. Set Up KMS Key

- Go to the **Key Management Service (KMS)** console.
- Create a **Symmetric Key**:
  - Choose **Single Region Key**.
  - Name it (e.g., `catpics`).
  - Leave permissions unconfigured initially.
- Finalize the creation. This key will be used later.

### 3. Upload Files with Different Encryption Types

- **Download the lesson files** and extract them.
- Upload each file to the bucket, applying specific encryption settings:

#### a) Upload Using `SSE-S3` (Amazon S3 Managed Keys)

1. Select the file `sse-s3-dweez.jpg`.
2. Expand **Properties** -> **Server Side Encryption**.
3. Choose **Amazon S3 Key (SSE-S3)**.
4. Upload the file.

#### b) Upload Using `SSE-KMS` (AWS KMS Managed Keys)

1. Select the file `sse-kms-jiny.jpeg`.
2. Expand **Properties** -> **Server Side Encryption**.
3. Choose **AWS Key Management Service Key (SSE-KMS)**:
   - Use either the **AWS-managed key** (default) or the **customer-managed key (`catpics`)** created earlier.
4. Upload the file.

### 4. Validate Permissions

#### a) Without Restrictions

- Open both uploaded files in the S3 console. Both should be accessible since the IAM admin user has full permissions.

#### b) Apply a Deny Policy

1. Create an inline policy to deny KMS access:
   - Navigate to **IAM** -> **Users** -> Select IAM admin user.
   - Add permissions with the following JSON:

```json
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Sid": "VisualEditor0",
      "Effect": "Deny",
      "Action": "kms:*",
      "Resource": "*"
    }
  ]
}
```

2. Apply the policy and test:
   - `SSE-S3` encrypted files remain accessible.
   - `SSE-KMS` encrypted files fail with **Access Denied** because S3 depends on KMS to decrypt keys.

### 5. Revert Permissions

- Remove the deny policy to restore access.
- Validate that the `SSE-KMS` file is accessible again.

### 6. Configure Default Encryption for the S3 Bucket

- Navigate to **Bucket Properties** -> **Default Encryption**.
- Set the default encryption to `SSE-KMS` using the `catpics` key.
- Test by uploading a new file (e.g., `default-merlin.jpeg`) without specifying encryption:
  - Verify that it uses the `SSE-KMS` encryption and the `catpics` key.

### 7. Clean Up Resources

- Empty and delete the S3 bucket.
- Schedule the KMS key for deletion:
  - Go to **KMS** -> **Customer Managed Keys** -> `catpics`.
  - Select **Key Actions** -> **Schedule Key Deletion** (minimum 7 days).

## Policies Used

### Enable IAM User Permissions

```json
{
  // The unique identifier for the policy
  "Id": "key-consolepolicy-3",

  // The version of the policy language
  "Version": "2012-10-17",

  // The main body of the policy
  "Statement": [
    {
      // The unique identifier for the statement
      "Sid": "Enable IAM User Permissions",

      // The effect of the statement, which is to allow the specified actions
      "Effect": "Allow",

      // The principal that is allowed to perform the actions, in this case, the root user of the specified AWS account
      "Principal": {
        "AWS": "arn:aws:iam::329599627644:root"
      },

      // The actions that are allowed, in this case, all KMS actions
      "Action": "kms:*",

      // The resources that the actions can be performed on, in this case, all resources
      "Resource": "*"
    }
  ]
}
```

### Deny KMS Access

```json
{
  // The version of the policy language
  "Version": "2012-10-17",

  // The main body of the policy
  "Statement": [
    {
      // The unique identifier for the statement
      "Sid": "VisualEditor0",

      // The effect of the statement, which is to deny the specified actions
      "Effect": "Deny",

      // The actions that are denied, in this case, all KMS actions
      "Action": "kms:*",

      // The resources that the actions cannot be performed on, in this case, all resources
      "Resource": "*"
    }
  ]
}
```

## Key Takeaways

1. `SSE-S3` encryption is entirely managed by Amazon S3 and does not require external key management.
2. `SSE-KMS` provides more control, allowing the use of customer-managed keys for compliance and security.
3. IAM policies can enforce or restrict access to encryption resources, enabling fine-grained access control.
