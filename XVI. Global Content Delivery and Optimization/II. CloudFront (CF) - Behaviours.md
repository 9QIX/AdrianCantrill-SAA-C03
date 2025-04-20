# AWS CloudFront Architecture: Distribution and Behaviors

## Introduction

This lesson provides a walkthrough of the **CloudFront architecture**, focusing on how **distributions and behaviors** are configured. It emphasizes understanding which settings are defined at the **distribution level** and which are defined per **behavior**.

## CloudFront Console Overview

- Navigate to the **CloudFront console** via AWS Services.
- CloudFront configurations are grouped under **Distributions**.
- Each **Distribution** represents a set of delivery rules for your content.

## Distribution-Level Configuration

Settings that apply **globally to the entire distribution** include:

### 1. **Price Class**

- Determines which **edge locations** your content is distributed to.
- Options:
  - **All Edge Locations**: Maximum performance, higher cost.
  - **US, Canada, Europe**: Lower cost, limited performance globally.
  - **Middle ground**: US, Canada, Europe, Asia, Middle East, and Africa.

### 2. **Web Application Firewall (WAF)**

- WAF (Web ACL) is configured **at the distribution level**.
- Protects applications from common web exploits.

### 3. **Alternate Domain Names (CNAMEs)**

- Default DNS: `abc123.cloudfront.net`
- Custom domain example: `labs-high-bucket.cantrill.io`
- Defined at the distribution level.

### 4. **SSL Certificates**

- **Default Certificate**: Only for default CloudFront domain.
- **Custom Certificate** (via ACM): Required for custom domains over HTTPS.
- Choose between:
  - **SNI (Server Name Indication)**: More common and cost-effective.
  - **Non-SNI**: Legacy, supports older clients.

### 5. **Security Policies**

- Defines the TLS versions and cipher suites.
- More secure policies may block older browsers.
- Choose based on the trade-off between **security** and **compatibility**.

### 6. **Other Settings**

- Supported **HTTP versions**.
- **Access logs** (enabled or disabled).

## Behavior-Level Configuration

Each **distribution** can have **multiple behaviors**, allowing different rules for different paths or content types.

### 1. **Path Patterns**

- Default behavior uses `*` to match all requests.
- More specific patterns (e.g. `/images/*`) can override defaults.

### 2. **Origin Selection**

- Choose which **origin** (or **origin group**) to fetch the content from.

### 3. **Viewer Protocol Policy**

- Controls HTTP/HTTPS between viewer and edge location:
  - **HTTP and HTTPS**
  - **Redirect HTTP to HTTPS**
  - **HTTPS only**

### 4. **HTTP Methods**

- Specify allowed HTTP methods (e.g., GET, POST).
- Helps secure endpoints by limiting method types.

### 5. **Field-Level Encryption**

- Encrypt sensitive fields at edge locations.
- Configured per behavior.
- Covered in detail in a separate lesson.

### 6. **Caching Controls**

#### **Legacy vs Modern**

- Older distributions may use **legacy cache settings**.
- Newer recommended approach:
  - **Cache Policy**
  - **Origin Request Policy**

#### **Cache Settings Include**:

- Cache based on **request headers**
- **Minimum TTL**, **Maximum TTL**, **Default TTL**
- Can vary **per behavior**

### 7. **Restrict Viewer Access**

- Controls whether access to content is **public or private**.

#### **Authorization Options**:

- **Trusted Key Groups** (recommended)
- **Trusted Signers** (legacy)

> For private content:
>
> - Requires **signed URLs** or **signed cookies**.
> - Common in premium content delivery (e.g. streaming platforms).

### 8. **Automatic Compression**

- Automatically compress objects (e.g., GZIP, Brotli).
- Reduces bandwidth and improves performance.

### 9. **Lambda@Edge Association**

- Attach **Lambda@Edge functions** to behaviors.
- Enables request/response manipulation at the edge.
- Examples: URL rewrites, authentication checks.

## Key Exam Tips

- **Caching controls** and **viewer restrictions** are set at the **behavior level**.
- One distribution can have **multiple behaviors** with different settings.
- Distribution-level vs behavior-level settings distinction is crucial for **SAA-C03 exam questions**.
- Common trick questions involve mixing up **SSL**, **WAF**, and **cache settings** placement.

## Recap

| Configuration                 | Level        |
| ----------------------------- | ------------ |
| Price Class                   | Distribution |
| WAF (Web ACL)                 | Distribution |
| Alternate Domain Names        | Distribution |
| SSL Certificates              | Distribution |
| Security Policy               | Distribution |
| HTTP Methods                  | Behavior     |
| Viewer Protocol Policy        | Behavior     |
| Field-Level Encryption        | Behavior     |
| Cache Settings (TTL, headers) | Behavior     |
| Restrict Viewer Access        | Behavior     |
| Lambda@Edge                   | Behavior     |

## Final Note

This lesson serves as a foundational overview of CloudFront’s two main configuration scopes:

- **Distribution-Level**: Broad settings, impacting the entire delivery system.
- **Behavior-Level**: Granular control, allowing for performance tuning and access control on a per-path basis.

Mastering the **difference between these two scopes** is essential for both **practical deployment** and **exam preparation**.
