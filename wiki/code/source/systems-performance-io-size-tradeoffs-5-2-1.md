# Systems Performance — I/O size and per-operation overhead (5.2 + 5.2.1) (Chapter 5 extract)

## Source

- Title: *Systems Performance: Enterprise and the Cloud* (Second Edition)
- Author: Brendan Gregg
- Raw: `raw/code/pdf/Systems.Performance.Enterprise.and.the.Cloud.pdf`
- Batch scope: Chapter 5, Section 5.2 intro + Section 5.2.1 Selecting an I/O Size

## Processed artifacts

- Converted slice: `processed/code/systems-performance-io-size-tradeoffs-5-2-1.md`
- Chunks:
  - `processed/code/systems-performance-io-size-tradeoffs-5-2-1-chunk-000001.md`

## Extracted ideas (with classification)

- (mechanism) **Fixed per-I/O costs** (metadata, privilege checks, mapping, syscall transitions, buffer lifecycle) create an **amortization incentive**: larger transfers spread shared overhead across more payload bytes—same pattern as batching RPCs or log writes.
- (measurement) Mis-sized I/O can **amplify latency** and waste bandwidth/cache when requests are small/random—tuning transfer units is a [[throughput-latency-metrics]] coupling, not a one-direction “bigger is better” knob.

## Concepts reused / refined / created

- Reused (measurement): [[throughput-latency-metrics]]
- Reused (structure): [[resource-vs-implementation-bottleneck]]
- Reused (mechanism): [[system-call]]
- Reused (heuristic): [[shift-computation-in-time]]
- Reused: [[systems-performance]]

## Links

- Concepts:
  - [[throughput-latency-metrics]]
  - [[resource-vs-implementation-bottleneck]]
  - [[system-call]]
  - [[shift-computation-in-time]]
  - [[systems-performance]]
