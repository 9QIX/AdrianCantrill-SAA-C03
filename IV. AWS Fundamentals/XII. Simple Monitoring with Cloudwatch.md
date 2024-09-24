# AWS Certified Solutions Architect - CloudWatch Demo (Learn Cantrill)

In this demo lesson, we explore **Amazon CloudWatch** by creating an **EC2 instance**, generating CPU load, and setting up a **CloudWatch alarm** to monitor CPU utilization. This guide will help you understand how CloudWatch interacts with EC2 and how to set up monitoring for resource utilization.

## Demo Overview

In this demo, you will:

1. Create an **EC2 instance** with the name `CloudWatch Test`.
2. Configure the instance with Amazon Linux (2023 version).
3. Optionally enable **detailed CloudWatch monitoring**.
4. Connect to the instance using EC2 Instance Connect and install the **Stress** application to simulate CPU load.
5. Set up a **CloudWatch Alarm** that triggers when CPU utilization exceeds 15%.
6. Monitor CloudWatch, trigger the alarm using **Stress**, and resolve it.
7. Clean up resources by deleting the instance and alarm.

## Step-by-Step Guide

### 1. Create an EC2 Instance

- **Instance Name**: `CloudWatch Test`
- **Amazon Machine Image (AMI)**: Amazon Linux 2023 (Free Tier eligible)
- **Instance Type**: `t2.micro` (Free Tier eligible)
- **VPC**: Ensure it's set to the **default VPC**.
- **Public IP**: Make sure **auto-assign public IP** is enabled.
- **Security Group**: Create a security group `CloudWatchSG` with SSH access enabled from any source.

**Advanced Configuration**:

- Optionally enable **detailed monitoring** (this incurs a small additional cost but provides faster data insights).

Once the settings are complete, click **Launch Instance** and wait for the instance to initialize.

### 2. Connect to the EC2 Instance

Once the instance is running:

- Select the instance, click **Connect**, and choose **EC2 Instance Connect**.
- Connect to the instance without an SSH key.

### 3. Install the `stress` Utility

To simulate high CPU usage, install the **stress** utility on your instance:

```bash
sudo yum install stress -y
```

### 4. Create a CloudWatch Alarm

- In the AWS console, search for **CloudWatch** and open the **CloudWatch console**.
- Select **Alarms** from the left panel, then click **Create Alarm**.
- Under **Select Metric**, choose **EC2** → **Per Instance Metrics**.
- Find the instance's CPU utilization metric by matching the instance ID.

#### Alarm Configuration

- Set the alarm condition for **CPU utilization ≥ 15%**.
- Optionally configure **SNS notifications** (optional for production use).
- Name the alarm `CloudWatch Test - High CPU` and click **Next** to finalize the alarm creation.

### 5. Simulate High CPU Usage

Back in the EC2 instance:

- Run the **stress** command to simulate CPU load:

```bash
stress -c 1 -t 3600
```

This will place a load on the CPU for 3600 seconds (1 hour).

### 6. Monitor the CloudWatch Alarm

- Return to the **CloudWatch console** and monitor the alarm state.
- Refresh the page periodically. The alarm should transition from **OK** to **In Alarm** once the CPU utilization exceeds 15%.

After confirming the alarm, stop the stress test:

- On the EC2 terminal, press **Ctrl + C** to stop the stress test.

Continue monitoring CloudWatch until the alarm status returns to **OK** once the CPU utilization drops below the threshold.

### 7. Clean Up Resources

Once the test is complete:

1. **Delete the CloudWatch Alarm**:

   - Go to **Alarms**, select the `CloudWatch Test - High CPU` alarm, and delete it.

2. **Terminate the EC2 Instance**:

   - Go back to the **EC2 console**, select the `CloudWatch Test` instance, right-click and select **Terminate Instance**.

3. **Delete the Security Group**:
   - Under **Security Groups**, find `CloudWatchSG`, select it, and delete the security group.

## Commands Summary

### Install Stress Utility

```bash
sudo yum install stress -y
```

### Run Stress to Simulate CPU Load

```bash
stress -c 1 -t 3600
```

### Stop Stress

Press `Ctrl + C` to stop the stress utility.
