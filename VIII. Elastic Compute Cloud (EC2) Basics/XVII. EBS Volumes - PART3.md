# Instance Store Volumes

## Overview

This document summarizes the process of working with **Instance Store Volumes** in AWS as covered in the **LearnCantrill.io AWS SA C03 course**.  
We will explore how to create, mount, and test instance store volumes while understanding their ephemeral nature.

## Key Concepts

- **Instance Store Volumes** are temporary storage volumes that come directly attached to an EC2 instance.
- Unlike **EBS (Elastic Block Store) volumes**, instance store volumes are lost when an instance is stopped and started.
- Instance store volumes persist **only** during an **instance restart**, as long as the instance remains on the same physical EC2 host.
- Stopping and starting an instance moves it to a different EC2 host, causing **all data on the instance store volume to be lost**.

## Launching an EC2 Instance with Instance Store Volumes

1. **Launch an EC2 instance manually**:
   - Use **Amazon Linux 2023** (`x86_64` architecture).
   - Choose **m5dn.large** instance type (includes one instance store volume).
   - Select the appropriate **VPC, Subnet, and Security Group**.
   - Under **storage settings**, ensure that an instance store volume is present (e.g., `/dev/nvme1n1`).
   - Click **Launch Instance** and wait for it to be in a running state.

## Working with Instance Store Volumes

### 1. Checking Available Storage Volumes

```sh
lsblk
```

**Explanation:**

- Lists all attached block storage devices.
- Used to identify instance store volumes (`/dev/nvme1n1`).

### 2. Checking If a Filesystem Exists on the Volume

```sh
sudo file -s /dev/nvme1n1
```

**Explanation:**

- Examines the volume to determine if a filesystem exists.
- If the output shows `data`, it means **no filesystem is present**.

### 3. Creating an XFS Filesystem on the Volume

```sh
sudo mkfs -t xfs /dev/nvme1n1
```

**Explanation:**

- Formats the instance store volume with the **XFS** filesystem.
- `mkfs -t xfs` creates a new **XFS filesystem**, which is efficient for large files.

### 4. Verifying the Filesystem

```sh
sudo file -s /dev/nvme1n1
```

**Explanation:**

- Checks if the volume now has a recognized filesystem (XFS).

### 5. Mounting the Volume

```sh
sudo mkdir /instancestore
sudo mount /dev/nvme1n1 /instancestore
```

**Explanation:**

- Creates a directory `/instancestore` to serve as a mount point.
- Mounts the volume at `/instancestore`, making it accessible.

### 6. Creating a Test File

```sh
cd /instancestore
sudo touch instancestore.txt
```

**Explanation:**

- Navigates to the mounted volume.
- Creates an empty file named `instancestore.txt`.

## Testing Persistence: Restart vs. Stop/Start

### After Restart (Instance Reboot)

1. **Reboot the instance** from the AWS Console.
2. **Check if the volume is mounted**:

```sh
df -k
```

- If the mount is missing, remount it:

```sh
sudo mount /dev/nvme1n1 /instancestore
cd /instancestore
ls -la
```

**Observation**: The file `instancestore.txt` **persists** after a restart.  
🔹 **Reason**: The EC2 instance remains on the **same physical host**, so the instance store volume remains attached.

### After Stop/Start (Instance Moved to a New Host)

1. **Stop the instance** from the AWS Console.
2. **Start the instance** again.
3. **Check if the volume still exists**:

```sh
lsblk
sudo file -s /dev/nvme1n1
```

**Observation**: The volume still exists, but all data is lost.

- **Reason**: The instance was moved to a **new EC2 host**, causing a complete reset of instance store volumes.

## Key Takeaways

- **Instance Store Volumes are ephemeral**:
  - Data **persists** through a **restart** (same EC2 host).
  - Data **is lost** after a **stop/start** (new EC2 host).
- **EBS Volumes are persistent** and retain data across stops, starts, and instance migrations.
- **Use Case for Instance Store**:
  - Temporary storage for applications that cache data (e.g., high-speed databases, session stores).
  - Not suitable for critical data storage—use **EBS** or **S3** instead.

## Cleaning Up

To avoid unnecessary charges, **terminate the instance**:

```sh
aws ec2 terminate-instances --instance-ids <instance-id>
```

If using **CloudFormation**, delete the stack:

```sh
aws cloudformation delete-stack --stack-name <stack-name>
```

## Summary

This lesson demonstrated:

1. How to launch an **EC2 instance** with **instance store volumes**.
2. How to **check, format, and mount** instance store volumes.
3. The difference between **restart** (data persists) and **stop/start** (data is lost).
4. Why **EBS is preferred for persistent storage**.
