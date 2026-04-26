# Systems Performance — algorithmic scaling / Big O framing (5.1.4) (Chapter 5 extract)

## Source

- Title: *Systems Performance: Enterprise and the Cloud* (Second Edition)
- Author: Brendan Gregg
- Raw: `raw/code/pdf/Systems.Performance.Enterprise.and.the.Cloud.pdf`
- Batch scope: Chapter 5, Section 5.1.4 Big O Notation (growth rates, scale pathologies, constants at small n)

## Processed artifacts

- Converted slice: `processed/code/systems-performance-algorithm-complexity-scaling-5-1-4.md`
- Chunks:
  - `processed/code/systems-performance-algorithm-complexity-scaling-5-1-4-chunk-000001.md`

## Extracted ideas (with classification)

- (abstraction) **Asymptotic growth** predicts which parts of logic become dominant as inputs/users/data grow—failure mode is “fine in the lab, catastrophic at fleet scale” when \(n\) crosses a knee in the curve.
- (diagnosis) Remedies are **algorithm replacement** or **partitioning/sharding** the population so effective \(n\) per unit of work stays bounded—same structural move as resharding hot tenants in distributed storage.
- (measurement) Big-O ignores **leading constants**; for small \(n\), constant factors and hardware realities can dominate—do not let asymptotic reasoning override measured profiles on current sizes.

## Concepts reused / refined / created

- Reused (structure): [[resource-vs-implementation-bottleneck]]
- Reused (abstraction): [[amdahls-law-of-scalability]]
- Reused (abstraction): [[universal-scalability-law]]
- Reused (measurement): [[throughput-latency-metrics]]
- Reused: [[systems-performance]]

## Links

- Concepts:
  - [[resource-vs-implementation-bottleneck]]
  - [[amdahls-law-of-scalability]]
  - [[universal-scalability-law]]
  - [[throughput-latency-metrics]]
  - [[systems-performance]]
