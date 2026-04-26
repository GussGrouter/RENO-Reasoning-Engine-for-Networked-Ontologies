# Systems Performance — distributed operating systems (3.5.4) (PDF pages 118–170)

## Source

- Title: *Systems Performance: Enterprise and the Cloud* (Second Edition)
- Author: Brendan Gregg
- Raw: `raw/code/pdf/Systems.Performance.Enterprise.and.the.Cloud.pdf`
- Batch scope: Chapter 3, Section 3.5.4 Distributed Operating Systems

## Processed artifacts

- Converted slice: `processed/code/systems-performance-distributed-operating-systems-3-5-4.md`
- Chunks:
  - `processed/code/systems-performance-distributed-operating-systems-3-5-4-chunk-000001.md`

## Extracted ideas (with classification)

- (abstraction) A “single OS image across nodes” model changes the unit of locality and failure domains compared to replicated independent OS instances behind load balancers.
- (diagnosis) Historical adoption constraints are mostly contextual; the performance-relevant comparison for practitioners is still whether the model changes measurement, debugging, and scaling bottlenecks versus common cloud patterns.

## Concepts reused / refined / created

- Reused (abstraction): [[kernel-architecture-models]]
- Reused (abstraction): [[resource-analysis-vs-workload-analysis]]

## Links

- Concepts:
  - [[kernel-architecture-models]]
  - [[resource-analysis-vs-workload-analysis]]
