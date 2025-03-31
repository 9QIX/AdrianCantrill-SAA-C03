# AWS SSM Parameter Store - Learn Cantrill.io AWS SA C03

## Overview

This guide provides a hands-on experience in interacting with AWS Systems Manager (SSM) Parameter Store. It covers creating, retrieving, and managing parameters using the AWS CLI within AWS CloudShell.

## Creating Parameters

Parameters are stored in the AWS Systems Manager Parameter Store, categorized into hierarchical structures. Below are the created parameters:

```bash
/my-cat-app/dbstring        db.allthecats.com:3306
/my-cat-app/dbuser          bosscat
/my-cat-app/dbpassword      amazingsecretpassword1337 (encrypted)
/my-dog-app/dbstring        db.ifwereallymusthavedogs.com:3306
/rate-my-lizard/dbstring    db.thisisprettyrandom.com:3306
```

### Hierarchical Structure

AWS SSM Parameter Store allows the use of hierarchical names, making it easier to organize configuration data. Example:

- `/my-cat-app/dbstring` → Stores the database connection string.
- `/my-cat-app/dbuser` → Stores the username.
- `/my-cat-app/dbpassword` → Stores an encrypted password.

The `SecureString` type is used for encrypted values.

## Retrieving Parameters

To fetch parameters using the AWS CLI:

### Get a Specific Parameter

```bash
aws ssm get-parameters --names /rate-my-lizard/dbstring
aws ssm get-parameters --names /my-dog-app/dbstring
aws ssm get-parameters --names /my-cat-app/dbstring
```

### Get All Parameters in a Path

```bash
aws ssm get-parameters-by-path --path /my-cat-app/
```

### Retrieve Encrypted Parameters with Decryption

```bash
aws ssm get-parameters-by-path --path /my-cat-app/ --with-decryption
```

## Sample Output

Example output for retrieving `/rate-my-lizard/dbstring`:

```json
{
  "Parameters": [
    {
      "Name": "/rate-my-lizard/dbstring",
      "Type": "String",
      "Value": "db.thisisprettyrandom.com:3306",
      "Version": 1,
      "LastModifiedDate": "2025-03-31T21:07:57.042000+00:00",
      "ARN": "arn:aws:ssm:us-east-1:329599627644:parameter/rate-my-lizard/dbstring",
      "DataType": "text"
    }
  ],
  "InvalidParameters": []
}
```

When retrieving an encrypted parameter with `--with-decryption`, the `Value` field contains the decrypted password.

## Using AWS CloudShell

AWS CloudShell provides a convenient way to interact with AWS services using the AWS CLI.

### Steps to Use CloudShell

1. Open the **AWS Management Console**.
2. Click on the **CloudShell** icon.
3. Wait for the session to initialize.
4. Run AWS CLI commands directly from the terminal.

## Explanation of AWS SSM Commands

### Creating Parameters

- **Standard Parameters**: Default, up to 10,000 parameters.
- **Advanced Parameters**: Allows more than 10,000 parameters, increased size, and additional features.

**Example Command:**

```bash
aws ssm put-parameter --name "/my-cat-app/dbpassword" --value "amazingsecretpassword1337" --type "SecureString"
```

- `--name`: Specifies the parameter name.
- `--value`: Defines the parameter's value.
- `--type`: Can be `String`, `StringList`, or `SecureString`.

### Retrieving Parameters

- **Single Parameter Retrieval:**
  ```bash
  aws ssm get-parameter --name /my-cat-app/dbstring
  ```
- **Multiple Parameters Retrieval:**
  ```bash
  aws ssm get-parameters --names /my-cat-app/dbstring /my-cat-app/dbuser
  ```
- **Retrieve Encrypted Parameters:**
  ```bash
  aws ssm get-parameter --name /my-cat-app/dbpassword --with-decryption
  ```

## Summary

- **AWS Systems Manager Parameter Store** is used to manage configuration data securely.
- Parameters can be stored in a **hierarchical** format.
- **SecureString** is used for encrypted values.
- **AWS CLI commands** enable interaction with SSM Parameter Store.
- **AWS CloudShell** provides an easy way to execute CLI commands within AWS.

By following these steps, you can efficiently manage and retrieve configuration data within AWS Parameter Store.
