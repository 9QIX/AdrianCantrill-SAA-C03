# EBS & EC2 Demo

## Overview

This demo lesson provides hands-on experience with Amazon Elastic Block Store (EBS), Instance Store Volumes, and Amazon EC2. The lesson involves:

- Creating an EBS volume
- Mounting the volume to an EC2 instance
- Creating and mounting a file system
- Generating a test file
- Migrating the volume to another EC2 instance within the same Availability Zone (AZ)
- Verifying file system and file integrity after migration
- Creating an EBS snapshot
- Restoring an EBS volume from a snapshot in a different AZ
- Copying a snapshot to another region
- Creating an EC2 instance with instance store volumes
- Testing file system persistence across restarts and stops

## Deployment

A one-click deployment CloudFormation stack is available:
[Deploy Stack](https://console.aws.amazon.com/cloudformation/home?region=us-east-1#/stacks/create/review?templateURL=https://learn-cantrill-labs.s3.amazonaws.com/awscoursedemos/0004-aws-associate-ec2-ebs-demo/A4L_VPC_3PUBLICINSTANCES_AL2023.yaml&stackName=EBSDEMO)

## Commands Reference

Lesson commands are available here:
[Lesson Commands](https://learn-cantrill-labs.s3.amazonaws.com/awscoursedemos/0004-aws-associate-ec2-ebs-demo/lesson_commands_AL2023.txt)

## Lesson Walkthrough

### Creating and Mounting an EBS Volume on EC2

#### 1. List Block Devices

```bash
lsblk
```

_Lists available block devices attached to the instance._

#### 2. Check if the Device Has a Filesystem

```bash
sudo file -s /dev/xvdf
```

_If the output shows `data`, the device has no filesystem._

#### 3. Format the Device with XFS Filesystem

```bash
sudo mkfs -t xfs /dev/xvdf
```

_Creates an XFS filesystem on the EBS volume._

#### 4. Verify the Filesystem

```bash
sudo file -s /dev/xvdf
```

_Confirms that the XFS filesystem is now present._

#### 5. Create a Mount Directory

```bash
sudo mkdir /ebstest
```

_Creates a directory where the EBS volume will be mounted._

#### 6. Mount the EBS Volume

```bash
sudo mount /dev/xvdf /ebstest
```

_Mounts the EBS volume to the `/ebstest` directory._

#### 7. Navigate to the Mounted Directory

```bash
cd /ebstest
```

#### 8. Create a Test File

```bash
sudo nano amazingtestfile.txt
```

_Creates a file and allows the user to enter a test message._

#### 9. Save and Exit the File

Press `CTRL + X`, then `Y`, then `ENTER` to save.

#### 10. Verify File Creation

```bash
ls -la
```

_Lists all files in the directory to confirm that `amazingtestfile.txt` exists._

### Rebooting and Verifying Persistence

#### 1. Reboot Instance

```bash
sudo reboot
```

_Reboots the EC2 instance._

#### 2. Reconnect to the Instance and Verify Mount Persistence

```bash
lsblk
```

_Checks if the device is still present._

```bash
df -h
```

_Checks if the filesystem is still mounted._

If the volume is not mounted, it must be remounted manually or configured for automatic mounting.

### Creating an EBS Snapshot

#### 1. Navigate to EBS Console

- Find the EBS volume attached to the instance.
- Click **Create Snapshot**.

#### 2. Restore an EBS Volume from the Snapshot

- Use the **Create Volume** option and select the snapshot.
- Attach the new volume to another EC2 instance in the same AZ.
- Mount and verify the filesystem integrity.

### Testing Instance Store Volumes

#### 1. Create an EC2 Instance with Instance Store Volumes

- Launch a new EC2 instance with **Instance Store** as the root volume.

#### 2. Create a Filesystem and Test File

```bash
sudo mkfs -t xfs /dev/xvdb
sudo mkdir /instancetest
sudo mount /dev/xvdb /instancetest
cd /instancetest
sudo nano instancefile.txt
```

#### 3. Restart the Instance

```bash
sudo reboot
```

#### 4. Verify the File System Persistence

```bash
ls -la /instancetest
```

_Instance store volumes do not persist after instance termination._

### Conclusion

This hands-on demo covers:

- Creating and managing EBS volumes
- Attaching and mounting volumes to EC2 instances
- Persisting data across reboots with EBS
- Testing non-persistent instance store volumes

Understanding EBS and instance store volumes is crucial for AWS operations, ensuring proper use cases for performance and cost optimization.
