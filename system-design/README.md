# System Design Project Structure
```
system-design/
|
├── 01_concepts/
├── 02_patterns/
├── 03_case-studies/
└── 04_exercises/
```

## Concepts

This is the core theoretical knowledge base, these files contain explanations of fundamental distributed systems topics.

```
concepts/
│
├── scalability.md
├── availability.md
├── consistency-models.md
├── load-balancing.md
├── caching.md
├── replication.md
├── sharding.md
├── message-queues.md
├── rate-limiting.md
├── cdn.md
├── distributed-locking.md
├── leader-election.md
└── consensus-algorithms.md
```

## Patterns

System design relies heavily on **architectural patterns**, which are reusable design solutions.

```
patterns/
│
├── api-gateway.md
├── microservices.md
├── event-driven-architecture.md
├── publish-subscribe.md
├── saga-pattern.md
├── circuit-breaker.md
├── backpressure.md
└── service-discovery.md
```

These should describe:
- when the pattern is used
- advantages
- disadvantages
- real-world examples

## Case Studies
Case studies are design walkthroughs that come straight from **System Design Interview Vol. 1 & 2** or some similar media.

```
case-studies/
│
├── url-shortener.md
├── instagram.md
├── twitter-timeline.md
├── news-feed.md
├── chat-system.md
├── rate-limiter.md
├── distributed-cache.md
├── search-autocomplete.md
└── youtube.md
```

Each file should contain:
```
Problem
Requirements
High-level design
Detailed design
Bottlenecks
Scaling strategies
Tradeoffs
```

## Exercises
These are practice prompts, similar to interview questions that I have worked thru.

```
exercises/
│
├── design-dropbox.md
├── design-notification-system.md
├── design-google-drive.md
├── design-uber.md
└── design-kafka.md
```

Structure:
```
Problem
Clarifying questions
Requirements
Capacity estimation
High-level design
Deep dives
Tradeoffs
```