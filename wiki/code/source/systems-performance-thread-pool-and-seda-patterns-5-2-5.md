# Systems Performance — service pools, CPU pools, and staged pipelines (5.2.5 part) (Chapter 5 extract)

## Source

- Title: *Systems Performance: Enterprise and the Cloud* (Second Edition)
- Author: Brendan Gregg
- Raw: `raw/code/pdf/Systems.Performance.Enterprise.and.the.Cloud.pdf`
- Batch scope: Chapter 5, Section 5.2.5 (common multithreaded architecture patterns + footnotes on fiber hazards)

## Processed artifacts

- Converted slice: `processed/code/systems-performance-thread-pool-and-seda-patterns-5-2-5.md`
- Chunks:
  - `processed/code/systems-performance-thread-pool-and-seda-patterns-5-2-5-chunk-000001.md`

## Extracted ideas (with classification)

- (abstraction) **Service thread pool** vs **CPU thread pool** vs **staged (SEDA-style) pipelines** are three different **load-shaping** shapes: connection-centric isolation, throughput-oriented partition-by-CPU, and assembly-line decoupling—pick based on dominant contention (I/O vs CPU vs queue handoffs).
- (diagnosis) **Footgun class**: user-mode fibers can violate assumptions baked into “thread” APIs (TLS lifetime, teardown semantics)—a portability and correctness constraint that also affects performance investigations.

## Concepts reused / refined / created

- Reused (abstraction): [[resource-vs-implementation-bottleneck]]
- Reused (measurement): [[throughput-latency-metrics]]
- Reused (heuristic): [[optimize-expected-case]]
- Reused (abstraction): [[process-abstraction]]
- Reused: [[systems-performance]]

## Links

- Concepts:
  - [[resource-vs-implementation-bottleneck]]
  - [[throughput-latency-metrics]]
  - [[optimize-expected-case]]
  - [[process-abstraction]]
  - [[systems-performance]]
