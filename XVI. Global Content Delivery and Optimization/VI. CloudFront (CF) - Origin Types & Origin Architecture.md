# CloudFront Origins & Architecture

## Overview

This lesson explores **CloudFront origin types**, **origin architecture**, and the differences between **S3** and **Custom origins**. These concepts are essential for both **real-world CloudFront usage** and **exam preparation**.

## What Are Origins in CloudFront?

**Origins** are the backend sources from which CloudFront retrieves content when it’s not available in an edge cache.

### Key Concepts:

- **CloudFront Distribution**: Connects edge locations to origins.
- **Origin Fetch**: Happens when a cached object is not found in an edge location.
- **Behavior**: Defines which origin or origin group is used for a specific path pattern.

## Origin Groups

- **Purpose**: Provide **resilience and failover**.
- **Configuration**: Combine multiple origins into an **origin group**.
- **Use in Behavior**: Behaviors can point to origin groups to increase availability.

## Types of Origins

| Origin Type                      | Description                         |
| -------------------------------- | ----------------------------------- |
| **Amazon S3 Buckets**            | Direct integration with CloudFront. |
| **AWS MediaPackage** (Channel)   | For media streaming.                |
| **AWS MediaStore** (Container)   | Another media-focused origin.       |
| **Custom Origins** (Web servers) | Everything else: EC2, on-prem, etc. |

> Note: Static website hosting on S3 is treated as a **Custom Origin**, not an S3 origin.

## S3 Origins

### Benefits

- Designed for seamless integration with CloudFront.
- Simple configuration.
- Advanced features like **origin access control**.

### Key Configuration Options

- **Origin Domain Name**: Points to an S3 bucket.
- **Origin Path**: Optional sub-path in the bucket.
- **Origin Access**:
  - **Legacy**: Origin Access Identity (OAI)
  - **Recommended**: Origin Access Control (OAC)

```plaintext
Example:
Origin Path = "/images"
=> Requests are routed to bucket/images/
```

### Protocol Behavior

- **Viewer Protocol Policy** and **Origin Protocol Policy** are **matched**.
  - e.g., HTTP → HTTP, HTTPS → HTTPS

### Headers

- Can pass **custom headers** to the origin.

## Custom Origins

### Example

```plaintext
Origin Domain Name: "categram.io"
```

CloudFront recognizes this is not an S3 bucket and presents additional options.

### Additional Configuration Options

| Setting                    | Description                                                            |
| -------------------------- | ---------------------------------------------------------------------- |
| **Minimum SSL Protocol**   | Choose TLS version. Best practice is using latest supported by origin. |
| **Origin Protocol Policy** | Choose between HTTP only, HTTPS only, or Match Viewer.                 |
| **Ports**                  | Set custom HTTP/HTTPS ports. Default: 80 (HTTP), 443 (HTTPS).          |
| **Headers**                | Custom headers can be passed for security.                             |

> Use **custom headers** to **restrict origin access to CloudFront** if you're not using an S3 origin.

## Comparison: S3 vs Custom Origins

| Feature                        | S3 Origin              | Custom Origin    |
| ------------------------------ | ---------------------- | ---------------- |
| Origin Access Control          | Yes (OAI or OAC)       | No (use headers) |
| Custom Protocol Settings       | No                     | Yes              |
| Custom Ports                   | No                     | Yes              |
| Direct AWS Integration         | Yes                    | No               |
| Treated as Web Server (Static) | Only with website mode | Yes              |

## Exam Tips

- Know the difference in **protocol flexibility**.
- Understand **origin access mechanisms**.
- Expect questions on:
  - Origin protocol matching
  - Minimum SSL versions
  - Custom ports
  - Origin groups

## Final Thoughts

- S3 origins are **ideal for static content**.
- Custom origins offer **granularity and flexibility**.
- Security varies:
  - S3 → Use OAI or OAC.
  - Custom → Use custom headers for access control.
