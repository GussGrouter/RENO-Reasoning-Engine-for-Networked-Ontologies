# Systems Performance — bucket count vs CPUs and false sharing on locks (5.2.5 part) (Chapter 5 extract)

## Source

- Title: *Systems Performance: Enterprise and the Cloud* (Second Edition)
- Author: Brendan Gregg
- Raw: `raw/code/pdf/Systems.Performance.Enterprise.and.the.Cloud.pdf`
- Batch scope: Chapter 5, Section 5.2.5 (parallelism potential of bucket count + false sharing on adjacent locks)

## Processed artifacts

- Converted slice: `processed/code/systems-performance-lock-scaling-and-false-sharing-5-2-5.md`
- Chunks:
  - `processed/code/systems-performance-lock-scaling-and-false-sharing-5-2-5-chunk-000001.md`

## Extracted ideas (with classification)

- (measurement) **Parallelism ceiling**: when striping locks, bucket count below CPU count can cap speedup even if contention per bucket is low—same “not enough shards” failure mode as under-partitioned data planes.
- (mechanism) **False sharing**: logically independent locks that share a **cache line** generate coherency traffic—micro-layout becomes a **serialization mechanism** despite correct fine-grained locking; padding trades **memory** for **independence** ([[time-space-tradeoff]]).

## Concepts reused / refined / created

- Reused (structure): [[resource-vs-implementation-bottleneck]]
- Reused (abstraction): [[time-space-tradeoff]]
- Reused (measurement): [[throughput-latency-metrics]]
- Reused: [[systems-performance]]

## Links

- Concepts:
  - [[resource-vs-implementation-bottleneck]]
  - [[time-space-tradeoff]]
  - [[throughput-latency-metrics]]
  - [[systems-performance]]
