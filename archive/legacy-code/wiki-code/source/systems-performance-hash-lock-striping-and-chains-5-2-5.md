# Systems Performance — lock striping via hash buckets and chain risks (5.2.5 part) (Chapter 5 extract)

## Source

- Title: *Systems Performance: Enterprise and the Cloud* (Second Edition)
- Author: Brendan Gregg
- Raw: `raw/code/pdf/Systems.Performance.Enterprise.and.the.Cloud.pdf`
- Batch scope: Chapter 5, Section 5.2.5 (hash table of locks: global vs per-object vs striped tradeoff + collision chains)

## Processed artifacts

- Converted slice: `processed/code/systems-performance-hash-lock-striping-and-chains-5-2-5.md`
- Chunks:
  - `processed/code/systems-performance-hash-lock-striping-and-chains-5-2-5-chunk-000001.md`

## Extracted ideas (with classification)

- (abstraction) **Lock granularity trilemma**: one big lock simplifies reasoning but **serializes** unrelated work; per-object locks minimize false contention but add **space/lifecycle** overhead; **striping** hashes objects to a fixed lock set—classic partition-for-contention pattern mirrored in sharded services.
- (diagnosis) **Skewed chains** under a bucket reintroduce serialization: long protected walks mean hold times dominate—validate **distribution** under production keys/addresses, not only “we have many buckets.”

## Concepts reused / refined / created

- Reused (structure): [[resource-vs-implementation-bottleneck]]
- Reused (measurement): [[throughput-latency-metrics]]
- Reused (heuristic): [[optimize-expected-case]]
- Reused (diagnosis): [[known-unknowns-framework]]
- Reused: [[systems-performance]]

## Links

- Concepts:
  - [[resource-vs-implementation-bottleneck]]
  - [[throughput-latency-metrics]]
  - [[optimize-expected-case]]
  - [[known-unknowns-framework]]
  - [[systems-performance]]
