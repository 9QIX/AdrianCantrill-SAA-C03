# LearnCantrill.io AWS SA-C03: EC2 Instance Selection

## Overview

This lesson provides a deep dive into selecting the appropriate EC2 instances for various workloads. It covers EC2 instance categories, instance naming conventions, and key considerations when choosing an instance type. Additionally, it introduces two valuable resources for further exploration:

- [AWS EC2 Instance Types Documentation](https://aws.amazon.com/ec2/instance-types/)
- [EC2Instances.info](https://ec2instances.info/)

## Understanding EC2 Instance Categories

| Category                  | Type                 | Details / Notes                                                                                                          |
| ------------------------- | -------------------- | ------------------------------------------------------------------------------------------------------------------------ |
| **General Purpose**       | A1, M6g              | Graviton (A1) Graviton 2 (M6g) ARM based processors. Efficient.                                                          |
|                           | T3, T3a              | Burst Pool - Cheaper assuming nominal low levels of usage, with occasional Peaks.                                        |
|                           | M5, M5a, M5n         | Steady state workload alternative to T3/3a - Intel / AMD Architecture                                                    |
| **Compute Optimized**     | C5, C5n              | Media encoding, Scientific Modelling, Gaming Servers, General Machine learning                                           |
| **Memory Optimized**      | R5, R5a              | Real time analytics, in-memory caches, certain DB applications (in-memory operations)                                    |
|                           | X1, X1e              | Large scale in-memory applications .. lowest $ per GiB memory in AWS                                                     |
|                           | High Memory (u-xtb1) | Highest memory of all AWS instances                                                                                      |
|                           | z1d                  | Large memory and CPU - with directly attached NVMe                                                                       |
| **Accelerated Computing** | P3                   | GPU instances (Tesla v100 GPUs) - parallel processing & machine learning                                                 |
|                           | G4                   | GPU Instances (NVIDIA T4 Tensor) - Machine learning inference and Graphics Intensive                                     |
|                           | F1                   | Field Programmable Gate Arrays (FPGA) - Genomics, Financial Analysis, Big Data                                           |
|                           | Inf1                 | Machine Learning - recommendation, forecasting, analysis, voice, conversation                                            |
| **Storage Optimized**     | I3/I3en              | Local high performance SSD (NVMe) - NoSQL Databases, warehousing, analytics                                              |
|                           | D2                   | Dense Storage (HDD) - data warehousing, HADOOP, Distributed File Systems, Data processing - lowest price disk throughput |
|                           | H1                   | High Throughput, balance CPU/Mem. HDFS, MAPR-FS, File systems, Apache Kafka, Big data                                    |

EC2 instances are grouped into several categories based on their use cases and optimizations. Below is an overview of the main categories and some of their representative instance types.

### **1. General Purpose Instances**

Designed for a balanced mix of compute, memory, and networking, suitable for a variety of applications.

- **A1, M6G**: ARM-based instances using AWS Graviton processors (cost-effective, high efficiency).
- **T3, T3A**: Burstable instances with CPU credit-based performance, ideal for workloads with occasional performance spikes.
- **M5, M5A, M5N**: Standard general-purpose instances for steady-state workloads.

### **2. Compute Optimized Instances**

Optimized for high-performance compute workloads such as gaming servers, media encoding, and machine learning.

- **C5, C5N**: Offer high-performance compute power for compute-intensive applications.

### **3. Memory Optimized Instances**

Designed for applications that require large amounts of memory for high-performance data processing.

- **R5, R5A**: Suitable for memory-intensive workloads.
- **X1, X1E**: Provide extreme amounts of memory for high-end use cases.
- **High Memory Series**: Offer the highest RAM capacities.
- **Z1D**: Includes large memory with NVMe storage.

### **4. Accelerated Computing Instances**

Equipped with GPUs or specialized hardware for specific high-performance tasks.

- **P3, G4**: Include GPUs for machine learning and graphics-intensive tasks.
- **F1**: Comes with field-programmable gate arrays (FPGAs) for hardware-level acceleration, useful in genomics and financial modeling.
- **M1**: Custom-built for machine learning applications.

### **5. Storage Optimized Instances**

Optimized for applications requiring high-speed and high-throughput local storage.

- Designed for workloads that need either high throughput, maximum IO, or a balance of both.

## Instance Type Naming Conventions

Understanding EC2 instance naming conventions helps in identifying their features quickly.

- **C** → Compute-Optimized
- **R** → RAM-Optimized (Memory)
- **I** → IO-Optimized
- **D** → Dense Storage
- **G** → GPU-Based
- **P** → Parallel Processing

## Choosing the Right Instance

To pick the best EC2 instance type for your workload, follow these general guidelines:

1. **Compute-heavy applications** → Use **Compute Optimized (C5, C5N)**.
2. **Memory-intensive applications** → Use **Memory Optimized (R5, X1, etc.)**.
3. **Accelerated computing workloads** → Use **GPU-based (P3, G4, F1)**.
4. **General workloads** → Start with **General Purpose (M5, T3)** and optimize from there.

## Useful Resources

To explore EC2 instance types further, refer to these essential resources:

- [AWS EC2 Instance Types Documentation](https://aws.amazon.com/ec2/instance-types/)
- [EC2Instances.info](https://ec2instances.info/) – A sortable, filterable database of all EC2 instances.

## Conclusion

Understanding EC2 instance categories and their use cases is crucial for both AWS certification exams and real-world production deployments. As you go through the course, refer back to these resources and build mental associations with different instance types to make the right selection for any given workload.
