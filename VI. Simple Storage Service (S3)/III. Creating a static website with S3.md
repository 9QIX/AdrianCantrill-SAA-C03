# AWS S3 Static Website Hosting with Route 53 Integration

This guide summarizes the process of using AWS S3 to host a static website and integrating it with a custom domain via Route 53. It covers the key steps required to set up the hosting, upload files, configure permissions, and integrate with a custom DNS. Follow these steps carefully for a smooth setup.

## Prerequisites

1. **AWS Account:** Ensure you're logged into the management account of your AWS organization using an IAM admin user.
2. **Region Selection:** Select the `us-east-1` (Northern Virginia) region.
3. **Optional Domain:** If you registered a custom domain (e.g., `example.com`), this guide will also cover its integration.
4. **Demo Files:** Download demo files from the video [here](https://learn-cantrill-labs.s3.amazonaws.com/awscoursedemos/0042-aws-mixed-s3-static-website/static_website_hosting.zip).

## Steps to Set Up S3 Static Website Hosting

### 1. Create an S3 Bucket

- Navigate to the **S3 Console** via the AWS Management Console.
- Click **Create Bucket** and provide a unique bucket name. If using a custom domain, name the bucket to match your domain (e.g., `static.example.com`).
- Uncheck **Block all public access** and confirm the risks. This step enables public access configuration later.
- Leave other options as default and click **Create Bucket**.

### 2. Enable Static Website Hosting

- Open the newly created bucket and navigate to the **Properties** tab.
- Scroll to **Static Website Hosting** and click **Edit**.
- Enable static website hosting and choose **Host a Static Website**.
- Provide the following:
  - **Index Document:** `index.html`
  - **Error Document:** `error.html`
- Save changes and note the **Bucket Website Endpoint** URL.

### 3. Upload Files to S3 Bucket

- Navigate to the **Objects** tab in the bucket.
- Click **Upload** and:
  - Use **Add Files** to upload `index.html` and `error.html`.
  - Use **Add Folder** to upload a folder containing images or other media.
- Review the upload details and click **Upload** to complete.

## Configuring Public Access

### 1. Add a Bucket Policy

- Go to the **Permissions** tab in the bucket.
- Under **Bucket Policy**, click **Edit** and paste the following policy template:

  ```json
  {
    "Version": "2012-10-17",
    "Statement": [
      {
        "Effect": "Allow",
        "Principal": "*",
        "Action": "s3:GetObject",
        "Resource": "arn:aws:s3:::<bucket-name>/*"
      }
    ]
  }
  ```

- Replace `<bucket-name>` with the ARN of your bucket, appending `/*` to include all objects.
- Save changes.

### 2. Verify Access

- Open the **Bucket Website Endpoint** URL in a browser.
- If configured correctly, the website should load. If you encounter a 403 error, double-check the bucket policy and permissions.

## (Optional) Route 53 Domain Integration

If using a custom domain, integrate it with Route 53:

1. **Navigate to Route 53:**

   - Go to the Route 53 console and select your domain's **Hosted Zone**.
   - Click **Create Record**.

2. **Create a Record:**

   - Choose **Simple Routing** and specify the bucket name (e.g., `static.example.com`).
   - In the endpoint dropdown, select **Alias to S3 Website Endpoint** and specify the bucket's region (`us-east-1`).

3. **Verify DNS:**
   - Wait for DNS propagation.
   - Open the custom domain URL in a browser to verify it resolves to the S3 bucket.

## Cleanup (Optional)

To clean up resources:

1. **Delete Route 53 Record:**

   - Select the record created and click **Delete**.

2. **Empty S3 Bucket:**

   - Open the S3 bucket, click **Empty**, and confirm by typing `permanently delete`.

3. **Delete S3 Bucket:**
   - After emptying the bucket, delete it from the S3 console.

## Notes

- **Error Handling:** The error document (`error.html`) will load if a non-existent resource is requested.
- **DNS Requirements:** The bucket name must match the fully qualified domain name (FQDN) for Route 53 integration.
- **Security:** Ensure that public access is only enabled for resources intended to be public.

By following these steps, you can successfully host a static website on AWS S3 and optionally integrate it with a custom domain using Route 53.
