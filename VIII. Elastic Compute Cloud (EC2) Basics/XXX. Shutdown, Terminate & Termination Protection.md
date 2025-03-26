# AWS SA C03 - EC2 Termination Protection

## Overview

This lesson focuses on **EC2 Termination Protection**, a feature that prevents accidental termination of critical EC2 instances. It also covers **shutdown behavior settings**, which determine whether an instance stops or terminates when shut down.

If you're following along, ensure that:

- You have the infrastructure from the previous demo lesson.
- You are logged in as the IAM admin user of the AWS management account.
- The **N. Virginia (us-east-1)** region is selected.

## What is EC2 Termination Protection?

Termination protection is an AWS feature that prevents an EC2 instance from being accidentally terminated.

By default, an EC2 instance can be **stopped**, **rebooted**, or **terminated**. However, an inexperienced user might unintentionally terminate an instance, leading to **data loss**.

To mitigate this risk, **termination protection** can be enabled, adding an additional security layer.

## How to Enable Termination Protection

To enable termination protection:

1. **Go to the EC2 Console** and select the instance.
2. **Right-click** on the instance and navigate to `Instance Settings` > `Change Termination Protection`.
3. **Enable** termination protection and click `Save`.

Once enabled:

- If someone attempts to terminate the instance, AWS will **prevent the termination**.
- A warning message will be displayed:  
  _"The instance [Instance ID] may not be terminated. Modify its disable API termination instance attribute and try again."_

## Advantages of Termination Protection

### 1. **Prevents Accidental Termination**

- Ensures critical instances are not deleted by mistake.

### 2. **Requires Explicit Permissions to Disable**

- Users need the following permissions:
  - Permission to **disable termination protection**
  - Permission to **terminate instances**
- This allows for **role separation**:
  - Senior admins can disable termination protection.
  - Junior admins can terminate instances only if protection is disabled.
- Adds an **approval process** before deletion.

### 3. **Ideal for Production Environments**

- Typically not needed for **development** or **test environments**.
- Should be **standard practice for production** workloads.

### 4. **Automation Support**

- Can be **automatically enabled** when provisioning instances using **CloudFormation** or other automation tools.

## API Attribute: `disableApiTermination`

In AWS, termination protection is controlled via the **`disableApiTermination`** attribute.

- If `true`, the instance **cannot be terminated** unless the attribute is set to `false` first.
- AWS exams may test your knowledge of this attribute and related error messages.

## Modifying Termination Protection

To **disable** termination protection:

1. **Right-click** the instance.
2. Go to `Instance Settings` > `Change Termination Protection`.
3. **Uncheck** the termination protection option.
4. Click `Save`.

Now, the instance can be terminated normally.

## EC2 Shutdown Behavior

Another related feature is **Shutdown Behavior**, which determines what happens when an instance is shut down from the OS level.

### How to Modify Shutdown Behavior:

1. **Right-click** the instance.
2. Navigate to `Instance Settings` > `Change Shutdown Behavior`.
3. Choose from the following options:
   - **Stop (Default):** The instance moves to a `stopped` state when shut down.
   - **Terminate:** The instance is **completely deleted** when shut down.

**When to Use Terminate Behavior:**

- If you do not want to keep instances after shutdown (e.g., ephemeral workloads).
- If you want to avoid accumulating stopped instances.
- Typically used in **stateless environments**.

## Cleaning Up (If Following Along)

If you deployed the CloudFormation stack, clean up by:

1. Going to **AWS CloudFormation**.
2. Selecting the **status checks and protect stack**.
3. Clicking `Delete Stack` and confirming the deletion.
4. Once completed, all deployed infrastructure will be removed.

## Key Takeaways

- **Termination Protection** prevents accidental deletion of EC2 instances.
- It requires **explicit permissions** to disable and terminate an instance.
- **Role separation** can be implemented using IAM policies.
- **Shutdown Behavior** controls whether an instance stops or terminates when shut down.
- These features are **essential for AWS SysOps and Developer exams**.

## Resources

- [AWS CloudFormation Template for Deployment](https://console.aws.amazon.com/cloudformation/home?region=us-east-1#/stacks/create/review?templateURL=https://learn-cantrill-labs.s3.amazonaws.com/awscoursedemos/0022-aws-associate-ec2-statuschecksandterminateprotection/A4L_VPC_PUBLICINSTANCE.yaml&stackName=STATUSCHECKSANDPROTECT)
- [AWS Documentation on Termination Protection](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/terminating-instances.html)
