# Shared AMIs in Amazon EC2

## Introduction

A **Shared AMI (Amazon Machine Image)** is an AMI created by a developer and made available for others to use. It allows users to quickly deploy pre-configured environments and customize them as needed.

> **Warning:** Use shared AMIs at your own risk. Amazon does not guarantee their integrity or security. It is recommended to obtain AMIs from trusted sources.

## **Verified Providers**

- Public AMIs owned by **Amazon** or **verified Amazon partners** are marked as **Verified Provider** in the EC2 console.
- Use the AWS CLI to check the owner of a public AMI:
  ```sh
  aws ec2 describe-images --owners amazon aws-backup-vault aws-marketplace
  ```
- To become a **verified provider**, register as a seller on **AWS Marketplace**.

## **Key Topics on Shared AMIs**

- [Finding Shared AMIs](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/sharing-amis.html)
- Preparing Linux AMIs for sharing
- Controlling AMI discovery with **Allowed AMIs**
- Making an AMI public
- **Block public access** for security
- Sharing AMIs with **specific AWS accounts** or **AWS Organizations**
- Cancelling an AMI shared with your account
- Best practices for **creating shared Linux AMIs**

## **Working with AMIs - Hands-On Demo**

### **1. AMIs Are Regional**

- AMIs are created and stored in **specific AWS regions**.
- If you change the region in the **EC2 Console**, the AMIs from the previous region will not be visible.
- Each AMI has a **unique AMI ID**, specific to its region.

### **2. Copying an AMI Between Regions**

#### **Steps to Copy an AMI:**

1. **Go to EC2 Console** → Select AMIs.
2. **Right-click** on the AMI → Select **Copy AMI**.
3. Choose the **destination region**.
4. (Optional) Modify the **name and description**.
5. Click **Copy AMI**.
6. Wait for the AMI and associated **snapshots** to be copied.

> **Important:** A copied AMI is a **new, separate** AMI in the destination region.

#### **Factors Affecting Copy Time:**

- Distance between **source and destination** region.
- Size and **amount of data** in the snapshot.
- AWS **infrastructure load**.

### **3. Managing AMI Permissions**

#### **Default Behavior:**

- By default, an AMI is **private** (accessible only within the AWS account that created it).

#### **Sharing an AMI:**

- **Public AMI:** Available to **any AWS account**.
  - **Risk:** Sensitive information (e.g., **access keys**) could be exposed.
- **Private AMI with Specific Accounts:**
  - Safer than making an AMI public.
  - Add AWS Account IDs explicitly to grant access.
- **Sharing within AWS Organizations:**
  - Share AMIs with an **entire AWS Organization** or **specific Organizational Units (OUs)**.

#### **Adding Permissions via Console:**

1. Right-click the AMI → **Edit AMI Permissions**.
2. Select **Public** (less secure) or add **specific AWS Account IDs**.
3. (Optional) Check the box for **Create Volume Permissions** (allows creating volumes from AMI snapshots).
4. Click **Save Changes**.

### **4. Deleting AMIs and Snapshots**

- Deregister an AMI to **prevent future use**.
- Delete associated **snapshots** to reclaim storage.

#### **Steps to Delete an AMI:**

1. **Right-click** on the AMI → Select **Deregister**.
2. Confirm deregistration.
3. **Go to Snapshots** → Identify related snapshots.
4. **Right-click** on each snapshot → **Delete**.
5. Repeat this process in **all regions where the AMI was copied**.

## **Best Practices for Shared AMIs**

1. **Use trusted sources**: Prefer AMIs from **AWS Marketplace** or **verified providers**.
2. **Regularly update and patch AMIs** to ensure security.
3. **Minimize sensitive data exposure**:
   - Remove **access keys** and sensitive files before sharing.
   - Verify permissions before making an AMI public.
4. **Use IAM roles** instead of embedding credentials.
5. **Monitor usage**: Track AMI usage with **AWS CloudTrail**.
6. **Follow AWS security guidelines** when sharing AMIs publicly.

## **Conclusion**

- Shared AMIs are a convenient way to deploy **pre-configured** environments.
- **Use caution** when sharing AMIs to avoid security risks.
- Always follow **best practices** when making AMIs public or granting permissions.
- AMIs are **region-specific**; copying an AMI creates a **new** AMI in the destination region.

For more details, refer to the **[AWS Documentation on AMI Sharing](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/sharing-amis.html)**.
