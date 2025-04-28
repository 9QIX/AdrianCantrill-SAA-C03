# Enhancing CloudFormation Templates for Portability

## Resources Used

- [AWS Systems Manager Parameter Store Documentation](https://docs.aws.amazon.com/systems-manager/latest/userguide/parameter-store-public-parameters.html)
- [Demo Files (Portable CloudFormation Templates)](https://learn-cantrill-labs.s3.amazonaws.com/awscoursedemos/0048-aws-mixed-cloudformation-portabletemplate/portable.zip)

## Introduction

This session focuses on improving CloudFormation templates to make them **portable** across AWS accounts and regions.

The main goals are:

- Avoid hardcoded values like specific **bucket names** and **AMI IDs**.
- Enable **dynamic referencing** (e.g., through AWS Systems Manager parameters).
- Allow the same template to deploy multiple times without conflicts.

## CloudFormation Templates Overview

### 1. Non-Portable Template

```yaml
Resources:
  Bucket:
    Type: "AWS::S3::Bucket"
    Properties:
      BucketName: "accatpics1333333337"
  Instance:
    Type: "AWS::EC2::Instance"
    Properties:
      InstanceType: "t2.micro"
      ImageId: "ami-090fa75af13c156b4"
```

**Explanation:**

- `BucketName` is explicitly defined. **Problem**: Must be globally unique across AWS.
- `ImageId` is hardcoded. **Problem**: May not work in different regions.

### 2. Portable Stage 1 Template

```yaml
Resources:
  Bucket:
    Type: "AWS::S3::Bucket"
  Instance:
    Type: "AWS::EC2::Instance"
    Properties:
      InstanceType: "t2.micro"
      ImageId: "ami-090fa75af13c156b4"
```

**Changes:**

- Removed explicit bucket name. CloudFormation now auto-generates a unique bucket name.
- **Issue remaining**: Still hardcodes the AMI ID (still region-specific).

### 3. Portable Stage 2 Template

```yaml
Parameters:
  AMIID:
    Type: "String"
    Description: "AMI for EC2"

Resources:
  Bucket:
    Type: "AWS::S3::Bucket"
  Instance:
    Type: "AWS::EC2::Instance"
    Properties:
      InstanceType: "t2.micro"
      ImageId: !Ref "AMIID"
```

**Changes:**

- Introduced a **parameter** for AMI ID.
- **Benefits**:
  - Allows user input at deployment time.
  - Enables use in multiple regions (user must supply the correct AMI ID for the region).

**Line-by-line breakdown:**

- `Parameters:` - Start defining inputs for the template.
- `AMIID:` - Defines a parameter called `AMIID`.
- `Type: "String"` - Expects a string input.
- `Description: "AMI for EC2"` - Human-readable description.
- `ImageId: !Ref "AMIID"` - Retrieves the supplied AMI ID dynamically at deployment.

### 4. Portable Stage 3 Template (Best Practice)

```yaml
Parameters:
  LatestAmiId:
    Description: "AMI for EC2"
    Type: "AWS::SSM::Parameter::Value<AWS::EC2::Image::Id>"
    Default: "/aws/service/ami-amazon-linux-latest/amzn2-ami-hvm-x86_64-gp2"

Resources:
  Bucket:
    Type: "AWS::S3::Bucket"
  Instance:
    Type: "AWS::EC2::Instance"
    Properties:
      InstanceType: "t2.micro"
      ImageId: !Ref "LatestAmiId"
```

**Changes:**

- **Uses AWS Systems Manager (SSM) Parameter Store** to fetch the latest AMI ID automatically.
- Default value provided from AWS managed public parameters.

**Line-by-line breakdown:**

- `Parameters:` - Input section of the template.
- `LatestAmiId:` - Parameter name.
- `Description: "AMI for EC2"` - Explains purpose of parameter.
- `Type: 'AWS::SSM::Parameter::Value<AWS::EC2::Image::Id>'` - Tells CloudFormation to resolve a value from SSM Parameter Store.
- `Default: '/aws/service/ami-amazon-linux-latest/amzn2-ami-hvm-x86_64-gp2'` - AWS-managed latest Amazon Linux 2 AMI.
- `ImageId: !Ref "LatestAmiId"` - Automatically fetches the latest AMI ID at stack creation time.

## Key Problems in Non-Portable Templates

1. **Hardcoding Names**: Naming resources like S3 buckets manually prevents multiple deployments.
2. **Hardcoding Regional Values**: Hardcoded AMI IDs won't work across regions.
3. **Static Configuration**: Reduces template flexibility and reusability.

## Steps to Make Templates Portable

| Stage | Improvements Made                       | Result                            |
| :---- | :-------------------------------------- | :-------------------------------- |
| 1     | Removed hardcoded bucket name           | Unique names auto-generated       |
| 2     | Made AMI ID configurable via parameters | Works across regions (with input) |
| 3     | Dynamically reference AMI using SSM     | Fully automated, no manual input  |

## Best Practices for CloudFormation Portability

- **Avoid hardcoding resource names** where uniqueness is required (e.g., S3 buckets).
- **Avoid hardcoding regional values** like AMI IDs or Availability Zones.
- **Use Parameters** for user-supplied values when necessary.
- **Use AWS SSM Parameter Store** for dynamic values such as latest AMIs.
- **Allow CloudFormation to auto-assign names** wherever possible.

## Cleanup Instructions

Before proceeding:

- **Delete** any stacks you created during this demo in **us-east-1**.
- **Switch to us-east-2** and make sure no residual resources remain.
