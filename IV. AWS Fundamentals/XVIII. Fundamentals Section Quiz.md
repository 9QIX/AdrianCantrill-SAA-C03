# AWS SA C03 - Fundamentals Section Quiz

## 1. What Permissions options does an AMI have?

- **Public Access, Owner only, Specific AWS Accounts** (✅ **Correct**)
  - AMI permissions can be set to allow public access, limit it to the owner, or grant access to specific AWS accounts.
- Public Access, Owner only, Specific IAM users (❌ **Incorrect**)
  - IAM users can't directly access AMIs; instead, access is controlled at the account level.
- Public Access, Owner only, Specific Regions (❌ **Incorrect**)
  - AMIs are region-specific by default and aren't shared across regions via permissions.
- Public Access, Specific AWS Accounts, Specific IAM users (❌ **Incorrect**)

## 2. What is NOT stored in an AMI?

- Boot volume (❌ **Incorrect**)
  - The boot volume is part of an AMI.
- Data volumes (❌ **Incorrect**)
  - Data volumes can be part of the AMI but are optional.
- AMI Permissions (❌ **Incorrect**)
  - AMI permissions are stored as part of the AMI.
- **Block Device Mapping** (✅ **Correct**)
  - Block device mapping defines how storage volumes attach to the instance.
- Instance settings (❌ **Incorrect**)
  - Instance settings (like the operating system) are part of the AMI.
- Network Settings (❌ **Incorrect**)
  - AMIs do not store network settings like VPC configuration; this is set during instance creation.

## 3. EC2 is an example of which service model?

- PAAS (❌ **Incorrect**)
  - EC2 is not Platform-as-a-Service; PAAS abstracts more of the infrastructure.
- **IAAS** (✅ **Correct**)
  - EC2 provides infrastructure (virtual machines), making it an Infrastructure-as-a-Service (IAAS).
- SAAS (❌ **Incorrect**)
  - SAAS refers to fully managed software applications, not virtual machines.
- DBaaS (❌ **Incorrect**)
  - DBaaS specifically refers to database services, which EC2 is not.
- FaaS (❌ **Incorrect**)
  - FaaS (Function-as-a-Service) refers to services like AWS Lambda, not EC2.

## 4. What is true of an AWS Public Service?

- Located in the public internet zone (❌ **Incorrect**)
  - Public services like S3 or Lambda are not directly in the public internet zone.
- **Located in the AWS Public zone** (✅ **Correct**)
  - Public services exist within the AWS infrastructure but are accessible via the internet.
- Located in a VPC (❌ **Incorrect**)
  - Public services are not tied to a VPC.
- Publicly accessible by anyone (❌ **Incorrect**)
  - Permissions are still required for access, even for public services.
- **Anyone can connect, but permissions are required to access the service** (✅ **Correct**)
  - Though services are public, access requires proper IAM policies or credentials.

## 5. What is true of an AWS Private Service?

- Located on the Public Internet (❌ **Incorrect**)
  - Private services are not exposed to the public internet.
- Located in the AWS Public Zone (❌ **Incorrect**)
  - Private services are not located in the public zone.
- **Located in a VPC** (✅ **Correct**)
  - Private services are hosted inside a Virtual Private Cloud (VPC).
- **Accessible from the VPC it is located in** (✅ **Correct**)
  - Services in a VPC are accessible within that VPC.
- Accessible from any other VPC (❌ **Incorrect**)
  - Cross-VPC access requires setup like VPC peering or VPNs.
- **Accessible from other VPCs or on-premises networks as long as private networking is configured** (✅ **Correct**)
  - With proper configurations (like Direct Connect or VPN), private services can be accessed.

## 6. What is true of Simple Storage Service (S3)?

- **S3 is an AWS Public Service** (✅ **Correct**)
  - S3 is publicly accessible but requires appropriate permissions.
- S3 is a private service (❌ **Incorrect**)
  - S3 is not a private service; it can be made public or kept private with proper permissions.
- S3 is a web-scale block storage system (❌ **Incorrect**)
  - S3 is an object storage system, not a block storage system.
- **S3 is an object storage system** (✅ **Correct**)
  - S3 stores data in a flat namespace using objects, not blocks or files.
- Buckets can store a limit of 100TB of data (❌ **Incorrect**)
  - There is no upper limit on S3 bucket size.
- **Buckets can store an unlimited amount of data** (✅ **Correct**)
  - S3 has no practical storage limit for buckets.

## 7. What is a CloudFormation Logical Resource?

- A resource in a stack which hasn't been created yet (❌ **Incorrect**)
  - This describes a planned but not-yet-created resource.
- **A resource defined in a CloudFormation Template** (✅ **Correct**)
  - Logical resources exist in the CloudFormation template before the stack is built.
- A resource created in an AWS Account by CloudFormation (❌ **Incorrect**)
  - These are physical resources, not logical resources.
- A name given to a resource created with best practice configuration (❌ **Incorrect**)

## 8. What is a CloudFormation Physical Resource?

- A resource defined in a CloudFormation template i.e., EC2Instance (❌ **Incorrect**)
  - This describes a logical resource, not a physical one.
- **A physical resource created by creating a CloudFormation stack** (✅ **Correct**)
  - Physical resources are actual AWS resources created when a stack is launched.
- A product in AWS which is a physical piece of hardware i.e., a router (❌ **Incorrect**)
  - CloudFormation doesn't create physical hardware but virtual resources.

## 9. What is a simple and correct definition of High Availability?

- **A system which maximizes uptime** (✅ **Correct**)
  - High availability focuses on keeping services running with minimal downtime.
- A System which is highly performing (❌ **Incorrect**)
  - High performance doesn't necessarily mean high availability.
- A System which can operate through failure (❌ **Incorrect**)
  - This describes fault tolerance, not high availability.
- A System which has regular backups and restore processes (❌ **Incorrect**)

## 10. Which of the following is a correct definition of a fault-tolerant system?

- A system which uses automation to return a service to operational status with little user disruption (❌ **Incorrect**)
  - Fault tolerance allows services to continue without needing to be restored.
- A system which has a 99.999% uptime (❌ **Incorrect**)
  - Uptime percentages alone don't define fault tolerance.
- **A system which allows failure, and can continue operating without disruption** (✅ **Correct**)
  - Fault-tolerant systems are designed to continue working even when parts fail.
- A system which has regular and reliable system backups and restore processes (❌ **Incorrect**)

## 11. How many DNS root servers exist?

- 12 (❌ **Incorrect**)
- **13** (✅ **Correct**)
  - There are 13 DNS root server addresses, though they use multiple servers and locations globally.
- 7 (❌ **Incorrect**)
- 100 (❌ **Incorrect**)

## 12. Who manages the DNS Root Servers?

- IANA (❌ **Incorrect**)
  - IANA is involved in the overall management of IP addresses but does not manage root servers.
- **12 Large Organizations** (✅ **Correct**)
  - The root servers are operated by 12 different large organizations around the world.
- IANA Root Server board (❌ **Incorrect**)
- Google (❌ **Incorrect**)
