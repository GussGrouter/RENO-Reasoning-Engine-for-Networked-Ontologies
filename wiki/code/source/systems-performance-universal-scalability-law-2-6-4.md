# Systems Performance — universal scalability law (2.6.4) (PDF pages 98–114)

## Source

- Title: *Systems Performance: Enterprise and the Cloud* (Second Edition)
- Author: Brendan Gregg
- Raw: `raw/code/pdf/Systems.Performance.Enterprise.and.the.Cloud.pdf`
- Batch scope: Chapter 2, Section 2.6.4 Universal Scalability Law

## Processed artifacts

- Converted slice: `processed/code/systems-performance-universal-scalability-law-2-6-4.md`
- Chunks:
  - `processed/code/systems-performance-universal-scalability-law-2-6-4-chunk-000001.md`

## Extracted ideas (with classification)

- (framework) USL extends Amdahl-style contention modeling with a coherency delay parameter \(\\beta\); when \(\\beta = 0\), it becomes Amdahl’s law.
- (diagnosis) It explains coherence-dominated scalability profiles where synchronization/propagation overhead outweighs scaling benefits.
- (method) Use measured scaling data to fit parameters and validate with held-out data points (prediction vs reality).

## Concepts reused / refined / created

- Created (framework): [[universal-scalability-law]]
- Reused (framework): [[amdahls-law-of-scalability]]
- Reused (method): [[micro-benchmarking]]
- Reused (insight): [[model-classify-intervene]]

## Links

- Concepts:
  - [[universal-scalability-law]]
  - [[amdahls-law-of-scalability]]
  - [[micro-benchmarking]]
  - [[model-classify-intervene]]

