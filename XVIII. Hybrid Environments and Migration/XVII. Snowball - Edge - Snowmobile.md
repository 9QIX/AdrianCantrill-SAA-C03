# AWS Snow Family

## Introduction

AWS provides **physical data transfer devices** for moving large amounts of data between **on-premises** environments and **AWS cloud**. These services include:

- **AWS Snowball**
- **AWS Snowball Edge**
- **AWS Snowmobile**

These services are essential when **internet-based transfers** (even with **Direct Connect**) are impractical due to **large data volumes** or **limited network speed**.

## AWS Snowball

### Overview

- A **physical storage device**.
- Used to move **large datasets** into or out of AWS.
- Devices are **ordered** through AWS and **physically delivered** to customers.
- **Encryption**: All data on Snowball is encrypted using **AWS KMS**.

### Device Details

- Two types of devices:
  - **50 TB** capacity
  - **80 TB** capacity
- **Network Connectivity**:
  - 1 Gigabit Ethernet (1GbE)
  - 10 Gigabit Ethernet (10GbE)

### Economical Use Case

- Best for data volumes **between 10 TB to 80 TB**.
- **Multiple devices** can be ordered for **multiple premises**.

### Key Points for Exam

- **Storage only** (no compute).
- **Physical networking** required.
- Best suited for **large scale, single-site data migration** without processing needs.

## AWS Snowball Edge

### Overview

- **Enhanced** version of Snowball.
- Provides **both storage and compute capabilities**.
- Suitable for **data processing at the edge** before transfer.

### Device Details

- **Networking Speeds**:
  - 10GbE over RJ45
  - 10/25GbE over SFP+
  - 40/50/100GbE over QSFP+

### Types of Snowball Edge

| Variant                        | Storage                      | Compute (vCPUs) | Memory (GIB) | Special Features                               |
| :----------------------------- | :--------------------------- | :-------------- | :----------- | :--------------------------------------------- |
| **Storage Optimized**          | 80 TB                        | 24 vCPUs        | 32 GiB       | Optional 1TB SSD for local EC2                 |
| **Compute Optimized**          | 100 TB + 7.68TB NVMe         | 52 vCPUs        | 208 GiB      | High-speed PCIe storage                        |
| **Compute Optimized with GPU** | Similar to Compute Optimized |                 |              | Includes GPU for parallel/scientific workloads |

### Key Points for Exam

- Use **Snowball Edge** if:
  - **Remote data processing** is needed.
  - **Faster data loading** is required.
  - **Higher compute and memory** capabilities are necessary.

## AWS Snowmobile

### Overview

- **Massive scale** physical data migration service.
- Literally a **truck with a shipping container** containing **a portable data center**.

### Device Details

- Capacity: **Up to 100 Petabytes** per Snowmobile.
- Delivered and installed on-premises.
- Requires **data center-grade power and networking**.

### Use Cases

- Suitable for **single-site** migrations.
- Typically used when **over 10 Petabytes** of data needs transferring.
- Not suited for **multi-site migrations**.

### Key Points for Exam

- **Single device** per location.
- **Cannot** move between multiple sites.
- Used only for **very large, single-location** data migrations.

## Important Architectural Considerations

- **Snowball**:
  - Storage-only.
  - Smaller scale migrations (10TB–80TB).
- **Snowball Edge**:
  - Storage and compute.
  - Edge processing needed or higher throughput required.
- **Snowmobile**:
  - Ultra-large data migrations (>10PB).
  - Single-site only.

## Code/Command References

**Note**: No direct code examples were provided in the lesson.  
However, typically in AWS CLI you would interact with Snowball like:

```bash
aws snowball create-job --job-type IMPORT --resources {...} --address-id addr-123456 --shipping-option SECOND_DAY --role-arn arn:aws:iam::123456789012:role/SnowballRole
```

### Line-by-Line Explanation

| Line                                                     | Explanation                                                    |
| :------------------------------------------------------- | :------------------------------------------------------------- |
| `aws snowball create-job`                                | AWS CLI command to create a new Snowball job.                  |
| `--job-type IMPORT`                                      | Specifies the type of job: `IMPORT` for uploading data to AWS. |
| `--resources {...}`                                      | Details the resources involved (like Amazon S3 buckets).       |
| `--address-id addr-123456`                               | The shipping address where Snowball will be delivered.         |
| `--shipping-option SECOND_DAY`                           | Chooses the shipping speed (e.g., second-day delivery).        |
| `--role-arn arn:aws:iam::123456789012:role/SnowballRole` | Specifies the IAM role for permissions to access AWS services. |

# Conclusion

Understanding the **AWS Snow Family** is crucial for the AWS Certified Solutions Architect Associate (SAA-C03) exam. Focus primarily on:

- **When to use each device**.
- **Storage vs Compute capabilities**.
- **Single vs Multi-site migration** needs.

You are not expected to memorize the **order processes** but to understand the **architectural decision points**.
