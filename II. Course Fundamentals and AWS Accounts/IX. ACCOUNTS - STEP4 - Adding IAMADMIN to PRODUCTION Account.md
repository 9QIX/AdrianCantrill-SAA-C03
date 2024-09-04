# Securing AWS Accounts and Creating IAM Admin Identities

## Overview

In this section, we will learn how to further secure AWS accounts by creating **IAM Admin** identities. This process is vital to ensure that we don't use the **root user** for day-to-day or production purposes. Instead, we create **IAM Admin** users for both the general and production accounts with full permissions, secured by **Multi-Factor Authentication (MFA)**.

The steps below summarize the process of creating these identities for both accounts and setting up MFA.

## Step 1: General AWS Account - Creating IAM Admin Identity

### 1.1: Importance of Avoiding the Root User

- **Root User** has unrestricted access and should only be used when absolutely necessary.
- Instead, create an **IAM Admin** user for administrative tasks.

### 1.2: Setting Up IAM Identity for General AWS Account

- Navigate to the **IAM Console** by typing "IAM" in the service search box.
- Go to **Users** and click **Add Users**.
- Name the user **IAM Admin** (this name only needs to be unique within this account).

### 1.3: Granting Permissions

- Grant the **IAM Admin** user access to the **AWS Management Console** by checking the appropriate box.
- Attach the **AdministratorAccess** policy, granting full control over the account.

### 1.4: Secure IAM Admin User with MFA

- Once created, go to **My Security Credentials** and click on **Assign MFA Device** under **Multi-factor Authentication**.
- Choose the **Authenticator App** option, scan the QR code, and enter two consecutive MFA codes to secure the identity.

### 1.5: Logging in as IAM Admin

- Sign out of the root user.
- Use the custom **IAM sign-in URL** and log in with the newly created **IAM Admin** user credentials.
- Test that the account is fully functional and MFA is correctly set up.

## Step 2: Production AWS Account - Creating IAM Admin Identity

### 2.1: Logging into the Production Account

- Log into the **production AWS account** using the **root user**.
- Ensure you are in the **US-East-1** region, as this is the default for AWS services.

### 2.2: Creating IAM Admin for the Production Account

- Follow the same steps as outlined for the general account:
  - Create a user named **IAM Admin**.
  - Grant console access and attach the **AdministratorAccess** policy.

### 2.3: Setting Up MFA for IAM Admin

- As with the general account, secure the **IAM Admin** user by assigning an MFA device.
- Use the **Authenticator App**, scan the QR code, and set up two consecutive MFA codes.

### 2.4: Logging in and Securing Production Account

- Log out of the **root user** and sign in using the **IAM Admin** account and MFA.
- Ensure the account is fully secured with the appropriate username, password, and one-time code.

## Conclusion

By the end of this process, you will have:

- Two AWS accounts (General and Production), each with:
  - A secured **root user**.
  - A fully functional **IAM Admin** identity.
- All accounts are protected with MFA, and you will require both usernames, passwords, and one-time passwords to access these identities.

These steps are essential for securing your AWS environments and ensuring best practices for identity and access management throughout your AWS journey.

With these setups complete, proceed with the next lesson for further guidance on managing your AWS infrastructure securely.
