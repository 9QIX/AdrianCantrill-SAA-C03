# Cleanup After Serverless Pet Cuddle-O-Tron Demo

This document summarizes the final cleanup phase of the **Advanced Serverless Demo** from [Cantrill.io's AWS SAA-C03 course](https://github.com/acantril/learn-cantrill-io-labs/tree/master/aws-serverless-pet-cuddle-o-tron). This step ensures your AWS account is returned to its original state after completing the project.

## Common Issues?

Before proceeding, if you face any problems during cleanup:

- **Check here**: [Common Issues Page](https://github.com/acantril/learn-cantrill-io-labs/blob/master/aws-serverless-pet-cuddle-o-tron/02_LABINSTRUCTIONS/CommonIssues.md)
- **Follow the latest instructions**: [Updated Instructions](https://github.com/acantril/learn-cantrill-io-labs/tree/master/aws-serverless-pet-cuddle-o-tron)

## 1. Delete the S3 Bucket (Hosting the Frontend)

**Steps:**

- Navigate to the **S3 Console**.
- Locate the S3 bucket used for your app (example: `petcodalitron1337`).
- Select the bucket.
- Click **Empty**:
  - Type `permanently delete` to confirm.
- After emptying, click **Delete**:
  - Type the exact bucket name to confirm deletion.

**Purpose:**  
The bucket hosted the static front-end for the demo. Deleting it ensures there are no lingering charges or artifacts.

## 2. Delete the API Gateway

**Steps:**

- Go to the **API Gateway Console**.
- Find and select the **`petcodalitron`** API.
- Click **Delete**.
- Confirm the deletion.

**Purpose:**  
This removes the REST API endpoint used by the front-end and Lambda to interact.

## 3. Delete Lambda Functions

**Steps:**

- Go to the **Lambda Console**.
- Delete both functions:
  - `email_reminder_lambda`
  - `api_lambda`
- For each:
  - Click the function.
  - Choose **Actions > Delete**.
  - Confirm deletion.

**Purpose:**  
These functions were responsible for sending emails and handling API logic. Removing them prevents unnecessary execution and charges.

## 4. Delete the Step Functions State Machine

**Steps:**

- Open the **Step Functions Console**.
- Select the **`petcodalitron`** state machine.
- Click **Delete** and confirm.

**Tip:**  
Deletion can take a few minutes. Refresh the page until it’s removed.

**Purpose:**  
This managed the orchestration flow (e.g., scheduling reminders) for the serverless workflow.

## 5. Delete CloudFormation Stacks (IAM Roles)

Two CloudFormation stacks were used to provision IAM roles.

**Steps:**

- Open the **CloudFormation Console**.
- Delete these stacks:
  1. `lambda-role`
  2. `state-machine-role`
- For each:
  - Select the stack.
  - Click **Delete**.
  - Confirm deletion.

**Purpose:**  
Removes IAM roles created specifically for Lambda and Step Functions, maintaining good IAM hygiene.

## Final State

After completing all the steps above, your AWS environment will be returned to the pre-demo state. All infrastructure related to the **Serverless Pet Cuddle-O-Tron** project will be removed.

## Additional Notes

- Always double-check each deletion before confirming.
- Make sure all deletions have completed before closing the console.
- This cleanup prevents unexpected charges on your AWS account.

## Want to Try Again?

Clone or review the full advanced demo repo here:

- [GitHub Repository - AWS Serverless Pet Cuddle-O-Tron](https://github.com/acantril/learn-cantrill-io-labs/tree/master/aws-serverless-pet-cuddle-o-tron)
