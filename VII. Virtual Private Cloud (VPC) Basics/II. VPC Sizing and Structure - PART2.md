# AWS SA-C03: VPC Sizing and Structure

## Lesson Links

- [AWS Single VPC Design](https://aws.amazon.com/answers/networking/aws-single-vpc-design/)
- [Google Cloud VPC Documentation](https://cloud.google.com/vpc/docs/vpc)
- [AWS SA Associate VPC Basics GitHub](https://github.com/acantril/aws-sa-associate-saac02/tree/master/07-VPC-Basics/01_vpc_sizing_and_structure)

## Overview

This lesson continues the discussion on VPC (Virtual Private Cloud) sizing and structure. It covers considerations for subnet allocation, availability zones, and IP address planning for scalable AWS architectures.

## VPC Sizing in AWS

![alt text](./Images/image-4.png)

| VPC Size    | Netmask | Subnet Size | Hosts/Subnet | Subnets/VPC | Total IPs |
| ----------- | ------- | ----------- | ------------ | ----------- | --------- |
| Micro       | /24     | /27         | 27           | 8           | 216       |
| Small       | /21     | /24         | 251          | 8           | 2008      |
| Medium      | /19     | /22         | 1019         | 8           | 8152      |
| Large       | /18     | /21         | 2043         | 8           | 16344     |
| Extra Large | /16     | /20         | 4091         | 16          | 65456     |

### **Explanation of VPC Size Categories and Their Details**

In AWS, a **Virtual Private Cloud (VPC)** allows users to create an isolated network environment within AWS. The table you provided outlines different VPC size configurations, including **netmask, subnet size, hosts per subnet, subnets per VPC, and total available IPs**.

### **Breakdown of the Table Components**

| **Column**       | **Explanation**                                                                                                           |
| ---------------- | ------------------------------------------------------------------------------------------------------------------------- |
| **VPC Size**     | Categorizes different VPC sizes (Micro, Small, Medium, Large, Extra Large).                                               |
| **Netmask**      | CIDR (Classless Inter-Domain Routing) notation defining the VPC’s address space (e.g., `/16` means 65,536 total IPs).     |
| **Subnet Size**  | CIDR notation defining the size of each subnet within the VPC (e.g., `/27` means fewer IPs per subnet, `/20` means more). |
| **Hosts/Subnet** | The number of usable IP addresses per subnet (AWS reserves 5 IPs per subnet).                                             |
| **Subnets/VPC**  | Number of subnets that can be created within the VPC.                                                                     |
| **Total IPs**    | The total number of usable IP addresses across all subnets in the VPC.                                                    |

### **Detailed Breakdown by VPC Size**

#### **1. Micro VPC**

- **Netmask:** `/24` (256 total IPs)
- **Subnet Size:** `/27` (32 IPs per subnet, 27 usable)
- **Hosts/Subnet:** 27
- **Subnets per VPC:** 8
- **Total Usable IPs:** **216**
- **Use Case:** Best for small applications with limited networking needs.

#### **2. Small VPC**

- **Netmask:** `/21` (2,048 total IPs)
- **Subnet Size:** `/24` (256 IPs per subnet, 251 usable)
- **Hosts/Subnet:** 251
- **Subnets per VPC:** 8
- **Total Usable IPs:** **2,008**
- **Use Case:** Suitable for small to medium-sized workloads.

#### **3. Medium VPC**

- **Netmask:** `/19` (8,192 total IPs)
- **Subnet Size:** `/22` (1,024 IPs per subnet, 1,019 usable)
- **Hosts/Subnet:** 1,019
- **Subnets per VPC:** 8
- **Total Usable IPs:** **8,152**
- **Use Case:** Medium-sized applications with significant scaling requirements.

#### **4. Large VPC**

- **Netmask:** `/18` (16,384 total IPs)
- **Subnet Size:** `/21` (2,048 IPs per subnet, 2,043 usable)
- **Hosts/Subnet:** 2,043
- **Subnets per VPC:** 8
- **Total Usable IPs:** **16,344**
- **Use Case:** Ideal for large-scale applications needing extensive subnet segmentation.

#### **5. Extra Large VPC**

- **Netmask:** `/16` (65,536 total IPs)
- **Subnet Size:** `/20` (4,096 IPs per subnet, 4,091 usable)
- **Hosts/Subnet:** 4,091
- **Subnets per VPC:** 16
- **Total Usable IPs:** **65,456**
- **Use Case:** Best for enterprise environments or organizations running multiple large applications.

### **Key Takeaways**

1. **Larger VPCs have more IPs but also require better subnet planning** to avoid waste.
2. **Subnet size affects the number of available IPs per subnet**—smaller subnets mean fewer hosts, while larger subnets allow more.
3. **AWS reserves 5 IPs per subnet** for internal use.
4. **Choosing the right VPC size depends on your application needs**—for example, if you anticipate rapid growth, start with a Medium or Large VPC.

AWS provides different VPC sizes, ranging from micro to extra-large:

- **Micro**: `/24` VPC with 8 subnets (`/27` each, 27 IPs per subnet, total 216 IPs)
- **Extra Large**: `/16` VPC with 16 subnets (`/20` each, 4,091 IPs per subnet, total 65,536 IPs)

### Key Questions When Designing a VPC:

1. **How many subnets will you need?**
2. **How many IP addresses per subnet and in total?**

## Subnets and Availability Zones

![alt text](./Images/image-5.png)

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

![alt text](./Images/image-6.png)

- A **documented IP plan** (available in the GitHub repo) outlines the allocation strategy.
- The plan ensures **non-overlapping VPCs** across accounts and regions.
- Future-proofing by reserving extra capacity.

## Animals4Life IP Addressing Plan

- Network: The 10.X network number
- Usage Level: Always "Level 1" in this document
- Region: (USREGION1, USREGION2, USREGION3, EUROPE, AUSTRALIA)
- Tier: (GENERAL, PROD, DEV, RESERVED)
- VPC: The VPC number (1-4)

## Common and Avoid Ranges (10.1 - 10.15)

| Network | Usage Level | Usage  | Region | Tier | VPC |
| ------- | ----------- | ------ | ------ | ---- | --- |
| 10.1    | Level 1     | COMMON | -      | -    | -   |
| 10.2    | Level 1     | COMMON | -      | -    | -   |
| 10.3    | Level 1     | COMMON | -      | -    | -   |
| 10.4    | Level 1     | COMMON | -      | -    | -   |
| 10.5    | Level 1     | RANGES | -      | -    | -   |
| 10.6    | Level 1     | RANGES | -      | -    | -   |
| 10.7    | Level 1     | AVOID  | -      | -    | -   |
| 10.8    | Level 1     | AVOID  | -      | -    | -   |
| 10.9    | Level 1     | AVOID  | -      | -    | -   |
| 10.10   | Level 1     | AVOID  | -      | -    | -   |
| 10.11   | Level 1     | AVOID  | -      | -    | -   |
| 10.12   | Level 1     | AVOID  | -      | -    | -   |
| 10.13   | Level 1     | AVOID  | -      | -    | -   |
| 10.14   | Level 1     | AVOID  | -      | -    | -   |
| 10.15   | Level 1     | AVOID  | -      | -    | -   |

## Main Infrastructure

| Network | Usage Level | Region    | Tier     | Account | VPC  |
| ------- | ----------- | --------- | -------- | ------- | ---- |
| 10.16   | Level 1     | USREGION1 | GENERAL  | ACC     | VPC1 |
| 10.17   | Level 1     | USREGION1 | GENERAL  | ACC     | VPC2 |
| 10.18   | Level 1     | USREGION1 | GENERAL  | ACC     | VPC3 |
| 10.19   | Level 1     | USREGION1 | GENERAL  | ACC     | VPC4 |
| 10.20   | Level 1     | USREGION1 | PROD     | ACC     | VPC1 |
| 10.21   | Level 1     | USREGION1 | PROD     | ACC     | VPC2 |
| 10.22   | Level 1     | USREGION1 | PROD     | ACC     | VPC3 |
| 10.23   | Level 1     | USREGION1 | PROD     | ACC     | VPC4 |
| 10.24   | Level 1     | USREGION1 | DEV      | ACC     | VPC1 |
| 10.25   | Level 1     | USREGION1 | DEV      | ACC     | VPC2 |
| 10.26   | Level 1     | USREGION1 | DEV      | ACC     | VPC3 |
| 10.27   | Level 1     | USREGION1 | DEV      | ACC     | VPC4 |
| 10.28   | Level 1     | USREGION1 | RESERVED | ACC     | VPC1 |
| 10.29   | Level 1     | USREGION1 | RESERVED | ACC     | VPC2 |
| 10.30   | Level 1     | USREGION1 | RESERVED | ACC     | VPC3 |
| 10.31   | Level 1     | USREGION1 | RESERVED | ACC     | VPC4 |
| 10.32   | Level 1     | USREGION2 | GENERAL  | ACC     | VPC1 |
| 10.33   | Level 1     | USREGION2 | GENERAL  | ACC     | VPC2 |
| 10.34   | Level 1     | USREGION2 | GENERAL  | ACC     | VPC3 |
| 10.35   | Level 1     | USREGION2 | GENERAL  | ACC     | VPC4 |
| 10.36   | Level 1     | USREGION2 | PROD     | ACC     | VPC1 |
| 10.37   | Level 1     | USREGION2 | PROD     | ACC     | VPC2 |
| 10.38   | Level 1     | USREGION2 | PROD     | ACC     | VPC3 |
| 10.39   | Level 1     | USREGION2 | PROD     | ACC     | VPC4 |
| 10.40   | Level 1     | USREGION2 | DEV      | ACC     | VPC1 |
| 10.41   | Level 1     | USREGION2 | DEV      | ACC     | VPC2 |
| 10.42   | Level 1     | USREGION2 | DEV      | ACC     | VPC3 |
| 10.43   | Level 1     | USREGION2 | DEV      | ACC     | VPC4 |
| 10.44   | Level 1     | USREGION2 | RESERVED | ACC     | VPC1 |
| 10.45   | Level 1     | USREGION2 | RESERVED | ACC     | VPC2 |
| 10.46   | Level 1     | USREGION2 | RESERVED | ACC     | VPC3 |
| 10.47   | Level 1     | USREGION2 | RESERVED | ACC     | VPC4 |
| 10.48   | Level 1     | USREGION3 | GENERAL  | ACC     | VPC1 |
| 10.49   | Level 1     | USREGION3 | GENERAL  | ACC     | VPC2 |
| 10.50   | Level 1     | USREGION3 | GENERAL  | ACC     | VPC3 |
| 10.51   | Level 1     | USREGION3 | GENERAL  | ACC     | VPC4 |
| 10.52   | Level 1     | USREGION3 | PROD     | ACC     | VPC1 |
| 10.53   | Level 1     | USREGION3 | PROD     | ACC     | VPC2 |
| 10.54   | Level 1     | USREGION3 | PROD     | ACC     | VPC3 |
| 10.55   | Level 1     | USREGION3 | PROD     | ACC     | VPC4 |
| 10.56   | Level 1     | USREGION3 | DEV      | ACC     | VPC1 |
| 10.57   | Level 1     | USREGION3 | DEV      | ACC     | VPC2 |
| 10.58   | Level 1     | USREGION3 | DEV      | ACC     | VPC3 |
| 10.59   | Level 1     | USREGION3 | DEV      | ACC     | VPC4 |
| 10.60   | Level 1     | USREGION3 | RESERVED | ACC     | VPC1 |
| 10.61   | Level 1     | USREGION3 | RESERVED | ACC     | VPC2 |
| 10.62   | Level 1     | USREGION3 | RESERVED | ACC     | VPC3 |
| 10.63   | Level 1     | USREGION3 | RESERVED | ACC     | VPC4 |
| 10.64   | Level 1     | EUROPE    | GENERAL  | ACC     | VPC1 |
| 10.65   | Level 1     | EUROPE    | GENERAL  | ACC     | VPC2 |
| 10.66   | Level 1     | EUROPE    | GENERAL  | ACC     | VPC3 |
| 10.67   | Level 1     | EUROPE    | GENERAL  | ACC     | VPC4 |
| 10.68   | Level 1     | EUROPE    | PROD     | ACC     | VPC1 |
| 10.69   | Level 1     | EUROPE    | PROD     | ACC     | VPC2 |
| 10.70   | Level 1     | EUROPE    | PROD     | ACC     | VPC3 |
| 10.71   | Level 1     | EUROPE    | PROD     | ACC     | VPC4 |
| 10.72   | Level 1     | EUROPE    | DEV      | ACC     | VPC1 |
| 10.73   | Level 1     | EUROPE    | DEV      | ACC     | VPC2 |
| 10.74   | Level 1     | EUROPE    | DEV      | ACC     | VPC3 |
| 10.75   | Level 1     | EUROPE    | DEV      | ACC     | VPC4 |
| 10.76   | Level 1     | EUROPE    | RESERVED | ACC     | VPC1 |
| 10.77   | Level 1     | EUROPE    | RESERVED | ACC     | VPC2 |
| 10.78   | Level 1     | EUROPE    | RESERVED | ACC     | VPC3 |
| 10.79   | Level 1     | EUROPE    | RESERVED | ACC     | VPC4 |
| 10.80   | Level 1     | AUSTRALIA | GENERAL  | ACC     | VPC1 |
| 10.81   | Level 1     | AUSTRALIA | GENERAL  | ACC     | VPC2 |
| 10.82   | Level 1     | AUSTRALIA | GENERAL  | ACC     | VPC3 |
| 10.83   | Level 1     | AUSTRALIA | GENERAL  | ACC     | VPC4 |
| 10.84   | Level 1     | AUSTRALIA | PROD     | ACC     | VPC1 |
| 10.85   | Level 1     | AUSTRALIA | PROD     | ACC     | VPC2 |
| 10.86   | Level 1     | AUSTRALIA | PROD     | ACC     | VPC3 |
| 10.87   | Level 1     | AUSTRALIA | PROD     | ACC     | VPC4 |
| 10.88   | Level 1     | AUSTRALIA | DEV      | ACC     | VPC1 |
| 10.89   | Level 1     | AUSTRALIA | DEV      | ACC     | VPC2 |
| 10.90   | Level 1     | AUSTRALIA | DEV      | ACC     | VPC3 |
| 10.91   | Level 1     | AUSTRALIA | DEV      | ACC     | VPC4 |
| 10.92   | Level 1     | AUSTRALIA | RESERVED | ACC     | VPC1 |
| 10.93   | Level 1     | AUSTRALIA | RESERVED | ACC     | VPC2 |
| 10.94   | Level 1     | AUSTRALIA | RESERVED | ACC     | VPC3 |
| 10.95   | Level 1     | AUSTRALIA | RESERVED | ACC     | VPC4 |

## Unused Animals4Life Ranges

| Network | Usage Level | Region | Tier | Account | VPC |
| ------- | ----------- | ------ | ---- | ------- | --- |
| 10.96   | Level 1     | UNUSED | -    | -       | -   |
| 10.97   | Level 1     | UNUSED | -    | -       | -   |
| 10.98   | Level 1     | UNUSED | -    | -       | -   |
| 10.99   | Level 1     | UNUSED | -    | -       | -   |
| 10.100  | Level 1     | UNUSED | -    | -       | -   |
| 10.101  | Level 1     | UNUSED | -    | -       | -   |
| 10.102  | Level 1     | UNUSED | -    | -       | -   |
| 10.103  | Level 1     | UNUSED | -    | -       | -   |
| 10.104  | Level 1     | UNUSED | -    | -       | -   |
| 10.105  | Level 1     | UNUSED | -    | -       | -   |
| 10.106  | Level 1     | UNUSED | -    | -       | -   |
| 10.107  | Level 1     | UNUSED | -    | -       | -   |
| 10.108  | Level 1     | UNUSED | -    | -       | -   |
| 10.109  | Level 1     | UNUSED | -    | -       | -   |
| 10.110  | Level 1     | UNUSED | -    | -       | -   |
| 10.111  | Level 1     | UNUSED | -    | -       | -   |
| 10.112  | Level 1     | UNUSED | -    | -       | -   |
| 10.113  | Level 1     | UNUSED | -    | -       | -   |
| 10.114  | Level 1     | UNUSED | -    | -       | -   |
| 10.115  | Level 1     | UNUSED | -    | -       | -   |
| 10.116  | Level 1     | UNUSED | -    | -       | -   |
| 10.117  | Level 1     | UNUSED | -    | -       | -   |
| 10.118  | Level 1     | UNUSED | -    | -       | -   |
| 10.119  | Level 1     | UNUSED | -    | -       | -   |
| 10.120  | Level 1     | UNUSED | -    | -       | -   |
| 10.121  | Level 1     | UNUSED | -    | -       | -   |
| 10.122  | Level 1     | UNUSED | -    | -       | -   |
| 10.123  | Level 1     | UNUSED | -    | -       | -   |
| 10.124  | Level 1     | UNUSED | -    | -       | -   |
| 10.125  | Level 1     | UNUSED | -    | -       | -   |
| 10.126  | Level 1     | UNUSED | -    | -       | -   |
| 10.127  | Level 1     | UNUSED | -    | -       | -   |

## Google Range

| Network       | Usage Level | Region | Tier | Account | VPC |
| ------------- | ----------- | ------ | ---- | ------- | --- |
| 10.128-10.255 | Level 1     | GOOGLE | -    | -       | -   |

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
