# AWS CloudFormation Non-Portable Template Demo - Part 1

## Resources Used

- **AWS CloudFormation Resource and Property Reference**  
  [AWS Documentation](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-template-resource-type-ref.html)

- **Example Templates**  
  [nonportable.json](https://learn-cantrill-labs.s3.amazonaws.com/awscoursedemos/0047-aws-mixed-cloudformation-nonportabletemplate/nonportable.json)  
  [nonportable.yaml](https://learn-cantrill-labs.s3.amazonaws.com/awscoursedemos/0047-aws-mixed-cloudformation-nonportabletemplate/nonportable.yaml)

# Summary

## Objective

The goal of this demo is to **implement a non-portable AWS CloudFormation template** to understand why non-portable templates are considered **bad practice** and the issues they can cause during deployment.

## Environment Setup

- **Login to AWS Management Account** as an IAM admin user.
- **Select the Northern Virginia region (us-east-1).**
- **Navigate to CloudFormation** from the AWS Management Console.

## Creating the CloudFormation Template

Templates are rarely created from scratch, but doing so improves understanding. Normally, ready-made templates or AWS documentation examples are used.

The demonstration uses **YAML** format for creating the CloudFormation template.

# Writing the YAML Template

## Template Structure

```yaml
Resources:
  Bucket:
    Type: "AWS::S3::Bucket"
    Properties:
      BucketName: "accatpics13333333333469"

  Instance:
    Type: "AWS::EC2::Instance"
    Properties:
      InstanceType: "t2.micro"
      ImageId: "ami-01a441511a92f6b0d"
```

# Line-by-Line Code Explanation

### Root Level: `Resources`

```yaml
Resources:
```

- The **Resources** section is required in every CloudFormation template.
- It holds all logical AWS resources definitions.

## S3 Bucket Resource: `Bucket`

```yaml
Bucket:
  Type: "AWS::S3::Bucket"
  Properties:
    BucketName: "accatpics13333333333469"
```

### Explanation:

| Line                                    | Purpose                                                                                       |
| --------------------------------------- | --------------------------------------------------------------------------------------------- |
| `Bucket:`                               | Logical name of the resource inside the stack (user-defined).                                 |
| `Type: "AWS::S3::Bucket"`               | Defines the AWS resource type to create: an S3 bucket.                                        |
| `Properties:`                           | Section to configure properties specific to an S3 bucket.                                     |
| `BucketName: "accatpics13333333333469"` | Specifies the actual name to assign to the S3 bucket. **(Static name makes it non-portable)** |

## EC2 Instance Resource: `Instance`

```yaml
Instance:
  Type: "AWS::EC2::Instance"
  Properties:
    InstanceType: "t2.micro"
    ImageId: "ami-01a441511a92f6b0d"
```

### Explanation:

| Line                               | Purpose                                                                                                   |
| ---------------------------------- | --------------------------------------------------------------------------------------------------------- |
| `Instance:`                        | Logical name of the EC2 instance resource inside the stack.                                               |
| `Type: "AWS::EC2::Instance"`       | Defines the AWS resource type to create: an EC2 instance.                                                 |
| `Properties:`                      | Configuration properties for the EC2 instance.                                                            |
| `InstanceType: "t2.micro"`         | Specifies the instance type (small, cheap, commonly used for demos and free tier).                        |
| `ImageId: "ami-01a441511a92f6b0d"` | Specifies the AMI ID used to launch the EC2 instance. (Static region-specific AMI makes it non-portable). |

# Important Notes

- **Indentation:** YAML requires proper indentation. Each level typically uses **2 spaces** (no tabs).
- **Quoting Strings:** It’s safer to quote resource types and properties values to avoid parsing errors.
- **Static Values = Non-Portability:**  
  Hardcoding the `BucketName` and `ImageId` makes the template **non-portable**.
  - A different AWS region or AMI version would require manual template edits.
  - Another user trying to create the same bucket might fail if the name already exists.

# Why Non-Portable Templates Are Bad Practice

- **Deployment Failures:** Due to hardcoded names or region-specific resources.
- **Maintenance Challenges:** Hard to update when migrating environments.
- **Reduced Reusability:** Cannot be reused across different projects, accounts, or regions.

# What Was Achieved

By following this lesson:

- You built a **basic CloudFormation YAML template** manually.
- Understood the **resource structure** in CloudFormation.
- Learned **why and how hardcoded values affect portability**.
- Prepared for best practices discussions (which will be covered in later lessons).

# Next Steps

- Save the template as `nonportable.yaml`.
- Deploy it using the AWS CloudFormation Console.
- After part 1, proceed to **Part 2** for continuing the practical hands-on with this setup.
