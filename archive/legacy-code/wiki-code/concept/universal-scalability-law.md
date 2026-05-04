# Universal scalability law

- Tag: abstraction

## Definition

The **universal scalability law (USL)** extends Amdahl-style contention modeling with a coherency term:

\[
C(N) = \\frac{N}{1 + \\alpha (N - 1) + \\beta N (N - 1)}
\]

where \(\\alpha\) captures contention/seriality and \(\\beta\) captures coherency delay. When \(\\beta = 0\), USL reduces to [[amdahls-law-of-scalability]].

## Relation

- Role: framework (a scalability model that includes coherency effects).
- Used with measured scaling data to estimate parameters and compare prediction vs reality.
- Supports [[model-classify-intervene]] by distinguishing contention-dominated vs coherence-dominated scaling limits before selecting interventions.

## Links

- Source: [[systems-performance-universal-scalability-law-2-6-4]]
- Source: [[systems-performance-algorithm-complexity-scaling-5-1-4]]
- Source: [[systems-performance-cpus-chapter-intro-and-parts-6]]
- Source: [[systems-performance-cpu-multiprocess-multithreading-tradeoffs-6-3-13]]
- Source: [[systems-performance-cpu-parallelism-footprint-and-word-size-6-3-14]]
- Source: [[systems-performance-cpu-on-chip-cache-hierarchy-and-llc-6-4-1]]
- Source: [[systems-performance-cpu-interconnect-scalability-memory-system-6-4-1]]
- Source: [[systems-performance-cpu-scheduling-classes-policies-workload-shape-6-4-2]]
- Source: [[systems-performance-cpu-micro-benchmarking-decision-rules-6-5-11]]
- Related concepts:
  - [[amdahls-law-of-scalability]]
  - [[micro-benchmarking]]
  - [[model-classify-intervene]]

