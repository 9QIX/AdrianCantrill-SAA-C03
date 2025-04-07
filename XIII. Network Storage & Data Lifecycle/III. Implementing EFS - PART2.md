# Implementing EFS on EC2 (Part 2)

This lesson demonstrates how to **implement AWS EFS** (Elastic File System) by connecting **two EC2 instances (Instance A & B)** to a shared EFS file system, enabling persistent shared storage across Availability Zones.

## **Resources**

- **1-Click CloudFormation Deployment**:  
  [Launch Stack](https://console.aws.amazon.com/cloudformation/home?region=us-east-1#/stacks/create/review?templateURL=https://learn-cantrill-labs.s3.amazonaws.com/awscoursedemos/0019-aws-associate-storage-implementing-efs/A4L_TWO_EFS_EC2_AL2023.yaml&stackName=IMPLEMENTINGEFS)

## **Overview**

1. Create EFS and EC2 instances using a pre-defined CloudFormation template.
2. Mount the EFS file system on **Instance A**.
3. Verify EFS is not mounted by default.
4. Install required tools and configure EFS mounting.
5. Add entry to `/etc/fstab` for persistent mount.
6. Create a file on EFS via **Instance A**.
7. Mount the same EFS on **Instance B**.
8. Confirm file visibility to demonstrate shared access.

## **Step-by-Step Walkthrough**

### ✅ Mounting EFS on Instance A

```bash
# Show mounted file systems
df -k

# Create directory for EFS mount
sudo mkdir -p /efs/wp-content

# Install EFS utility
sudo dnf -y install amazon-efs-utils

# Move to /etc directory to edit fstab
cd /etc
sudo nano /etc/fstab
```

**Add the following line to `/etc/fstab` (replace `file-system-id`):**

```bash
file-system-id:/ /efs/wp-content efs _netdev,tls,iam 0 0
```

```bash
# Mount EFS using fstab
sudo mount /efs/wp-content

# Confirm mount
df -k

# Move into mounted directory and create a test file
cd /efs/wp-content
sudo touch amazingtestfile.txt
```

### ✅ Mounting EFS on Instance B

```bash
# Show mounted file systems
df -k

# Install EFS utility
sudo dnf -y install amazon-efs-utils

# Create EFS mount directory
sudo mkdir -p /efs/wp-content

# Edit fstab file
sudo nano /etc/fstab
```

**Add the same line again (with same `file-system-id`):**

```bash
file-system-id:/ /efs/wp-content efs _netdev,tls,iam 0 0
```

```bash
# Mount EFS
sudo mount /efs/wp-content

# List contents to verify shared file
ls -la
```

## **Code Explanation (Line-by-Line)**

### Instance A

```bash
df -k
```

Shows all mounted filesystems and their disk usage (in kilobytes).

```bash
sudo mkdir -p /efs/wp-content
```

Creates the mount directory. `-p` ensures parent directories are created if missing.

```bash
sudo dnf -y install amazon-efs-utils
```

Installs AWS EFS utilities. `dnf` is the package manager for Amazon Linux 2023.

```bash
cd /etc
```

Navigate to `/etc` to modify configuration files.

```bash
sudo nano /etc/fstab
```

Opens `fstab` file using the `nano` text editor.

```bash
file-system-id:/ /efs/wp-content efs _netdev,tls,iam 0 0
```

- **file-system-id**: Replace this with your actual EFS ID.
- **/efs/wp-content**: Target mount directory.
- **efs**: File system type.
- **\_netdev**: Delays mount until network is ready.
- **tls**: Enables encryption.
- **iam**: Enables IAM authentication.

```bash
sudo mount /efs/wp-content
```

Mounts the EFS using `fstab` configuration.

```bash
cd /efs/wp-content
sudo touch amazingtestfile.txt
```

Creates a test file to verify EFS accessibility.

### Instance B (Differences)

```bash
ls -la
```

Lists all files, including the test file created on Instance A, proving shared EFS.

## **EFS Summary**

- **EFS** is a **managed, shared file system** for EC2 and on-prem Linux systems.
- Can be mounted across **multiple AZs and instances**.
- Uses **NFSv4** under the hood.
- Useful for **web content, shared configurations, and persistent data**.

## **Cleanup**

1. Go to **EFS Console**.
2. Select and delete the EFS file system.
3. Confirm deletion by entering the file system ID.
4. Go to **CloudFormation Console**.
5. Select `IMPLEMENTINGEFS` stack.
6. Click **Delete** and confirm.

## **Final Thoughts**

This demo showed how easy it is to:

- Deploy and mount EFS on EC2
- Share files across multiple instances
- Automate persistent mounts via `/etc/fstab`

You're now ready to build more complex storage-backed architectures using **EFS and EC2**.
