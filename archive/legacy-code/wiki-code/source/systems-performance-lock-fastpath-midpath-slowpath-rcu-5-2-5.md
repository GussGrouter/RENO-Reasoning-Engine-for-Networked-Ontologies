# Systems Performance — lock acquisition paths and RCU-style read scaling (5.2.5 part) (Chapter 5 extract)

## Source

- Title: *Systems Performance: Enterprise and the Cloud* (Second Edition)
- Author: Brendan Gregg
- Raw: `raw/code/pdf/Systems.Performance.Enterprise.and.the.Cloud.pdf`
- Batch scope: Chapter 5, Section 5.2.5 (mutex fast/mid/slow paths + RCU read-mostly pattern + developer ownership note)

## Processed artifacts

- Converted slice: `processed/code/systems-performance-lock-fastpath-midpath-slowpath-rcu-5-2-5.md`
- Chunks:
  - `processed/code/systems-performance-lock-fastpath-midpath-slowpath-rcu-5-2-5-chunk-000001.md`

## Extracted ideas (with classification)

- (structure) **Hybrid mutex paths** mirror generic **fast vs slow path** engineering: try cheap atomic success, **optimistically spin** only while the holder is actively running, then fall back to **blocking** when probability of quick release is low ([[fast-path-slow-path]]).
- (mechanism) **RCU-class read-mostly schemes** shift **read hot paths** away from lock acquisition by versioning updates—same decision pattern as **read-heavy** systems using immutable snapshots / double buffering in application layers.
- (diagnosis) Lock-heavy regressions often need **source-level** reasoning (who orders locks, which invariants are assumed)—performance ownership lands with the team that can change invariants, not only ops metrics.

## Concepts reused / refined / created

- Reused (structure): [[fast-path-slow-path]]
- Reused (measurement): [[throughput-latency-metrics]]
- Reused (structure): [[resource-vs-implementation-bottleneck]]
- Reused (heuristic): [[drill-down-analysis]]
- Reused: [[systems-performance]]

## Links

- Concepts:
  - [[fast-path-slow-path]]
  - [[throughput-latency-metrics]]
  - [[resource-vs-implementation-bottleneck]]
  - [[drill-down-analysis]]
  - [[systems-performance]]
