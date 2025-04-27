# AWS Shield Overview

AWS Shield is a critical tool for protecting internet-connected environments from Distributed Denial of Service (DDoS) attacks. It comes in two versions: **Shield Standard** and **Shield Advanced**, offering varying levels of protection.

## Types of DDoS Attacks AWS Shield Protects Against

### 1. **Network Volumetric Attacks (Layer 3)**

- These attacks flood the network with a massive volume of traffic to overwhelm the target system.
- Focus is on sending as much data as possible to congest network resources.

### 2. **Network Protocol Attacks (Layer 4)**

- Example: **SYN floods** where numerous connection requests are initiated but never completed.
- Aim: To exhaust server resources (connections), making it unable to handle legitimate users.
- **Analogy**: Like a call center where all lines are occupied by silent calls, preventing real customers from reaching an agent.

### 3. **Application Layer Attacks (Layer 7)**

- Targets specific application functions, such as search features.
- These attacks send massive legitimate-looking requests that are cheap to make but expensive to process for the server.
- Can severely degrade performance without necessarily consuming network bandwidth.

## AWS Shield Versions

### Shield Standard

- **Cost**: Free for all AWS customers.
- **Protection Scope**:
  - Operates at the **network perimeter** (at VPC level or AWS Edge locations via CloudFront/Global Accelerator).
  - Protects against **common Layer 3 and Layer 4 attacks**.
- **Best When Used With**:
  - Amazon Route 53
  - AWS CloudFront
  - AWS Global Accelerator
- **Limitations**:
  - No proactive, configurable, or fine-grained protection.
  - Works automatically in the background without user intervention.

### Shield Advanced

- **Cost**:
  - $3,000 USD/month per organization (annual commitment required).
  - $36,000 USD/year.
  - Additional **data transfer costs** apply.
- **Protection Scope**:
  - Extends to:
    - CloudFront
    - Route 53
    - Global Accelerator
    - Elastic IP addresses (e.g., EC2 instances)
    - Application Load Balancers (ALB)
    - Classic Load Balancers (CLB)
    - Network Load Balancers (NLB)
- **Configuration**:
  - **Protection must be explicitly enabled** (either manually or via AWS Firewall Manager policies).
  - **Not enabled automatically** — must configure protected resources.

## Additional Features of Shield Advanced

### 1. **Cost Protection**

- Protects customers from unexpected charges resulting from a DDoS attack.
- **Example**: Costs from EC2 auto-scaling events triggered by a DDoS attack.
- **Conditions**:
  - Coverage must have been enabled on the impacted resources.
  - Not every cost will qualify; AWS evaluates it based on guidelines.

### 2. **Access to AWS Shield Response Team (SRT)**

- Specialized support during and after DDoS attacks.
- SLA (Service Level Agreement) response times vary by support plan (e.g., 15 minutes to 1 hour).
- Helps in attack mitigation, incident analysis, and post-event reviews.

# Important Exam Tip

- **Shield Standard** is **automatic**.
- **Shield Advanced** requires **explicit configuration**.
- Understand the differences for both real-world use and AWS Certified Solutions Architect Associate (SAA-C03) exam questions.
