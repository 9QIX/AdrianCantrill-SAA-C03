# Route 53 Failover and Private Hosted Zones

## One-Click Deployment

To deploy the CloudFormation stack for this lesson, use the following link:

[Deploy CloudFormation Stack](https://console.aws.amazon.com/cloudformation/home?region=us-east-1#/stacks/create/review?templateURL=https://learn-cantrill-labs.s3.amazonaws.com/awscoursedemos/0027-aws-associate-dns-failover-and-private-zones/A4L_VPC_PUBLICINSTANCE.yaml&stackName=DNSANDFAILOVERDEMO)

## Lesson Overview

This lesson covers setting up a private hosted zone in Route 53, associating it with a VPC, creating DNS records, and testing DNS resolution within AWS.

## Steps to Set Up a Private Hosted Zone

### 1. Creating a Private Hosted Zone

1. Navigate to the **Route 53 console**.
2. Go to **Hosted Zones**.
3. Click **Create Hosted Zone**.
4. Enter a domain name (e.g., `ilikedogsreally.com`).
5. Select **Private Hosted Zone**.
6. Associate it with a **default VPC** in `us-east-1`.
7. Click **Create Hosted Zone**.

### 2. Creating a DNS Record

1. Inside the hosted zone, create a new record.
2. Use **Simple Routing Policy**.
3. Set the **Record Name** to `www`.
4. Set the **Record Type** to `A`.
5. Point it to an IP address (e.g., `1.1.1.1`).
6. Set the TTL to `60 seconds`.
7. Click **Create Record**.

### 3. Testing the Private Hosted Zone

1. Copy `www.ilikedogsreally.com`.
2. Open the **EC2 console**.
3. Connect to an instance using **EC2 Instance Connect**.
4. Run the command:
   ```sh
   ping www.ilikedogsreally.com
   ```
5. If the response is "Name or Service not Found," it means the instance is not in the associated VPC.

### 4. Associating Another VPC

1. Go to the **Route 53 console**.
2. Open the **Hosted Zone details**.
3. Click **Edit Hosted Zone**.
4. Add another VPC (`A4L-VPC-1`).
5. Click **Save Changes**.
6. Wait a few minutes and retry the ping test.
7. Once associated, the `ping` command should resolve correctly.

## Cleanup Process

To revert the AWS environment to its original state:

### 1. Delete Health Checks

1. Go to **Route 53 console**.
2. Select **Health Checks**.
3. Delete the health check (`A4L Health`).

### 2. Delete DNS Records and Hosted Zones

1. In **Route 53**, select the private hosted zone.
2. Delete the `www.ilikedogsreally.com` record.
3. Delete the **private hosted zone**.
4. Repeat for the **public hosted zone**.

### 3. Delete S3 Buckets

1. Navigate to **S3 console**.
2. Select the bucket created in the lesson.
3. Empty the bucket and confirm deletion.
4. Delete the bucket.

### 4. Release Elastic IPs

1. Go to **EC2 console**.
2. Navigate to **Elastic IPs**.
3. Disassociate and release the Elastic IP.

### 5. Delete CloudFormation Stack

1. Open the **CloudFormation console**.
2. Select the `DNSANDFAILOVERDEMO` stack.
3. Click **Delete Stack** and confirm.

## Conclusion

This lesson demonstrated the creation of **private hosted zones** and **failover routing** in AWS Route 53. These concepts are valuable for both the **AWS certification exam** and real-world cloud networking scenarios.
