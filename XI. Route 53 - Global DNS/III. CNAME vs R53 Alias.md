# CNAME vs Alias Records in AWS Route 53

## **Introduction**

This lesson explains the key differences between **CNAME records** and **Alias records** in **AWS Route 53**. Understanding when to use each is critical for both AWS **certification exams** and real-world implementations, especially when working with **Elastic Load Balancers (ELBs), API Gateway, CloudFront, and S3**.

## **What is a CNAME Record?**

A **CNAME (Canonical Name) record** is used in **DNS (Domain Name System)** to map one domain name to another. This is useful when multiple domain names need to resolve to the same destination.

### **Example of a CNAME Record**

```plaintext
www.categram.io  CNAME  categram.io
```

- This means that when a user visits `www.categram.io`, it resolves to `categram.io`, which in turn resolves to an **A record** that points to an IP address.

### **CNAME Record Limitations**

1. **Cannot be used at the apex (root) of a domain**
   - Example: You **cannot** set `categram.io` as a CNAME pointing to another domain.
   - This is because **CNAMEs must map a domain name to another domain name, not an IP**.
2. **AWS services like ELBs only provide DNS names, not IPs**
   - Since AWS **Elastic Load Balancers (ELB)** do not provide fixed IP addresses, you **cannot use CNAME records at the root domain**.

## **Alias Records: The Solution to CNAME Limitations**

To overcome CNAME limitations, AWS provides **Alias Records**, which allow domain names (including the root domain) to resolve to **AWS-managed services** such as:

- **Elastic Load Balancer (ELB)**
- **CloudFront**
- **API Gateway**
- **S3 Static Website Hosting**
- **Global Accelerator**

### **How Alias Records Work**

- Alias records **map a domain name to an AWS service's DNS name**.
- Unlike CNAME records, **alias records are allowed at the root domain**.
- AWS **does not charge for DNS queries made to alias records** when pointing to AWS resources.

### **Example of an Alias Record**

```plaintext
categram.io  A (Alias)  my-load-balancer-1234.elb.amazonaws.com
```

- Here, `categram.io` is an **A record alias**, pointing to an ELB DNS name.
- AWS resolves the alias to the current IP addresses of the **load balancer** dynamically.

## **Key Differences Between CNAME and Alias Records**

| Feature                                            | CNAME Record | Alias Record                           |
| -------------------------------------------------- | ------------ | -------------------------------------- |
| Can be used at the root domain (apex)              | ❌ No        | ✅ Yes                                 |
| Can point to another domain name                   | ✅ Yes       | ✅ Yes                                 |
| Can point to AWS services like ELB, S3, CloudFront | ❌ No        | ✅ Yes                                 |
| AWS charges for DNS queries                        | ✅ Yes       | ❌ No (when pointing to AWS resources) |

## **Alias Record Types: A Record Alias vs CNAME Alias**

AWS supports two types of alias records:

1. **A Record Alias**
   - Used when mapping to AWS services that provide **A records** (IP addresses).
   - Example: ELB provides an **A record**, so you must use an **A record alias**.
2. **CNAME Record Alias**
   - Used when mapping to AWS services that return **CNAME records**.
   - Less commonly used compared to **A record alias**.

### **Example Scenario**

If an **Elastic Load Balancer (ELB)** provides the following DNS name:

```plaintext
my-load-balancer-1234.elb.amazonaws.com
```

- This resolves to an **A record (IP address)**.
- Therefore, you must create an **A record alias**, not a CNAME alias.

## **When to Use Alias Records**

You should use **Alias Records** when pointing to the following AWS resources:

- **Elastic Load Balancers (ELB)**
- **CloudFront distributions**
- **API Gateway**
- **S3 static website hosting**
- **Global Accelerator**

Since AWS **Alias Records are not part of the standard DNS system**, they only work when using **Route 53 as your DNS provider**.

## **Summary**

- **CNAME records** map one domain name to another but **cannot be used at the root domain (apex)**.
- **AWS services like ELB, CloudFront, and S3 do not provide fixed IP addresses**, so CNAMEs cannot be used at the root.
- **Alias records** are AWS-specific and allow mapping both **root domains and subdomains** to AWS services.
- **Alias records are free when resolving AWS services**, making them the preferred choice for AWS-hosted domains.

This concludes the lesson on **CNAME vs Alias Records in AWS Route 53**.
