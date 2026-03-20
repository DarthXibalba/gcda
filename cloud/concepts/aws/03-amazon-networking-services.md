# Amazon Networking Services

## Overview

Amazon networking services provide the foundational infrastructure that enables communication between resources in the AWS cloud and with the internet. The core service is the Virtual Private Cloud (VPC), which allows you to define isolated networks, control traffic flow, and enforce security boundaries.

---

## Virtual Private Cloud (vpc)

A VPC is a logically isolated network within AWS where you can launch resources such as EC2 instances.

### Key Characteristics

- Region-scoped (exists within a single AWS region)
- Fully customizable IP address range using CIDR blocks
- Supports both public and private networking configurations
- Provides isolation from other AWS customers

### CIDR Blocks

- Define the IP address range of the VPC (e.g., `10.0.0.0/16`)
- Determines how many IP addresses are available
- Larger ranges allow more resources but require planning

---

## Subnets

Subnets are subdivisions of a VPC that segment the IP address space.

### Purpose

- Organize resources by function or security level
- Control routing behavior (internet access vs internal-only)
- Enable high availability across multiple availability zones

### Types of Subnets

#### Public Subnet
- Has a route to an Internet Gateway
- Resources can receive public IP addresses
- Used for web servers, load balancers

#### Private Subnet
- No direct route to the internet
- Used for databases, internal services
- Outbound internet access typically via NAT

---

## Internet Gateway (igw)

An Internet Gateway allows communication between a VPC and the internet.

### Characteristics

- Horizontally scaled and highly available
- Enables inbound and outbound internet traffic
- Required for public subnets

---

## NAT Gateway

A NAT Gateway allows instances in private subnets to access the internet without being directly exposed.

### Use Cases

- Software updates
- External API calls
- Package downloads

### Properties

- Managed service (no maintenance)
- Must be placed in a public subnet
- Charges based on usage

---

## Route Tables

Route tables determine how traffic is directed within a VPC.

### Components

- Rules that map destination IP ranges to targets
- Targets include:
  - Internet Gateway
  - NAT Gateway
  - Local VPC routing

### Behavior

- Each subnet is associated with a route table
- Controls whether a subnet is public or private

---

## Security Groups

Security groups act as virtual firewalls at the instance level.

### Features

- Stateful (responses automatically allowed)
- Allow rules only (no explicit deny)
- Applied to EC2 instances and other resources

### Common Rules

- Allow SSH (port 22)
- Allow HTTP/HTTPS (ports 80/443)

---

## Network Access Control Lists (NACL)

NACLs operate at the subnet level and provide an additional layer of security.

### Features

- Stateless (must define both inbound and outbound rules)
- Supports allow and deny rules
- Evaluated in order (rule numbers matter)

### Comparison with Security Groups

| feature        | security group | nacl        |
|----------------|--------------|------------|
| scope          | instance     | subnet     |
| stateful       | yes          | no         |
| rule type      | allow only   | allow/deny |
| evaluation     | all rules    | ordered    |

---

## Elastic IP (EIP)

An Elastic IP is a static public IPv4 address that can be associated with resources.

### Use cases

- Stable endpoints for services
- Avoid IP changes on instance restart

---

## VPC Peering

Allows communication between two VPCs.

### Characteristics

- Private IP communication
- No need for internet gateway
- Non-transitive (must be explicitly configured between each pair)

---

## DNS and DHCP

AWS provides built-in DNS and DHCP services within a VPC.

### DNS

- Resolves domain names to IP addresses
- Internal DNS for private resources
- Public DNS for internet-facing services

### DHCP

- Automatically assigns IP addresses and network configuration

---

## High Availability Considerations

- Use multiple Availability Zones
- Distribute subnets across AZs
- Avoid single points of failure (e.g., NAT Gateway per AZ)

---

## Key Takeaways

- VPC is the foundational networking construct in AWS
- Subnets control segmentation and routing behavior
- Internet Gateway and NAT Gateway define internet access patterns
- Security Groups and NACLs enforce layered security
- Proper design enables scalability, isolation, and fault tolerance
