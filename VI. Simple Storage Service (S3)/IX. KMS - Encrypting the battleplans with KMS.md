# Learn Cantrill.io AWS SA C03 - Practical KMS Demo

This markdown provides a detailed breakdown of the KMS (Key Management Service) demonstration provided in the video. Follow along to understand KMS concepts and operations with practical examples.

## Introduction

This demonstration simulates encrypting and decrypting data using AWS KMS. The scenario involves the "Cat Ruler" sending encrypted battle plans to the "Robot General."

Key concepts covered:

- Creation of a symmetric KMS key
- Encrypting and decrypting data
- Managing KMS key policies

## Creating a KMS Key

1. **Log in**: Use the IAM Admin user for your AWS Management account.
2. **Navigate to KMS Console**:
   - Select the Northern Virginia region.
   - Search for "KMS" in the AWS Management Console.
3. **Create a KMS Key**:
   - Select **Symmetric Key** for simplicity.
   - Use AWS-generated key material.
   - Ensure the key is single-region.
   - Create an alias: `catrobot`.
   - Configure Key Policy:
     - Assign IAM Admin as a Key Administrator.
     - Define IAM Admin as a user for cryptographic operations.

## Encrypting Data

### Step 1: Create Plain Text File

```bash
echo "find all the doggos, distract them with the yumz" > battleplans.txt
```

This creates a plain text file `battleplans.txt` containing the battle plans.

### Step 2: Encrypt the File

```bash
aws kms encrypt \
    --key-id alias/catrobot \
    --plaintext fileb://battleplans.txt \
    --output text \
    --query CiphertextBlob \
    | base64 --decode > not_battleplans.enc
```

#### Command Breakdown

- `aws kms encrypt`: Invokes KMS encryption.
- `--key-id alias/catrobot`: Specifies the key alias.
- `--plaintext fileb://battleplans.txt`: Inputs the plaintext file for encryption.
- `--output text`: Outputs the result in text format.
- `--query CiphertextBlob`: Extracts the ciphertext blob.
- `base64 --decode`: Decodes the base64 ciphertext to binary format.
- `> not_battleplans.enc`: Saves the encrypted file.

## Decrypting Data

### Step 1: Decrypt the File

```bash
aws kms decrypt \
    --ciphertext-blob fileb://not_battleplans.enc \
    --output text \
    --query Plaintext | base64 --decode > decryptedplans.txt
```

#### Command Breakdown

- `aws kms decrypt`: Invokes KMS decryption.
- `--ciphertext-blob fileb://not_battleplans.enc`: Inputs the encrypted file.
- `--output text`: Outputs the result in text format.
- `--query Plaintext`: Extracts the plaintext.
- `base64 --decode`: Decodes the base64 plaintext to its original form.
- `> decryptedplans.txt`: Saves the decrypted file.

### Step 2: Verify Decrypted Content

```bash
cat decryptedplans.txt
```

Expected output:

```
find all the doggos, distract them with the yumz
```

## Cleaning Up

1. Navigate to the KMS Console.
2. Delete the KMS Key:
   - Select the key (e.g., `catrobot`).
   - Schedule the deletion with a 7-day waiting period.

## Key Policy

```json
{
  "Id": "key-consolepolicy-3",
  "Version": "2012-10-17",
  "Statement": [
    {
      "Sid": "Enable IAM User Permissions",
      "Effect": "Allow",
      "Principal": { "AWS": "arn:aws:iam::329599627644:root" },
      "Action": "kms:*",
      "Resource": "*"
    },
    {
      "Sid": "Allow access for Key Administrators",
      "Effect": "Allow",
      "Principal": { "AWS": "arn:aws:iam::329599627644:user/iamadmin" },
      "Action": [
        "kms:Create*",
        "kms:Describe*",
        "kms:Enable*",
        "kms:List*",
        "kms:Put*",
        "kms:Update*",
        "kms:Revoke*",
        "kms:Disable*",
        "kms:Get*",
        "kms:Delete*",
        "kms:TagResource",
        "kms:UntagResource",
        "kms:ScheduleKeyDeletion",
        "kms:CancelKeyDeletion",
        "kms:RotateKeyOnDemand"
      ],
      "Resource": "*"
    },
    {
      "Sid": "Allow use of the key",
      "Effect": "Allow",
      "Principal": { "AWS": "arn:aws:iam::329599627644:user/iamadmin" },
      "Action": ["kms:Encrypt", "kms:Decrypt", "kms:ReEncrypt*", "kms:GenerateDataKey*", "kms:DescribeKey"],
      "Resource": "*"
    },
    {
      "Sid": "Allow attachment of persistent resources",
      "Effect": "Allow",
      "Principal": { "AWS": "arn:aws:iam::329599627644:user/iamadmin" },
      "Action": ["kms:CreateGrant", "kms:ListGrants", "kms:RevokeGrant"],
      "Resource": "*",
      "Condition": {
        "Bool": { "kms:GrantIsForAWSResource": "true" }
      }
    }
  ]
}
```

## Command Explanation

### Encrypt Command

```bash
aws kms encrypt \
    --key-id alias/catrobot \
    --plaintext fileb://battleplans.txt \
    --output text \
    --query CiphertextBlob \
    | base64 --decode > not_battleplans.enc
```

- Encrypts `battleplans.txt` using the KMS key `alias/catrobot`.
- Outputs a binary file `not_battleplans.enc`.

### Decrypt Command

```bash
aws kms decrypt \
    --ciphertext-blob fileb://not_battleplans.enc \
    --output text \
    --query Plaintext | base64 --decode > decryptedplans.txt
```

- Decrypts `not_battleplans.enc` to retrieve the original plaintext.
- Saves the result in `decryptedplans.txt`.

This concludes the KMS demonstration. Follow these steps to implement encryption and decryption in your AWS environment.
