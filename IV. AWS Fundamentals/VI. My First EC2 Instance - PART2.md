# Connecting to Your EC2 Instance: Part Two

## Introduction

Welcome back to part two of our lesson. In this section, we'll continue from where we left off in part one and demonstrate how to connect to your EC2 instance. Make sure your instance has passed the necessary status checks before proceeding.

## Verifying Instance Status

1. **Check Status**:

   - Ensure that your instance has passed both status checks (2 out of 2) before continuing.
   - Confirm that the instance is provisioned in the desired region (e.g., US-East-1c) and has a public IP and DNS name for access.

2. **View Instance Details**:
   - **Details Tab**: Provides high-level information about the instance.
   - **Security Tab**: Displays security-related information.
   - **Networking Tab**: Shows networking configuration details.
   - **Storage Tab**: Provides an overview of the storage.
   - **Status Checks Tab**: Displays the pass/fail states of status checks.
   - **Monitoring Tab**: Shows metrics gathered by CloudWatch.

## Connecting to the EC2 Instance

### Using EC2 Instance Connect

1. **Connect via EC2 Instance Connect**:
   - Click on the instance and then click **Connect**.
   - Select the **EC2 Instance Connect** tab and click **Connect**.
   - This will open a terminal in your web browser, allowing you to interact with the EC2 instance.

### Using SSH Client

1. **Prepare Your SSH Key**:

   - Ensure you have the private key file (e.g., `A4L.pem`) downloaded earlier.
   - Change the permissions of the key file to ensure it's not accessible to other users. Use the following command on MacOS/Linux:
     ```bash
     chmod 400 A4L.pem
     ```
   - For Windows users, follow the instructions provided in the linked resources to adjust permissions.

2. **Connect Using SSH**:

   - Open your terminal (or command prompt in Windows).
   - Navigate to the folder where the key file is stored (e.g., Downloads):
     ```bash
     cd ~/Downloads
     ```
   - Use the SSH command provided in the AWS Console to connect to the instance:
     ```bash
     ssh -i A4L.pem ec2-user@<Public-IP-or-DNS>
     ```
   - Confirm the authenticity of the host and accept the connection.

   - If prompted about the unprotected private key file, adjust permissions using `chmod` as shown above.

### Understanding Key Pair Authentication

- **Public and Private Keys**:
  - The key pair consists of a public key stored on the EC2 instance and a private key you have on your local machine.
  - Authentication is achieved by matching the private key with the public key on the instance.

## Clean Up

1. **Terminate the EC2 Instance**:

   - Go to **Instances**, select your instance (e.g., "My First EC2 Instance").
   - Right-click on it, select **Terminate Instance**, and confirm.

2. **Delete Security Group**:
   - Navigate to **Security Groups**.
   - Find and select the security group associated with your instance (e.g., "My First Instance SG").
   - Click on **Actions** and select **Delete Security Group**.
   - If you receive an error, wait until the instance is fully terminated and try again.

## Conclusion

This concludes part two of the lesson. You have learned how to connect to your EC2 instance using various methods and how to clean up resources afterward. Complete the video and prepare to join the next lesson for further learning.

### Useful Links

- **[Using PuTTY to Connect to Your Instance](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/putty.html)**
- **[Connecting to Linux Instances](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/AccessingInstancesLinux.html)**
- **[Connection Prerequisites](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/connection-prereqs.html#connection-prereqs-private-key)**

Feel free to refer to these resources for more detailed instructions and troubleshooting.
