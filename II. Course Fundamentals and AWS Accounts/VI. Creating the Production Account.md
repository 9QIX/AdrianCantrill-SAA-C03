# Creating and Configuring a Production AWS Account

Welcome back! You’ve successfully set up and configured the general AWS account for this course. Now, to give you a realistic multi-account environment experience, we'll create a new production AWS account. This account will be separate from the general account and will be used for demos requiring multiple AWS accounts.

## Objectives

1. **Create a New Production AWS Account**
2. **Configure the Production AWS Account**
3. **Set Up Multi-Factor Authentication (MFA)**
4. **Configure Billing Preferences and Budgets**

## Steps to Create and Configure the Production AWS Account

### 1. **Decide on an Email Address**

- Use a unique email address for the production AWS account.
- If you used a Gmail address for the general account, consider using the Gmail plus trick to create a unique email address. For example, `yourname+production@gmail.com`.

### 2. **Create the Production AWS Account**

- **Sign-Up**: Follow the same sign-up process you used for the general account.
- **Account Details**: You can use similar details, but choose a different account name, such as `yourname-production` instead of `yourname-general`.
- **Credit Card**: You can use the same credit card.
- **Support Plan**: Pick the same support plan as the general account.

### 3. **Secure the Production AWS Account**

- **Multi-Factor Authentication (MFA)**:
  - Add MFA to the account root user.
  - Ensure you use a separate profile in your MFA application (e.g., Google Authenticator, OnePassword) for the production account.
  - Don’t reuse the MFA setup from the general AWS account.

### 4. **Configure Billing Preferences**

- **Billing Dashboard**:
  - Go to **Billing Dashboard**.
  - Navigate to **Billing Preferences**.
  - Check the following boxes:
    - Receive PDF invoices by email.
    - Receive Free Tier usage alerts.
    - Receive billing alerts.
  - Enter your email address for notifications.

### 5. **Set Up a Budget**

- **Budgets**:
  - Go to the **Budgets** section in the billing console.
  - Click **Create Budget**.
  - Choose a template (e.g., Zero Spend Budget or Monthly Cost Budget).
  - Name your budget and specify the amount if using a monthly cost budget.
  - Enter your email address for notifications.
  - Click **Create Budget**.

### 6. **Enable IAM User and Role Access to Billing**

- **Account Settings**:
  - Go to the **Account Settings**.
  - Enable IAM user and role access to billing.

### 7. **Optional: Add Account Contacts**

- **Account Contacts** (Optional):
  - If you did this for the general account, you can add the same contacts to the production account.

## Conclusion

Follow these steps to create and configure your production AWS account. This hands-on experience will ensure you’re comfortable setting up new AWS accounts and configuring them for various uses.

Complete this video and proceed to create and configure the production AWS account. I look forward to seeing you in the next lesson!
