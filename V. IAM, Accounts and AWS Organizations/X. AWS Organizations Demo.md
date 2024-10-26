# AWS SA C03: AWS Account Structure Creation

In this demo lesson, we create and configure a multi-account structure within AWS Organizations, setting up roles to facilitate cross-account access between a general, production, and development AWS account. This structure will serve as the foundation for the remainder of the course.

## Overview of AWS Account Structure Creation

### Objectives

1. **Establish AWS Organizations** - Convert the general AWS account into the management account.
2. **Add Production and Development Accounts** - Invite an existing production account and create a new development account within the organization.
3. **Configure IAM Roles** - Set up IAM roles for seamless cross-account access.

## Step 1: Create AWS Organization

1. **Login as IAM Admin**:
   - Ensure you are in the general AWS account with the IAM admin role, using the **Northern Virginia region**.
   - **Multiple Browser Sessions**: Use two browsers or separate sessions within one browser to handle multiple accounts simultaneously.
2. **Navigate to AWS Organizations**:
   - Go to **Services > Organizations**, then select **Create Organization**.
   - This process converts the general account into the **management account** of the organization.
3. **Email Verification**:
   - AWS may send a verification email to confirm the management account. Verify before proceeding if prompted.

## Step 2: Invite Production AWS Account

1. **Log into Production AWS Account** in a Separate Browser/Session:
   - As IAM admin of the production account, copy its **Account ID**.
2. **Invite Production Account to Organization**:
   - In the management account, go to **Organizations > Add Account**.
   - Select **Invite Existing Account** and enter the production account's ID.
3. **Account Quota Check**:

   - If you encounter a “too many accounts” error, request a quota increase from AWS Support.

4. **Accept Invitation**:
   - In the production account, navigate to **Organizations > Invitations** and **Accept** the invitation.

## Step 3: Set Up Role for Cross-Account Access

1. **Create IAM Role in Production Account**:
   - **Navigate to IAM > Roles > Create Role** in the production account.
   - Choose **Trusted Entity** as **Another AWS Account** and enter the management account ID.
2. **Grant Permissions**:

   - Assign **Administrator Access** to this role for administrative tasks.

3. **Name the Role**:
   - Use the name **OrganizationAccountAccessRole** (US spelling).
4. **Verify Trust Relationships**:
   - Confirm that the trust relationship in the role allows the management account ID to assume the role.

## Step 4: Role Switching Between Accounts

1. **Switch to Production Account from Management Account**:

   - In the management account, go to **Account Dropdown > Switch Roles**.
   - Enter the **Production Account ID** and **OrganizationAccountAccessRole** as the role name.
   - Assign a **display name** (e.g., `prod`) and select a **color** (e.g., red for production).

2. **Role Switching Shortcut**:
   - This switch role shortcut saves in your browser, enabling quick access to the production account.
   - Switch back to the management account by selecting **Switch Back** in the account dropdown.

## Step 5: Create Development AWS Account

1. **Add Development Account**:

   - In **AWS Organizations > Add Account**, select **Create Account**.
   - Use a naming structure consistent with other accounts (e.g., `development`) and provide a unique email.

2. **Auto-Generated Role**:

   - AWS automatically creates **OrganizationAccountAccessRole** within new accounts, allowing role switching from the management account.

3. **Set Up Switch Role for Development Account**:
   - Repeat the **Switch Role** steps as above for the development account.
   - Use a display name like `dev` and select **yellow** as the color for the development environment.

## Step 6: Verifying Role Switching Across Accounts

1. **Testing Role Switches**:
   - Ensure that switching between **general, production, and development accounts** is seamless using the shortcuts.
   - Confirm access permissions and verify the color codes and names align with account purposes.

## Final Structure Overview

After completing these steps, your AWS Organization includes:

- **Management Account** (General AWS account)
- **Production Account** (Invited account with manually created IAM role)
- **Development Account** (Created within the organization with an auto-generated IAM role)

This three-account structure enables you to manage AWS resources securely and efficiently across separate environments.

Complete this setup before proceeding to the next lesson.
