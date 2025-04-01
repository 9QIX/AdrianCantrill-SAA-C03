# AWS Route 53 DNS Failover and Private Hosted Zones

## Overview

This guide covers configuring DNS failover and private hosted zones using AWS Route 53. The demonstration involves setting up an EC2 instance as the primary web server and an S3 bucket as the backup failover site. If the EC2 instance fails, traffic is automatically redirected to the S3 bucket.

## Prerequisites

- AWS Account
- IAM Admin access
- Domain registered in Route 53 (e.g., `animalsforlife1337.org`)
- AWS region: `us-east-1` (Northern Virginia)

## One-Click Deployment

You can deploy the necessary infrastructure using AWS CloudFormation:
[One-Click Deployment](https://console.aws.amazon.com/cloudformation/home?region=us-east-1#/stacks/create/review?templateURL=https://learn-cantrill-labs.s3.amazonaws.com/awscoursedemos/0027-aws-associate-dns-failover-and-private-zones/A4L_VPC_PUBLICINSTANCE.yaml&stackName=DNSANDFAILOVERDEMO)

## Assets

[Download Assets](https://learn-cantrill-labs.s3.amazonaws.com/awscoursedemos/0027-aws-associate-dns-failover-and-private-zones/r53_zones_and_failover.zip)

### Directory Structure

```
r53_zones_and_failover/
├── 01_a4lwebsite/
│   ├── index.html
│   └── minimal.jpg
├── 02_a4lfailover/
│   ├── index.html
│   └── minimal.jpg
├── A4L_VPC_v2.yaml
├── A4L_WEB.yaml
└── bucket_policy.json
```

## Configuring AWS Infrastructure

### 1. Deploy CloudFormation Stack

1. Click the one-click deployment link.
2. In the CloudFormation console, ensure the `Stack Name` is set to `DNSANDFAILOVERDEMO`.
3. Scroll down, check the required capabilities box, and click **Create Stack**.
4. Wait for the stack status to change to `CREATE_COMPLETE`.

### 2. Verify EC2 Instance

1. Navigate to **EC2 Console**.
2. Click **Instances Running**.
3. Select `A4L_WEB` instance.
4. Copy the **Public IPv4 Address**.
5. Open the IP in a browser to verify the website is live.

### 3. Assign an Elastic IP

1. In the **EC2 Console**, go to **Elastic IPs** under **Network & Security**.
2. Click **Allocate Elastic IP**.
3. Select **us-east-1** region and click **Allocate**.
4. Select the newly allocated IP, click **Actions → Associate Elastic IP**.
5. Associate it with `A4L_WEB` instance.

### 4. Set Up S3 Bucket for Failover

1. Go to **S3 Console**.
2. Create a bucket named `www.yourdomain.com` (replace `yourdomain.com` with your actual domain).
3. Uncheck **Block all public access**.
4. Upload files from `02_a4lfailover/` directory.
5. Enable **Static Website Hosting**:
   - Set `index.html` as **Index Document** and **Error Document**.
6. Set **Bucket Policy** for public access:

```json
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Sid": "PublicRead",
      "Effect": "Allow",
      "Principal": "*",
      "Action": ["s3:GetObject"],
      "Resource": ["arn:aws:s3:::yourbucketname/*"]
    }
  ]
}
```

### 5. Configure Route 53 Health Check

1. Go to **Route 53 Console**.
2. Click **Health Checks → Create Health Check**.
3. Name it `A4L_Health`.
4. Select **Endpoint → IP Address**.
5. Use **Elastic IP of EC2 instance**.
6. Set **Path** to `index.html`.
7. Set **Request Interval** to `Fast`.
8. Click **Create Health Check**.

### 6. Configure Route 53 Failover DNS

1. Go to **Hosted Zones**.
2. Select the domain’s hosted zone.
3. Click **Create Record** → Switch to **Wizard Mode**.
4. Create **Primary Record (EC2)**:
   - Type: `A`
   - Name: `www`
   - TTL: `60` seconds
   - Failover: `Primary`
   - Value: **Elastic IP of EC2**
   - Associate with `A4L_Health` check
5. Create **Secondary Record (S3)**:
   - Type: `A`
   - Name: `www`
   - Failover: `Secondary`
   - Alias: **S3 website endpoint**
   - Record ID: `S3`
6. Click **Create Records**.

### 7. Test Failover Mechanism

1. Open `www.yourdomain.com` in a browser (should load from EC2).
2. Stop the EC2 instance.
3. Refresh Route 53 **Health Checks**.
4. Wait for it to change to `Unhealthy`.
5. Refresh the website; it should load from **S3 Failover**.
6. Start the EC2 instance again.
7. Verify **Health Check** returns `Healthy` and EC2 site is restored.

## Summary

This guide demonstrates how to set up **Route 53 DNS Failover** using an EC2 instance as the primary website and an S3 bucket as the secondary failover site. The failover mechanism is based on health checks that detect EC2 failure and automatically redirect traffic to the S3 bucket.
