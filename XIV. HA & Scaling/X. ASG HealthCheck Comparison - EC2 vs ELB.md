# AWS Auto Scaling Groups: Health Checks

## Overview

Auto Scaling Groups (ASGs) in AWS monitor the health of their EC2 instances using **health checks**. If an instance fails a health check, it is automatically replaced. This behavior enables **self-healing infrastructure**, which is key to building reliable cloud-native systems.

## Types of Health Checks in Auto Scaling Groups

There are **three types of health checks** available in ASGs:

### 1. EC2 Health Checks (Default)

- **Default health check type.**
- An instance is marked as **unhealthy** if its state is anything other than `running`.
- The following states are considered unhealthy:
  - `stopping`
  - `stopped`
  - `shutting-down`
  - `terminated`
  - `impaired` (failing 1 or both EC2 status checks)

> This type does not provide insight into the application running on the instance — only the EC2-level health is considered.

### 2. ELB (Elastic Load Balancer) Health Checks

- Must be **enabled explicitly** on the ASG.
- For an instance to be **healthy**, it must:
  - Be in the `running` state.
  - **Pass the health check** as defined by the load balancer.

> Especially useful with **Application Load Balancers (ALBs)**, as these support application-level checks. You can:

- Check a specific path (e.g., `/health`)
- Use **pattern matching** to verify application output
- Implement logic that understands your app's readiness

This enables **application-aware health assessments** and better instance lifecycle management.

### 3. Custom Health Checks

- Allows **external systems or scripts** to mark instances as `healthy` or `unhealthy`.
- Useful for:
  - Business-specific logic
  - Integration with monitoring tools
  - Custom bootstrap or shutdown processes

> Extends the health-checking capabilities beyond what AWS provides out-of-the-box.

## Health Check Grace Period

The **Health Check Grace Period** is a critical setting that defines the delay **before** health checks begin on a newly launched instance.

- **Default**: `300 seconds` (5 minutes)
- This timer allows:
  - Bootstrapping (e.g., user data scripts)
  - App/service startup
  - Configuration and registration tasks

### Why It's Important

If the grace period is **too short**, instances may:

- Fail health checks before they're ready
- Get terminated prematurely
- Cause a loop of provisioning → failure → termination

> This often leads to **ASG thrashing**, where instances are continuously created and terminated, consuming resources and incurring cost.

### Best Practice

Know your application startup time and set the grace period **accordingly**.

Example:

```plaintext
If your EC2 instance takes 7 minutes to fully bootstrap and run your app,
set the health check grace period to at least 420 seconds.
```

## Summary

| Feature                       | Description                                     |
| ----------------------------- | ----------------------------------------------- |
| **EC2 Health Checks**         | Default, basic instance-level checks            |
| **ELB Health Checks**         | Application-aware via load balancer             |
| **Custom Health Checks**      | External marking of health status               |
| **Health Check Grace Period** | Delay before checks begin after instance launch |

### Key Takeaways for the Exam

- Know the **default health check behavior**
- Understand how ELB checks add **application-level intelligence**
- Remember the **impact of grace period misconfiguration**
- Recognize when to use **custom health checks**
