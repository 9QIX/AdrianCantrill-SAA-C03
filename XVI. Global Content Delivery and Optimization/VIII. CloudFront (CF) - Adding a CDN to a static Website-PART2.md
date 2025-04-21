# CloudFront (CF) - Adding a CDN to a static Website-PART2

## Resources Used

- **CloudFormation Template**: [Deploy via 1-Click](https://console.aws.amazon.com/cloudformation/home?region=us-east-1#/stacks/create/review?templateURL=https://learn-cantrill-labs.s3.amazonaws.com/awscoursedemos/0026-aws-associate-cdn-cloudfront-and-s3/top10catsbucket.yaml&stackName=CFANDS3)
- **Image Resource**: [Whiskers.jpg](https://learn-cantrill-labs.s3.amazonaws.com/awscoursedemos/0026-aws-associate-cdn-cloudfront-and-s3/whiskers.jpg)

## ✅ What This Lesson Covers

- Exploring CloudFront CDN behavior
- Understanding how object caching works
- Overwriting cached objects
- Using invalidation to update cache
- SSL via default CloudFront certificate
- Avoiding direct origin access
- Best practices for dynamic content delivery

## Step-by-Step Summary

### 1. CloudFront Deployment Verification

After deploying the CloudFormation template:

- Go to the **CloudFront console** and click on the **Distribution ID**.
- You'll find a unique default domain name (e.g., `d123abc456xyz.cloudfront.net`).
- Open this in a new tab to verify the static site loads from the **edge location**, not the S3 origin.

### 2. Performance and Caching

- Once cached at the edge location, refresh the CloudFront domain multiple times.
- The site (HTML and images) loads faster due to **edge caching**.
- Objects served: 11 images (`10 top cats + Merlin.jpg`).

## Edge Caching Concept

- **Edge Locations** store a cached copy after the **first origin fetch**.
- Refreshes are now served from edge cache until **TTL expires**.
- Demonstrated using `Merlin.jpg` inside `/IMG/` folder.

### 3. Overwriting Cached Content

#### Objective:

Replace `Merlin.jpg` with `whiskers.jpg` (renamed to Merlin.jpg) to see caching in action.

#### Steps:

1. Download `whiskers.jpg`
2. Rename to `Merlin.jpg`
3. Upload to S3 > Bucket > `IMG/` folder (overwrite existing file)

**Observation:**

- **CloudFront still serves the old Merlin.jpg**, despite S3 having a new version.
- Direct S3 URL shows the updated image (because it's bypassing CloudFront).

## CloudFront Invalidation

### What is Invalidation?

Invalidation forces CloudFront edge locations to discard cached content and **fetch the updated file from origin**.

### How to Invalidate:

1. Go to CloudFront distribution > **Invalidations**
2. Click **Create Invalidation**
3. Use the following path options:
   - `/*` – invalidate entire distribution
   - `/IMG/*` – invalidate all images
   - `/IMG/Merlin.jpg` – only this specific image

**Wildcard `/*`** used in the demo for simplicity.

> Invalidation might take a few minutes. Once complete, a **refresh in a private browser tab** fetches the updated image from the origin.

## Cost and Best Practice Warning

- **You are billed for invalidation requests.**
- To reduce cost:
  - Use **versioned filenames**: e.g., `Merlin_v1.jpg`, `Merlin_v2.jpg`
  - Avoid overwriting files directly if you expect frequent updates

## HTTPS with CloudFront

- CloudFront **automatically provides HTTPS** via a wildcard certificate on its default domain.
- No need to manually configure SSL to use `https://your-distribution.cloudfront.net`.
- View certificate info via browser lock icon (browser-dependent).

## Origin Access Concern

- **S3 bucket is still publicly accessible**.
- Anyone can bypass CloudFront and access content directly from S3.
- This can:
  - Bypass caching
  - Bypass CloudFront security rules (e.g., geo restrictions, signed URLs)

> To fix this, **restrict S3 access to only CloudFront using Origin Access Identity (OAI)** – covered in a later lesson.

## Infrastructure Continuation

- **Do NOT delete this setup.**
- Infrastructure will be reused in upcoming lessons.
- It falls entirely within the **AWS Free Tier**.

## Key Takeaways

| Topic        | Key Insight                                                              |
| ------------ | ------------------------------------------------------------------------ |
| Edge Caching | Improves performance by storing objects at the closest AWS edge location |
| Overwrites   | New files with the same name are NOT immediately reflected in CloudFront |
| Invalidation | Forces edge locations to refresh objects from S3                         |
| Versioning   | Prefer versioned object names to avoid cache conflict                    |
| HTTPS        | CloudFront supports HTTPS out of the box                                 |
| Security     | Restrict S3 origin to avoid direct access                                |

## Folder/File Structure Summary

```
S3 Bucket
│
├── index.html
├── IMG/
│   ├── TopCat1.jpg
│   ├── ...
│   └── Merlin.jpg   <- Originally Merlin, later replaced by Whiskers
```

## Commands / Concepts Glossary

| Term         | Explanation                                                                   |
| ------------ | ----------------------------------------------------------------------------- |
| TTL          | Time-to-Live: Duration an object remains cached before rechecking with origin |
| Invalidation | Manual clearing of cache at edge locations                                    |
| OAI          | Origin Access Identity: used to restrict S3 access only to CloudFront         |
| Wildcard     | `/*` or `*.jpg` used to apply a rule to multiple objects                      |
