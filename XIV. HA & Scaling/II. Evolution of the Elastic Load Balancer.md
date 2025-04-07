# Elastic Load Balancer (ELB) Evolution

This document summarizes the **Elastic Load Balancer (ELB) Evolution** lesson from the **Cantrill.io AWS Solutions Architect Associate (SAA-C03)** course. Understanding the history and types of load balancers in AWS is important for both **real-world application architecture** and **exam success**.

## Overview

AWS currently offers **three types** of Elastic Load Balancers (ELBs), which are divided into **two versions**:

- **Version 1 (Legacy)**
- **Version 2 (Modern, Preferred)**

## ELB Terminology

- **ELB** (Elastic Load Balancer) refers to the entire **family** of AWS load balancer types.
- You will encounter three specific products:
  - **Classic Load Balancer (CLB)** – Version 1
  - **Application Load Balancer (ALB)** – Version 2
  - **Network Load Balancer (NLB)** – Version 2

## Version 1: Classic Load Balancer (CLB)

### Introduction

- Launched in **2009**, part of the early AWS product set.
- Supports both **Layer 4** (TCP/SSL) and **basic Layer 7** (HTTP/HTTPS), but with significant limitations.

### Key Limitations

- **Not truly Layer 7 aware** – Lacks deep understanding of HTTP protocol.
- **Limited features** compared to version 2:
  - No advanced routing or rules.
  - No native support for WebSockets.
- **Only supports one SSL certificate** per load balancer.
  - In large deployments, this limitation could require many CLBs.
- **Higher operational cost** when scaled.

### Recommendation

> Do **not use CLBs** in any new deployments. Always prefer Version 2 load balancers (ALB or NLB).

## Version 2: Modern Load Balancers

Version 2 includes both **Application Load Balancer (ALB)** and **Network Load Balancer (NLB)**. These are fully-featured and should be used for **all modern architectures**.

### 1. Application Load Balancer (ALB)

#### Overview

- **Layer 7 load balancer** (Application Layer).
- Supports:
  - **HTTP**
  - **HTTPS**
  - **WebSocket**

#### Use Cases

- Web applications
- Microservices
- REST APIs

#### Features

- Content-based routing
- Path- or host-based routing rules
- Native WebSocket support
- Can handle multiple services using **target groups**

### 2. Network Load Balancer (NLB)

#### Overview

- **Layer 4 load balancer** (Transport Layer).
- Supports:
  - **TCP**
  - **TLS** (Encrypted TCP)
  - **UDP**

#### Use Cases

- Applications that do **not** use HTTP/S:
  - Email servers (SMTP)
  - SSH
  - Custom protocols (e.g., game servers)

#### Features

- Extremely **high performance** and **low latency**
- Can handle **millions of requests per second**
- Native support for static IPs and Elastic IPs
- Supports **target groups** like ALB

## Shared Benefits of Version 2 (ALB and NLB)

- Support for **target groups** (group of EC2 instances, Lambda, etc.)
- Use of **routing rules** for intelligent traffic management
- Can consolidate multiple use cases into a **single load balancer**
- More **cost-effective** and **scalable** than CLB
- Recommended for **all new deployments**

## Exam Tips

For the AWS SAA-C03 exam:

- Know when to choose between:
  - **ALB** – for HTTP/HTTPS/WebSocket workloads
  - **NLB** – for TCP/UDP/custom protocol workloads
- Be familiar with the **differences in features and protocols** supported by each.
- Understand **target groups**, **routing rules**, and **protocol-level differences**.

## Summary

| Feature                 | Classic Load Balancer (CLB) | Application Load Balancer (ALB) | Network Load Balancer (NLB) |
| ----------------------- | --------------------------- | ------------------------------- | --------------------------- |
| AWS Version             | v1                          | v2                              | v2                          |
| Layer                   | 4 & basic 7                 | 7 (Application Layer)           | 4 (Transport Layer)         |
| Protocols               | HTTP, HTTPS, TCP            | HTTP, HTTPS, WebSockets         | TCP, TLS, UDP               |
| SSL Certificate Support | Single only                 | Multiple via listeners          | Multiple via listeners      |
| Advanced Routing        | No                          | Yes (host/path-based)           | No                          |
| WebSocket Support       | No                          | Yes                             | No                          |
| Target Groups           | No                          | Yes                             | Yes                         |
| Cost                    | Higher (when scaled)        | Lower                           | Lower                       |
| Use in New Deployments  | Not recommended             | Recommended                     | Recommended                 |
