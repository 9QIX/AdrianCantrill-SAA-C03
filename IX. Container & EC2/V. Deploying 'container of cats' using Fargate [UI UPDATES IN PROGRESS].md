# Deploying a Docker Container on AWS ECS Fargate

## Overview

This guide provides a step-by-step approach to deploying a Docker container on an **Amazon ECS Fargate** cluster. The tutorial uses a pre-built container image named **Container of Cats**, and you will deploy it using **AWS Fargate**.

## Prerequisites

Before starting, ensure you have:

- **AWS IAM Admin Access**
- **An AWS Management Account**
- **Access to AWS ECS Console**
- **Located in the Northern Virginia (us-east-1) region**
- **Default VPC Available**

## Step 1: Create an ECS Cluster

1. **Navigate to ECS:**
   - In the AWS Console, go to `Find Services` → `ECS`.
2. **Create a Cluster:**
   - Click `Clusters` → `Create Cluster`.
   - Name the cluster **all-the-cats**.
3. **Select VPC:**
   - Use the **default VPC**.
   - Ensure all available subnets are selected.
4. **Cluster Mode:**
   - Select **AWS Fargate** as the launch type.
   - Leave other settings as default.
5. **Create the Cluster:**
   - Click `Create`.
   - If an error occurs, wait a few minutes and retry.

## Step 2: Create a Task Definition

1. **Go to ECS Console → Task Definitions → Create New Task Definition**.
2. **Task Name:**
   - Enter `container-of-cats`.
3. **Container Details:**
   - Name: `container-of-cats-web`
   - Image URI: `docker.io/n9vem/containerofcats`
   - Port Mapping:
     - **Container Port:** `80`
     - **Host Port:** `80`
     - **Protocol:** `TCP`
     - **Application Protocol:** `HTTP`
4. **Task Environment:**
   - OS: `Linux/x86_64`
   - CPU: `0.5 vCPU`
   - Memory: `1 GB`
   - Disable Log Collection.
5. **Create Task Definition:**
   - Click `Next`, review the settings, and `Create`.

### Task Definition JSON Explained

```json
{
  "taskDefinitionArn": "arn:aws:ecs:us-east-1:329599627644:task-definition/containerofcats:1",
  "containerDefinitions": [
    {
      "name": "containerofcatsweb",
      "image": "docker.io/n9vem/containerofcats",
      "cpu": 0,
      "portMappings": [
        {
          "name": "containerofcatsweb-80-tcp",
          "containerPort": 80,
          "hostPort": 80,
          "protocol": "tcp",
          "appProtocol": "http"
        }
      ],
      "essential": true
    }
  ],
  "networkMode": "awsvpc",
  "requiresCompatibilities": ["FARGATE"],
  "cpu": "512",
  "memory": "1024",
  "runtimePlatform": {
    "cpuArchitecture": "X86_64",
    "operatingSystemFamily": "LINUX"
  }
}
```

### Breakdown of JSON Configuration

- **`containerDefinitions`**: Defines the container properties.
  - **`name`**: Specifies the container name.
  - **`image`**: The Docker image source.
  - **`portMappings`**: Maps container ports to the host.
- **`networkMode`**: Uses `awsvpc` for networking.
- **`requiresCompatibilities`**: Defines compatibility with `FARGATE`.
- **`cpu` / `memory`**: Allocates resources.

## Step 3: Deploy the Container

1. **Navigate to ECS Clusters → Select `all-the-cats`**.
2. **Click `Tasks` → `Run New Task`**.
3. **Select Compute Options:**
   - `Launch Type`: **Fargate**
   - `Platform Version`: **Latest**
   - `Task Type`: **Task**
4. **Assign Task Definition:**
   - Family: `container-of-cats`
   - Revision: `Latest`
5. **Networking Configuration:**
   - VPC: **Default VPC**
   - Subnets: **All default subnets**
   - Security Group:
     - Name: `container-of-cats-SG`
     - Rule: **Allow HTTP (Port 80) from anywhere**
   - Enable `Public IP`.
6. **Create and Run the Task**
   - Click `Create`.
   - Wait for the status to change to **Running**.

## Step 4: Access the Deployed Application

1. **Go to ECS Console → Clusters → `all-the-cats` → Tasks**.
2. **Click the running task and find the Public IP Address**.
3. **Open a Web Browser and enter the IP**.
4. **You should see the deployed application.**

## Step 5: Cleanup Resources

To avoid unnecessary AWS costs, clean up the resources:

1. **Stop Running Task:**
   - Navigate to ECS Console → `Tasks` → `Stop`.
2. **Deregister Task Definition:**
   - Go to `Task Definitions` → Select `container-of-cats` → `Actions` → `Deregister`.
3. **Delete ECS Cluster:**
   - Navigate to `Clusters` → Select `all-the-cats` → `Delete Cluster`.

## Conclusion

In this guide, you:

- Created an **AWS ECS Fargate Cluster**.
- Defined a **Task Definition** for a Docker container.
- **Deployed** the container on Fargate.
- **Accessed the running application** via a Public IP.
- **Cleaned up resources** to avoid additional costs.

This process is fundamental for deploying containerized applications at scale using AWS ECS Fargate. Keep practicing, and as the course progresses, you'll work on more complex architectures!
