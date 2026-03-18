# Amazon EC2 and Compute Services

## Overview

Amazon EC2 (Elastic Compute Cloud) is a foundational AWS service that provides scalable, on-demand virtual servers in the cloud. It allows engineers to provision compute capacity without managing physical hardware, forming the backbone of most cloud-based systems.

This chapter introduces EC2 along with adjacent compute services, focusing on how AWS abstracts infrastructure and enables flexible deployment models.

---

## Core Concepts

### Elastic Compute Cloud (EC2)

EC2 provides virtual machines (instances) that can be launched, configured, and terminated on demand.

Key properties:
- On-demand provisioning
- Pay-as-you-go pricing
- Full control over OS and runtime
- Scalable capacity

---

### EC2 Instance Lifecycle

1. Launch
2. Running
3. Stopping / Stopped
4. Terminated

Important distinction:
- **Stopped**: Can be restarted (persistent storage retained)
- **Terminated**: Permanently deleted

---

### Instance Types

Instances are categorized based on workload optimization:

- **General Purpose** → balanced CPU, memory, networking
- **Compute Optimized** → high CPU workloads
- **Memory Optimized** → large in-memory datasets
- **Storage Optimized** → high I/O throughput
- **Accelerated Computing** → GPUs / specialized hardware

---

### Amazon Machine Image (AMI)

An AMI is a preconfigured template used to launch EC2 instances.

Includes:
- Operating system
- Application stack (optional)
- Configuration settings

Types:
- AWS-provided
- Marketplace
- Custom (user-created)

---

### Storage Options

#### Elastic Block Store (EBS)
**An Amazon EBS volume is a storage device that functions like a physical hard drive.** The root volume is a special EBS volume that stores the AMI, which includes the operating system and software needed to boot your EC2 instance.

- Persistent block storage
- Attached to EC2 instances
- Survives instance stop/start

#### Instance Store
- Ephemeral storage
- Lost when instance stops or terminates

---

### Networking

EC2 instances run inside a Virtual Private Cloud (VPC).

Key components:
- **IP Addressing** (public/private)
- **Security Groups** → instance-level firewall
- **Subnets** → logical network segmentation

---

### Security

#### Security Groups
- Stateful firewall
- Control inbound/outbound traffic
- Applied at instance level

#### Key Pairs
- Used for SSH authentication
- Public/private key cryptography

---

### Pricing Models

- **On-Demand** → pay per use
- **Reserved Instances** → discounted long-term commitment
- **Spot Instances** → unused capacity at reduced cost (can be interrupted)
- **Savings Plans** → flexible pricing model

---

## Scaling and Availability

#### Elasticity

EC2 supports dynamic scaling:
- Manual scaling
- Auto Scaling Groups (ASG)

#### High Availability

Achieved through:
- Multiple Availability Zones (AZs)
- Load balancing (ELB)

### Elastic Load Balancing

- An ELB automatically distributes the incoming traffic *(workload)* across multiple targets *(i.e. EC2 instances)* in one or more AZs, so as to balance the workload for high performance and high availability.
- AN ELB monitors the health of its registered targets and distributes traffic only to healthy targets.
- Application Load Balancer (ALB)

### Auto Scaling Groups (ASG)

- Behind an ELB, there is usually an ASG that manages the fleet of ELB targets
- ASG monitors the workload of the instances and uses auto-scaling policies to scale:
  - When the workload reaches a certain up-threshold, such as 80% CPU utilization, ASG will launch new EC2s and add them into the fleet to offload the traffic until the utilization drops below the up-threshold.
  - When the workload  reaches a certain down-threshold, such as 30% CPU utilization, ASG will shut down EC2s from the fleet until the utilization rises above the threshold.
- ASG also utilizates a health check to monitor the instances and replace unhealthy ones as needed.
- During the auto-scaling process, ASG makes sure that the running EC2 instances are loaded within the thresholds and are laid out across as many AZs in a region.

---

## AWS Compute - from VMs to Containers to Serverless

#### Containerization (Docker)

Docker was the first to solve the problem of application portability without being bolted down to an OS by introducing containerization technology.

##### Docker Image

A Docker image is a lightweight, standalone, executable package of software that includes everything needed to run an application: code, runtime, system tools, system libraries, settings

##### Containers

- A container is a runtime of the Docker image, and the application runs quickly and reliably from one computing environment to another.
- Multiple containers can run on the same VM and share the OS kernel with other containers, each running as isolated processes in user space.

#### Serverless

To further achieve fast and robust deployments and low lead times, the concept of **serverless** computing emerged. With serverless computing, workloads run on servers behind the scenes.

From a developer/user 's point of view, they just need to submit the code and get the running results back; there is no hassle of building and managing any infrastructure platforms at all, while resources can continuously scale and be dynamically allocated as needed, yet you never pay for idle time as it is pay per usage.

### ECS / EKS

- Container orchestration
- ECS (AWS-native)
- EKS (Kubernetes-based)

### AWS Lambda

- Serverless compute
- No server management
- Event-driven execution

### Elastic Beanstalk

- Platform-as-a-Service (PaaS)
- Simplifies deployment and scaling

#### ECS (Additional info)

- ECS is a fully managed container orchestration services that helps you easily deploy, manage, and scale containerized applications using Docker or K8s
- ECS provides a highly available and scalable platform for running container-based applications
- Enterprises use ECS to grow and manage enterprise applications portfolios,scale web applications, perform batch processing, and run services

#### EKS (Additional info)

- EKS on the other hand is a fully managed service that makes it easy to deploy, manage, and scale Kubernetes in the AWS cloud
- EKS leverages the global cloud's performance, scale, reliability, and availability, andintegrates it with other AWS services such as networking, storage, and security services.

#### AWS Lambda (Additional info)

- Event-driven, serverless computing service that runs code in response to events and automatically manages the computing resources required by that code
- Lambda provides HA with automatic scaling, cost optimization, and security
- Supports multiple programming languages, environment variables, and tight integration with other AWS services

---

## Key Tradeoffs

| Feature            | EC2                          | Lambda                     |
|------------------|------------------------------|---------------------------|
| Control           | Full                         | Limited                   |
| Management        | Manual                       | Fully managed             |
| Scaling           | Configured                   | Automatic                 |
| Use Case          | Long-running services        | Event-driven workloads    |

---

## Mental Models

- EC2 = "virtual server you manage"
- Lambda = "function you deploy"
- Beanstalk = "app platform abstraction"
- Containers (ECS/EKS) = "portable runtime layer"

---

## When to Use EC2

Use EC2 when:
- You need OS-level control
- Running long-lived services
- Custom environments are required
- Migration from on-prem systems

Avoid EC2 when:
- Workloads are highly event-driven → use Lambda
- You want minimal infrastructure management → use managed services

---

## Summary

Amazon EC2 is the foundational compute service in AWS, offering maximum flexibility and control. However, it comes with operational overhead. Modern cloud architecture often balances EC2 with higher-level abstractions like Lambda and container services depending on workload requirements.

Understanding EC2 is critical because it underpins most cloud systems, even when abstracted by higher-level services.
