# CFN Init and CloudFormation Creation Policies

## Overview

This lesson focuses on deploying an EC2 instance with WordPress pre-installed using an advanced AWS CloudFormation template. Unlike traditional `UserData` scripts, this method leverages `CFN Init` and `Creation Policies` for a more robust and controlled deployment.

## Resources Used

1. **VPC Deployment**: [1-Click Deployment - VPC](https://console.aws.amazon.com/cloudformation/home?region=us-east-1#/stacks/create/review?templateURL=https://learn-cantrill-labs.s3.amazonaws.com/awscoursedemos/0033-aws-associate-cfninit/A4L_VPC_v2.yaml&stackName=A4LVPC)
2. **EC2 Instance Deployment with CFN Init**: [1-Click Deployment - EC2 CFN Init](https://console.aws.amazon.com/cloudformation/home?region=us-east-1#/stacks/create/review?templateURL=https://learn-cantrill-labs.s3.amazonaws.com/awscoursedemos/0033-aws-associate-cfninit/A4L_EC2_CFNINITWordpress_AL2023.yaml&stackName=A4LEC2CFNINIT)
3. **Lesson Commands**: [Lesson Commands](https://learn-cantrill-labs.s3.amazonaws.com/awscoursedemos/0033-aws-associate-cfninit/lesson_commands.txt)

## Key Concepts

### What is `CFN Init`?

- `CFN Init` is a CloudFormation helper script that allows for instance-level configuration management.
- Unlike `UserData`, `CFN Init` can manage desired state configurations using metadata defined in the CloudFormation template.
- Supports updates without requiring instance replacement.

### CloudFormation Creation Policies

- Creation policies create a **hold point** before marking a resource as `CREATE_COMPLETE`.
- Requires an explicit **success or failure signal** from the instance.
- Ensures complete and correct bootstrapping before the stack progresses.

## Deployment Process

### 1. Deploying the VPC

- Use the provided **VPC CloudFormation link**.
- Check the **acknowledgment box** and create the stack.
- Wait for the stack to reach `CREATE_COMPLETE` status.

### 2. Deploying the EC2 Instance with CFN Init

- Use the **EC2 CFN Init CloudFormation link**.
- Check the **acknowledgment box** and create the stack.
- CloudFormation will **pause** until `CFN Init` completes.
- The EC2 instance will send a **CFN signal** to indicate success.

## How CFN Init Works

### Logical Resource Creation Policy

- CloudFormation holds the creation process for **15 minutes**.
- Instance sends a **CFN Signal** upon successful bootstrapping.

### CFN Init Process

1. **Retrieve metadata** from the stack.
2. **Substitutes variables** like stack ID and region.
3. **Runs configuration sets**, which include multiple steps:
   - Install required software.
   - Configure instance settings.
   - Install and configure WordPress.

### Configuration Breakdown

#### CFN Init Metadata

```yaml
Metadata:
  AWS::CloudFormation::Init:
    configSets:
      WordPress_install:
        - install_cfn_software
        - install_configure_instance
        - install_wordpress
        - configure_wordpress
```

- Defines a `configSets` named `WordPress_install`.
- Each config key represents a step in the installation process.

#### Installing Software

```yaml
install_cfn_software:
  packages:
    yum:
      httpd: []
      mariadb: []
      wget: []
```

- Uses `yum` to install necessary packages like Apache and MariaDB.

#### Configuring the Instance

```yaml
install_configure_instance:
  files:
    /etc/update-motd.d/40-cow:
      content: |
        echo 'Welcome to WordPress on AWS!'
```

- Creates a custom **MOTD** (Message of the Day) on SSH login.

#### Installing WordPress

```yaml
install_wordpress:
  sources:
    /var/www/html: https://wordpress.org/latest.tar.gz
```

- Downloads and extracts WordPress into `/var/www/html`.

#### Configuring WordPress

```yaml
configure_wordpress:
  commands:
    set_permissions:
      command: "chown -R apache:apache /var/www/html"
```

- Sets proper file permissions for Apache.

### CloudFormation Signals

```bash
/opt/aws/bin/cfn-signal -e $? --stack MyStack --resource MyInstance --region us-east-1
```

- Sends success (`0`) or failure (`1`) to CloudFormation.
- CloudFormation waits for this signal before marking the instance as `CREATE_COMPLETE`.

## Verification

1. **Check the EC2 Instance**

   - Navigate to the EC2 console.
   - Copy the **public IP** and open it in a browser.
   - The WordPress installation screen should appear.

2. **Check CloudFormation Logs**
   ```bash
   cd /var/log
   cat cfn-init-cmd.log
   ```
   - Shows detailed execution logs for `CFN Init`.

## Cleanup

1. **Delete the EC2 CFN Init Stack**.
2. **Delete the VPC Stack**.
3. Ensure the AWS account returns to its initial state.

## Summary

- **CFN Init** provides an alternative to `UserData`, allowing better configuration management.
- **Creation Policies** ensure CloudFormation waits for successful instance configuration.
- **CFN Signals** explicitly confirm instance readiness before proceeding.
- **CFNHUP** enables automatic updates if metadata changes.

This method offers a **more reliable, scalable, and maintainable** way to configure EC2 instances via CloudFormation.

# Cloudformation Template

## **1. A4LVPC (Animals4Life VPC Template)**

```json
Description:  Animals4Life base VPC Template
Resources:
  VPC:
    Type: AWS::EC2::VPC
    Properties:
      CidrBlock: 10.16.0.0/16
      EnableDnsSupport: true
      EnableDnsHostnames: true
      Tags:
        - Key: Name
          Value: a4l-vpc1
  IPv6CidrBlock:
    Type: AWS::EC2::VPCCidrBlock
    Properties:
      VpcId: !Ref VPC
      AmazonProvidedIpv6CidrBlock: true
  InternetGateway:
    Type: 'AWS::EC2::InternetGateway'
    Properties:
      Tags:
      - Key: Name
        Value: A4L-vpc1-igw
  InternetGatewayAttachment:
    Type: 'AWS::EC2::VPCGatewayAttachment'
    Properties:
      VpcId: !Ref VPC
      InternetGatewayId: !Ref InternetGateway
  RouteTableWeb:
    Type: 'AWS::EC2::RouteTable'
    Properties:
      VpcId: !Ref VPC
      Tags:
      - Key: Name
        Value: A4L-vpc1-rt-web
  RouteTableWebDefaultIPv4:
    Type: 'AWS::EC2::Route'
    DependsOn: InternetGatewayAttachment
    Properties:
      RouteTableId:
        Ref: RouteTableWeb
      DestinationCidrBlock: '0.0.0.0/0'
      GatewayId:
        Ref: InternetGateway
  RouteTableWebDefaultIPv6:
    Type: 'AWS::EC2::Route'
    DependsOn: InternetGatewayAttachment
    Properties:
      RouteTableId:
        Ref: RouteTableWeb
      DestinationIpv6CidrBlock: '::/0'
      GatewayId:
        Ref: InternetGateway
  RouteTableAssociationWebA:
    Type: 'AWS::EC2::SubnetRouteTableAssociation'
    Properties:
      SubnetId: !Ref SubnetWEBA
      RouteTableId:
        Ref: RouteTableWeb
  RouteTableAssociationWebB:
    Type: 'AWS::EC2::SubnetRouteTableAssociation'
    Properties:
      SubnetId: !Ref SubnetWEBB
      RouteTableId:
        Ref: RouteTableWeb
  RouteTableAssociationWebC:
    Type: 'AWS::EC2::SubnetRouteTableAssociation'
    Properties:
      SubnetId: !Ref SubnetWEBC
      RouteTableId:
        Ref: RouteTableWeb
  SubnetReservedA:
    Type: AWS::EC2::Subnet
    DependsOn: IPv6CidrBlock
    Properties:
      VpcId: !Ref VPC
      AvailabilityZone: !Select [ 0, !GetAZs '' ]
      CidrBlock: 10.16.0.0/20
      AssignIpv6AddressOnCreation: true
      Ipv6CidrBlock:
        Fn::Sub:
          - "${VpcPart}${SubnetPart}"
          - SubnetPart: '00::/64'
            VpcPart: !Select [ 0, !Split [ '00::/56', !Select [ 0, !GetAtt VPC.Ipv6CidrBlocks ]]]
      Tags:
        - Key: Name
          Value: sn-reserved-A
  SubnetReservedB:
    Type: AWS::EC2::Subnet
    DependsOn: IPv6CidrBlock
    Properties:
      VpcId: !Ref VPC
      AvailabilityZone: !Select [ 1, !GetAZs '' ]
      CidrBlock: 10.16.64.0/20
      AssignIpv6AddressOnCreation: true
      Ipv6CidrBlock:
        Fn::Sub:
          - "${VpcPart}${SubnetPart}"
          - SubnetPart: '04::/64'
            VpcPart: !Select [ 0, !Split [ '00::/56', !Select [ 0, !GetAtt VPC.Ipv6CidrBlocks ]]]
      Tags:
        - Key: Name
          Value: sn-reserved-B
  SubnetReservedC:
    Type: AWS::EC2::Subnet
    DependsOn: IPv6CidrBlock
    Properties:
      VpcId: !Ref VPC
      AvailabilityZone: !Select [ 2, !GetAZs '' ]
      CidrBlock: 10.16.128.0/20
      AssignIpv6AddressOnCreation: true
      Ipv6CidrBlock:
        Fn::Sub:
          - "${VpcPart}${SubnetPart}"
          - SubnetPart: '08::/64'
            VpcPart: !Select [ 0, !Split [ '00::/56', !Select [ 0, !GetAtt VPC.Ipv6CidrBlocks ]]]
      Tags:
        - Key: Name
          Value: sn-reserved-C
  SubnetDBA:
    Type: AWS::EC2::Subnet
    DependsOn: IPv6CidrBlock
    Properties:
      VpcId: !Ref VPC
      AvailabilityZone: !Select [ 0, !GetAZs '' ]
      CidrBlock: 10.16.16.0/20
      AssignIpv6AddressOnCreation: true
      Ipv6CidrBlock:
        Fn::Sub:
          - "${VpcPart}${SubnetPart}"
          - SubnetPart: '01::/64'
            VpcPart: !Select [ 0, !Split [ '00::/56', !Select [ 0, !GetAtt VPC.Ipv6CidrBlocks ]]]
      Tags:
        - Key: Name
          Value: sn-db-A
  SubnetDBB:
    Type: AWS::EC2::Subnet
    DependsOn: IPv6CidrBlock
    Properties:
      VpcId: !Ref VPC
      AvailabilityZone: !Select [ 1, !GetAZs '' ]
      CidrBlock: 10.16.80.0/20
      AssignIpv6AddressOnCreation: true
      Ipv6CidrBlock:
        Fn::Sub:
          - "${VpcPart}${SubnetPart}"
          - SubnetPart: '05::/64'
            VpcPart: !Select [ 0, !Split [ '00::/56', !Select [ 0, !GetAtt VPC.Ipv6CidrBlocks ]]]
      Tags:
        - Key: Name
          Value: sn-db-B
  SubnetDBC:
    Type: AWS::EC2::Subnet
    DependsOn: IPv6CidrBlock
    Properties:
      VpcId: !Ref VPC
      AvailabilityZone: !Select [ 2, !GetAZs '' ]
      CidrBlock: 10.16.144.0/20
      AssignIpv6AddressOnCreation: true
      Ipv6CidrBlock:
        Fn::Sub:
          - "${VpcPart}${SubnetPart}"
          - SubnetPart: '09::/64'
            VpcPart: !Select [ 0, !Split [ '00::/56', !Select [ 0, !GetAtt VPC.Ipv6CidrBlocks ]]]
      Tags:
        - Key: Name
          Value: sn-db-C
  SubnetAPPA:
    Type: AWS::EC2::Subnet
    DependsOn: IPv6CidrBlock
    Properties:
      VpcId: !Ref VPC
      AvailabilityZone: !Select [ 0, !GetAZs '' ]
      CidrBlock: 10.16.32.0/20
      AssignIpv6AddressOnCreation: true
      Ipv6CidrBlock:
        Fn::Sub:
          - "${VpcPart}${SubnetPart}"
          - SubnetPart: '02::/64'
            VpcPart: !Select [ 0, !Split [ '00::/56', !Select [ 0, !GetAtt VPC.Ipv6CidrBlocks ]]]
      Tags:
        - Key: Name
          Value: sn-app-A
  SubnetAPPB:
    Type: AWS::EC2::Subnet
    DependsOn: IPv6CidrBlock
    Properties:
      VpcId: !Ref VPC
      AvailabilityZone: !Select [ 1, !GetAZs '' ]
      CidrBlock: 10.16.96.0/20
      AssignIpv6AddressOnCreation: true
      Ipv6CidrBlock:
        Fn::Sub:
          - "${VpcPart}${SubnetPart}"
          - SubnetPart: '06::/64'
            VpcPart: !Select [ 0, !Split [ '00::/56', !Select [ 0, !GetAtt VPC.Ipv6CidrBlocks ]]]
      Tags:
        - Key: Name
          Value: sn-app-B
  SubnetAPPC:
    Type: AWS::EC2::Subnet
    DependsOn: IPv6CidrBlock
    Properties:
      VpcId: !Ref VPC
      AvailabilityZone: !Select [ 2, !GetAZs '' ]
      CidrBlock: 10.16.160.0/20
      AssignIpv6AddressOnCreation: true
      Ipv6CidrBlock:
        Fn::Sub:
          - "${VpcPart}${SubnetPart}"
          - SubnetPart: '0A::/64'
            VpcPart: !Select [ 0, !Split [ '00::/56', !Select [ 0, !GetAtt VPC.Ipv6CidrBlocks ]]]
      Tags:
        - Key: Name
          Value: sn-app-C
  SubnetWEBA:
    Type: AWS::EC2::Subnet
    DependsOn: IPv6CidrBlock
    Properties:
      VpcId: !Ref VPC
      AvailabilityZone: !Select [ 0, !GetAZs '' ]
      CidrBlock: 10.16.48.0/20
      MapPublicIpOnLaunch: true
      Ipv6CidrBlock:
        Fn::Sub:
          - "${VpcPart}${SubnetPart}"
          - SubnetPart: '03::/64'
            VpcPart: !Select [ 0, !Split [ '00::/56', !Select [ 0, !GetAtt VPC.Ipv6CidrBlocks ]]]
      Tags:
        - Key: Name
          Value: sn-web-A
  SubnetWEBB:
    Type: AWS::EC2::Subnet
    DependsOn: IPv6CidrBlock
    Properties:
      VpcId: !Ref VPC
      AvailabilityZone: !Select [ 1, !GetAZs '' ]
      CidrBlock: 10.16.112.0/20
      MapPublicIpOnLaunch: true
      Ipv6CidrBlock:
        Fn::Sub:
          - "${VpcPart}${SubnetPart}"
          - SubnetPart: '07::/64'
            VpcPart: !Select [ 0, !Split [ '00::/56', !Select [ 0, !GetAtt VPC.Ipv6CidrBlocks ]]]
      Tags:
        - Key: Name
          Value: sn-web-B
  SubnetWEBC:
    Type: AWS::EC2::Subnet
    DependsOn: IPv6CidrBlock
    Properties:
      VpcId: !Ref VPC
      AvailabilityZone: !Select [ 2, !GetAZs '' ]
      CidrBlock: 10.16.176.0/20
      MapPublicIpOnLaunch: true
      Ipv6CidrBlock:
        Fn::Sub:
          - "${VpcPart}${SubnetPart}"
          - SubnetPart: '0B::/64'
            VpcPart: !Select [ 0, !Split [ '00::/56', !Select [ 0, !GetAtt VPC.Ipv6CidrBlocks ]]]
      Tags:
        - Key: Name
          Value: sn-web-C
  IPv6WorkaroundSubnetWEBA:
    Type: Custom::SubnetModify
    Properties:
      ServiceToken: !GetAtt IPv6WorkaroundLambda.Arn
      SubnetId: !Ref SubnetWEBA
  IPv6WorkaroundSubnetWEBB:
    Type: Custom::SubnetModify
    Properties:
      ServiceToken: !GetAtt IPv6WorkaroundLambda.Arn
      SubnetId: !Ref SubnetWEBB
  IPv6WorkaroundSubnetWEBC:
    Type: Custom::SubnetModify
    Properties:
      ServiceToken: !GetAtt IPv6WorkaroundLambda.Arn
      SubnetId: !Ref SubnetWEBC
  IPv6WorkaroundRole:
    Type: AWS::IAM::Role
    Properties:
      AssumeRolePolicyDocument:
        Version: '2012-10-17'
        Statement:
        - Effect: Allow
          Principal:
            Service:
            - lambda.amazonaws.com
          Action:
          - sts:AssumeRole
      Path: "/"
      Policies:
        - PolicyName: !Sub "ipv6-fix-logs-${AWS::StackName}"
          PolicyDocument:
            Version: '2012-10-17'
            Statement:
            - Effect: Allow
              Action:
              - logs:CreateLogGroup
              - logs:CreateLogStream
              - logs:PutLogEvents
              Resource: arn:aws:logs:*:*:*
        - PolicyName: !Sub "ipv6-fix-modify-${AWS::StackName}"
          PolicyDocument:
            Version: '2012-10-17'
            Statement:
            - Effect: Allow
              Action:
              - ec2:ModifySubnetAttribute
              Resource: "*"
  IPv6WorkaroundLambda:
    Type: AWS::Lambda::Function
    Properties:
      Handler: "index.lambda_handler"
      Code: #import cfnresponse below required to send respose back to CFN
        ZipFile:
          Fn::Sub: |
            import cfnresponse
            import boto3

            def lambda_handler(event, context):
                if event['RequestType'] is 'Delete':
                  cfnresponse.send(event, context, cfnresponse.SUCCESS)
                  return

                responseValue = event['ResourceProperties']['SubnetId']
                ec2 = boto3.client('ec2', region_name='${AWS::Region}')
                ec2.modify_subnet_attribute(AssignIpv6AddressOnCreation={
                                                'Value': True
                                              },
                                              SubnetId=responseValue)
                responseData = {}
                responseData['SubnetId'] = responseValue
                cfnresponse.send(event, context, cfnresponse.SUCCESS, responseData, "CustomResourcePhysicalID")
      Runtime: python3.9
      Role: !GetAtt IPv6WorkaroundRole.Arn
      Timeout: 30
  DefaultInstanceSecurityGroup:
    Type: 'AWS::EC2::SecurityGroup'
    Properties:
      VpcId: !Ref VPC
      GroupDescription: Enable SSH access via port 22 IPv4 & v6
      SecurityGroupIngress:
        - Description: 'Allow SSH IPv4 IN'
          IpProtocol: tcp
          FromPort: '22'
          ToPort: '22'
          CidrIp: '0.0.0.0/0'
        - Description: 'Allow HTTP IPv4 IN'
          IpProtocol: tcp
          FromPort: '80'
          ToPort: '80'
          CidrIp: '0.0.0.0/0'
        - Description: 'Allow SSH IPv6 IN'
          IpProtocol: tcp
          FromPort: '22'
          ToPort: '22'
          CidrIpv6: ::/0
Outputs:
  a4lvpc1:
    Description: Animals4Life VPC1_ID
    Value: !Ref VPC
    Export:
      Name: a4l-vpc1
  a4lvpc1subnetweba:
    Description: Animals4Life VPC1 SubnetWEBA
    Value: !Ref SubnetWEBA
    Export:
      Name: a4l-vpc1-subnet-weba
  a4lvpc1subnetwebb:
    Description: Animals4Life VPC1 SubnetWEBB
    Value: !Ref SubnetWEBB
    Export:
      Name: a4l-vpc1-subnet-webb
  a4lvpc1subnetwebc:
    Description: Animals4Life VPC1 SubnetWEBC
    Value: !Ref SubnetWEBC
    Export:
      Name: a4l-vpc1-subnet-webc
  a4lvpc1subnetappa:
    Description: Animals4Life VPC1 SubnetAPPA
    Value: !Ref SubnetAPPA
    Export:
      Name: a4l-vpc1-subnet-appa
  a4lvpc1subnetappb:
    Description: Animals4Life VPC1 SubnetAPPB
    Value: !Ref SubnetAPPB
    Export:
      Name: a4l-vpc1-subnet-appb
  a4lvpc1subnetappc:
    Description: Animals4Life VPC1 SubnetAPPC
    Value: !Ref SubnetAPPC
    Export:
      Name: a4l-vpc1-subnet-appc
  a4lvpc1subnetdba:
    Description: Animals4Life VPC1 SubnetDBA
    Value: !Ref SubnetDBA
    Export:
      Name: a4l-vpc1-subnet-dba
  a4lvpc1subnetdbb:
    Description: Animals4Life VPC1 SubnetDBB
    Value: !Ref SubnetDBB
    Export:
      Name: a4l-vpc1-subnet-dbb
  a4lvpc1subnetdbc:
    Description: Animals4Life VPC1 SubnetDBC
    Value: !Ref SubnetDBC
    Export:
      Name: a4l-vpc1-subnet-dbc
  a4lvpc1subnetreserveda:
    Description: Animals4Life VPC1 SubnetReservedA
    Value: !Ref SubnetReservedA
    Export:
      Name: a4l-vpc1-subnet-reserveda
  a4lvpc1subnetreservedb:
    Description: Animals4Life VPC1 SubnetReservedB
    Value: !Ref SubnetReservedB
    Export:
      Name: a4l-vpc1-subnet-reservedb
  a4lvpc1subnetreservedc:
    Description: Animals4Life VPC1 SubnetReservedC
    Value: !Ref SubnetReservedC
    Export:
      Name: a4l-vpc1-subnet-reservedc
  a4lvpc1defaultinstancesg:
    Description: Animals4Life VPC1 Default Instance SecurityGroup
    Value: !Ref DefaultInstanceSecurityGroup
    Export:
      Name: a4l-vpc1-default-instance-sg
```

### **VPC and Networking Components**

- **VPC**: Creates a Virtual Private Cloud (VPC) with a primary **IPv4 CIDR block (10.16.0.0/16)** and enables **IPv6 support**.
- **IPv6CidrBlock**: Assigns an **Amazon-provided IPv6 block** to the VPC.
- **InternetGateway & Attachment**: Adds an **Internet Gateway (IGW)** for external internet access and attaches it to the VPC.

### **Subnets (IPv4 and IPv6 enabled)**

This template creates **multiple subnets** across three availability zones (AZs). These subnets are categorized into:

- **Reserved subnets** (`sn-reserved-*`) for future use.
- **Database subnets** (`sn-db-*`) for database instances.
- **Application subnets** (`sn-app-*`) for application servers.
- **Web subnets** (`sn-web-*`) for web servers (public-facing).
- **IPv6 Fix for Web Subnets**: Since IPv6 auto-assignment isn't enabled by default, a **Lambda function** (`IPv6WorkaroundLambda`) modifies subnets to allow IPv6 address auto-assignment.

### **Route Table & Routing**

- **RouteTableWeb**: A route table for web subnets.
- **Default IPv4 Route (0.0.0.0/0)**: Sends traffic to the **Internet Gateway**.
- **Default IPv6 Route (::/0)**: Allows IPv6 traffic to the **Internet Gateway**.
- **RouteTableAssociation**: Associates the route table with **public subnets (WebA, WebB, WebC)** to enable internet access.

### **Security Group**

- **DefaultInstanceSecurityGroup**: Allows incoming **SSH (22)** and **HTTP (80)** traffic from both **IPv4 (0.0.0.0/0)** and **IPv6 (::/0)**.

### **Outputs**

Exports the **VPC ID, subnet IDs, and security group ID** so they can be used by other CloudFormation stacks.

## **2. A4LEC2CFNINIT (EC2 for WordPress Installation)**

```json
Description:  A4L CFN-INIT Wordpress Template
  Requires A4L VPC Template to run
Parameters:
  LatestAmiId:
    Description: AMI for Instance (default is latest AmaLinux2023)
    Type: 'AWS::SSM::Parameter::Value<AWS::EC2::Image::Id>'
    Default: '/aws/service/ami-amazon-linux-latest/al2023-ami-kernel-default-x86_64'
  DBName:
    AllowedPattern: '[a-zA-Z][a-zA-Z0-9]*'
    ConstraintDescription: must begin with a letter and contain only alphanumeric
      characters.
    Default: a4lwordpress
    Description: The WordPress database name
    MaxLength: '64'
    MinLength: '1'
    Type: String
  DBPassword:
    AllowedPattern: '[a-zA-Z0-9]*'
    ConstraintDescription: must contain only alphanumeric characters.
    Description: The WordPress database admin account password
    MaxLength: '41'
    MinLength: '8'
    NoEcho: 'true'
    Default: 'Sup3rS3cr3tP4ssw0rd'
    Type: String
  DBRootPassword:
    AllowedPattern: '[a-zA-Z0-9]*'
    ConstraintDescription: must contain only alphanumeric characters.
    Description: MySQL root password
    MaxLength: '41'
    MinLength: '8'
    NoEcho: 'true'
    Default: 'Sup3rS3cr3tP4ssw0rd'
    Type: String
  DBUser:
    AllowedPattern: '[a-zA-Z][a-zA-Z0-9]*'
    ConstraintDescription: must begin with a letter and contain only alphanumeric
      characters.
    Description: The WordPress database admin account username
    Default: a4lwordpress
    MaxLength: '16'
    MinLength: '1'
    Type: String
Resources:
  EC2Instance:
    Type: AWS::EC2::Instance
    CreationPolicy:
      ResourceSignal:
        Timeout: PT15M
    Metadata:
      AWS::CloudFormation::Init:
        configSets:
          wordpress_install:
            - install_cfn
            - software_install
            - configure_instance
            - install_wordpress
            - configure_wordpress
        install_cfn:
          files:
            /etc/cfn/cfn-hup.conf:
              content: !Sub |
                [main]
                stack= ${AWS::StackId}
                region=${AWS::Region}
              group: root
              mode: '000400'
              owner: root
            /etc/cfn/hooks.d/cfn-auto-reloader.conf:
              content: !Sub |
                [cfn-auto-reloader-hook]
                triggers=post.update
                path=Resources.EC2Instance.Metadata.AWS::CloudFormation::Init
                action=/opt/aws/bin/cfn-init -v --stack ${AWS::StackName} --resource EC2Instance --configsets wordpress_install --region ${AWS::Region}
              group: root
              mode: '000400'
              owner: root
          services:
            sysvinit:
              cfn-hup:
                enabled: true
                ensureRunning: true
                files:
                - /etc/cfn/cfn-hup.conf
                - /etc/cfn/hooks.d/cfn-auto-reloader.conf
        software_install:
          commands:
            0_manual_installs:
              command: dnf install wget php-mysqlnd httpd php-fpm php-mysqli mariadb105-server php-json php php-devel cowsay -y
          services:
            sysvinit:
              httpd:
                enabled: true
                ensureRunning: true
              mariadb:
                enabled: true
                ensureRunning: true
        configure_instance:
          files:
            /etc/update-motd.d/40-cow:
              content: !Sub |
                #!/bin/sh
                cowsay "Amazon Linux 2023 AMI - Animals4Life"
              group: root
              mode: '000755'
              owner: root
          commands:
            01_set_mysql_root_password:
              command: !Sub |
                mysqladmin -u root password '${DBRootPassword}'
              test: !Sub |
                $(mysql ${DBName} -u root --password='${DBRootPassword}' >/dev/null 2>&1 </dev/null); (( $? != 0 ))
            02_updatemotd:
              command: update-motd
        install_wordpress:
          sources:
            /var/www/html: http://wordpress.org/latest.tar.gz
          files:
            /tmp/create-wp-config:
              content: !Sub |
                #!/bin/bash -xe
                cp /var/www/html/wp-config-sample.php /var/www/html/wp-config.php
                sed -i "s/'database_name_here'/'${DBName}'/g" wp-config.php
                sed -i "s/'username_here'/'${DBUser}'/g" wp-config.php
                sed -i "s/'password_here'/'${DBPassword}'/g" wp-config.php
              group: root
              mode: '000500'
              owner: root
            /tmp/db.setup:
              content: !Sub |
                CREATE DATABASE ${DBName};
                CREATE USER '${DBUser}'@'localhost' IDENTIFIED BY '${DBPassword}';
                GRANT ALL ON ${DBName}.* TO '${DBUser}'@'localhost';
                FLUSH PRIVILEGES;
              group: root
              mode: '000400'
              owner: root
        configure_wordpress:
          files:
            /tmp/permissionsfix:
              content: !Sub |
                usermod -a -G apache ec2-user
                chown -R ec2-user:apache /var/www
                chmod 2775 /var/www
                find /var/www -type d -exec chmod 2775 {} \;
                find /var/www -type f -exec chmod 0664 {} \;
              group: root
              mode: '000500'
              owner: root
          commands:
            01_create_database:
              command: !Sub |
                mysql -u root --password='${DBRootPassword}' < /tmp/db.setup
              test: !Sub |
                $(mysql ${DBName} -u root --password='${DBRootPassword}' >/dev/null 2>&1 </dev/null); (( $? !=0))
            02_move_wordpress:
              command: !Sub |
                cp -rvf /var/www/html/wordpress/* /var/www/html/
            03_tidyup:
              command: !Sub |
                rm -R /var/www/html/wordpress
            04_configure_wordpress:
              command: /tmp/create-wp-config
              cwd: /var/www/html
            04_fix_permissions:
              command: /tmp/permissionsfix
    Properties:
      InstanceType: "t2.micro"
      ImageId: !Ref LatestAmiId
      SubnetId: !ImportValue a4l-vpc1-subnet-weba
      SecurityGroupIds:
        - !ImportValue a4l-vpc1-default-instance-sg
      Tags:
        - Key: Name
          Value: A4L-Wordpress
      UserData:
        Fn::Base64: !Sub |
          #!/bin/bash -xe
          /opt/aws/bin/cfn-init -v --stack ${AWS::StackId} --resource EC2Instance --configsets wordpress_install --region ${AWS::Region}
          /opt/aws/bin/cfn-signal -e $? --stack ${AWS::StackId} --resource EC2Instance --region ${AWS::Region}
```

### **Parameters**

- **AMI (Amazon Linux 2023)**: Uses the latest Amazon Linux AMI.
- **Database Name, User, Passwords**: WordPress database credentials (set as parameters).

### **EC2 Instance for WordPress**

- **Creates an EC2 instance** in the VPC (subnet not explicitly mentioned but assumed to be in a web or app subnet).
- **Uses AWS CloudFormation Init (CFN-INIT)** to install and configure:

  - `install_cfn`: AWS CloudFormation helper scripts.
  - `software_install`: Required software (Apache, PHP, MySQL, etc.).
  - `configure_instance`: Configures the EC2 instance settings.
  - `install_wordpress`: Downloads and installs WordPress.
  - `configure_wordpress`: Sets up the WordPress configuration file.

- **Signals completion to CloudFormation** (`CreationPolicy -> ResourceSignal`) to ensure setup completes within **15 minutes**.

## **Summary**

### **This CloudFormation template does the following:**

1. **Creates a VPC** with **IPv4 and IPv6 support**, an **Internet Gateway**, and proper routing.
2. **Defines multiple subnets** for reserved, database, app, and web layers across **3 availability zones**.
3. **Configures public subnets** to allow internet access via **IPv6 workaround (Lambda function)**.
4. **Creates a Security Group** to allow SSH (22) and HTTP (80) traffic.
5. **Deploys an EC2 instance** to install **WordPress**, configure the database, and complete the setup using **CloudFormation Init**.

This setup provides a **scalable and well-structured AWS architecture** for hosting a WordPress site in a **secure, multi-AZ environment**.
