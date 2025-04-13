# Stage 6: Cleanup

This stage focuses on **reverting the AWS environment** used in the Elastic WordPress Evolution lab to its original, clean state by systematically deleting all resources that were created.

## Step-by-Step Cleanup Instructions

### 1. **Delete the Load Balancer**

- Navigate to **EC2 Console > Load Balancers**
- Select the load balancer used in the demo
- Click `Actions > Delete`, confirm deletion

### 2. **Delete Target Group**

- Navigate to **EC2 Console > Target Groups**
- Select `A4L-WordPress-ALB-TG`
- Click `Actions > Delete`, confirm deletion

### 3. **Delete Auto Scaling Group (ASG)**

- Navigate to **EC2 Console > Auto Scaling Groups**
- Select `A4L-WordPress-ASG`
- Click `Delete`, type `delete` to confirm
- This may take time since EC2 instances will terminate

### 4. **Delete EFS File System**

- Open **EFS Console**
- Select the created file system
- Click `Delete`, paste the File System ID to confirm
- Wait as mount targets and file system are deleted

### 5. **Delete RDS Instance**

- Navigate to **RDS Console > Databases**
- Select `A4L-WordPress`
- Click `Actions > Delete`
- Uncheck:
  - `Create final snapshot`
  - `Retain automated backups`
- Acknowledge deletion, type `delete me`, click delete

### 6. **Delete Launch Template**

- Navigate to **EC2 Console > Launch Templates**
- Select the created launch template
- Click `Actions > Delete Template`, type `delete` to confirm

### 7. **Delete Parameter Store Entries**

- Navigate to **Systems Manager > Parameter Store**
- Select parameters starting with:
  ```
  /A4L/WordPress/*
  ```
- Click `Delete`, confirm deletion

### 8. **Wait for Final RDS Deletion**

- Return to **RDS Console**, ensure `A4L-WordPress` instance is fully deleted

### 9. **Delete Subnet Group**

- In the **RDS Console > Subnet Groups**
- Select the `WordPress-RDS-Subnet-Group`
- Click `Delete`, confirm

### 10. **Delete CloudFormation Stack**

- Navigate to **CloudFormation Console**
- Select the initial deployment stack
- Click `Delete`, confirm
- This will remove:
  - VPC
  - Subnets
  - Any remaining resources from the one-click deployment

## Final Notes

- **Congratulations** – once the above steps are completed, the AWS environment is fully reset.
- This cleanup process ensures **no lingering resources** which might incur costs.
- The demo series is ideal for those preparing for **scenario-based AWS interviews**, especially for:
  - Solutions Architects
  - Cloud Consultants

## Purpose of the Demo Series

- Teaches how to evolve infrastructure using **AWS-native tools**
- Moves from a **single-server WordPress deployment** to a **scalable, resilient, self-healing architecture**
- Focuses on applying **real-world AWS skills**, making it suitable for:
  - First-time AWS job applicants
  - Practicing AWS architecture tasks
  - Improving practical cloud knowledge

## Instructor’s Recommendation

Keep an eye on:

- **[GitHub Repository](https://github.com/acantril/learn-cantrill-io-labs)**
- **Course Updates** for new advanced demos

These demos offer real-world relevance and can significantly boost your AWS skillset and interview readiness.
