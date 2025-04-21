# CloudFront (CF) - Adding an Alternate CNAME and SSL

This demo lesson walks through how to configure a **CloudFront distribution** with a **custom domain name** and **SSL certificate** using **AWS Certificate Manager (ACM)**. The setup builds upon an earlier lesson involving CloudFront and an S3 static website.

## Prerequisites

Before starting, ensure the following:

- You have completed the previous lesson with:
  - An S3 static website deployed.
  - A CloudFront distribution pointing to the S3 origin.
- You are logged in as the **IAM admin user**.
- You are using the **management account** in AWS Organizations.
- **Region must be set to us-east-1 (Northern Virginia)**, as ACM certificates for CloudFront must be in this region.
- You have a **domain name registered and hosted in Route 53**.

If you don't have a domain, you can still follow along and observe the steps.

## Step-by-Step Instructions

### 1. Choose a Custom Domain Name

Choose a fully qualified domain name (FQDN) for your CloudFront distribution.

Example:

```
merlin.animalsforlife1337.org
```

> Replace this with your own domain name.

### 2. Edit CloudFront Distribution

1. Go to the CloudFront console.
2. Select your distribution ID.
3. Click on **Edit**.
4. In **Alternate Domain Names (CNAMEs)**, click **Add item** and enter your chosen domain name.

### 3. Request an SSL Certificate in ACM

1. Navigate to **AWS Certificate Manager (ACM)**.
2. Click on **Request a certificate**.
3. Select **Request a public certificate** → **Next**.
4. Enter your domain name (e.g., `merlin.animalsforlife1337.org`).
5. Choose **DNS validation** (easier than email validation).
6. Click **Request**.

### 4. Create DNS Validation Record in Route 53

If your domain is hosted in Route 53:

1. In the certificate request details, click **Create record in Route 53**.
2. ACM adds a CNAME record to validate domain ownership.
3. Wait a few minutes. The certificate status should change to **Issued**.

> If it takes more than 20 minutes, check for domain misconfigurations.

### 5. Attach the Certificate to CloudFront

1. Return to the CloudFront distribution settings.
2. Click **Refresh** next to the **Custom SSL Certificate** dropdown.
3. Select the certificate you just created.
4. Ensure the alternate domain name matches exactly with the certificate name.
5. Leave the **SSL support method** as default (SNI only).
6. Click **Save changes**.

> Deployment to edge locations can take ~15 minutes.

### 6. Create Route 53 Alias Record

1. Go to **Route 53 > Hosted Zones**.
2. Choose your domain’s hosted zone.
3. Click **Create record**.
4. Choose **Simple routing** → **Define simple record**.
5. Enter the subdomain (e.g., `merlin`).
6. Set traffic routing to:
   - **Alias to CloudFront distribution**
   - **Region**: us-east-1 (Northern Virginia)
   - **Choose distribution**: Select your CloudFront distribution
7. Record type: `A` (IPv4)
8. Click **Create records**

### 7. Test the Setup

Open a browser and go to:

```
https://your-custom-domain.com
```

If configured correctly, you should see your S3 website via CloudFront with HTTPS enabled.

## Notes

- All services used (CloudFront and ACM) fall under AWS Free Tier.
- **No cleanup** is required as the infrastructure will be used in the next demo.
- If you **don’t have a domain**, just follow along visually; the next lesson won't depend on SSL being set up.

## DNS Validation Record Explained (Conceptual)

When using DNS validation, ACM provides a CNAME record like:

```text
Name: _abcd1234.example.com
Type: CNAME
Value: _xyz9876.acm-validations.aws
```

Adding this to Route 53 proves domain ownership because AWS can query your DNS and confirm that you control the domain.

## Troubleshooting Tips

- Ensure region is **Northern Virginia**.
- Certificate, CloudFront Alternate Domain Name, and Route 53 record **must match exactly**.
- DNS propagation can take time—wait patiently or use `dig`/`nslookup` to verify.

## Summary

This lesson taught you how to:

- Add a **custom domain** to a CloudFront distribution.
- Generate and validate an **SSL certificate with ACM**.
- Create **Route 53 alias records** for the custom domain.
- Access your site securely via **HTTPS**.

> You are now ready for the next lesson in the AWS Solutions Architect Associate course on Cantrill.io!
