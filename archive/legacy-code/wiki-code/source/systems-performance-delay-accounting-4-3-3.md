# Systems Performance — delay accounting (4.3.3) (PDF pages 171–220)

## Source

- Title: *Systems Performance: Enterprise and the Cloud* (Second Edition)
- Author: Brendan Gregg
- Raw: `raw/code/pdf/Systems.Performance.Enterprise.and.the.Cloud.pdf`
- Batch scope: Chapter 4, Section 4.3.3 Delay Accounting

## Processed artifacts

- Converted slice: `processed/code/systems-performance-delay-accounting-4-3-3.md`
- Chunks:
  - `processed/code/systems-performance-delay-accounting-4-3-3-chunk-000001.md`

## Extracted ideas (with classification)

- (measurement) Delay accounting decomposes per-task time spent waiting in a few canonical **stall buckets** (scheduler, block I/O, swap pressure, memory reclaim), turning “slow” into a structured attribution signal.
- (diagnosis) The value is in **where waiting accumulates** across subsystems, not in the feature name—this supports narrowing from “CPU looks busy” to “tasks are actually off-CPU waiting for X.”

## Concepts reused / refined / created

- Reused (structure): [[throughput-latency-metrics]]
- Reused (structure): [[utilization-and-saturation]]
- Reused: [[latency-analysis]]
- Reused (measurement): [[counters-statistics-metrics]]
- Reused: [[systems-performance]]

## Links

- Concepts:
  - [[throughput-latency-metrics]]
  - [[utilization-and-saturation]]
  - [[latency-analysis]]
  - [[counters-statistics-metrics]]
  - [[systems-performance]]
