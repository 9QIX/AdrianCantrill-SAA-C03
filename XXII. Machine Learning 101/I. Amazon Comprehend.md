# Amazon Comprehend

## Overview

**Amazon Comprehend** is a fully managed **Natural Language Processing (NLP)** service provided by AWS. It uses machine learning to extract insights and relationships from unstructured text. This lesson introduces its key features and demonstrates how to interact with the service through the AWS Management Console.

## What Amazon Comprehend Does

Amazon Comprehend processes documents (plain text) and identifies:

- **Entities** (e.g., names, organizations, locations)
- **Key Phrases**
- **Language**
- **Sentiment** (positive, negative, neutral, or mixed)
- **PII** (Personally Identifiable Information)

## Key Features

### 1. **Pre-trained and Custom Models**

- **Pre-trained Models**: Built-in models by AWS for general text analysis.
- **Custom Models**: Trained using your domain-specific data.

### 2. **Real-time & Asynchronous Processing**

- **Real-time**: Suitable for small, interactive workloads.
- **Asynchronous**: Scalable for larger document sets via batch jobs.

### 3. **Access Methods**

- AWS Management **Console**
- AWS **Command Line Interface (CLI)**
- **API** Integration for applications

## Using Amazon Comprehend: Console Walkthrough

### Step-by-Step Guide:

1. Log into the AWS Console.
2. Navigate to **Amazon Comprehend** using the search bar.
3. Click on **"Launch Amazon Comprehend"**.
4. Enter a sample text into the input box.
5. Use the built-in analysis type (AWS pre-trained models).

### Sample Text Analysis Example:

Input:

```
Hi John, here’s your new credit card issued by Company Financial Services. Your card number ends in 1234.
```

**Detected Features:**

| Feature Type | Example Detected           | Confidence |
| ------------ | -------------------------- | ---------- |
| Entity       | Person: John               | > 99%      |
| Organization | Company Financial Services | > 99%      |
| PII          | Credit Card Info           | High       |
| Language     | English                    | > 99%      |
| Sentiment    | Neutral                    | -          |

## Custom Text Example & Sentiment Analysis

### Input Text:

```
My name is Adrian and I'm 1337 years old. My favorite animals are cats and I own 500 of them. My least favorite are spiders.
```

### Detected:

- **Entities**: Name (Adrian), Quantities (1337, 500)
- **Language**: English
- **Sentiment**: **Mixed**
  - Positive: Likes cats
  - Negative: Dislikes spiders

### Modified Text:

Removed "spiders" to test sentiment again:

```
My name is Adrian and I'm 1337 years old. My favorite animals are cats and I own 500 of them.
```

### Updated Sentiment:

- **Neutral and Positive**
- No negative elements present

## PII Detection Capabilities

Amazon Comprehend can identify a range of sensitive data:

- Names
- Credit card numbers
- Bank account and routing numbers
- Phone numbers
- Addresses
- Email addresses
- Dates

## Integration and Use Cases

You can integrate Amazon Comprehend via:

- **Console**: Manual inspection and learning
- **CLI**: Automation scripts
- **API**: Embedding NLP into applications or pipelines

### Ideal for:

- Developers
- Solution Architects
- DevOps/Operations

## Summary

| Feature          | Details                                                |
| ---------------- | ------------------------------------------------------ |
| Type             | NLP as a Service                                       |
| Input            | Plain text                                             |
| Outputs          | Entities, phrases, sentiment, language, PII            |
| Processing Modes | Real-time or batch (asynchronous)                      |
| Model Support    | Built-in and custom                                    |
| Access Methods   | Console, CLI, API                                      |
| Ideal For        | Analyzing unstructured text, building intelligent apps |

Amazon Comprehend enables AWS users to quickly extract meaning from text without building their own NLP models. It is especially useful in applications involving customer feedback, emails, support tickets, or document processing.
