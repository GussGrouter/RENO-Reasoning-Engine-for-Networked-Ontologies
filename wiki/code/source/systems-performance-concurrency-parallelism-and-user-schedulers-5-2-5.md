# Systems Performance — concurrency vs parallelism and user-level schedulers (5.2.5 part) (Chapter 5 extract)

## Source

- Title: *Systems Performance: Enterprise and the Cloud* (Second Edition)
- Author: Brendan Gregg
- Raw: `raw/code/pdf/Systems.Performance.Enterprise.and.the.Cloud.pdf`
- Batch scope: Chapter 5, Section 5.2.5 opening (through user-level concurrency models and hybrid runtime example)

## Processed artifacts

- Converted slice: `processed/code/systems-performance-concurrency-parallelism-and-user-schedulers-5-2-5.md`
- Chunks:
  - `processed/code/systems-performance-concurrency-parallelism-and-user-schedulers-5-2-5-chunk-000001.md`

## Extracted ideas (with classification)

- (abstraction) **Concurrency vs parallelism**: overlapping lifetimes is not the same as simultaneous CPU execution—true speedup on multicore requires schedulable units the OS can place on different CPUs ([[process-abstraction]]).
- (mechanism) **User-level schedulers** (fibers/co-routines/event queues) trade **kernel scheduler involvement** for **application-controlled** interleaving; I/O still crosses [[kernel-user-boundary]], so OS threads often remain part of the story.
- (diagnosis) **Hybrid runtimes** split “cheap concurrency” from “hardware parallelism” by migrating work off threads that block—same structural pattern as sharding work away from saturated executors in distributed systems.

## Concepts reused / refined / created

- Reused (abstraction): [[process-abstraction]]
- Reused (mechanism): [[context-switching]]
- Reused (structure): [[kernel-user-boundary]]
- Reused (measurement): [[throughput-latency-metrics]]
- Reused: [[systems-performance]]

## Links

- Concepts:
  - [[process-abstraction]]
  - [[context-switching]]
  - [[kernel-user-boundary]]
  - [[throughput-latency-metrics]]
  - [[systems-performance]]
