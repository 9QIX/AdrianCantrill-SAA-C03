# AWS SA-C03: VPC Sizing and Structure

## Lesson Links

- [AWS Single VPC Design](https://aws.amazon.com/answers/networking/aws-single-vpc-design/)
- [Google Cloud VPC Documentation](https://cloud.google.com/vpc/docs/vpc)
- [AWS SA Associate VPC Basics GitHub](https://github.com/acantril/aws-sa-associate-saac02/tree/master/07-VPC-Basics/01_vpc_sizing_and_structure)

## Overview

This lesson continues the discussion on VPC (Virtual Private Cloud) sizing and structure. It covers considerations for subnet allocation, availability zones, and IP address planning for scalable AWS architectures.

## VPC Sizing in AWS

![alt text](image-4.png)

AWS provides different VPC sizes, ranging from micro to extra-large:

- **Micro**: `/24` VPC with 8 subnets (`/27` each, 27 IPs per subnet, total 216 IPs)
- **Extra Large**: `/16` VPC with 16 subnets (`/20` each, 4,091 IPs per subnet, total 65,536 IPs)

### Key Questions When Designing a VPC:

1. **How many subnets will you need?**
2. **How many IP addresses per subnet and in total?**

## Subnets and Availability Zones

![alt text](image-5.png)

- Services in AWS use **subnets** within a VPC, not the VPC itself.
- Each **subnet is located in a single availability zone (AZ)**.
- The number of AZs a VPC spans affects **high availability and resilience**.
- Some AWS regions have limited AZs (e.g., three or more).

### Recommended Availability Zone Setup

- Default recommendation: **3 AZs + 1 spare (A, B, C, and a spare)**.
- This means the VPC must have **at least 4 subnets**.

### Infrastructure Tiers

- Typical architecture includes the following tiers:
  - **Web Tier**
  - **Application Tier**
  - **Database Tier**
  - **Spare (future expansion)**
- Each tier requires its own subnet in each AZ.

### Example Subnet Allocation

- **1 AZ, 4 tiers**: 4 subnets
- **4 AZs, 4 tiers**: 16 subnets

### Example VPC Size Breakdown

| VPC Prefix | Number of Subnets | Subnet Prefix |
| ---------- | ----------------- | ------------- |
| `/16`      | 16                | `/20`         |
| `/17`      | 16                | `/21`         |
| `/18`      | 16                | `/22`         |

## IP Address Planning for a Global Organization

### Assumptions

- **Organization**: "Animals for Life"
- **Expected Growth**: High
- **Regions**:
  - **3 in the US**
  - **1 in Europe**
  - **1 in Australia**
- **IP Address Range**: Avoiding common and Google Cloud reserved ranges.
- **Preferred Range**: `10.16.0.0/12`

### Regional IP Address Allocation

| Region      | IP Range                            |
| ----------- | ----------------------------------- |
| US Region 1 | `10.16.0.0/16` - `10.31.255.255/16` |
| US Region 2 | `10.32.0.0/16` - `10.47.255.255/16` |
| US Region 3 | `10.48.0.0/16` - `10.63.255.255/16` |
| Europe      | `10.64.0.0/16` - `10.79.255.255/16` |
| Australia   | `10.80.0.0/16` - `10.95.255.255/16` |

### AWS Account and VPC Structure

- **3 AWS Accounts**: `General`, `Prod`, `Dev`
- **1 Reserved Account**
- **Each account gets 4 VPCs per region**
- **Each VPC gets a `/16` range**

## Implementation Strategy

![alt text](image-6.png)

- A **documented IP plan** (available in the GitHub repo) outlines the allocation strategy.
- The plan ensures **non-overlapping VPCs** across accounts and regions.
- Future-proofing by reserving extra capacity.

## Summary and Next Steps

- **Key Takeaways**:
  - Plan for **growth** and **high availability**.
  - Choose a **VPC size** based on **subnet requirements**.
  - Allocate **IP addresses efficiently** to prevent conflicts.
  - Follow a **structured approach** for subnetting within a VPC.
- **Next Topics**:
  - Technical aspects of AWS private networking.
  - Detailed configurations for VPCs and subnets.

This lesson serves as the **foundation for network topology** planning throughout the AWS SA-C03 course. The referenced IP planning document will be used in future lessons.
