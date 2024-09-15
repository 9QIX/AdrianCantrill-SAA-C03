# Creating and Connecting to an EC2 Instance: Detailed Guide

## Introduction

In this demo lesson, we will walk through the process of creating and connecting to an EC2 instance on AWS. This lesson is covered under the AWS Free Tier, ensuring that if you're using a new AWS account for this course, you will not incur any charges. We'll use the Northern Virginia region (US-East-1) for this demonstration.

## Steps to Create an EC2 Instance

### 1. Access the EC2 Console

1. **Log in to your AWS account** and ensure you have the Northern Virginia region selected.
2. **Navigate to the EC2 Console**:
   - Type `EC2` in the search box at the top of the AWS Management Console.
   - Select the EC2 service to open the EC2 console.

### 2. Create an SSH Key Pair

1. **Go to Key Pairs**:
   - In the left-hand menu, under "Network & Security", click on **Key Pairs**.
2. **Create a Key Pair**:
   - Click on **Create Key Pair**.
   - Name your key pair (e.g., `A4L` for Animals for Life) for consistency.
   - Choose the key pair type (default is RSA).
   - Select the file format for the private key:
     - **PEM** for MacOS, Linux, or modern Windows.
     - **PPK** if you are using an older version of Windows with PuTTY.
   - Click **Create Key Pair** and download the private key file. Store it securely, as you will only have one chance to download it.

### 3. Launch an EC2 Instance

1. **Start the Launch Instance Wizard**:

   - Click on **Instances** in the EC2 dashboard.
   - Click on **Launch Instances**.

2. **Configure Instance Details**:

   - **Name Your Instance**: Enter a name (e.g., "My First EC2 Instance").
   - **Choose an Amazon Machine Image (AMI)**: Select **Amazon Linux 2023** (or your preferred AMI). The default version is free tier eligible.
   - **Select an Instance Type**: Choose the instance type, typically `t2.micro` for free tier eligibility.
   - **Select a Key Pair**: Choose the key pair you created earlier (e.g., `A4L`).

3. **Configure Network Settings**:

   - **Default VPC**: Leave the default VPC selected.
   - **Auto-Assign Public IP**: Enable this option to allow public access to the instance.
   - **Configure Security Group**:
     - Create a new security group (e.g., "My First Instance SG").
     - Set rules to allow **SSH** access from anywhere (`0.0.0.0/0`).

4. **Configure Storage**:

   - Default storage is typically an 8 GiB GP3 root volume. You can leave this as default.

5. **Review and Launch**:
   - Expand **Advanced Details** if needed (advanced configuration will be covered later).
   - Click **Launch**. The instance will be created, and you will see a success dialog. Click on **View All Instances**.

### 4. Monitor Instance Status

1. **Instance State**:

   - The instance will initially be in a **pending** state.
   - After a few minutes, it will transition to **running** and then to **initializing** under the status checks.

2. **Status Checks**:
   - Wait for the status checks to complete. This can take some time.

## Next Steps

In the next part of this lesson, you will learn how to connect to your EC2 instance.

### Useful Links

- **[Using PuTTY to Connect to Your Instance](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/putty.html)**
- **[Connecting to Linux Instances](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/AccessingInstancesLinux.html)**
- **[Connection Prerequisites](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/connection-prereqs.html#connection-prereqs-private-key)**
- **[Troubleshooting Connection Issues](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/TroubleshootingInstancesConnecting.html#troubleshoot-unprotected-key)**

## Conclusion

This concludes part one of the lesson. Please take a moment to review and proceed to part two for further instructions on connecting to your EC2 instance.
