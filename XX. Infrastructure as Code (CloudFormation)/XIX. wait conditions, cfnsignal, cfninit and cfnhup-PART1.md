# AWS CloudFormation Demo Evolution: UserData, CFN-Signal, CFN-Init, CFN-Hup

## Resources Used

- [AWS CloudFormation Updating Stacks - Documentation](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html)
- [Cantrill Labs Demo Files](https://learn-cantrill-labs.s3.amazonaws.com/awscoursedemos/0049-aws-mixed-cloudformation-cfninitcfnsignalcfnhup/cfninitcfnsignalcfnhup.zip)

## CloudFormation Templates Overview

There are **four templates** used progressively to show the evolution:

1. `user_data.yaml`
2. `user_data_with_signal.yaml`
3. `cfn_init_with_signal.yaml`
4. `cfn_init_with_signal_and_cfn_hup.yaml`

This summary focuses on the **first two**:

- Basic UserData
- UserData + CFN-Signal

# 1. Basic `user_data.yaml`

## Purpose

- Deploy an EC2 instance with Apache (HTTPD) installed via **UserData**.
- No awareness of instance bootstrapping status by CloudFormation.

## YAML Template Breakdown

```yaml
Parameters:
  LatestAmiId:
    Description: "AMI for EC2"
    Type: "AWS::SSM::Parameter::Value<AWS::EC2::Image::Id>"
    Default: "/aws/service/ami-amazon-linux-latest/amzn2-ami-hvm-x86_64-gp2"

  Message:
    Description: "Message for HTML page"
    Default: "Cats are the best"
    Type: "String"

Resources:
  InstanceSecurityGroup:
    Type: "AWS::EC2::SecurityGroup"
    Properties:
      GroupDescription: Enable SSH and HTTP access via port 22 and 80
      SecurityGroupIngress:
        - Description: "Allow SSH IPv4 IN"
          IpProtocol: tcp
          FromPort: "22"
          ToPort: "22"
          CidrIp: "0.0.0.0/0"
        - Description: "Allow HTTP IPv4 IN"
          IpProtocol: tcp
          FromPort: "80"
          ToPort: "80"
          CidrIp: "0.0.0.0/0"

  Bucket:
    Type: "AWS::S3::Bucket"

  Instance:
    Type: "AWS::EC2::Instance"
    Properties:
      InstanceType: "t2.micro"
      ImageId: !Ref "LatestAmiId"
      SecurityGroupIds:
        - !Ref InstanceSecurityGroup
      Tags:
        - Key: Name
          Value: A4L-UserData Test
      UserData:
        Fn::Base64: !Sub |
          #!/bin/bash -xe
          yum -y update
          yum -y upgrade
          sleep 300
          yum install -y httpd
          systemctl enable httpd
          systemctl start httpd
          echo "<html><head><title>Amazing test page</title></head><body><h1><center>${Message}</center></h1></body></html>" > /var/www/html/index.html
```

## UserData Script Line-by-Line

| Command                               | Purpose                                                    |
| :------------------------------------ | :--------------------------------------------------------- |
| `#!/bin/bash -xe`                     | Bash script with debug/verbose output.                     |
| `yum -y update`                       | Update system package list.                                |
| `yum -y upgrade`                      | Upgrade all packages to latest versions.                   |
| `sleep 300`                           | Simulate long bootstrapping by sleeping for 5 minutes.     |
| `yum install -y httpd`                | Install Apache HTTP server.                                |
| `systemctl enable httpd`              | Enable Apache service to start on boot.                    |
| `systemctl start httpd`               | Start Apache service immediately.                          |
| `echo ... > /var/www/html/index.html` | Create a simple HTML page using the **Message** parameter. |

## Problems Identified

- **CloudFormation unaware of the bootstrapping process:** Stack shows `CREATE_COMPLETE` before EC2 is fully configured.
- **Updating UserData triggers instance stop/start:**  
  Changing UserData via parameters causes instance to stop → lose public IP → start → new IP assigned.
- **UserData is run only at launch:** Updates to UserData do not affect existing EC2 instance unless it is replaced.

# 2. `user_data_with_signal.yaml`

## Purpose

- Solve the **bootstrapping unawareness** issue.
- Make CloudFormation wait for the instance to finish bootstrapping before marking it as complete.

## YAML Template Breakdown

```yaml
Parameters:
  LatestAmiId:
    Description: "AMI for EC2"
    Type: "AWS::SSM::Parameter::Value<AWS::EC2::Image::Id>"
    Default: "/aws/service/ami-amazon-linux-latest/amzn2-ami-hvm-x86_64-gp2"

  Message:
    Description: "Message for HTML page"
    Default: "Cats are the best"
    Type: "String"

Resources:
  InstanceSecurityGroup:
    Type: "AWS::EC2::SecurityGroup"
    Properties:
      GroupDescription: Enable SSH and HTTP access via port 22 and 80
      SecurityGroupIngress:
        - Description: "Allow SSH IPv4 IN"
          IpProtocol: tcp
          FromPort: "22"
          ToPort: "22"
          CidrIp: "0.0.0.0/0"
        - Description: "Allow HTTP IPv4 IN"
          IpProtocol: tcp
          FromPort: "80"
          ToPort: "80"
          CidrIp: "0.0.0.0/0"

  Bucket:
    Type: "AWS::S3::Bucket"

  Instance:
    Type: "AWS::EC2::Instance"
    CreationPolicy:
      ResourceSignal:
        Timeout: PT15M
    Properties:
      InstanceType: "t2.micro"
      ImageId: !Ref "LatestAmiId"
      SecurityGroupIds:
        - !Ref InstanceSecurityGroup
      Tags:
        - Key: Name
          Value: A4L-UserData Test
      UserData:
        Fn::Base64: !Sub |
          #!/bin/bash -xe
          yum -y update
          yum -y upgrade
          sleep 300
          yum install -y httpd
          systemctl enable httpd
          systemctl start httpd
          echo "<html><head><title>Amazing test page</title></head><body><h1><center>${Message}</center></h1></body></html>" > /var/www/html/index.html
          /opt/aws/bin/cfn-signal -e $? --stack ${AWS::StackId} --resource Instance --region ${AWS::Region}
```

## Key Additions Explained

### `CreationPolicy`

```yaml
CreationPolicy:
  ResourceSignal:
    Timeout: PT15M
```

- Sets a **15-minute timeout** for the instance to send a signal back.
- CloudFormation waits for a success/failure signal before continuing.

### `cfn-signal` Command

```bash
/opt/aws/bin/cfn-signal -e $? --stack ${AWS::StackId} --resource Instance --region ${AWS::Region}
```

| Part                      | Purpose                                                                    |
| :------------------------ | :------------------------------------------------------------------------- |
| `/opt/aws/bin/cfn-signal` | AWS CLI helper tool to send signals.                                       |
| `-e $?`                   | Passes the exit code of the last command (Apache setup) to CloudFormation. |
| `--stack ${AWS::StackId}` | Sends signal to this CloudFormation stack.                                 |
| `--resource Instance`     | Tells CloudFormation which logical resource to update status for.          |
| `--region ${AWS::Region}` | Specifies the AWS Region.                                                  |

## Results

- CloudFormation **waits** for the EC2 instance to complete UserData successfully before marking `CREATE_COMPLETE`.
- If bootstrapping fails, **stack creation fails** too.
- **Instant availability** of the web page after the stack finishes.

# Conclusion

| Feature               | Basic UserData | UserData with Signal |
| :-------------------- | :------------- | :------------------- |
| Bootstrap Awareness   | No             | Yes                  |
| Stack Timing Accuracy | No             | Yes                  |
| Update Handling       | Poor           | Improved             |
| Failure Detection     | No             | Yes                  |

# Next Steps

- The next templates will move from **UserData** to **CFN-Init** and finally to **CFN-Hup** to dynamically handle updates without needing EC2 replacement.
