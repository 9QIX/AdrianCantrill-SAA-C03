# AWS Macie Demo

## Overview

This mini-project provides hands-on experience with **Amazon Macie**, an AWS security service that uses machine learning to **detect sensitive data** stored in **Amazon S3**. The project involves uploading sample data, enabling Macie, running discovery jobs, setting up notifications via **SNS** and **EventBridge**, creating a custom data identifier for Australian license plates, and cleaning up AWS resources afterward.

## Resources

- **Instructions:** [Learn Cantrill Labs - Macie Demo](https://github.com/acantril/learn-cantrill-io-labs/tree/master/00-aws-simple-demos/aws-macie)

# Step-by-Step Instructions

## 1. Preparation

- Ensure you are logged into AWS with **admin permissions**.
- Recommended AWS Region: **US-East-1 (N. Virginia)**.
- Download or copy the sample data files:
  - `cc.txt` (Credit Card Data)
  - `employees.txt` (Employee Info)
  - `keys.txt` (Access Credentials)
  - `plates.txt` (Vehicle License Plates - AU format)

## 2. Create and Populate an S3 Bucket

- Navigate to **S3 Console**.
- Create a new bucket named:
  ```
  [your-initials]-mixed-data-[random number]
  ```
  Example: `AC-mixed-data-1337`
- Upload all four text files to the bucket.
- Optionally upload a **non-sensitive** file (e.g., a picture of a cat) for variety.

## 3. Enable Amazon Macie

- Go to **Amazon Macie** via the AWS Console.
- Click **Get Started** and **Enable Macie**.
- Ensure you see the Macie console dashboard before proceeding.

## 4. Create a Macie Job

- Go to **S3 Buckets** within Macie.
- Select your newly created bucket.
- Click **Create Job**.
- Choose **One-time Job**.
- Use the default **Managed Data Identifiers** (select **All**).
- Skip custom data identifiers and allow lists for now.
- Name the job (e.g., `SensitiveDataScan`).
- Review and submit the job.

> **Note:** It can take up to 20 minutes for the job to complete.

## 5. Review Macie Findings

- After the job completes, review the findings.
- Identified sensitive data types:
  - **Personal Data** (e.g., names, emails)
  - **Credentials** (e.g., API keys)
  - **Credit Card Information**
- Observations:
  - `plates.txt` (Australian license plates) was **not** flagged because the format is not recognized by default.

## 6. Set Up Notifications with SNS

- Open **Simple Notification Service (SNS)**.
- Create a **Standard Topic** named `macie-alerts`.
- Configure **Access Policy**:
  - Publishers: Only your AWS account.
  - Subscribers: Only your AWS account.
- Create a **Subscription**:
  - Protocol: **Email**
  - Endpoint: Your email address.
- Confirm subscription via email.

## 7. Configure EventBridge for Automation

- Open **Amazon EventBridge**.
- Create a **New Rule** named `macie-events`.
- Event Source: **AWS Services**.
- AWS Service: **Macie**.
- Event Type: **Macie Finding**.
- Target: **SNS Topic** (`macie-alerts`).
- Save and enable the rule.

## 8. Create a Custom Data Identifier

- Go back to **Macie Console**.
- Navigate to **Settings → Custom Data Identifiers**.
- Create a new identifier named `LicensePlates`.
- Use the provided regular expression (regex) to detect **Australian vehicle plates**.

> **Example Regex (provided in the course material):**
>
> ```
> [A-Z]{3}-\d{3}
> ```
>
> _(matches format like "ABC-123")_

## 9. Scan with Custom Identifier

- Create another **One-time Macie Job**.
- Select:
  - **All Managed Data Identifiers**.
  - **Custom Data Identifier**: `LicensePlates`.
- Name the job (e.g., `LicensePlatesScan`).
- Submit and wait for completion.

## 10. Review New Findings

- After job completion:
  - New findings should highlight sensitive data in `plates.txt`.
  - Notifications are sent via **SNS** confirming findings.

# Code Explanation

## Example: Regular Expression Used

```regex
[A-Z]{3}-\d{3}
```

| Part       | Explanation                                   |
| :--------- | :-------------------------------------------- |
| `[A-Z]{3}` | Matches exactly 3 uppercase alphabet letters. |
| `-`        | Matches a hyphen (`-`) character.             |
| `\d{3}`    | Matches exactly 3 digits (0-9).               |

> **In plain words:**  
> This regex matches strings that look like "ABC-123", where "ABC" are capital letters and "123" are numbers.

# Clean Up

After completing the project, **delete** all resources to avoid unnecessary charges:

### 1. SNS Cleanup

- Delete the **SNS topic** (`macie-alerts`).
- Delete **subscriptions**.

### 2. Macie Cleanup

- Disable Macie (if enabled specifically for this project).

### 3. EventBridge Cleanup

- Delete the **EventBridge rule** (`macie-events`).

### 4. S3 Cleanup

- Empty and delete the S3 bucket used for this project.

# Final Notes

This project demonstrated how to:

- Use **Amazon Macie** for automated sensitive data discovery.
- Create **Custom Data Identifiers**.
- Implement **real-time alerts** with **SNS** and **EventBridge**.
- Maintain **event-driven security** within AWS.

Skills from this mini-project are highly applicable to **production environments** for **automated compliance and security monitoring**.
