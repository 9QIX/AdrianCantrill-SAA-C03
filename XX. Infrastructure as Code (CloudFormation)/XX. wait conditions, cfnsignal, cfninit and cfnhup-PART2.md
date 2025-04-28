# Deep Dive: CloudFormation with `cfn-init`, `cfn-signal`, and `cfn-hup`

## Resources Used

- [AWS CloudFormation Updating Stacks](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html)
- [Lab Files (Download)](https://learn-cantrill-labs.s3.amazonaws.com/awscoursedemos/0049-aws-mixed-cloudformation-cfninitcfnsignalcfnhup/cfninitcfnsignalcfnhup.zip)

# Lab Overview

This lab explores configuring EC2 instances during provisioning using AWS CloudFormation's built-in tools:

- `cfn-init` (desired state application)
- `cfn-signal` (signaling success/failure back to CloudFormation)
- `cfn-hup` (listening for metadata changes to trigger reconfiguration)

Rather than placing complex logic into the `UserData` section, this method uses CloudFormation **metadata** to define the desired state.

# Part 1: Using `cfn-init` with `cfn-signal`

## Template Breakdown

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
```

- **LatestAmiId**: Retrieves the latest Amazon Linux 2 AMI ID from SSM Parameter Store.
- **Message**: Custom message to appear on the webpage.

```yaml
Resources:
  InstanceSecurityGroup:
    Type: "AWS::EC2::SecurityGroup"
    Properties:
      GroupDescription: Enable SSH and HTTP access via port 22 IPv4 & port 80 IPv4
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
```

- Opens ports 22 (SSH) and 80 (HTTP) to the world.

```yaml
Bucket:
  Type: "AWS::S3::Bucket"
```

- Creates a simple S3 bucket (not actively used here).

```yaml
Instance:
  Type: "AWS::EC2::Instance"
  Metadata:
    "AWS::CloudFormation::Init":
      config:
        packages:
          yum:
            httpd: []
        files:
          /var/www/html/index.html:
            content: !Sub |
              <html><head><title>Amazing test page</title></head><body><h1><center>${Message}</center></h1></body></html>
        commands:
          simulatebootstrap:
            command: "sleep 300"
        services:
          sysvinit:
            httpd:
              enabled: "true"
              ensureRunning: "true"
              files:
                - "/var/www/html/index.html"
```

- **`AWS::CloudFormation::Init`** block:
  - Installs Apache (`httpd`) via YUM.
  - Creates an HTML file with dynamic content (`${Message}`).
  - Simulates a long bootstrapping process (`sleep 300`).
  - Ensures the Apache service is **running** and **enabled**.

```yaml
CreationPolicy:
  ResourceSignal:
    Timeout: PT15M
```

- Waits for an instance signal for up to **15 minutes**.

```yaml
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
      /opt/aws/bin/cfn-init -v --stack ${AWS::StackId} --resource Instance --region ${AWS::Region}
      /opt/aws/bin/cfn-signal -e $? --stack ${AWS::StackId} --resource Instance --region ${AWS::Region}
```

- **`cfn-init`**: Applies the instance metadata configuration.
- **`cfn-signal`**: Sends success or failure to CloudFormation based on `cfn-init` execution.

## Key Learning Points

- Use `Metadata` to define the full desired configuration for EC2 instances.
- `cfn-init` reads this metadata and configures the system accordingly.
- `cfn-signal` ensures the CloudFormation stack only completes when bootstrapping is successful.

# Part 2: Adding `cfn-hup` for Dynamic Updates

## Template Breakdown (Extension of Part 1)

In addition to previous configuration:

```yaml
files:
  /etc/cfn/cfn-hup.conf:
    content: !Sub |
      [main]
      stack=${AWS::StackName}
      region=${AWS::Region}
      interval=1
      verbose=true
```

- **cfn-hup.conf**: Configures how often the instance checks for metadata changes (every 1 minute).

```yaml
/etc/cfn/hooks.d/cfn-auto-reloader.conf:
  content: !Sub |
    [cfn-auto-reloader-hook]
    triggers=post.update
    path=Resources.Instance.Metadata.AWS::CloudFormation::Init
    action=/opt/aws/bin/cfn-init -v --stack ${AWS::StackId} --resource Instance --region ${AWS::Region}
    runas=root
```

- **cfn-auto-reloader.conf**:
  - Trigger `cfn-init` whenever the `Metadata` of the instance changes.
  - Monitors the metadata path and applies changes automatically.

```yaml
services:
  sysvinit:
    cfn-hup:
      enabled: "true"
      ensureRunning: "true"
      files:
        - /etc/cfn/cfn-hup.conf
        - /etc/cfn/hooks.d/cfn-auto-reloader.conf
```

- Ensures `cfn-hup` runs persistently.

## Important Log Files

When diagnosing issues, several log files help:
| File | Purpose |
| ----------------------------- | ------------------------------------------------------- |
| `/var/log/cloud-init-output.log` | Outputs regular UserData execution results |
| `/var/log/cfn-init.log` | Details operations performed by `cfn-init` |
| `/var/log/cfn-init-cmd.log` | Specific commands run by `cfn-init` |
| `/var/log/cfn-hup.log` | Monitors updates caught by `cfn-hup` |

> Use `sudo cat <file>` if permission errors occur.

# Part 3: Key Diagnostics and Debugging Techniques

## Common Commands

```bash
# List log files
ls -la /var/log

# View cloud-init output
sudo cat /var/log/cloud-init-output.log

# View cfn-init operations
sudo cat /var/log/cfn-init.log

# View cfn-init commands output
sudo cat /var/log/cfn-init-cmd.log

# View cfn-hup output
sudo cat /var/log/cfn-hup.log
```

- `sudo` is often necessary because `/var/log` files are root-only readable.

# Part 4: Real-World Observations

## Without `cfn-hup`

- If you update parameters and re-apply a CloudFormation stack, the instance does **NOT** automatically apply configuration changes.
- Manual interventions (reboot, re-run `cfn-init`) would be needed.

## With `cfn-hup`

- When metadata changes, the `cfn-hup` daemon automatically detects the change.
- It re-applies configuration without needing manual intervention.

# Summary

| Feature      | Description                                                        |
| ------------ | ------------------------------------------------------------------ |
| `cfn-init`   | Configures the EC2 instance based on CloudFormation metadata.      |
| `cfn-signal` | Informs CloudFormation that bootstrapping completed successfully.  |
| `cfn-hup`    | Monitors instance metadata for updates and re-triggers `cfn-init`. |

- These tools allow powerful, declarative, and dynamic instance configuration **without embedding scripts into user data**.
- Helps keep CloudFormation templates **cleaner**, **more modular**, and **easy to update**.

# Next Steps

- Experiment with changing the `Message` parameter and updating the stack to observe `cfn-hup` reapplying the changes.
- Explore more complex bootstrapping workflows combining **CloudFormation**, **cfn-init**, and **CodeDeploy**.
