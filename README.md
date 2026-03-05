# 📜 Grand Compendium of Digital Alchemy

A **monorepo of software engineering knowledge** exploring the craft of transforming ideas into reliable systems.

This repository serves as a personal **knowledge compendium and engineering laboratory**, documenting concepts across multiple disciplines in computer science.

# 🧠 Philosophy & Inspiration ✨

Software engineering is both a **science and a craft**.

Like alchemy, it involves:

- 🧩 transforming **data into knowledge**
- ⚙️ transforming **algorithms into solutions**
- 🏗️ transforming **infrastructure into systems**
- 🔬 transforming **experiments into engineering practices**

The **Grand Compendium of Digital Alchemy** is intended to be a lifelong record of exploration into the craft of building software; a living embodiment of the spirit of discovery found in fictional worlds like *Fullmetal Alchemist*, where knowledge and experimentation drive mastery.

# 🗂 Repository Structure

The repository follows a **monorepo philosophy**, where each major discipline is treated as its own **knowledge discovery project**.
```
grand-compendium-of-digital-alchemy/
├── dsa/
├── system-design/
├── cloud/
└── README.md
```

Each domain maintains its own internal structure suited to the way that topic is studied and practiced.

---

# 🧮 Data Structures & Algorithms

The **DSA project** focuses on algorithmic thinking and problem solving.
```
dsa/
├── concepts/
├── problems/
└── solutions/
```

## 📖 concepts
Core theoretical material and algorithmic foundations.

Examples include:

- algorithm complexity analysis
- recursion and dynamic programming
- graph traversal strategies
- hashing techniques
- common data structure patterns

These notes are written as structured Markdown documents for easy browsing.

## 🧩 problems

Problem statements organized using a custom taxonomy system.

Example:
```
problems/A_Easy/A_Arrays/AAD_ContainsDuplicate.md
```

Each problem document typically contains:

- problem description
- examples
- constraints
- hints or discussion of follow-up questions

## ⚙️ solutions

Python3-specific implementations of each problem.

Example:
```
solutions/python/A_Easy/A_Arrays/AAD_ContainsDuplicate.py
```

Solutions emphasize:

- clarity
- algorithmic correctness
- performance considerations

## 🧪 tests

Each solution has an accompanying **pytest** suite to verify correctness of implementation.

Example:
```
solutions/python/A_Easy/A_Arrays/AAD_ContainsDuplicate_test.py
```

---

# 🏗 System Design

The **System Design project** explores architecture for large-scale systems.

```
system-design/
├── concepts/
└── patterns/
```

Topics include:

- distributed systems fundamentals
- load balancing strategies
- caching architectures
- consistency models
- event-driven systems
- scalability patterns

---

# ☁️ Cloud Computing

The **Cloud project** explores infrastructure and platform engineering.
```
cloud/
├── concepts/
└── labs/
```

Topics include:

- networking and VPC design
- container orchestration
- infrastructure as code
- observability and monitoring
- cloud architecture patterns

Hands-on experiments and labs may include tools such as:

- Docker
- Kubernetes
- Terraform
- cloud provider services

---

# 📁 File Naming Conventions

To ensure portability across operating systems and developer environments, the repository follows consistent naming rules:

- lowercase paths
- hyphen-separated directory names
- no spaces or special characters


This avoids issues with:

- shell commands
- CI pipelines
- cross-platform filesystems

---

# 🔮 Long-Term Vision

Over time, this compendium aims to grow into a structured knowledge base covering:

- algorithms and data structures
- distributed systems
- system architecture
- cloud infrastructure
- engineering patterns and best practices

Future domains may include:

- networking
- operating systems
- security engineering
- programming language theory

# 📚 References

The following resources serve as foundational material and inspiration for the topics explored throughout this compendium.

## 🌐 Online Platforms

- **LeetCode** – A widely used platform for practicing data structures and algorithms problems commonly encountered in technical interviews.  
  https://leetcode.com/

---

## 📖 Books

- **Cracking the Coding Interview** — *Gayle Laakmann McDowell*  
  A comprehensive guide to technical interviews covering data structures, algorithms, and problem-solving strategies.

- **System Design Interview – An Insider's Guide (Volume 1)** — *Alex Xu*  
  Introduces core concepts and practical approaches to designing scalable distributed systems.

- **System Design Interview – An Insider's Guide (Volume 2)** — *Alex Xu*  
  Expands on advanced system design topics with additional real-world architecture case studies.

- **Software Engineering at Google** — *Titus Winters, Tom Manshreck, Hyrum Wright*  
  Explores engineering practices, tooling, and cultural principles used to build and maintain large-scale software systems.
