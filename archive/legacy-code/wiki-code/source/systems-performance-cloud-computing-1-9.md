# Systems Performance — cloud computing (1.9) (PDF pages 52–54)

## Source

- Title: *Systems Performance: Enterprise and the Cloud* (Second Edition)
- Author: Brendan Gregg
- Raw: `raw/code/pdf/Systems.Performance.Enterprise.and.the.Cloud.pdf`
- Batch scope: Chapter 1, Section 1.9 Cloud Computing (intro; tenant effects + observability constraints)

## Processed artifacts

- Converted slice: `processed/code/systems-performance-cloud-computing-1-9.md`
- Chunks:
  - `processed/code/systems-performance-cloud-computing-1-9-chunk-000001.md`

## Extracted ideas (with classification)

- (diagnosis) Cloud economics can make performance wins translate directly into cost reduction via fewer instances, changing the incentive for analysis.
- (diagnosis) Virtualization/tenancy introduces performance isolation issues (neighbor contention) that complicate root-cause attribution.
- (measurement) Tenant-visible observability may be incomplete (e.g., physical disk usage not observable), constraining diagnosis and increasing ambiguity.

## Concepts reused / refined / created

- Reused (diagnosis): [[cross-component-interactions]] (neighbor contention / multi-tenant effects are an interaction pattern).

## Links

- Concepts:
  - [[cross-component-interactions]]
  - [[counters-statistics-metrics]]

