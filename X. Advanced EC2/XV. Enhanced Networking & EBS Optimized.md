# Enhanced Networking & EBS Optimized Instances

## Introduction

This lesson covers two important EC2 optimization topics: **Enhanced Networking** and **EBS Optimized Instances**. These features improve EC2 performance and support other enhancements like placement groups. Understanding these optimizations is crucial for a solutions architect.

## Enhanced Networking

### Overview

Enhanced Networking improves EC2 networking performance using **Single Root I/O Virtualization (SR-IOV)**. It allows a **physical network interface** inside an EC2 host to be **aware of virtualization**.

### Standard Networking Architecture

Without Enhanced Networking, EC2 instances communicate with a **single physical network interface** through **virtual network interfaces** managed by the EC2 host:

1. **Two or more EC2 instances** share the same physical network interface.
2. The **host's CPU** manages network traffic between instances and the physical interface.
3. This leads to **higher CPU usage**, potential **latency spikes**, and **reduced network performance** under heavy load.

### Enhanced Networking with SR-IOV

SR-IOV allows the physical network interface to create **multiple logical network interfaces**, each dedicated to a specific EC2 instance.

**Key Benefits:**

- **Higher IO**: More efficient network traffic handling, reducing host CPU involvement.
- **Higher Bandwidth**: Allows faster data transfer without impacting host CPU.
- **Higher Packets Per Second (PPS)**: Improves performance for applications requiring high networking speeds.
- **Lower and Consistent Latency**: Since network traffic is offloaded to the physical network interface, latency remains low and stable.

### Enabling Enhanced Networking

Enhanced Networking is enabled **by default** on most modern EC2 instances at **no extra cost**.

## EBS Optimized Instances

### Overview

EBS Optimized Instances ensure that **storage networking** does not compete with **data networking** for bandwidth.

### Standard EC2 Networking for EBS

Previously, EC2 instances used a **shared network stack** for both **data traffic** and **EBS storage traffic**, leading to **performance contention**.

### EBS Optimized Architecture

EBS Optimized Instances provide **dedicated network capacity** for EBS traffic, separating it from regular instance networking.

**Key Benefits:**

- **Faster Storage Performance**: Dedicated bandwidth allows higher throughput for EBS volumes.
- **Reduced Contention**: Storage traffic does not interfere with regular network performance.
- **Better Performance for High IOPS Volumes**: Essential for high-throughput EBS volumes like **gp2** and **io1**.

### Enabling EBS Optimization

- Most modern EC2 instances **have EBS Optimization enabled by default** at **no extra charge**.
- On **older instances**, it may be a **paid feature** that needs manual activation.

## Summary

| Feature                     | Purpose                                  | Benefits                                       |
| --------------------------- | ---------------------------------------- | ---------------------------------------------- |
| **Enhanced Networking**     | Improves network performance with SR-IOV | Higher bandwidth, lower latency, better PPS    |
| **EBS Optimized Instances** | Dedicated bandwidth for EBS storage      | Faster storage performance, reduced contention |

Understanding these features helps in architecting **high-performance** EC2-based solutions, ensuring **efficient network and storage performance**.

## Further Reading

For more details, refer to the official AWS documentation:

- [AWS Enhanced Networking](https://docs.aws.amazon.com/AWSEC2/latest/WindowsGuide/enhanced-networking.html)
