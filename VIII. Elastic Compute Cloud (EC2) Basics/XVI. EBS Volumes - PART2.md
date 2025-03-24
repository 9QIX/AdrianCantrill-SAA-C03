# EBS Volume Attachment and Persistence

## Overview

This lesson covers how to attach, mount, persist, detach, and move AWS Elastic Block Store (EBS) volumes across EC2 instances and availability zones (AZs). It includes hands-on commands and explanations for ensuring EBS persistence even after reboots.

## Instance 1: Persisting EBS Mount After Reboot

After an EC2 instance is restarted, manually mounted EBS volumes are not automatically remounted. To enable persistence, the `fstab` file must be updated.

### Commands Used:

```bash
# Check available file systems
 df -k

# List block devices and their UUIDs
 sudo blkid

# Edit fstab to auto-mount the volume
 sudo nano /etc/fstab
```

#### Add the following line in `/etc/fstab`:

```
UUID=YOURUUIDHEREREPLACEME  /ebstest  xfs  defaults,nofail
```

```bash
# Apply the new fstab configuration
 sudo mount -a

# Navigate to the mounted directory and list files
 cd /ebstest
 ls -la
```

### Explanation

- `df -k`: Displays disk space usage.
- `sudo blkid`: Lists block devices with their UUIDs.
- `sudo nano /etc/fstab`: Opens `fstab` to configure auto-mounting.
- `UUID=... /ebstest xfs defaults,nofail`: Ensures the EBS volume is mounted at `/ebstest` at boot.
- `sudo mount -a`: Applies `fstab` configurations immediately.
- `cd /ebstest && ls -la`: Verifies that the mount is persistent.

## Instance 2: Attaching and Mounting an EBS Volume

Once an EBS volume is detached from one instance, it can be attached to another.

### Commands Used:

```bash
# List block devices
 lsblk

# Check if the EBS volume has a file system
 sudo file -s /dev/xvdf

# Create a directory for mounting
 sudo mkdir /ebstest

# Mount the EBS volume
 sudo mount /dev/xvdf /ebstest

# Verify files on the mounted volume
 cd /ebstest
 ls -la
```

### Explanation

- `lsblk`: Lists block storage devices.
- `sudo file -s /dev/xvdf`: Checks if a file system exists on `/dev/xvdf`.
- `sudo mkdir /ebstest`: Creates a mount point.
- `sudo mount /dev/xvdf /ebstest`: Mounts the volume.
- `cd /ebstest && ls -la`: Confirms that data persists across instances.

## Instance 3: Mounting the Volume in Another Availability Zone

EBS volumes are restricted to a single AZ. To move a volume across AZs, a snapshot is created and restored in the target AZ.

### Steps:

1. **Detach the EBS volume from Instance 2.**

```bash
# Detach the volume
 aws ec2 detach-volume --volume-id vol-xxxxxxxx
```

2. **Create a snapshot of the volume.**

```bash
# Create a snapshot
 aws ec2 create-snapshot --volume-id vol-xxxxxxxx --description "EBS test snapshot"
```

3. **Create a new volume from the snapshot in a different AZ.**

```bash
# Create volume from snapshot in AZ 1b
 aws ec2 create-volume --snapshot-id snap-xxxxxxxx --availability-zone us-east-1b
```

4. **Attach and mount the new volume on Instance 3.**

```bash
# List block devices
 lsblk

# Verify the file system
 sudo file -s /dev/xvdf

# Create a mount point
 sudo mkdir /ebstest

# Mount the volume
 sudo mount /dev/xvdf /ebstest

# Confirm file persistence
 cd /ebstest
 ls -la
```

### Explanation

- `aws ec2 detach-volume`: Detaches the EBS volume from the instance.
- `aws ec2 create-snapshot`: Creates an S3-backed snapshot of the volume.
- `aws ec2 create-volume`: Recreates the volume in another AZ.
- Mounting and verifying steps remain the same as in previous instances.

## Cross-Region Snapshot Copying

EBS snapshots enable cross-region movement of data.

### Command:

```bash
# Copy snapshot to another region
 aws ec2 copy-snapshot --source-region us-east-1 --source-snapshot-id snap-xxxxxxxx --destination-region ap-southeast-2
```

### Explanation

- Copies an EBS snapshot from `us-east-1` to `ap-southeast-2`.
- Useful for disaster recovery and global deployments.

## Conclusion

- **EBS volumes persist** beyond the lifecycle of EC2 instances.
- **Auto-mounting with `fstab`** ensures persistence after reboots.
- **Snapshots enable volume movement** across AZs and regions.
- **Mounting EBS volumes on different instances** preserves data integrity.

This knowledge is essential for designing resilient AWS architectures where persistent block storage is required.

# LearnCantrill.io AWS SA C03 - EBS Volume Attachment and Persistence

## Overview

This lesson covers how to attach, mount, persist, detach, and move AWS Elastic Block Store (EBS) volumes across EC2 instances and availability zones (AZs). It includes hands-on commands and explanations for ensuring EBS persistence even after reboots.

## Instance 1: Persisting EBS Mount After Reboot

After an EC2 instance is restarted, manually mounted EBS volumes are not automatically remounted. To enable persistence, the `fstab` file must be updated.

### Commands Used:

```bash
# Check available file systems
 df -k

# List block devices and their UUIDs
 sudo blkid

# Edit fstab to auto-mount the volume
 sudo nano /etc/fstab
```

#### Add the following line in `/etc/fstab`:

```
UUID=YOURUUIDHEREREPLACEME  /ebstest  xfs  defaults,nofail
```

```bash
# Apply the new fstab configuration
 sudo mount -a

# Navigate to the mounted directory and list files
 cd /ebstest
 ls -la
```

### Explanation

- `df -k`: Displays disk space usage.
- `sudo blkid`: Lists block devices with their UUIDs.
- `sudo nano /etc/fstab`: Opens `fstab` to configure auto-mounting.
- `UUID=... /ebstest xfs defaults,nofail`: Ensures the EBS volume is mounted at `/ebstest` at boot.
- `sudo mount -a`: Applies `fstab` configurations immediately.
- `cd /ebstest && ls -la`: Verifies that the mount is persistent.

## Instance 2: Attaching and Mounting an EBS Volume

Once an EBS volume is detached from one instance, it can be attached to another.

### Commands Used:

```bash
# List block devices
 lsblk

# Check if the EBS volume has a file system
 sudo file -s /dev/xvdf

# Create a directory for mounting
 sudo mkdir /ebstest

# Mount the EBS volume
 sudo mount /dev/xvdf /ebstest

# Verify files on the mounted volume
 cd /ebstest
 ls -la
```

### Explanation

- `lsblk`: Lists block storage devices.
- `sudo file -s /dev/xvdf`: Checks if a file system exists on `/dev/xvdf`.
- `sudo mkdir /ebstest`: Creates a mount point.
- `sudo mount /dev/xvdf /ebstest`: Mounts the volume.
- `cd /ebstest && ls -la`: Confirms that data persists across instances.

## Instance 3: Mounting the Volume in Another Availability Zone

EBS volumes are restricted to a single AZ. To move a volume across AZs, a snapshot is created and restored in the target AZ.

### Steps:

1. **Detach the EBS volume from Instance 2.**

```bash
# Detach the volume
 aws ec2 detach-volume --volume-id vol-xxxxxxxx
```

2. **Create a snapshot of the volume.**

```bash
# Create a snapshot
 aws ec2 create-snapshot --volume-id vol-xxxxxxxx --description "EBS test snapshot"
```

3. **Create a new volume from the snapshot in a different AZ.**

```bash
# Create volume from snapshot in AZ 1b
 aws ec2 create-volume --snapshot-id snap-xxxxxxxx --availability-zone us-east-1b
```

4. **Attach and mount the new volume on Instance 3.**

```bash
# List block devices
 lsblk

# Verify the file system
 sudo file -s /dev/xvdf

# Create a mount point
 sudo mkdir /ebstest

# Mount the volume
 sudo mount /dev/xvdf /ebstest

# Confirm file persistence
 cd /ebstest
 ls -la
```

### Explanation

- `aws ec2 detach-volume`: Detaches the EBS volume from the instance.
- `aws ec2 create-snapshot`: Creates an S3-backed snapshot of the volume.
- `aws ec2 create-volume`: Recreates the volume in another AZ.
- Mounting and verifying steps remain the same as in previous instances.

## Cross-Region Snapshot Copying

EBS snapshots enable cross-region movement of data.

### Command:

```bash
# Copy snapshot to another region
 aws ec2 copy-snapshot --source-region us-east-1 --source-snapshot-id snap-xxxxxxxx --destination-region ap-southeast-2
```

### Explanation

- Copies an EBS snapshot from `us-east-1` to `ap-southeast-2`.
- Useful for disaster recovery and global deployments.

## Conclusion

- **EBS volumes persist** beyond the lifecycle of EC2 instances.
- **Auto-mounting with `fstab`** ensures persistence after reboots.
- **Snapshots enable volume movement** across AZs and regions.
- **Mounting EBS volumes on different instances** preserves data integrity.

This knowledge is essential for designing resilient AWS architectures where persistent block storage is required.
