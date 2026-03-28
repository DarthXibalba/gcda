# System Design Concepts Tree
```
gcda/
  system-design/
    concepts/
      001-system-design-fundamentals/
        001-what-is-system-design.md
        002-functional-vs-non-functional-requirements.md
        003-latency-throughput-and-availability.md
        004-scalability-and-bottlenecks.md
        005-capacity-estimation.md
        006-trade-offs-in-system-design.md

      002-architecture/
        001-monoliths-vs-microservices.md
        002-client-server-architecture.md
        003-layered-architecture.md
        004-service-oriented-architecture.md
        005-event-driven-architecture.md
        006-serverless-architecture.md

      003-networking/
        001-dns.md
        002-http-and-https.md
        003-tcp-vs-udp.md
        004-load-balancers.md
        005-reverse-proxies.md
        006-cdns.md
        007-websockets-and-long-polling.md

      004-data-and-databases/
        relational/
          001-relational-databases.md
          002-schema-design.md
          003-normalization-and-denormalization.md
          004-sql-joins.md
          005-transactions-and-acid.md
        non-relational/
          001-non-relational-databases.md
          002-key-value-stores.md
          003-document-databases.md
          004-column-family-databases.md
          005-graph-databases.md
        shared/
          001-database-indexing.md
          002-query-optimization.md
          003-replication.md
          004-sharding-and-partitioning.md
          005-consistency-models.md
          006-cap-theorem.md
          007-oltp-vs-olap.md
          008-time-series-and-analytical-workloads.md

      005-caching/
        001-why-caching-works.md
        002-cache-aside.md
        003-read-through-and-write-through.md
        004-write-back-and-write-around.md
        005-cache-eviction-policies.md
        006-cache-invalidation.md
        007-distributed-caching.md

      006-messaging-and-asynchronous-systems/
        001-message-queues.md
        002-pub-sub.md
        003-event-streaming.md
        004-delivery-semantics.md
        005-idempotency.md
        006-dead-letter-queues.md
        007-workflows-and-background-jobs.md

      007-storage/
        001-block-vs-file-vs-object-storage.md
        002-blobs-media-and-large-objects.md
        003-static-asset-storage.md
        004-data-durability-and-redundancy.md
        005-backups-and-restore.md

      008-compute-and-scaling/
        001-vertical-vs-horizontal-scaling.md
        002-stateless-vs-stateful-services.md
        003-auto-scaling.md
        004-service-discovery.md
        005-health-checks.md
        006-graceful-degradation.md

      009-reliability/
        001-availability-and-redundancy.md
        002-single-points-of-failure.md
        003-failover.md
        004-retries-timeouts-and-backoff.md
        005-circuit-breakers.md
        006-bulkheads.md
        007-disaster-recovery.md

      010-consistency-coordination-and-distributed-systems/
        001-distributed-systems-basics.md
        002-strong-vs-eventual-consistency.md
        003-consensus.md
        004-leader-election.md
        005-distributed-locking.md
        006-clock-and-ordering-problems.md
        007-sagas-and-distributed-transactions.md

      011-api-design/
        001-rest.md
        002-graphql.md
        003-rpc-and-grpc.md
        004-api-gateways.md
        005-pagination-filtering-and-sorting.md
        006-versioning.md
        007-rate-limiting-and-throttling.md
        008-idempotency-keys.md

      012-security/
        001-authentication-vs-authorization.md
        002-sessions-cookies-and-tokens.md
        003-oauth-and-openid-connect.md
        004-encryption-in-transit-and-at-rest.md
        005-secrets-management.md
        006-common-web-security-risks.md

      013-observability-and-operations/
        001-logging.md
        002-metrics.md
        003-tracing.md
        004-monitoring-and-alerting.md
        005-slos-slis-and-slas.md
        006-debugging-production-systems.md

      014-patterns/
        001-load-balancing-patterns.md
        002-caching-patterns.md
        003-database-scaling-patterns.md
        004-messaging-patterns.md
        005-reliability-patterns.md
        006-data-partitioning-patterns.md
        007-backpressure-patterns.md

    case-studies/
      001-url-shortener.md
      002-rate-limiter.md
      003-chat-system.md
      004-notification-system.md
      005-search-autocomplete.md
      006-news-feed.md
      007-web-crawler.md
      008-file-storage-system.md

    diagrams/
      README.md

    templates/
      system-design-question-template.md
      case-study-template.md
      concept-template.md
```

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