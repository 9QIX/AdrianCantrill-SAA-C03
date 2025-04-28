# AWS CloudFormation Non-Portable Template Demo - Part 2

## Resources Used

- **CloudFormation Resource and Property Reference:**  
  [AWS Documentation](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-template-resource-type-ref.html)
- **Template Files:**  
  [Non-Portable JSON Template](https://learn-cantrill-labs.s3.amazonaws.com/awscoursedemos/0047-aws-mixed-cloudformation-nonportabletemplate/nonportable.json)  
  [Non-Portable YAML Template](https://learn-cantrill-labs.s3.amazonaws.com/awscoursedemos/0047-aws-mixed-cloudformation-nonportabletemplate/nonportable.yaml)

# Lesson Overview

This lesson builds upon a previous one, focusing on deploying a **non-portable CloudFormation template** and understanding why it fails across different stacks and regions.  
The objective is to understand **why the template is non-portable** and **prepare for converting it into a portable one** in future sessions.

# Step-by-Step Summary

## 1. Upload and Deploy the Non-Portable YAML Template

- Navigate to the AWS Console → **Services → CloudFormation**.
- Create a new stack:
  - **Template is ready** → **Upload a template file** → Choose the downloaded **nonportable.yaml**.
  - Name the stack **Non-Portable-One**.
- Scroll to the bottom and **Create Stack**.

## 2. Encountering the First Error

- Stack creation fails because the **S3 Bucket name** is hardcoded.
- S3 Bucket names must be **globally unique across all AWS accounts and regions**.
- The hardcoded bucket name (`ACCapix133333337`) already exists, causing failure.

### Diagnosing the Error

- Go to the **Events tab** in CloudFormation.
- Find the **first red error** stating:  
  `"Bucket already exists"`.

## 3. Fixing the Bucket Name

- **Edit the template** to modify the S3 bucket name:
  - Make it unique by changing the prefix or suffix.
  - Example: Add extra digits (`ACCapix13333333733`).
- Save the file.

- Delete the failed stack.
- Recreate the stack using the updated template.

## 4. Successful Stack Creation

- Both resources now create successfully:

  - **S3 Bucket** (bucket logical resource).
  - **EC2 Instance** (instance logical resource).

- **Resource creation states** seen in the event logs:
  - `CREATE_IN_PROGRESS`
  - `RESOURCE_CREATION_INITIATED`
  - `CREATE_COMPLETE`

## 5. Attempt to Reuse the Same Template

- **Try creating another stack** using the same (still hardcoded) template.
- The new stack fails again:
  - Because the **same bucket name** is hardcoded.
  - You cannot have two buckets with the same name.

### Important Observation

- **Templates with hardcoded resource names are not reusable**.
- They are **non-portable** within the same account or region.

## 6. Cleaning Up

- Delete both stacks (**Non-Portable-One** and **Non-Portable-Two**).
- Deleting a stack removes:
  - The **logical resources**.
  - The **corresponding physical resources**.

### Benefit Highlight

- **CloudFormation automatically ties lifecycle** of logical and physical resources:
  - Simplifies cleanup.

## 7. Testing in a Different Region

- **Switch AWS region** to Oregon (`us-west-2`).
- Try creating the stack again.

### New Error Encountered

- The stack fails with:
  ```plaintext
  Image ID [ami-xxxxxxxxxxxxxxxxx] does not exist
  ```
- Problem: **AMI IDs are region-specific**.
  - The hardcoded AMI ID only exists in the **N. Virginia (`us-east-1`)** region.

# Key Concepts and Learnings

## Why is this Template Non-Portable?

| Reason                   | Explanation                                                                                     |
| :----------------------- | :---------------------------------------------------------------------------------------------- |
| Hardcoded S3 bucket name | Bucket names must be unique globally. Reusing the template creates a conflict.                  |
| Hardcoded AMI ID         | AMIs differ by region. Using a region-specific AMI ID makes the template fail in other regions. |

# Code Explanation (YAML Template Example)

Example (simplified from nonportable.yaml):

```yaml
Resources:
  Bucket:
    Type: AWS::S3::Bucket
    Properties:
      BucketName: accapix133333337

  Instance:
    Type: AWS::EC2::Instance
    Properties:
      ImageId: ami-0abcdef1234567890
      InstanceType: t2.micro
```

### Line-by-Line Breakdown:

- `Resources:`  
  Starts the definition of resources to be created.

- `Bucket:`  
  Logical name for the S3 Bucket.

- `Type: AWS::S3::Bucket`  
  Defines the resource type as an **S3 Bucket**.

- `Properties:`  
  Properties of the S3 bucket are specified here.

- `BucketName: accapix133333337`  
  **Hardcoded bucket name** causing the non-portability issue.

- `Instance:`  
  Logical name for the EC2 Instance.

- `Type: AWS::EC2::Instance`  
  Defines the resource type as an **EC2 Instance**.

- `ImageId: ami-0abcdef1234567890`  
  **Hardcoded AMI ID**, specific to a particular region.

- `InstanceType: t2.micro`  
  Specifies a **small instance type** suitable for basic workloads.

# Final Thoughts

- **Non-portable templates** cause friction when scaling infrastructure across multiple regions or accounts.
- **Best Practice:** Avoid hardcoding unique values. Use:

  - Parameters.
  - Mappings.
  - Pseudo Parameters (like `AWS::Region`).

- Future sessions will focus on **converting non-portable templates into portable, reusable templates**.
