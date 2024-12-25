# Learn Cantrill.io AWS SA C03: Service Control Policies (SCPs) Demo Summary

## Introduction

This demo lesson covers the creation and application of AWS Service Control Policies (SCPs) as part of the AWS Organizations service. By the end of the demonstration, you will:

- Structure AWS accounts within an organization using Organizational Units (OUs).
- Apply SCPs to control access for different AWS accounts.
- Observe how SCPs can restrict certain operations even for users or roles with administrator permissions.

## Prerequisites

Before starting this demo, you should have:

- Created an AWS Organization with a **management account** (referred to as the "general account").
- Invited a **production AWS account** and created a **development AWS account** within the organization.

## Step-by-Step Instructions

### 1. Organizing AWS Accounts with OUs

1. Log into the **management account** of your AWS Organization.
2. Navigate to the AWS Organizations console.
3. Create Organizational Units (OUs) for **Production** and **Development**:

   - Select the **root container** at the top of the hierarchy.
   - Click **Actions** → **Create New** → name the OU as "Prod".
   - Repeat for the Development OU, naming it "Dev".

4. Move accounts into their respective OUs:
   - Select the **Production AWS account** → click **Actions** → **Move** → select the **Prod** OU.
   - Similarly, move the **Development AWS account** to the **Dev** OU.

### 2. Switching Roles into the Production Account

1. Return to the AWS Management Console.
2. Switch roles into the **Production AWS account** using the **OrganizationAccountAccessRole**.
   - This role provides **Administrator Access** to the production account.

### 3. Creating and Interacting with an S3 Bucket

1. Navigate to the **S3 console**.
2. Create a bucket named "catpics" followed by a unique random number.
3. [Download the cat picture](https://learn-cantrill-labs.s3.amazonaws.com/awscoursedemos/0034-aws-orgscp/samson.JPG).
4. Upload the downloaded **samson.JPG** image to the bucket.

### 4. Understanding Permissions

- At this point, you have **Administrator Access** permissions via the assumed role, allowing full access to S3 and other services.

### 5. Enabling Service Control Policies (SCPs)

1. Switch back to the **management account**.
2. Go to the **AWS Organizations** console and click on **Policies**.
3. Enable **Service Control Policies**.

   - This action attaches the default **Full AWS Access** policy, granting unrestricted access to all accounts within the organization.

### 6. Creating a Custom SCP

1. Use the following JSON policy code to create the custom SCP:

   ```json
   {
     "Version": "2012-10-17",
     "Statement": [
       {
         "Effect": "Allow",
         "Action": "*",
         "Resource": "*"
       },
       {
         "Effect": "Deny",
         "Action": "s3:*",
         "Resource": "*"
       }
     ]
   }
   ```

2. Go to the **Policies** section in AWS Organizations.
3. Create a new policy:
   - Name it **"Allow All Except S3"**.
   - Copy and paste the policy content above.

### 7. Attaching the SCP to the Production OU

1. Navigate to the **Production OU**.
2. Click on **Policies** → **Attach** → select the **"Allow All Except S3"** policy.
3. Detach the **Full AWS Access** policy to enforce the restriction.

### 8. Observing the Effect of the SCP

- **Switch roles** into the **Production AWS account**.
- Try accessing the **S3 console**:
  - You will receive a **permissions error** due to the **explicit deny** in the SCP.
- Access other services (e.g., EC2) to confirm unrestricted access remains for those services.

### 9. Reverting the SCP

1. Switch back to the **management account**.
2. Navigate to **AWS Organizations** → **Production OU** → **Policies**.
3. Reattach the **Full AWS Access** policy and detach **"Allow All Except S3"**.
4. Verify that access to S3 is restored by switching back to the **Production AWS account** and accessing the S3 bucket.

### 10. Cleanup

1. Delete the **catpics** S3 bucket:
   - Empty the bucket.
   - Delete the bucket.

## Summary

- Created and applied a custom SCP that restricts access to S3 while allowing all other AWS services.
- Demonstrated how SCPs can override permissions, even for roles with **Administrator Access**.
- Illustrated how SCPs are a powerful tool for governing access across AWS accounts in an organization.

This concludes the demonstration. Future lessons will explore further boundaries and restrictions in AWS accounts and identities.
