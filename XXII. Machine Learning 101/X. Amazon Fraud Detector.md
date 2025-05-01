# Amazon Fraud Detector

## What is Amazon Fraud Detector?

**Amazon Fraud Detector** is a **fully managed AWS machine learning service** that detects **potential fraudulent online activity** by analyzing historical and contextual data. The service helps identify fraud in real-time, especially for activities like:

- **New account sign-ups**
- **Online payments**
- **Guest checkouts**

## Key Features

- **Managed service** – No need to build and train ML models from scratch.
- **Real-time scoring** of events for risk assessment.
- **Rule-based decisions** – Allows you to define business-specific responses to different fraud scores.
- **Seamless integration** into applications (backend use case).

## Supported Model Types

Amazon Fraud Detector offers **three model types**, each suited for a different fraud detection scenario.

### 1. **Online Fraud Model**

- **Use Case:** Minimal or no historical data (e.g., new user sign-ups).
- **Focus:**  
  Detects suspicious patterns in metadata during user registration, such as:
  - IP address
  - Location
  - Browser fingerprint
  - Device type
- **Goal:** Identify fake or risky user accounts during creation.

### 2. **Transaction Fraud Model**

- **Use Case:** You have **detailed transaction history** for users.
- **Focus:**  
  Detects anomalies in financial transactions such as:

  - Purchase location
  - Frequency
  - Time and value of transactions
  - Known merchant types

- **Example:** Credit card fraud detection using patterns like:

  ```text
  - Normal spend: $50, groceries, local store
  - Suspicious activity: $3,000 electronics, overseas
  ```

- **Goal:** Compare current transaction to known customer behavior to flag unusual activity.

### 3. **Account Takeover Model**

- **Use Case:** Prevent identity theft or unauthorized account access.
- **Focus:**  
  Looks at behavioral deviations such as:

  - Sudden login from a foreign location
  - Access from a suspicious referrer (e.g., phishing site)
  - Device or browser mismatch

- **Goal:** Detect signs of compromised accounts or phishing attacks.

## Workflow Overview

1. **Data Upload:** Provide historical and contextual data (e.g., CSV of past transactions).
2. **Model Selection:** Choose one of the three predefined model types.
3. **Scoring Events:** Each event (login, transaction, etc.) is assigned a **fraud risk score**.
4. **Create Rules:** Define rules based on score thresholds and other conditions.
5. **Take Action:** Use the rules to:
   - Block the action
   - Trigger a manual review
   - Allow but log the event for further analysis

## Integration Options

| Method         | Description                                                              |
| -------------- | ------------------------------------------------------------------------ |
| **API**        | Integrate fraud detection directly into your apps or backend workflows   |
| **Console**    | Limited use – mostly for setup and monitoring                            |
| **Automation** | Typically used within event-driven architectures or business logic flows |

## Exam Relevance

- **High-level knowledge** of Amazon Fraud Detector is sufficient for most AWS certification exams.
- Understand the **purpose**, **model types**, and **typical use cases**.
- Hands-on or deep theory not required unless preparing for advanced certifications or real-world deployment.

## Summary

Amazon Fraud Detector is a specialized AWS machine learning service aimed at **proactively detecting fraud in real-time**. It supports three distinct fraud detection models tailored for **sign-ups, transactions, and account takeovers**, making it highly adaptable. With rule-based responses and easy API integration, it's an essential tool for businesses with online operations.
