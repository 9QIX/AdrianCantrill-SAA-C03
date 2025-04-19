# AWS Lambda & EventBridge EC2 Automation - Part 1

## Overview

This hands-on lesson demonstrates how to automate the start, stop, and protection of EC2 instances using **AWS Lambda** and **Amazon EventBridge**. The session includes:

- Provisioning EC2 instances with CloudFormation
- Creating and assigning IAM roles with custom policies
- Writing Lambda functions to manage EC2 instances
- Using environment variables in Lambda
- Manually testing the functions via the AWS Console

## Resources

**1-Click EC2 Deployment**  
Creates two t2.micro EC2 instances using CloudFormation:  
[CloudFormation Template](https://console.aws.amazon.com/cloudformation/home?region=us-east-1#/stacks/create/review?templateURL=https://learn-cantrill-labs.s3.amazonaws.com/awscoursedemos/0024-aws-associate-lambda-eventdrivenlambda/twoec2instances.yaml&stackName=TWOEC2)

**Lambda Role Policy (IAM)**  
IAM policy for Lambda execution role:  
[lambdarole.json](https://learn-cantrill-labs.s3.amazonaws.com/awscoursedemos/0024-aws-associate-lambda-eventdrivenlambda/lambdarole.json)

**Python Lambda Scripts**

- Stop EC2: [lambda_instance_stop.py](https://learn-cantrill-labs.s3.amazonaws.com/awscoursedemos/0024-aws-associate-lambda-eventdrivenlambda/01_lambda_instance_stop.py)
- Start EC2: [lambda_instance_start.py](https://learn-cantrill-labs.s3.amazonaws.com/awscoursedemos/0024-aws-associate-lambda-eventdrivenlambda/02_lambda_instance_start.py)
- Protect EC2: [lambda_instance_protect.py](https://learn-cantrill-labs.s3.amazonaws.com/awscoursedemos/0024-aws-associate-lambda-eventdrivenlambda/03_lambda_instance_protect.py)

## IAM Role and Policy Setup

Create an IAM execution role for Lambda with the following custom policy.

### IAM Policy JSON

```json
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Action": ["logs:CreateLogGroup", "logs:CreateLogStream", "logs:PutLogEvents"],
      "Resource": "arn:aws:logs:*:*:*"
    },
    {
      "Effect": "Allow",
      "Action": ["ec2:Start*", "ec2:Stop*"],
      "Resource": "*"
    }
  ]
}
```

### Role Setup Summary

- Service: **Lambda**
- Attach policy above (named e.g., `LambdaStartStop`)
- Role Name: `EC2StartStopLambdaRole`

## Lambda: Stop EC2 Instances

### Python Code

```python
import boto3
import os
import json

region = 'us-east-1'  # Specify the AWS region
ec2 = boto3.client('ec2', region_name=region)  # Create EC2 client

def lambda_handler(event, context):
    instances = os.environ['EC2_INSTANCES'].split(",")  # Read instance IDs from env variable
    ec2.stop_instances(InstanceIds=instances)  # Stop EC2 instances
    print('stopped instances: ' + str(instances))  # Log result
```

### Explanation

- `boto3` is the AWS SDK for Python.
- EC2 instance IDs are passed via the environment variable `EC2_INSTANCES`.
- `stop_instances()` is called with a list of instance IDs.
- This function is manually tested using the AWS Console's "Test" button.

## Lambda: Start EC2 Instances

### Python Code

```python
import boto3
import os
import json

region = 'us-east-1'  # Define the region
ec2 = boto3.client('ec2', region_name=region)  # Create EC2 client

def lambda_handler(event, context):
    instances = os.environ['EC2_INSTANCES'].split(",")  # Get list of instances from env variable
    ec2.start_instances(InstanceIds=instances)  # Start EC2 instances
    print('started instances: ' + str(instances))  # Log output
```

### Explanation

- Nearly identical to the stop function.
- Calls `start_instances()` instead of stopping them.
- Same environment variable mechanism is used for flexibility.

## Steps to Deploy & Test Lambda Functions

### 1. Deploy EC2 via CloudFormation

- Use the 1-click deployment link
- Wait for stack completion
- Note the **Instance IDs** of the two EC2s created

### 2. Create IAM Role

- Go to **IAM > Roles > Create role**
- Choose **Lambda**
- Attach custom policy from `lambdarole.json`
- Name: `EC2StartStopLambdaRole`

### 3. Create Lambda Function (Stop)

- Name: `EC2_Stop`
- Runtime: Python 3.x (as specified in course)
- Execution Role: Use existing – `EC2StartStopLambdaRole`
- Replace default code with contents from `lambda_instance_stop.py`
- Set environment variable:
  - Key: `EC2_INSTANCES`
  - Value: `<instance_id_1>,<instance_id_2>`
- Deploy and **Test** function (no input needed)

### 4. Create Lambda Function (Start)

- Same process as above
- Name: `EC2_Start`
- Use script from `lambda_instance_start.py`
- Use same environment variable
- Deploy and **Test** function

## Summary of Concepts Covered

| Concept                      | Description                                                                   |
| ---------------------------- | ----------------------------------------------------------------------------- |
| **Lambda**                   | Serverless compute to run functions without managing servers                  |
| **EventBridge (later part)** | Allows scheduling/triggering of Lambda functions                              |
| **IAM Role**                 | Provides necessary permissions for Lambda to interact with EC2 and CloudWatch |
| **Environment Variables**    | Passed to Lambda to dynamically control which EC2 instances to affect         |
| **boto3**                    | Python SDK for AWS – used to manage EC2 in this case                          |
| **CloudFormation**           | Infrastructure-as-code to provision EC2 instances                             |
| **Manual Testing**           | Using Lambda Console to run functions without events                          |

## Next Step (Preview)

- Part 2 will explore **automatic** EC2 protection using EventBridge + Lambda.
- The protect function monitors EC2 state changes and automatically restarts if stopped.
