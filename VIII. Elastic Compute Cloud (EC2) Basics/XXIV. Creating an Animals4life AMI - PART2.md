# Creating an Animals4life AMI - PART2

## Resources Used

- **1-Click Deployment**  
  [AWS CloudFormation Template](https://console.aws.amazon.com/cloudformation/home?region=us-east-1#/stacks/create/review?templateURL=https://learn-cantrill-labs.s3.amazonaws.com/awscoursedemos/0007-aws-associate-ec2-ami-demo/A4L_VPC_PUBLICINSTANCE_AL2023.yaml&stackName=AMIDEMO)

- **Lesson Commands**  
  [Lesson Commands File](https://learn-cantrill-labs.s3.amazonaws.com/awscoursedemos/0007-aws-associate-ec2-ami-demo/lesson_commands_AL2023.txt)

- **EC2 WordPress Deployment**  
  [AWS CloudFormation Template](https://console.aws.amazon.com/cloudformation/home?region=us-east-1#/stacks/create/review?templateURL=https://learn-cantrill-labs.s3.amazonaws.com/awscoursedemos/0007-aws-associate-ec2-ami-demo/A4L_VPC_PUBLICINSTANCE.yaml&stackName=AMIDEMO)

## Overview

This lesson focuses on automating WordPress installation on AWS EC2 by creating a **custom Amazon Machine Image (AMI)**. The AMI includes WordPress pre-installed and pre-configured up to the "Create Site" stage, eliminating the need for manual setup each time an instance is launched. Additionally, the EC2 login screen is customized using `cowsay`, adding a fun, animal-themed banner.

## Steps Covered in the Lesson

### 1. Stopping the EC2 Instance

Before creating an AMI, the EC2 instance must be stopped to prevent consistency issues:

1. Navigate to **EC2 Instances** in the AWS Console.
2. Right-click on the target instance.
3. Select **Stop Instance** and confirm the action.
4. Wait for the instance status to change to `stopped`.

Stopping the instance ensures that the AMI is created from a stable state, avoiding potential data corruption or missing files.

### 2. Creating the AMI

Once the instance is stopped:

1. Right-click the instance → **Image and Templates** → **Create Image**.
2. Provide an AMI name (e.g., `animals-for-life-template-wordpress`).
3. The AMI creation process:
   - Takes a snapshot of all **Elastic Block Store (EBS) volumes** attached to the instance.
   - Creates a **block device mapping**, ensuring the new instances replicate the storage setup.
   - Uses the same **device IDs and volume configurations** as the original instance.
4. Click **Create Image**.
5. Monitor progress under **Elastic Block Store (EBS) → Snapshots**.
6. Wait for the AMI status to change from `pending` to `available`.

### 3. Launching an EC2 Instance from the AMI

Once the AMI is created, a new instance can be launched with all configurations pre-applied:

1. Navigate to **EC2 → AMIs**, select the new AMI, and click **Launch Instance**.
2. Configure:
   - Instance name: `instance-from-AMI`.
   - Security group: **AMI Demo Security Group**.
   - Storage: Defaults to the original instance’s settings.
3. Click **Launch Instance**.

This step eliminates the need to install and configure WordPress manually. Every new instance launched from this AMI is already pre-configured.

### 4. Connecting to the New Instance

1. Select the newly launched instance.
2. Click **Connect** → **EC2 Instance Connect**.
3. Change the default username from `root` to `ec2-user`.
4. Click **Connect**.
5. Upon login, a custom **cowsay banner** appears, confirming the customizations are applied.

### 5. Verifying WordPress Installation

1. Copy the instance’s **public IPv4 address** from the AWS console.
2. Open a web browser and enter the IP.
3. The WordPress installation screen should appear, confirming the setup is working.

### 6. Cleaning Up Resources

After completing the lesson:

1. **Terminate the instance**:
   - Navigate to **EC2 → Instances**.
   - Right-click on the instance launched from the AMI.
   - Click **Terminate Instance** and confirm.
2. **Delete the CloudFormation Stack**:
   - Navigate to **AWS CloudFormation**.
   - Select `AMI Demo Stack`.
   - Click **Delete** and confirm.
3. **Retain the AMI and Snapshots**:
   - These will be used in future lessons to demonstrate **AMI copying and sharing across regions**.

## Key Takeaways

- **Automating EC2 Deployments**:

  - Using AMIs speeds up EC2 instance creation by removing manual configuration steps.
  - Ensures consistency across multiple instances.

- **Best Practices for AMI Creation**:

  - Always stop the instance before creating an AMI.
  - Allow snapshots to complete before launching new instances.

- **Reusability**:

  - Once an AMI is created, it can be used to launch **hundreds or thousands of instances** with the exact same configuration.
  - Saves time and effort on repetitive setup tasks.

- **Customization**:
  - System banners (like `cowsay`) can be applied to personalize login experiences.

## Next Steps

- Explore **copying and sharing AMIs across AWS regions**.
- Compare AMI-based automation with other automation methods like **AWS Systems Manager, CloudFormation, and EC2 Image Builder**.

-
