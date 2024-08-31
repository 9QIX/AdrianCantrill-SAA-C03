# Basic Cost Management for AWS Accounts

Welcome back! In this demo lesson, we'll cover how to manage costs within an AWS account. Specifically, we'll explore the AWS Free Tier and set up a budget to monitor your spending as you progress through the course. Although the goal is to stay within the AWS Free Tier, knowing how to effectively monitor usage is crucial.

## AWS Free Tier Overview

The AWS Free Tier offers a range of services at no cost, which is useful for learning and experimentation. Here are the main categories of Free Tier offers:

- **Free Trials**: Short-term offers for specific services.
- **12-Month Free**: Some services are free for 12 months from the date you first sign up.
- **Always Free**: Certain services are always free up to a specific allocation.

For example:

- **EC2 Instances**: 750 hours per month for the first 12 months.
- **Amazon S3**: 5 GB of standard storage.
- **Amazon RDS**: 750 hours of certain instance types.

Refer to the [AWS Free Tier Overview](https://aws.amazon.com/free/) for a complete list of offers.

## Monitoring Your AWS Costs

AWS provides several tools to help you monitor and manage costs:

1. **Billing Dashboard**:

   - **Access**: Log in as the account root user and navigate to **Billing Dashboard**.
   - **Features**: View bills, payments, credits, cost and usage reports, and forecasts.

2. **Cost Explorer**:

   - Provides granular views of your spending.
   - Allows you to analyze cost trends and forecast future expenses.

3. **Billing Preferences**:
   - **PDF Invoices**: Check the box to receive PDF invoices by email.
   - **Free Tier Alerts**: Enable alerts for approaching Free Tier usage limits.
   - **Billing Alerts**: Set up billing alerts to monitor spending.

## Creating a Cost Budget

Setting up a budget is an effective way to monitor and control your AWS spending. Follow these steps:

1. **Access Budgets**:

   - Navigate to **Billing Dashboard** and click on **Budgets**.

2. **Create a Budget**:

   - Click on **Create Budget**.
   - Choose **Use a Template**.

3. **Select Budget Type**:

   - **Zero Spend Budget**: Alerts you if any charges are incurred.
   - **Monthly Cost Budget**: Alerts you if spending exceeds a specified amount.

4. **Set Up Your Budget**:

   - Enter a name for your budget.
   - For a **Monthly Cost Budget**, specify the amount (e.g., $10 USD).
   - Enter the email address where notifications will be sent.
   - Click **Create Budget**.

5. **Budget Activation**:
   - The budget will take up to 24 hours to populate your spending data.

## Conclusion

You've now set up basic cost management for your AWS account, including understanding the Free Tier and creating a budget to monitor your spending. For production accounts or real business usage, it’s essential to maintain these practices.

Complete this lesson and proceed to the next. I look forward to seeing you there!
