# Stage 5: Cleanup and Resource Deletion

**Resources:**

- **Project Repository:** [acantril/learn-cantrill-io-labs - aws-simple-site2site-vpn](https://github.com/acantril/learn-cantrill-io-labs/tree/master/aws-simple-site2site-vpn)
- **Stage 5 Instructions:** [STAGE5.md](https://github.com/acantril/learn-cantrill-io-labs/blob/master/aws-simple-site2site-vpn/02_LABINSTRUCTIONS/STAGE5.md)

## Objective

The goal of Stage 5 is to **clean up all AWS resources** created during the mini-project to:

- Avoid unnecessary billing charges
- Return the account to its original, pre-project state

## Step-by-Step Cleanup Guide

### 1. **Delete the Site-to-Site VPN Connection**

- Go to the **VPC Console** in AWS.
- In the left-hand menu, scroll to **Site-to-Site VPN Connections**.
- Select the **VPN connection** you created.
- Click **Actions** → **Delete VPN Connection**.
- Type `delete` when prompted, and confirm deletion.

### 2. **Detach and Delete the Virtual Private Gateway (VGW)**

- Navigate to **Virtual Private Gateways** in the same VPC console.
- Select the VGW used in this lab (typically named something like `AWS VGW`).
- Click **Actions** → **Detach from VPC**.
- After it's detached, again click **Actions** → **Delete Virtual Private Gateway**.
- Confirm the deletion by typing `delete`.

### 3. **Delete the Customer Gateway**

- Navigate to **Customer Gateways**.
- Select the customer gateway named something like `a4l on-prem router`.
- Click **Actions** → **Delete Customer Gateway**.
- Type `delete` and confirm.

## 4. **Delete the CloudFormation Stack**

The lab environment was deployed using a **one-click CloudFormation stack**, which should also be deleted:

- Open the **CloudFormation Console**.
- Locate the stack named **S2S VPN**.
- Select it and click **Delete**.
- Confirm deletion by clicking **Delete Stack**.

Once the stack deletion is complete, all associated resources (EC2 instances, networking elements, IAM roles, etc.) will be cleaned up.

## Summary

By following this process, your AWS account will be returned to its **initial state**, preventing further charges and keeping your environment tidy.

### Key Skills Practiced in This Mini Project:

- Setting up a **Site-to-Site VPN** between AWS and a simulated on-prem environment
- Using **SSM Fleet Manager** for GUI access to private EC2 instances
- Testing VPN connectivity with **ping** and **web access**
- Cleaning up AWS networking and compute resources manually and via **CloudFormation**

## Final Note

This project demonstrated a practical, foundational VPN setup. While production environments may include additional complexity like **redundant tunnels**, **dynamic routing (BGP)**, and **advanced firewall configurations**, the core principles remain the same.

Thank you for completing the project. You're now better equipped to manage hybrid cloud networking in AWS.
