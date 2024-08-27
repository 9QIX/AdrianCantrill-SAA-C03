# Animals for Life Scenario: AWS SA-C03 Course

## Introduction

This lesson introduces the fictitious organization **Animals for Life**, a global animal rescue and awareness organization. The purpose of this scenario is to create a real-world foundation for understanding the concepts and implementations in this AWS Solutions Architect course. It will be used throughout the course to illustrate architecture, theory, and demo implementations.

## Organization Overview

### Animals for Life Mission

- Focuses on **animal rescue, medical care, rehoming**, and **wildlife habitat conservation**.
- Involved in **animal migration monitoring** and **habitat destruction observation** globally.
- Uses **Internet of Things (IoT)** and handles **big data sets** to support its operations.

### Global Structure

- **Headquarters**: Brisbane, Australia  
  100 staff members (Admin, IT, Marketing, Legal, Accounts)
- **Remote Staff**: 100 field workers across regional Australia and globally  
  Roles include animal care workers, vets, research scientists, political lobbyists.
- **Major Offices**:
  - **London** (EU region)
  - **New York** and **Seattle** (US East and West Coast)

## Current Technical Infrastructure

### On-Premises & KOLO Facilities

- **Brisbane Office**: Contains an aging on-premises data center  
  Using **5 KOLO facilities** (rented rack space)  
  Data center is being decommissioned in 18 months, prompting migration planning.

### Cloud Pilots

- Previously ran a **poorly implemented AWS pilot** in the Sydney region.
- Tried **Microsoft Azure** and **Google Cloud pilots**, but none met the business needs in terms of resilience, scalability, or cost.

### Network Structure

- Brisbane on-premises network: **192.168.10.0/24** (Class C).
- AWS pilot: **10.0.0.0/16** (Class B).
- Azure pilot: **172.31.0.0/16** (Class B).

## Business Challenges

### Technical Issues

1. **Aging Hardware**: On-premises hardware reaching end of life.
2. **Data Center Closure**: Data center decommission in 18 months.
3. **Performance**: Remote offices consume IT services from Brisbane, resulting in poor performance and downtimes during maintenance.
4. **Scalability & Availability**: Struggles with highly available systems and scalability.
5. **Failed Cloud Trials**: AWS, Azure, and Google Cloud pilots failed to reduce costs or improve reliability.

### Operational Limitations

- **Global Expansion Costs**: High infrastructure costs have limited global expansion.
- **Limited IT Resources**: Small IT team with on-premises experience but limited cloud/automation expertise.
- **Vendor Issues**: Past experiences with third-party vendors were suboptimal due to poor choices.

## Business Objectives

### Key Requirements

1. **Field Worker Performance**: Provide fast and reliable performance for field workers who are integral to the organization's core mission.
2. **Global Deployment**: Enable quick, automated deployments into new global regions with pay-as-you-go billing.
3. **Disaster Response**: Infrastructure should scale up or down based on demand, particularly during natural disasters.
4. **Cost Efficiency**: Maintain a low base cost for infrastructure while allowing rapid scalability when required.

### Agility & Automation

- **Agility**: The organization needs to quickly launch social media campaigns and respond to real-world events within **48 hours**.
- **Automation**: Automation should minimize IT staff needs and reduce costs, allowing the organization to focus its funds on its core mission.

### Technology Adoption

The organization is **progressive**, seeking to leverage **IoT, Big Data, Machine Learning**, and other emerging technologies in its solutions.

## Learning Outcome

### Scenario Use Throughout the Course

The **Animals for Life** scenario will be referenced throughout the course to explain AWS products, services, and architectural theory. The goal is to provide a **real-world-like context** to AWS deployments, which will enhance understanding of architecting solutions in AWS.

### Practical Takeaways

The scenario serves as a learning tool to help identify the **questions to ask** and **information to prioritize** during real-world AWS deployments. The course will also prepare learners for **AWS exam questions** by building familiarity with real-world scenarios.

**Thanks for Watching!**  
You can now proceed to the next lesson, where the scenario will continue to guide our discussions and demos.
