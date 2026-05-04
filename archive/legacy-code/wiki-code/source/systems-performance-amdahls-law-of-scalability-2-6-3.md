# Systems Performance — Amdahl's law of scalability (2.6.3) (PDF pages 98–114)

## Source

- Title: *Systems Performance: Enterprise and the Cloud* (Second Edition)
- Author: Brendan Gregg
- Raw: `raw/code/pdf/Systems.Performance.Enterprise.and.the.Cloud.pdf`
- Batch scope: Chapter 2, Section 2.6.3 Amdahl’s Law of Scalability

## Processed artifacts

- Converted slice: `processed/code/systems-performance-amdahls-law-of-scalability-2-6-3.md`
- Chunks:
  - `processed/code/systems-performance-amdahls-law-of-scalability-2-6-3-chunk-000001.md`

## Extracted ideas (with classification)

- (framework) Amdahl’s law models scalability with a serial fraction/contended component (parameter \(\\alpha\)), explaining deviation from linear scaling.
- (method) Apply it by collecting scaling data across \(N\), fitting \(\\alpha\) via regression, and plotting model vs data to predict scaling and inspect deviations.
- (diagnosis) Differences between model and data can indicate either model misunderstanding or real system behaviors not captured by the model.

## Concepts reused / refined / created

- Created (framework): [[amdahls-law-of-scalability]]
- Reused (method): [[micro-benchmarking]] (data collection across \(N\)).
- Reused (technique): [[latency-analysis]] (conceptual “decompose then pursue the larger contributor” is analogous to attributing limiting components, without forcing equivalence).
- Reused (insight): [[model-classify-intervene]]

## Links

- Concepts:
  - [[amdahls-law-of-scalability]]
  - [[micro-benchmarking]]
  - [[latency-analysis]]
  - [[model-classify-intervene]]

