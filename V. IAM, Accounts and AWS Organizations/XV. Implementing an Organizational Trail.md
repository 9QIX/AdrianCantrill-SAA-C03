# CloudTrail Demo: Setting Up an Organizational Trail

This guide walks you through setting up an AWS CloudTrail organizational trail to log data for all accounts in your organization to S3 and CloudWatch Logs. This demo provides detailed steps for configuration, along with insights into key concepts and pricing.

## **Prerequisites**

- Log in as the **IAM Admin User** of the **Management Account** in your AWS Organization.

## **CloudTrail Pricing Overview**

- **90 Days of Event History**: Free for every AWS account.
- **One Copy of Management Events per Region**: Free in every account.
- **Additional Management Events**: $2 per 100,000 events.
- **Data Events**: $0.10 per 100,000 events (regardless of the number of trails).
- **S3 Storage**: Charged based on usage (covered by S3 free tier in this demo).

## **Steps to Create an Organizational Trail**

### 1. **Access CloudTrail Console**

- Navigate to **CloudTrail Console** from the management account.
- Ensure you are using the **new console version**.

### 2. **Create a New Trail**

- Click **Create Trail**.
- Provide a **Trail Name**: e.g., `animals-for-life-org`.
- Enable the trail for **all regions in all accounts**.

### 3. **Set Up S3 Bucket for Logs**

- Choose to **create a new S3 bucket**.
- Use a globally unique bucket name (e.g., `cloudtrail-animals-for-life-12345`).
- **Uncheck encryption options** for this demo.

### 4. **Optional Additional Settings**

- **Log File Validation**: Enables detection of tampered files.
- **SNS Notification**: Sends notifications for log delivery (not enabled in this demo).

### 5. **Enable CloudWatch Logs**

- Enable storing logs in **CloudWatch Logs** for enhanced functionality:
  - Perform searches and analyze historical logs.
  - Trigger events for specific log patterns (e.g., via Lambda functions).

### 6. **Set Up IAM Role for CloudWatch Logs**

- Create a new IAM role for CloudTrail with a descriptive name:
  - e.g., `cloudtrail_role_for_cloudwatch_logs_animals_for_life`.
- Review the IAM policy document (details discussed in the course).

## **Configure Event Logging**

### Event Types:

1. **Management Events**: Logs actions like starting/stopping EC2 instances, modifying AWS resources.
2. **Data Events**: Logs actions on resources (e.g., S3 object-level actions).
   - **Not enabled** in this demo.
3. **Insight Events**: Identifies unusual activity or errors.
   - **Not enabled** in this demo.

### Configuration for this Demo:

- **Log Management Events**: Ensure both read and write are checked.
- Leave **Data Events** and **Insight Events** unchecked.

## **Verify and Access Logs**

### 1. **Check S3 Bucket**

- After ~10–15 minutes, logs should appear in the S3 bucket.
- Navigate the folder structure to access specific logs.

### 2. **View Logs in CloudWatch**

- Open **CloudWatch Logs** console.
- Locate the log group created for your trail.
- Explore log streams categorized by:
  - **Organizational ID**
  - **Account Number**
  - **Region**

### 3. **Inspect Event Details**

- CloudTrail events contain detailed information, such as:
  - **User Identity**: Who performed the action.
  - **Event Name**: Action taken (e.g., `CreateTrail`).
  - **Source IP and Region**.
- Logs in CloudWatch have the same format as those in S3.

## **Event History**

- **Event History** in CloudTrail provides 90 days of events without a trail.
- Trails enable persistent storage in S3 and integration with CloudWatch Logs.

## **Conclusion**

This demo covered creating a CloudTrail organizational trail, storing logs in S3, and enabling CloudWatch Logs integration. These steps form the foundation for advanced AWS monitoring and event-driven workflows.
