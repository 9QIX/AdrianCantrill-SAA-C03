# Amazon Inspector Overview

_Amazon Inspector_ is a security assessment service from AWS that analyzes the behavior of AWS resources (such as EC2 instances and container workloads) to identify vulnerabilities or deviations from best practices.

It plays a **minor role in most AWS exams**, and this summary provides the **fundamental 101-level knowledge** you need.

## Purpose of Amazon Inspector

- Scans **EC2 instances**, **operating systems**, and **containers** for vulnerabilities.
- Identifies **unusual traffic** or **configuration risks**.
- Produces a **security findings report**, ordered by severity.

> **Exam Tip**: If you encounter questions about **security reports** or **security assessments** — think **Amazon Inspector**.

## How Amazon Inspector Works

Amazon Inspector can perform two types of assessments:

### 1. Network Assessment

- **Agent optional**: Can run without an agent but adding an agent provides **richer information**.
- **Focus**: Examines network exposure of EC2 instances and other network components.

### 2. Host Assessment

- **Agent required**: Requires an installed agent inside the instance.
- **Focus**: Checks operating system vulnerabilities at the OS level.

## Rule Packages in Amazon Inspector

**Rules packages** determine what Inspector checks. There are two types:

### Network Reachability Package

- Can be used **with or without an agent**.
- **Checks**:

  - Exposure of instances to public networks.
  - End-to-end reachability analysis across:
    - EC2
    - ALB (Application Load Balancer)
    - ELB (Elastic Load Balancer)
    - Direct Connect
    - Internet Gateways
    - Access Control Lists (ACLs)
    - Route Tables
    - Security Groups
    - Subnet and VPC configurations
    - Virtual Private Gateways
    - VPC Peering connections

- **Findings**:
  - **Recognized ports with listeners**: Known ports with applications actively listening.
  - **Recognized ports without listeners**: Known ports exposed but without listening applications.
  - **Unrecognized ports with listeners**: Unknown ports that have active listeners.
  - **No agent installed**: Limited visibility; no way to confirm if something is listening.

> **Important**: Using an agent **provides more detailed information**.

### Host Assessment Packages (Agent Required)

The following packages **require an agent** and are essential for the exam:

#### Common Vulnerabilities and Exposures (CVE)

- Checks against the **CVE database** of known vulnerabilities.
- Vulnerabilities are assigned unique **CVE IDs**.
- Inspector reports include any detected CVE IDs.

> **Exam Tip**: If you see **CVE** mentioned, associate it with **Amazon Inspector**.

#### Center for Internet Security (CIS) Benchmarks

- Verifies compliance with **industry-standard best practices**.
- CIS benchmarks provide **objective security guidance**.
- Helps organizations assess and improve their security posture.

> **Exam Tip**: **CIS** reference → **Amazon Inspector**.

#### Security Best Practices

- A set of **Amazon-provided best practices**, such as:
  - Disabling **root login over SSH**.
  - Using **modern SSH versions**.
  - Enforcing **password complexity**.
  - Setting proper **folder permissions**.

> **Exam Tip**: Keywords like **best practices** or **hardening** link to **Amazon Inspector**.

## Important Exam Notes

- **Agent Use**:
  - Without agent → Only network checks (limited).
  - With agent → Both network and host-level detailed checks.
- **Keywords to Remember**:

  - **Security findings**
  - **CVE IDs**
  - **CIS benchmarks**
  - **Best practices**
  - **Network reachability**
  - **Inspector agent**

- **Minimal memorization required**, but knowing these keywords **helps avoid losing exam marks**.

# Final Thoughts

This is a **fundamental introduction** to Amazon Inspector. If you are preparing for an AWS exam that requires **deeper knowledge**, additional lessons will cover Amazon Inspector **in more depth**.
