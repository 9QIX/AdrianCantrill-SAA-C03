# AWS Access Keys and CLI Configuration Summary

This lesson covers the creation of AWS access keys for IAM admin users in both the general and production AWS accounts. It further guides the installation and configuration of the AWS Command Line Interface (CLI), enabling interaction with AWS services using the access keys.

## Steps to Create Access Keys

### General AWS Account Access Keys

1. **Log in as IAM Admin for General AWS Account**
   - Navigate to the account drop-down and select "Security Credentials."
2. **Create Access Keys**

   - Scroll down and click "Create Access Key."
   - Select "Command Line Interface" as the use case.
   - Confirm understanding and proceed.
   - Add a description like `local CLI IAM admin-general`.
   - Create and **download the CSV file** containing the access key.
   - Rename the file to `IAM admin_Access Keys_General.csv`.

3. **Manage Access Keys**

   - You can have two sets of access keys.
   - Access keys can be activated, deactivated, or deleted.
   - Always **deactivate** before deleting an access key.

4. **Save and Secure Access Keys**
   - Ensure to **download** and securely store the CSV file containing the secret access key, as it cannot be retrieved again after creation.

### Production AWS Account Access Keys

1. **Log in as IAM Admin for Production AWS Account**
   - Similar steps as the general account: Create a new set of access keys.
   - Add a description like `local CLI IAM admin-production`.
   - Download and rename the CSV file to `IAM admin_Access Keys_Production.csv`.

## AWS CLI Installation and Configuration

### AWS CLI Installation

- Visit the provided [AWS CLI download link](https://aws.amazon.com/cli/) and select the version based on your operating system (Windows, Linux, MacOS).
- Follow the instructions to **install** AWS CLI version 2.
- Verify the installation by running:
  ```bash
  aws --version
  ```

### AWS CLI Profile Configuration

#### General Account CLI Configuration

1. Open the terminal and run the following command:
   ```bash
   aws configure --profile IAM admin-general
   ```
2. Enter the access key ID and secret access key from the CSV file for the general account.
3. Set the **default region** to `us-east-1` (Northern Virginia).
4. Leave the output format blank (press enter).

#### Production Account CLI Configuration

1. Open the terminal and run the following command:
   ```bash
   aws configure --profile IAM admin-production
   ```
2. Repeat the steps as done for the general account, entering the access key details for the production account.

### Testing AWS CLI Configuration

1. To test the general account profile:
   ```bash
   aws s3 ls --profile IAM admin-general
   ```
   - This should return an empty list or any existing S3 buckets. If there's an error, reconfigure the profile.
2. To test the production account profile:
   ```bash
   aws s3 ls --profile IAM admin-production
   ```
   - Similar to the general account, ensure no errors occur.

## Security Considerations

- **Do not share credentials:** Anyone with the access key ID and secret access key can access your AWS account.
- **Rotate access keys regularly:** If credentials are leaked, delete and recreate access keys.
- **Store credentials securely:** Delete the CSV files after configuring the CLI to prevent unauthorized access.

## Final Notes

By the end of this lesson, you should have:

- Created access keys for both the general and production AWS accounts.
- Installed and configured the AWS CLI.
- Set up two named profiles: `IAM admin-general` and `IAM admin-production`.

These configurations will be used in future lessons for managing AWS resources via the command line.
