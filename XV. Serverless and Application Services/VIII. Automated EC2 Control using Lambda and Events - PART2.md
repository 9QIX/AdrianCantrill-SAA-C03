# AWS Event-Driven Lambda with EC2 - Part 2

## Overview

This lab demonstrates how to build an **event-driven architecture** using **AWS Lambda**, **EventBridge**, and **EC2**. The goal is to automatically respond to EC2 instance state changes using Lambda functions triggered by events.

## Resources Used

- **CloudFormation Template (Deploys 2 EC2 Instances):**  
  [twoec2instances.yaml](https://learn-cantrill-labs.s3.amazonaws.com/awscoursedemos/0024-aws-associate-lambda-eventdrivenlambda/twoec2instances.yaml)

- **IAM Role for Lambda (Lambda Execution Role):**  
  [lambdarole.json](https://learn-cantrill-labs.s3.amazonaws.com/awscoursedemos/0024-aws-associate-lambda-eventdrivenlambda/lambdarole.json)

- **Lambda Functions:**
  - [lambda_instance_stop.py](https://learn-cantrill-labs.s3.amazonaws.com/awscoursedemos/0024-aws-associate-lambda-eventdrivenlambda/01_lambda_instance_stop.py)
  - [lambda_instance_start.py](https://learn-cantrill-labs.s3.amazonaws.com/awscoursedemos/0024-aws-associate-lambda-eventdrivenlambda/02_lambda_instance_start.py)
  - [lambda_instance_protect.py](https://learn-cantrill-labs.s3.amazonaws.com/awscoursedemos/0024-aws-associate-lambda-eventdrivenlambda/03_lambda_instance_protect.py)

## Lambda Function: EC2 Protect

This function is designed to **automatically start an EC2 instance** if it enters a **stopped** state. It is triggered by EventBridge.

### Python Code

```python
import boto3
import os
import json

region = 'us-east-1'  # Define the AWS region
ec2 = boto3.client('ec2', region_name=region)  # Create an EC2 client in that region

def lambda_handler(event, context):
    print("Received event: " + json.dumps(event))  # Log the event data
    instances = [event['detail']['instance-id']]  # Extract instance ID from the event
    ec2.start_instances(InstanceIds=instances)  # Start the instance using EC2 API
    print('Protected instance stopped - starting up instance: ' + str(instances))  # Log the action
```

### Code Explanation

- **`boto3.client('ec2')`** – Creates a client to interact with EC2.
- **`lambda_handler(event, context)`** – Entry point of the Lambda function.
- **`event['detail']['instance-id']`** – Extracts the instance ID from the CloudWatch event.
- **`ec2.start_instances()`** – Starts the specified EC2 instance.
- **Logging** is used to track the event and actions taken.

## Architecture Flow

1. **Lambda Function Creation (EC2 Protect)**

   - Name: `EC2_protect`
   - Runtime: Python 3.x
   - Uses an **existing IAM role** with EC2 permissions.

2. **Paste and Deploy the Lambda Code**

   - Paste the code into `lambda_function.py`.
   - Deploy.

3. **Create EventBridge Rule**

   - **Rule Name:** `EC2_protect`
   - **Description:** Start protected instance
   - **Event Pattern Rule**
     - Event Source: `aws.ec2`
     - Detail Type: `EC2 Instance State-change Notification`
     - State: `stopped`
     - Specific Instance ID: `<your-instance-1-id>`

4. **Target Configuration**

   - Target: Lambda Function (`EC2_protect`)

5. **Behavior**
   - When instance 1 stops, it generates a state-change event.
   - EventBridge matches the pattern and invokes `EC2_protect`.
   - `EC2_protect` restarts the instance.

## Testing the Workflow

### Scenario 1: Stopping Instance 2

- Not protected.
- Stays stopped after stopping.

### Scenario 2: Stopping Instance 1

- Is protected.
- Triggers EventBridge rule.
- Lambda is invoked.
- Instance is automatically restarted.

## Logs and Monitoring

- Logs are available in **CloudWatch Logs** under:
  ```
  /aws/lambda/EC2_protect
  ```
- Each log stream represents an invocation.
- Event data passed to Lambda is visible in the logs.

## Creating a Competing Scheduled Rule

You can also create a **scheduled EventBridge rule** to stop both instances daily.

### Example CRON Expression (UTC):

```
50 8 * * ? *
```

Runs every day at 8:50 AM UTC.

### Target

- Lambda function: `EC2_stop`

### Behavior

- Scheduled rule runs and stops both EC2 instances.
- Generates state change events.
- Protected instance (Instance 1) is immediately restarted by `EC2_protect`.

## Real-Time Conflict Resolution

- **Stop Rule** stops both instances.
- **Protect Rule** immediately restarts the protected one.
- Demonstrates **multiple rules interacting** via EventBridge and Lambda.

## Cleanup Steps

1. **Delete Lambda Functions**

   - EC2_protect
   - EC2_stop
   - EC2_start (if used)

2. **Delete EventBridge Rules**

   - EC2_protect
   - EC2_stop

3. **Delete IAM Roles/Policies** created for Lambda.

## Final Notes

This lab serves as a great **intro to event-driven architecture** using AWS-native services. You’ve seen:

- EventBridge pattern matching
- Lambda function automation
- Real-time infrastructure control
- CloudWatch for visibility

This model can scale to more complex production environments.
