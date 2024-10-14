# AWS IAM Groups Demo - Learn Cantrill IO AWS SA C03

## Overview

This demo lesson walks through using **AWS IAM Groups** to manage user permissions. We focus on migrating a user's direct permissions (from the IAM user `Sally`) to an IAM group (`Developers`) and explore the steps to assign group-level policies that the user inherits. The demo replicates the previous setup where `Sally` had direct access to specific S3 buckets and modifies it by managing these permissions at the group level.

## Steps in the Demo

### 1. Setup

Ensure you are logged in as the **IAM Admin** user in your AWS account. You'll need to be in the **Northern Virginia (us-east-1)** region.  
Download and extract the provided demo files from the following link:

- [Demo Files - Permissions and Infrastructure](https://learn-cantrill-labs.s3.amazonaws.com/awscoursedemos/0023-aws-associate-iam-groups/permissionsgroups.zip)

You should also have deleted any previous demo infrastructure, as instructed.

### 2. Recreating the Infrastructure

Use the one-click deployment link below to recreate the demo infrastructure. This setup includes an IAM user (`Sally`) and two S3 buckets (`catpics` and `animalpics`):

- [Deploy Demo Infrastructure](https://console.aws.amazon.com/cloudformation/home?region=us-east-1#/stacks/create/review?templateURL=https://learn-cantrill-labs.s3.amazonaws.com/awscoursedemos/0023-aws-associate-iam-groups/groupsdemoinfrastructure.yaml&stackName=IAMGROUPS)

Make sure to:

- Enter a valid password following the password policy for your AWS account.
- Confirm creation by clicking the **Capabilities** checkbox and then **Create Stack**.

### 3. Verifying Permissions

Upload the images to the S3 buckets:

- **Merlin.jpeg** to the `catpics` bucket.
- **Thor.jpeg** to the `animalpics` bucket.

After that:

- Attach the `AllowAllS3ExceptCats` policy to `Sally` to simulate previous permissions.
- Verify `Sally` has access to both S3 buckets by logging in as `Sally` and checking access in a new browser session.

### 4. Migrating Permissions to IAM Group

Steps to move `Sally's` permissions to a group:

1. **Remove the Policy** from `Sally`.  
   This detaches the `AllowAllS3ExceptCats` policy from her directly, resulting in no permissions.
2. **Create a New Group**.  
   Name the group `Developers`, and attach the same `AllowAllS3ExceptCats` policy to the group.
3. **Add Sally to the Group**.  
   Add `Sally` to the `Developers` group, which now inherits the permissions.

### 5. Validating Group Permissions

Log back in as `Sally` (in a separate browser session) and:

- Verify access to the `animalpics` bucket.
- Confirm the `Access Denied` response when trying to access the `catpics` bucket (as per the policy).

### 6. Cleanup

Before ending the demo:

1. **Detach the Policy** from the `Developers` group.
2. **Delete the Developers Group**.
3. **Empty and Delete the S3 Buckets**.
4. **Delete the CloudFormation Stack**.

You can verify successful cleanup by checking for errors in the CloudFormation stack events.

## Code and Infrastructure Explained

### IAM Policy: `AllowAllS3ExceptCats`

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
      "Resource": ["arn:aws:s3:::iamgroups-catpics-f5wm1qckzf1b", "arn:aws:s3:::iamgroups-catpics-f5wm1qckzf1b/*"],
      "Effect": "Deny"
    }
  ]
}
```

#### Explanation:

- **Version**: Specifies the version of the policy language (always `2012-10-17`).
- **Statement Array**: Contains multiple permission rules.
  - **Allow Statement**: Grants access (`Action: "s3:*"`) to all S3 resources (`Resource: "*"`) across the account.
  - **Deny Statement**: Denies access to the `catpics` bucket and its contents (`Resource: "arn:aws:s3:::iamgroups-catpics-*"`)—specific to the bucket ARN.

### CloudFormation Template: `groupsdemoinfrastructure.yaml`

```yaml
AWSTemplateFormatVersion: "2010-09-09"
Description: >
  This template implements an IAM user 'Sally'
  An S3 bucket for cat pictures
  An S3 bucket for dog pictures
  And permissions appropriate for Sally.
Parameters:
  sallypassword:
    Description: IAM User Sally's Password
    Default: "4n1m4l54L1f3"
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
        PasswordResetRequired: "false"
  AllowAllS3ExceptCats:
    Type: AWS::IAM::ManagedPolicy
    Properties:
      Description: Allow access to all S3 buckets, except catpics
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
    Description: Bucket name for cat pictures
    Value: !Ref catpics
  animalpicsbucketname:
    Description: Bucket name for animal pictures
    Value: !Ref animalpics
  sallyusername:
    Description: IAM Username for Sally
    Value: !Ref sally
```

#### Explanation:

- **AWSTemplateFormatVersion**: Defines the template format version (`2010-09-09`).
- **Description**: Provides an overview of the resources created, including S3 buckets and an IAM user.
- **Parameters**:
  - `sallypassword`: User-defined parameter for setting `Sally`'s password.
- **Resources**:
  - `catpics`: Creates an S3 bucket for cat pictures.
  - `animalpics`: Creates an S3 bucket for animal pictures.
  - `sally`: Defines an IAM user (`Sally`) and associates a login profile.
  - `AllowAllS3ExceptCats`: Implements the S3 permission policy as a managed policy.
- **Outputs**:
  - Outputs the bucket names (`catpicsbucketname`, `animalpicsbucketname`) and the IAM username (`sallyusername`) for easy reference.

## Conclusion

This demo lesson highlighted the process of moving user-specific permissions to IAM groups for easier management. By grouping users into functional teams and attaching policies at the group level, administrators can simplify permission management without affecting access controls for individual users.

## References

- [IAM Groups Demo - CloudFormation Template](https://console.aws.amazon.com/cloudformation/home?region=us-east-1#/stacks/create/review?templateURL=https://learn-cantrill-labs.s3.amazonaws.com/awscoursedemos/0023-aws-associate-iam-groups/groupsdemoinfrastructure.yaml&stackName=IAMGROUPS)
- [Permissions and Infrastructure Files](https://learn-cantrill-labs.s3.amazonaws.com/awscoursedemos/0023-aws-associate-iam-groups/permissionsgroups.zip)
