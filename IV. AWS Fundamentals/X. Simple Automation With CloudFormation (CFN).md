# AWS CloudFormation Demo: Creating and Deleting an EC2 Instance

This lesson demonstrates how to use **AWS CloudFormation** to create and delete an **EC2 instance** within AWS. It provides a step-by-step guide for using a pre-defined CloudFormation template, including key concepts such as parameters, resources, outputs, and how to automate infrastructure management in AWS.

## Prerequisites

- Ensure you are logged into your **AWS account**.
- Select the **Northern Virginia (us-east-1)** region.
- Access the **CloudFormation console**.

## Steps to Create Resources Using CloudFormation

### 1. **Access the CloudFormation Console**

CloudFormation operates around the concepts of **stacks** and **templates**. A stack consists of AWS resources defined in a template.

### 2. **Download and Upload the CloudFormation Template**

- Use the provided template:
  [EC2 Instance Template](https://learn-cantrill-labs.s3.amazonaws.com/awscoursedemos/0058-aws-simplecfn/ec2instance.yaml)
- Download the template and upload it to the CloudFormation console.

### 3. **Template Overview**

The CloudFormation template contains three main sections:

- **Parameters**: Define user inputs that the template can dynamically adjust, such as:

  - `LatestAmiId`: Retrieves the latest Amazon Linux 2023 AMI.
  - `SSHandWebLocation`: Defines an IP address range for SSH access to the EC2 instance.

- **Resources**: The key resources created by this template:

  - **EC2 Instance**: A `t2.micro` instance type.
  - **Security Group**: Allows SSH (port 22) and HTTP (port 80) access to the instance.
  - **IAM Roles**: These roles allow session management using AWS **Session Manager**.

- **Outputs**: The output values once the stack is created, including:
  - `InstanceId`, `AZ` (Availability Zone), `PublicDNS`, and `PublicIP`.

### 4. **Review and Configure the Stack**

- After uploading the template, configure the parameters:

  - **AMI ID**: Automatically retrieves the latest Amazon Linux 2023 AMI.
  - **SSH and Web Location**: Defaults to allowing SSH from any IP (`0.0.0.0/0`).

- Name the stack as `CFN Demo 1`, leave the default values, and click **Next**.

### 5. **IAM Role and Permissions**

Certain resources in CloudFormation require explicit acknowledgment. In this template, an **IAM role** is created to allow EC2 instance session management.

- Acknowledge the permissions and click **Submit**.

### 6. **Monitor Stack Creation**

- The stack creation process will begin. You can monitor its progress by refreshing the **events**.
- Each resource will transition from `Create in Progress` to `Create Complete`.
- Once the EC2 instance is created, you can check its outputs, which include the **InstanceId**, **PublicDNS**, **AZ**, and **PublicIP**.

## Connecting to the EC2 Instance

Once the instance is running, you can connect via **AWS Session Manager** instead of using SSH and key pairs:

- Navigate to the **EC2 dashboard**.
- Select the instance and click **Connect**.
- Choose the **Session Manager** option, which allows connecting without using SSH keys.
- Use the standard Linux commands once connected.

## Deleting the Stack

Once the demo is complete, you can delete the resources:

1. Navigate to the **CloudFormation console**.
2. Select the stack `CFN Demo 1` and choose **Delete**.
3. CloudFormation will clean up all resources (EC2 instance, security group, etc.) and terminate the stack.

## Key CloudFormation Benefits

- **Automated and Consistent Provisioning**: Using a template ensures repeatable and consistent infrastructure.
- **Portable**: Templates can be used across different AWS regions.
- **Clean Up**: Deleting the stack removes all associated resources, ensuring your account remains tidy and free of unnecessary charges.

## Template

Here’s the template used for this demo:

```yaml
Parameters:
  LatestAmiId:
    Type: "AWS::SSM::Parameter::Value<AWS::EC2::Image::Id>"
    Default: "/aws/service/ami-amazon-linux-latest/al2023-ami-kernel-default-x86_64"
  SSHandWebLocation:
    Description: The IP address range that can be used to SSH to the EC2 instances
    Type: String
    MinLength: "9"
    MaxLength: "18"
    Default: 0.0.0.0/0
    AllowedPattern: '(\d{1,3})\.(\d{1,3})\.(\d{1,3})\.(\d{1,3})/(\d{1,2})'
    ConstraintDescription: must be a valid IP CIDR range of the form x.x.x.x/x.
Resources:
  EC2Instance:
    Type: AWS::EC2::Instance
    Properties:
      InstanceType: "t2.micro"
      ImageId: !Ref LatestAmiId
      IamInstanceProfile: !Ref SessionManagerInstanceProfile
      SecurityGroups:
        - !Ref InstanceSecurityGroup
  InstanceSecurityGroup:
    Type: "AWS::EC2::SecurityGroup"
    Properties:
      GroupDescription: Enable SSH access via port 22 and 80
      SecurityGroupIngress:
        - IpProtocol: tcp
          FromPort: "22"
          ToPort: "22"
          CidrIp: !Ref SSHandWebLocation
        - IpProtocol: tcp
          FromPort: "80"
          ToPort: "80"
          CidrIp: !Ref SSHandWebLocation
  SessionManagerRole:
    Type: "AWS::IAM::Role"
    Properties:
      AssumeRolePolicyDocument:
        Version: 2012-10-17
        Statement:
          - Effect: Allow
            Principal:
              Service:
                - ec2.amazonaws.com
            Action:
              - "sts:AssumeRole"
      Path: /
      ManagedPolicyArns:
        - "arn:aws:iam::aws:policy/AmazonSSMManagedInstanceCore"
  SessionManagerInstanceProfile:
    Type: "AWS::IAM::InstanceProfile"
    Properties:
      Path: /
      Roles:
        - !Ref SessionManagerRole
Outputs:
  InstanceId:
    Description: InstanceId of the newly created EC2 instance
    Value: !Ref EC2Instance
  AZ:
    Description: Availability Zone of the newly created EC2 instance
    Value: !GetAtt
      - EC2Instance
      - AvailabilityZone
  PublicDNS:
    Description: Public DNSName of the newly created EC2 instance
    Value: !GetAtt
      - EC2Instance
      - PublicDnsName
  PublicIP:
    Description: Public IP address of the newly created EC2 instance
    Value: !GetAtt
      - EC2Instance
      - PublicIp
```

### Parameters

1. **LatestAmiId**:

   - **Type**: This specifies that the parameter is of type `AWS::SSM::Parameter::Value<AWS::EC2::Image::Id>`, meaning it references an Amazon Machine Image (AMI) ID stored in the AWS Systems Manager (SSM) Parameter Store.
   - **Default**: This is the default value, pointing to the latest Amazon Linux AMI.

2. **SSHandWebLocation**:
   - **Description**: A brief explanation of what this parameter represents, which is the IP address range allowed to SSH into the EC2 instances.
   - **Type**: Specifies that this parameter is a string.
   - **MinLength/MaxLength**: Sets the minimum and maximum character lengths for the string (9 to 18 characters).
   - **Default**: The default value is set to `0.0.0.0/0`, which allows access from any IP address (not recommended for production).
   - **AllowedPattern**: A regex pattern that defines the valid format for a CIDR notation IP range (e.g., `x.x.x.x/x`).
   - **ConstraintDescription**: Describes the requirement for the input to be a valid CIDR range.

### Resources

3. **EC2Instance**:

   - **Type**: Specifies that this resource is an EC2 instance.
   - **Properties**:
     - **InstanceType**: Specifies the instance type (`t2.micro`).
     - **ImageId**: References the `LatestAmiId` parameter to define which AMI to use.
     - **IamInstanceProfile**: References an IAM instance profile (`SessionManagerInstanceProfile`) for role permissions.
     - **SecurityGroups**: Associates the instance with a security group (`InstanceSecurityGroup`).

4. **InstanceSecurityGroup**:

   - **Type**: This resource is a security group.
   - **Properties**:
     - **GroupDescription**: A description of what this security group does.
     - **SecurityGroupIngress**: Defines the inbound rules:
       - **First Rule**: Allows TCP traffic on port 22 (SSH) from the IP range specified in `SSHandWebLocation`.
       - **Second Rule**: Allows TCP traffic on port 80 (HTTP) from the same IP range.

5. **SessionManagerRole**:

   - **Type**: This resource is an IAM role.
   - **Properties**:
     - **AssumeRolePolicyDocument**: Defines who can assume this role (EC2 instances).
     - **ManagedPolicyArns**: Attaches the AWS managed policy for SSM (Session Manager).

6. **SessionManagerInstanceProfile**:
   - **Type**: This resource is an IAM instance profile.
   - **Properties**:
     - **Roles**: Associates the `SessionManagerRole` with this profile.

### Outputs

7. **InstanceId**:

   - **Description**: Provides a description for the output (the ID of the created EC2 instance).
   - **Value**: Uses `!Ref` to get the reference to `EC2Instance`.

8. **AZ**:

   - **Description**: Describes the availability zone of the EC2 instance.
   - **Value**: Uses `!GetAtt` to retrieve the availability zone attribute of `EC2Instance`.

9. **PublicDNS**:

   - **Description**: Describes the public DNS name of the EC2 instance.
   - **Value**: Uses `!GetAtt` to retrieve the public DNS name.

10. **PublicIP**:
    - **Description**: Describes the public IP address of the EC2 instance.
    - **Value**: Uses `!GetAtt` to retrieve the public IP address.

## Conclusion

This demonstration illustrated how CloudFormation can be used to automate the creation of an EC2 instance and associated resources. Throughout the course, you will dive deeper into using CloudFormation for more advanced use cases, highlighting the power of Infrastructure as Code (IaC) on AWS.
