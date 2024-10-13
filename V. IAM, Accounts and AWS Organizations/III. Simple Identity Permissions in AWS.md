# AWS IAM User Demo Lesson - Detailed Summary

## Overview

In this demo lesson, we explore **AWS Identity and Access Management (IAM) Users** by creating an IAM user named _Sally_ and assigning her permissions using AWS policies. We also interact with S3 buckets to demonstrate how policies manage access permissions. This guide will cover all the key steps, including how to manage and modify policies in IAM for specific users.

## Prerequisites

- Log in as the **IAM admin user** in your AWS account.
- Ensure you have selected the **Northern Virginia (us-east-1)** region.
- You will use **CloudFormation** to deploy the required resources.

## Demo Files and Links

- **[One-click Deployment Link](https://console.aws.amazon.com/cloudformation/home?region=us-east-1#/stacks/create/review?templateURL=https://learn-cantrill-labs.s3.amazonaws.com/awscoursedemos/0052-aws-mixed-iam-simplepermissions/demo_cfn.yaml&stackName=IAM)** - This will deploy the infrastructure for the demo.
- **[Demo Files](https://learn-cantrill-labs.s3.amazonaws.com/awscoursedemos/0052-aws-mixed-iam-simplepermissions/simpleidentitypermissions.zip)** - Download the necessary files for this lesson.

## Steps to Follow

### Step 1: CloudFormation Stack Creation

1. **CloudFormation Deployment**:

   - Deploy the CloudFormation stack using the provided link.
   - This will create:
     - An IAM user named **Sally**.
     - Two S3 buckets: `Catpics` and `Animalpics`.
     - A managed policy that will grant **Sally** permissions.

2. **Password Setup**:
   - When prompted during the stack setup, enter a password for Sally that complies with AWS's password policy (minimum 8 characters, with uppercase, lowercase, numbers, or special characters).

### Step 2: Review CloudFormation Resources

- After the stack deployment is complete, verify the creation of:
  - The **Catpics** and **Animalpics** S3 buckets.
  - The IAM **Sally** user with an attached managed policy.

### Step 3: IAM User Login and Password Change

1. **Login with Sally**:

   - Use the **IAM user sign-in link** provided by the CloudFormation output.
   - Open a private browser or a different browser session to avoid logging out of your current session as an admin.

2. **Password Reset**:
   - Log in with the username and the password you set for **Sally**.
   - Change the password upon first login using the **IAM Change Password** policy assigned to Sally.

### Step 4: Testing IAM User Permissions

1. **Verify Limited Permissions**:
   - Try accessing **EC2** or **S3** services. Sally will have **no permissions** initially, except for changing her password.
2. **Applying an Inline Policy**:
   - Assign an inline policy granting **Sally** full access to S3 using the `s3_fulladmin.json` file.

```json
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Sid": "statement1",
      "Effect": "Allow",
      "Action": ["s3:*"],
      "Resource": ["arn:aws:s3:::*"]
    }
  ]
}
```

- This policy allows all S3 actions on any S3 resources.

### Step 5: Test S3 Access Permissions

1. **Uploading to S3 Buckets**:

   - **Sally** can now interact with both the **Animalpics** and **Catpics** buckets. You can upload files (e.g., `Thor.jpeg` and `Merlin.jpeg`) to the S3 buckets.

2. **Testing Read Permissions**:
   - Open objects in the S3 buckets to ensure **Sally** can read them.

### Step 6: Restricting Permissions with Managed Policy

1. **Remove Inline Policy**:

   - After testing, remove the inline policy, which restores **Sally's** limited access.

2. **Attach a Managed Policy**:
   - Attach a managed policy created by the CloudFormation stack, which allows access to all S3 resources **except** the **Catpics** bucket. This is defined in the `AllowAllS3ExceptCats.json` policy:

```json
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Action": "s3:*",
      "Resource": "*",
      "Effect": "Allow"
    },
    {
      "Action": "s3:*",
      "Resource": ["arn:aws:s3:::iam-catpics-hsvwmf4mipkf", "arn:aws:s3:::iam-catpics-hsvwmf4mipkf/*"],
      "Effect": "Deny"
    }
  ]
}
```

- **Sally** can now access all S3 resources **except** the **Catpics** bucket.

### Step 7: Clean Up

- Remove the permissions from **Sally**:
  - Delete the managed policy and empty the S3 buckets.
  - Delete the CloudFormation stack to clean up all resources created during the lesson.

## CloudFormation Template

Below is the CloudFormation template used in this demo.

```yaml
AWSTemplateFormatVersion: "2010-09-09"
Description: >
  This template implements an IAM user 'Sally'
  An S3 bucket for cat pictues
  An S3 bucket for dog pictures
  An S3 bucket for other animals
  And permissions appropriate for Sally.
Parameters:
  sallypassword:
    NoEcho: true
    Description: IAM User Sallys Password
    Type: String
Resources:
  catpics:
    Type: AWS::S3::Bucket
  animalpics:
    Type: AWS::S3::Bucket
  sally:
    Type: AWS::IAM::User
    Properties:
      ManagedPolicyArns:
        - arn:aws:iam::aws:policy/IAMUserChangePassword
      LoginProfile:
        Password: !Ref sallypassword
        PasswordResetRequired: "true"
  policy:
    Type: AWS::IAM::ManagedPolicy
    Properties:
      Description: Allow access to all S3 buckets, except catpics
      ManagedPolicyName: AllowAllS3ExceptCats
      PolicyDocument:
        Version: 2012-10-17
        Statement:
          - Effect: Allow
            Action: "s3:*"
            Resource: "*"
          - Effect: Deny
            Action: "s3:*"
            Resource: [!GetAtt catpics.Arn, !Join ["", [!GetAtt catpics.Arn, "/*"]]]
Outputs:
  catpicsbucketname:
    Description: Bucketname for catpictures (the best animal!)
    Value: !Ref catpics
  animalpicsbucketname:
    Description: Bucketname for animalpics (the almost best animals!)
    Value: !Ref animalpics
  sallyusername:
    Description: IAM Username for Sally
    Value: !Ref sally
```

## Conclusion

This lesson provided hands-on experience in managing IAM users, attaching policies, and working with AWS S3 buckets to define granular access permissions. By practicing these steps, you have learned how to implement and manage user access in AWS using both inline and managed policies.
