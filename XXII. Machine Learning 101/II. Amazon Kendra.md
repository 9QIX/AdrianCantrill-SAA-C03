# Amazon Kendra

## Overview

**Amazon Kendra** is a fully managed intelligent search service powered by machine learning and natural language processing (NLP). It allows users to search across structured and unstructured data using natural, human-like language queries.

This summary provides key concepts, features, integrations, and usage patterns of Amazon Kendra, aligned with the AWS Solutions Architect – Associate (SA-C03) exam requirements.

## What is Amazon Kendra?

Amazon Kendra is designed to deliver:

- Intelligent search experiences using **semantic understanding**.
- Human-like interaction that interprets intent and context.
- Search across various **enterprise data repositories**.

Unlike traditional search systems based on keywords, Kendra analyzes **contextual relevance** and **question intent** to return accurate results.

## Types of Queries Supported

### 1. Factoid Questions

- Simple fact-based questions like:
  - "Who wrote this book?"
  - "Where is the nearest office?"
- Returns concise answers like names, places, or dates.

### 2. Descriptive Questions

- More detailed questions requiring fuller responses.
  - Example: "How do I connect my device to Wi-Fi?"
- Answers can be a paragraph, passage, or document.

### 3. Keyword/Natural Language Questions

- Conversational or ambiguous queries.
  - Example: "Keynote address"
- Requires context understanding to distinguish meanings (e.g., "address" as location vs. speech).

## Key Components

### Index

- A searchable data structure built from crawled documents.
- Kendra searches this index to answer user queries.

### Data Sources

- Original content repositories connected to Kendra.
- Documents are indexed from these sources and synced on a schedule.

**Common data sources include:**

- AWS: S3, RDS (MySQL, PostgreSQL, Oracle), FSx, WorkDocs
- Microsoft: SharePoint, OneDrive, Exchange, SQL Server, Teams, Yammer
- Others: Google Drive, Gmail, Dropbox, Confluence, Jira, Salesforce, GitHub, Zendesk

> Synchronization keeps indexes updated with additions, deletions, and modifications in the original data.

### Documents

- Can be:
  - **Structured** (e.g., FAQs)
  - **Unstructured** (e.g., PDFs, HTML, text)
- Stored in various formats and scanned into the index.

## Integration with AWS

Amazon Kendra integrates with:

- **IAM** and **IAM Identity Center (formerly AWS SSO)** for access control.
- Other AWS services such as:
  - **Amazon Lex** (chatbots)
  - **Amazon Q Business** (enterprise search)
  - **Amazon Bedrock** (generative AI apps)

Access to search results can be filtered based on user credentials and group membership.

## Editions of Amazon Kendra

| Edition Name         | Description                                                      |
| -------------------- | ---------------------------------------------------------------- |
| **GenAI Enterprise** | Best accuracy; designed for production workloads and GenAI apps. |
| **Basic Enterprise** | Supports semantic search; reliable for production.               |
| **Basic Developer**  | For development/testing; not suitable for production.            |

## Benefits of Using Amazon Kendra

- **Simplicity**: Easy-to-use API and management console.
- **Connectivity**: Supports a broad range of third-party and AWS data sources.
- **Accuracy**: Semantic search retrieves the most relevant responses.
- **Security**: Honors enterprise permissions for document-level access.
- **Scalability**: Suitable for high-throughput, enterprise-scale applications.

## Getting Started: Typical Workflow

1. **Create an Index** – Central searchable storage.
2. **Add Documents** – Via batch upload or sync from data sources.
3. **Configure Access** – Using IAM or identity center.
4. **Search the Index** – Using the Kendra Query API.
5. **Integrate** – Add search functionality to custom apps (e.g., websites, mobile apps).

## Pricing

- **Free Tier**:
  - 750 hours for the first 30 days with Developer or GenAI index.
- **Post-Free Tier Charges**:
  - Charged per provisioned index (even if unused).
  - Additional fees for:
    - Document sync
    - Connector usage

> Connector usage is not included in the free trial.

Refer to the official [Amazon Kendra Pricing](https://aws.amazon.com/kendra/pricing/) page for up-to-date details.

## Example Use Case Explained

**Query:**

```text
What time is the keynote address?
```

**Challenge:**

- The word **"address"** can refer to:
  - A **location** (e.g., street address), or
  - A **speech** (e.g., keynote).

**How Kendra Handles It:**

- Uses **semantic analysis** to determine that "keynote address" means a speech.
- Returns the time of the keynote event.

## Summary

Amazon Kendra provides:

- A **powerful semantic search engine**.
- Integration with numerous data sources.
- **Enterprise-grade scalability and security**.
- Suitable for both traditional search and **generative AI applications**.

For certification and real-world application, knowing its components, query types, indexing process, and integration points will help you build efficient search solutions on AWS.
