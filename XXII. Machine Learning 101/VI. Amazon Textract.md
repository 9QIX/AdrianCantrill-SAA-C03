# Amazon Textract

## Overview

**Amazon Textract** is a machine learning service provided by AWS designed to automatically extract printed text, handwriting, and structured data from scanned documents. It supports input formats like **JPEG, PNG, PDF, and TIFF** and can return **plain text**, **structured form data**, and **tables**.

Textract is designed for use cases such as:

- Document digitization
- Data extraction from identity documents
- Receipt and invoice analysis
- KYC/AML compliance support

This summary offers a high-level architectural understanding of Textract, which is all that's typically required for the **AWS Solutions Architect Associate (SAA-C03)** certification exam.

## Key Features

### Supported Input Formats

- JPEG
- PNG
- PDF
- TIFF

### Outputs

- Extracted text (including handwritten content)
- Structural relationships (forms and tables)
- Metadata (such as bounding boxes)
- Specialized field abstraction for identity documents

## Operating Modes

### Synchronous Processing

Used for:

- Small to medium-sized documents
- Near real-time use cases

### Asynchronous Processing

Used for:

- Large documents (e.g., multi-hundred-page PDFs)
- Jobs that require longer execution time

## Pricing

- **Pay-as-you-go** model
- Custom pricing available for high-volume usage

## Use Cases

### 1. **Generic Document Analysis**

- Extracts fields like names, addresses, dates of birth
- Detects text layout and positioning

### 2. **Invoices and Receipts**

- Detects:
  - Line items
  - Prices
  - Vendors
  - Taxes
  - Dates

### 3. **Identity Documents**

- Extracts and **abstracts** fields like:
  - Driver’s License Number → `document_id`
  - Passport Number → `document_id`
- Enables uniform data handling across multiple ID types

## Integration Options

- **AWS Console** (for demo and UI-based interaction)
- **AWS SDK / APIs** (for application integration)
- Integration with other **AWS Services**:
  - Lambda
  - S3
  - DynamoDB
  - Step Functions
  - Kinesis, etc.

## Demonstrated Examples from AWS Console

### 1. **Vaccination Card**

- Structured fields: Last name, first name, DOB, patient ID
- Table format (e.g., vaccine dates) is also recognized even when:
  - Handwritten
  - Slanted
  - Outside cell boundaries

### 2. **Payslip**

- Extracts:
  - Tabular financial data
  - Metadata (e.g., page numbers, formatting info)

### 3. **Loan Application**

- Handles:
  - Large paragraphs of text
  - Forms with varied field alignment

### 4. **Identity Documents (Specialized Analysis)**

- Example:
  - Driver’s License → Extracts `Driver License Number` as `document_id`
  - Passport → Extracts `Passport Number` as `document_id`
- Useful in KYC (Know Your Customer) and AML (Anti-Money Laundering) contexts

## Data Structure Abstraction Example

Textract’s identity document processing can **standardize** fields like:

```json
{
  "document_id": "D12345678",
  "first_name": "Jane",
  "last_name": "Doe",
  "date_of_birth": "1990-05-01"
}
```

> This allows different document types (e.g., passports, licenses) to feed into the same backend data schema for simplified processing and querying.

## Sample Architectural Workflow

```text
1. A user uploads a document (e.g., receipt) to an S3 bucket.
2. An S3 event triggers an AWS Lambda function.
3. The Lambda function calls Amazon Textract.
4. Textract returns structured data (e.g., total price, item list).
5. Lambda processes and stores the result in DynamoDB.
```

## Summary for Exam Tips

- **Default to Amazon Textract** when a question involves:
  - Text extraction from scanned documents or images
  - Analyzing invoices, forms, or identity documents
  - Working with receipts or extracting tabular/structured data
