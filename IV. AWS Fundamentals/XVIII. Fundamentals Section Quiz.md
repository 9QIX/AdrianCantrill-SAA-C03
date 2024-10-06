# AWS SA C03 - Fundamentals Section Quiz

## 1. What Permissions options does an AMI have?

- **Public Access, Owner only, Specific AWS Accounts** (✅ **Correct**)
  - AMIs (Amazon Machine Images) can be shared publicly, restricted to the owner only, or shared with specific AWS accounts. This allows for flexibility in controlling who can use an AMI to launch EC2 instances.
- Public Access, Owner only, Specific IAM users (❌ **Incorrect**)
  - IAM users cannot be directly specified for AMI access. Access is granted at the AWS account level, not the user level.
- Public Access, Owner only, Specific Regions (❌ **Incorrect**)
  - AMIs are region-specific but permissions don't involve selecting specific regions.
- Public Access, Specific AWS Accounts, Specific IAM users (❌ **Incorrect**)

### Conclusion:

- AMIs can be shared publicly, restricted to the owner, or made available to specific AWS accounts, giving you control over who can launch instances from the AMI.

---

## 2. What is NOT stored in an AMI?

- Boot volume (❌ **Incorrect**)
  - The AMI contains a snapshot of the boot volume used to create the instance.
- Data volumes (❌ **Incorrect**)
  - AMIs can include additional data volumes, depending on the configuration.
- AMI Permissions (❌ **Incorrect**)
  - Permissions are a part of the AMI metadata.
- **Block Device Mapping** (✅ **Correct**)
  - Block device mapping refers to how volumes are attached to instances, but this information is not part of the AMI itself.
- Instance settings (❌ **Incorrect**)
  - AMIs include instance configurations like instance type and size.
- Network Settings (❌ **Incorrect**)
  - Network settings are not stored in AMIs; they are configured during instance creation.

### Conclusion:

- AMIs do not store block device mappings. They only store boot volumes and data volumes, along with other essential settings such as permissions and instance configurations.

---

## 3. EC2 is an example of which service model?

- PAAS (❌ **Incorrect**)
  - PAAS abstracts away infrastructure and focuses on providing platforms for developers (e.g., AWS Elastic Beanstalk).
- **IAAS** (✅ **Correct**)
  - EC2 provides virtual machines, making it an Infrastructure-as-a-Service (IAAS) offering where users control the operating system, security patches, etc.
- SAAS (❌ **Incorrect**)
  - SAAS (Software-as-a-Service) refers to complete software solutions (e.g., Gmail, Office365).
- DBaaS (❌ **Incorrect**)
  - DBaaS (Database-as-a-Service) refers to services like Amazon RDS that focus specifically on database management.
- FaaS (❌ **Incorrect**)
  - FaaS (Function-as-a-Service) refers to services like AWS Lambda where users manage code execution, not infrastructure.

### Conclusion:

- EC2 is part of the IAAS (Infrastructure-as-a-Service) model, where AWS provides virtual servers and users control the OS and software environment.

---

## 4. What is true of an AWS Public Service?

- Located in the public internet zone (❌ **Incorrect**)
  - AWS public services are accessible over the internet but aren't part of the public internet zone.
- **Located in the AWS Public zone** (✅ **Correct**)
  - Public services are available in the AWS public zone and can be accessed via the internet.
- Located in a VPC (❌ **Incorrect**)
  - Public services like S3 and DynamoDB do not reside within a VPC.
- Publicly accessible by anyone (❌ **Incorrect**)
  - Although public services are accessible via the internet, proper permissions are still required to access data.
- **Anyone can connect, but permissions are required to access the service** (✅ **Correct**)
  - AWS public services like S3 require correct permissions and authentication, even though they are accessible from the public internet.

### Conclusion:

- Public AWS services are located in the AWS public zone, and while they are internet-accessible, access permissions and security controls are enforced.

---

## 5. What is true of an AWS Private Service?

- Located on the Public Internet (❌ **Incorrect**)
  - Private services are isolated from the public internet.
- Located in the AWS Public Zone (❌ **Incorrect**)
  - Private services reside within private networks, such as VPCs.
- **Located in a VPC** (✅ **Correct**)
  - Private AWS services are hosted inside a VPC (Virtual Private Cloud), giving you control over the network.
- **Accessible from the VPC it is located in** (✅ **Correct**)
  - Private services are accessible only from within the VPC they are hosted in.
- Accessible from any other VPC (❌ **Incorrect**)
  - Private services in one VPC are not directly accessible from other VPCs unless you configure VPC peering or other networking options.
- **Accessible from other VPCs or on-premises networks as long as private networking is configured** (✅ **Correct**)
  - You can access private services from other VPCs or on-prem networks using private connections like Direct Connect or VPN.

### Conclusion:

- AWS private services are located in VPCs and can only be accessed within those VPCs or through specific private networking configurations.

---

## 6. What is true of Simple Storage Service (S3)?

- **S3 is an AWS Public Service** (✅ **Correct**)
  - S3 is a public service that is accessible via the internet, but with strong permission controls.
- S3 is a private service (❌ **Incorrect**)
  - S3 is a public service, though data can be kept private using appropriate permissions.
- S3 is a web-scale block storage system (❌ **Incorrect**)
  - S3 is an object storage system, not block storage.
- **S3 is an object storage system** (✅ **Correct**)
  - S3 stores data as objects, each containing data, metadata, and a unique identifier.
- Buckets can store a limit of 100TB of data (❌ **Incorrect**)
  - S3 does not have a maximum limit for bucket size.
- **Buckets can store an unlimited amount of data** (✅ **Correct**)
  - S3 is designed for unlimited storage capacity across multiple buckets.

### Conclusion:

- S3 is a highly scalable object storage service that belongs to the AWS public service group and allows for unlimited data storage per bucket.

---

## 7. What is a CloudFormation Logical Resource?

- A resource in a stack which hasn't been created yet (❌ **Incorrect**)
  - This description is close but doesn't capture the full meaning of a logical resource.
- **A resource defined in a CloudFormation Template** (✅ **Correct**)
  - A logical resource is an abstraction defined in the CloudFormation template, representing an AWS service or component.
- A resource created in an AWS Account by CloudFormation (❌ **Incorrect**)
  - This refers to a physical resource, not a logical one.
- A name given to a resource created with best practice configuration (❌ **Incorrect**)

### Conclusion:

- A CloudFormation logical resource is defined in the template and represents resources (such as EC2 instances) that will be created when the stack is executed.

---

## 8. What is a CloudFormation Physical Resource?

- A resource defined in a CloudFormation template i.e., EC2Instance (❌ **Incorrect**)
  - This describes a logical resource.
- **A physical resource created by creating a CloudFormation stack** (✅ **Correct**)
  - A physical resource is a real AWS service created by CloudFormation, like an EC2 instance or S3 bucket.
- A product in AWS which is a physical piece of hardware i.e., a router (❌ **Incorrect**)
  - CloudFormation deals with virtual services, not physical hardware.

### Conclusion:

- CloudFormation physical resources are actual AWS services created when a CloudFormation stack is launched.

---

## 9. What is a simple and correct definition of High Availability?

- **A system which maximizes uptime** (✅ **Correct**)
  - High availability refers to a system's ability to maintain operational status and minimize downtime.
- A System which is highly performing (❌ **Incorrect**)
  - High performance does not guarantee high availability.
- A System which can operate through failure (❌ **Incorrect**)
  - This describes a fault-tolerant system.
- A System which has regular backups and restore processes (❌ **Incorrect**)

### Conclusion:

- High availability focuses on maximizing system uptime and reducing the duration of outages.

---

## 10. Which of the following is a correct definition of a fault-tolerant system?

- A system which uses automation to return a service to operational status with little user disruption (❌ **Incorrect**)
  - This definition leans more towards high availability and disaster recovery.
- A system which has a 99.999% uptime (❌ **Incorrect**)
  - Uptime percentages alone do not describe fault tolerance.
- **A system which allows failure, and can continue operating without disruption** (✅ **Correct**)
  - Fault-tolerant systems can withstand component failures and continue operating smoothly.
- A system which has regular and reliable system backups and restore processes (❌ **Incorrect**)

### Conclusion:

- Fault-tolerant systems are designed to continue operating even in the face of failure, ensuring that services remain uninterrupted and available despite potential disruptions.

---

## 11. How many DNS root servers exist?

- 12 (❌ **Incorrect**)
- **13** (✅ **Correct**)
  - There are 13 DNS root server addresses, though each address corresponds to a group of servers distributed across different locations globally, providing redundancy and load balancing.
- 7 (❌ **Incorrect**)
- 100 (❌ **Incorrect**)

### Conclusion:

- There are 13 DNS root servers that serve as the foundation of the global DNS system, helping resolve top-level domain (TLD) queries.

---

## 12. Who manages the DNS Root Servers?

- IANA (❌ **Incorrect**)
  - IANA manages the overall DNS infrastructure and delegation of IP addresses but does not operate the root servers themselves.
- **12 Large Organizations** (✅ **Correct**)
  - The DNS root servers are managed by 12 different organizations around the world. Each of these organizations operates one or more root servers.
- IANA Root Server board (❌ **Incorrect**)
- Google (❌ **Incorrect**)

### Conclusion:

- DNS root servers are managed by 12 major organizations worldwide, which ensures the distributed and secure management of this critical internet infrastructure.

---

## 13. Who Manages the DNS Root Zone?

- **IANA** (✅ **Correct**)
  - IANA (Internet Assigned Numbers Authority) is responsible for managing the root zone, including delegating TLDs to their appropriate registries.
- 12 Large Organizations (❌ **Incorrect**)
  - While 12 organizations manage the root servers, IANA oversees the root zone.
- IANA Root Server Board (❌ **Incorrect**)
- Microsoft (❌ **Incorrect**)
- Nobody manages the root zone – it's managed via the root hints file (❌ **Incorrect**)

### Conclusion:

- IANA is responsible for managing the root zone of the DNS, ensuring that TLDs like .com, .org, and others are correctly delegated.

---

## 14. Which DNS Record Type converts a HOST into an IPv4 Address?

- **A** (✅ **Correct**)
  - The "A" record (Address Record) maps a domain name to an IPv4 address, allowing DNS to convert human-readable domain names into machine-readable IP addresses.
- AAAA (❌ **Incorrect**)
  - AAAA records map domain names to IPv6 addresses.
- TXT (❌ **Incorrect**)
  - TXT records are used to store text information, often for purposes like verifying domain ownership.
- MX (❌ **Incorrect**)
  - MX records specify mail exchange servers for email routing.
- CNAME (❌ **Incorrect**)
  - CNAME records create an alias, mapping one domain name to another.
- NS (❌ **Incorrect**)
  - NS records specify the authoritative name servers for a domain.

### Conclusion:

- The "A" record is responsible for converting a hostname to an IPv4 address, a key function in DNS resolution.

---

## 15. Which DNS Record Type is how the root zone delegates control of .org to the .org registry?

- A (❌ **Incorrect**)
  - The "A" record is used to map domain names to IP addresses, not for delegating control.
- AAAA (❌ **Incorrect**)
  - The "AAAA" record is used to map domain names to IPv6 addresses.
- TXT (❌ **Incorrect**)
  - TXT records are used to store text values, not for domain delegation.
- CNAME (❌ **Incorrect**)
  - CNAME records create aliases for domain names.
- MX (❌ **Incorrect**)
  - MX records are used for email routing.
- **NS** (✅ **Correct**)
  - NS (Name Server) records delegate control of a zone (e.g., .org) to authoritative name servers. For example, the root zone uses NS records to delegate control of the .org zone to the appropriate registry responsible for .org domains.

### Conclusion:

- The NS record is used for delegating control of a domain or zone to the appropriate DNS servers, such as delegating control of .org to the .org registry.

---

## 16. Which type of organization maintains the zones for a TLD (e.g., .ORG)?

- Registrar (❌ **Incorrect**)
  - A registrar is responsible for allowing users to register domain names but does not maintain the TLD zones.
- **Registry** (✅ **Correct**)
  - A registry is responsible for maintaining the zones for a TLD (e.g., .org, .com), including managing the authoritative name servers and database for that TLD.
- IANA (❌ **Incorrect**)
  - IANA oversees the overall coordination of the DNS, but the actual maintenance of the TLD zones is done by registries.
- None of the above (❌ **Incorrect**)

### Conclusion:

- A registry is the organization responsible for maintaining the authoritative DNS zones for a TLD, ensuring that domains under the TLD are properly registered and resolved.

---

## 17. Which type of organization has relationships with the .org TLD zone manager allowing domain registration?

- **Registrar** (✅ **Correct**)
  - A registrar is responsible for registering domain names on behalf of customers and acts as the intermediary between the domain owners and the TLD registry.
- Registry (❌ **Incorrect**)
  - The registry maintains the DNS records for the TLD, but it’s the registrar that facilitates domain name registrations.
- IANA (❌ **Incorrect**)
  - IANA does not handle individual domain registrations; it oversees broader DNS coordination.
- None of the above (❌ **Incorrect**)

### Conclusion:

- Registrars are the organizations responsible for registering domain names with the TLD registry on behalf of customers.

---

## 18. How many subnets are in a default VPC?

- 2 (❌ **Incorrect**)
- 3 (❌ **Incorrect**)
- **Equal to the number of AZs in the region the VPC is located in** (✅ **Correct**)
  - A default VPC automatically creates one subnet per availability zone (AZ) in the AWS region. The number of subnets, therefore, depends on the number of AZs in that specific region.
- 10 (❌ **Incorrect**)

### Conclusion:

- The default VPC creates one subnet per availability zone in a region, meaning the number of subnets is tied to the number of AZs in that region.

---

## 19. What is the IP CIDR of a default VPC?

- It depends on the region (❌ **Incorrect**)
  - The CIDR of the default VPC is the same across all regions.
- Random based on the AWS account (❌ **Incorrect**)
  - The IP CIDR is not randomly assigned.
- You can configure an IP range suitable for your network (❌ **Incorrect**)
  - While you can configure custom VPCs with your own CIDR range, the default VPC has a predefined CIDR block.
- **172.31.0.0/16** (✅ **Correct**)
  - The default VPC always uses the IP address range of `172.31.0.0/16`.
- 10.0.0.0/16 (❌ **Incorrect**)

### Conclusion:

- The IP address range of the default VPC is always `172.31.0.0/16`, providing private IP addresses for resources launched within the default VPC.

---

# **Conclusion:**

This quiz tests key AWS concepts, including **AMI permissions**, the nature of **public and private AWS services**, and foundational services like **S3**, **EC2**, and **CloudFormation**. Other questions cover **DNS**, **VPC subnets**, and networking knowledge, such as **fault tolerance** and **high availability**.

Understanding the difference between various AWS service models (IAAS, PAAS, SAAS), how resources are managed, and the significance of DNS management is crucial for succeeding in AWS certification exams and real-world AWS cloud deployments.
