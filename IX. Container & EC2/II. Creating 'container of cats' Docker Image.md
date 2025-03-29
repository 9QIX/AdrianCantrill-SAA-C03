# AWS SA C03: Running Docker on EC2

### Overview

This lesson covers installing and running Docker on an EC2 instance, building a Docker image, and deploying a containerized application. It also includes an optional step to upload the container to Docker Hub.

## 1. Setting Up the Environment

### Prerequisites

- Ensure you are logged into the **IAM admin user** of your AWS account.
- Use the **Northern Virginia (us-east-1) region**.
- Deploy an EC2 instance using **One-Click Deployment**:
  - [CloudFormation Stack Deployment](https://console.aws.amazon.com/cloudformation/home?region=us-east-1#/stacks/create/review?templateURL=https://learn-cantrill-labs.s3.amazonaws.com/awscoursedemos/0030-aws-associate-ec2docker/ec2docker_AL2023.yaml&stackName=EC2DOCKER).

### Connecting to the EC2 Instance

1. Go to the **AWS Console → CloudFormation → Stacks**.
2. Wait for the stack status to change to **CREATE_COMPLETE**.
3. Navigate to the **Resources** tab and locate the **Public EC2 Instance**.
4. Click on the **Physical ID** of the EC2 instance to open the EC2 Console.
5. Use **Session Manager** to connect:
   - Right-click the instance → Select **Connect**.
   - Choose **Session Manager** → Click **Connect**.

## 2. Installing and Configuring Docker

### Install Docker Engine on EC2

```sh
sudo dnf install docker  # Install Docker
sudo service docker start  # Start Docker service
sudo usermod -a -G docker ec2-user  # Add ec2-user to Docker group
```

- `dnf install docker`: Installs Docker using the **DNF package manager**.
- `service docker start`: Starts the **Docker service**.
- `usermod -a -G docker ec2-user`: Grants **Docker permissions** to `ec2-user`.

### Log Out & Log Back In

1. **Logout** to apply group membership changes:
   ```sh
   exit
   ```
2. **Reconnect** using Session Manager.
3. Switch to `ec2-user`:
   ```sh
   sudo su - ec2-user
   ```

### Verify Docker Installation

```sh
docker ps
```

- If the installation is correct, it should return **an empty container list with headers**.

## 3. Building and Running a Docker Container

### Navigate to the Project Directory

```sh
cd container
ls -l
```

- The directory contains:
  - `index.html`: A simple **webpage**.
  - `containerandcat*.jpg`: **Images** used in the webpage.
  - `Dockerfile`: Instructions for **building the Docker image**.

### Dockerfile Explanation

```dockerfile
FROM redhat/ubi8  # Use Red Hat UBI8 as base image

LABEL maintainer="Animals4life"  # Metadata about the image

RUN yum -y install httpd  # Install Apache HTTP Server

COPY index.html /var/www/html/  # Copy webpage into the server directory
COPY containerandcat*.jpg /var/www/html/  # Copy images

ENTRYPOINT ["/usr/sbin/httpd", "-D", "FOREGROUND"]  # Start Apache server

EXPOSE 80  # Declare port 80 for HTTP traffic
```

#### Explanation of Each Line:

1. `FROM redhat/ubi8`: Uses **Red Hat Universal Base Image 8** as the foundation.
2. `LABEL maintainer="Animals4life"`: Metadata about the image creator.
3. `RUN yum -y install httpd`: Installs **Apache HTTP Server**.
4. `COPY index.html /var/www/html/`: Copies **HTML file** into the web directory.
5. `COPY containerandcat*.jpg /var/www/html/`: Copies **image files** into the web directory.
6. `ENTRYPOINT ["/usr/sbin/httpd", "-D", "FOREGROUND"]`: Runs **Apache in the foreground**, ensuring the container stays running.
7. `EXPOSE 80`: Informs Docker that the application runs on **port 80**.

## 4. Creating and Running the Docker Image

### Build the Docker Image

```sh
docker build -t containerofcats .
```

- `docker build`: Creates a Docker image from the **Dockerfile**.
- `-t containerofcats`: Tags the image with the name **containerofcats**.
- `.`: Specifies the **current directory** as the build context.

### Verify the Image Exists

```sh
docker images --filter reference=containerofcats
```

- Lists images with the name **containerofcats**.

### Run a Container from the Image

```sh
docker run -t -i -p 80:80 containerofcats
```

- `docker run`: Starts a new container.
- `-t -i`: Allocates a terminal session.
- `-p 80:80`: Maps **port 80** on the container to **port 80** on the EC2 instance.
- `containerofcats`: Specifies the image to run.

### Verify Web Application

1. Go to **AWS Console → EC2 → Instances**.
2. Copy the **Public IP Address** of the EC2 instance.
3. Open a browser and visit:
   ```
   http://<PUBLIC_IP>
   ```
4. If successful, the **web application** should be displayed.

## 5. Uploading the Image to Docker Hub (Optional)

### Login to Docker Hub

```sh
docker login --username=YOUR_USER
```

- Replace `YOUR_USER` with your **Docker Hub username**.

### Tag the Image

```sh
docker tag IMAGEID YOUR_USER/containerofcats
```

- `IMAGEID`: Replace with the **actual image ID** from `docker images`.
- Tags the image for **Docker Hub upload**.

### Push the Image to Docker Hub

```sh
docker push YOUR_USER/containerofcats:latest
```

- Uploads the container to **Docker Hub**.

## 6. Additional Resources

- **Docker Hub**: [https://hub.docker.com/](https://hub.docker.com/)
- **Lesson Commands**: [Lesson Commands File](https://learn-cantrill-labs.s3.amazonaws.com/awscoursedemos/0030-aws-associate-ec2docker/lesson_commands_AL2023.txt)
- **One-Click Deployment**: [CloudFormation Stack](https://console.aws.amazon.com/cloudformation/home?region=us-east-1#/stacks/create/review?templateURL=https://learn-cantrill-labs.s3.amazonaws.com/awscoursedemos/0030-aws-associate-ec2docker/ec2docker_AL2023.yaml&stackName=EC2DOCKER)

## Summary

This lesson walks through:

1. **Setting up an EC2 instance** with Docker pre-installed.
2. **Installing Docker manually** on an Amazon Linux 2023 instance.
3. **Building a Docker image** from a simple web application.
4. **Running a container** to serve the web application.
5. **Optional: Uploading the container** to Docker Hub for reuse.

By the end of this guide, you should be able to deploy and manage Docker containers on AWS EC2.
