# Systems Performance — multimodal distributions (2.8.5) (PDF pages 110–120)

## Source

- Title: *Systems Performance: Enterprise and the Cloud* (Second Edition)
- Author: Brendan Gregg
- Raw: `raw/code/pdf/Systems.Performance.Enterprise.and.the.Cloud.pdf`
- Batch scope: Chapter 2, Section 2.8.5 Multimodal Distributions

## Processed artifacts

- Converted slice: `processed/code/systems-performance-multimodal-distributions-2-8-5.md`
- Chunks:
  - `processed/code/systems-performance-multimodal-distributions-2-8-5-chunk-000001.md`

## Extracted ideas (with classification)

- (diagnosis) Many statistics (mean, standard deviation, percentiles) assume unimodal/normal-like distributions; systems performance is often bimodal or multimodal.
- (diagnosis) Multimodality often comes from distinct paths/tier outcomes (fast vs slow path; cache hits vs misses; mixed workloads).
- (diagnosis) Average latency can be seriously misleading for multimodal distributions; always ask for the distribution (visualize it).

## Concepts reused / refined / created

- Created (diagnosis): [[multimodal-latency-distribution]]
- Reused (mechanism): [[caching]]
- Reused (structure): [[fast-path-slow-path]]
- Reused (measurement): [[latency-percentiles]]
- Reused (insight): [[model-classify-intervene]]

## Links

- Concepts:
  - [[multimodal-latency-distribution]]
  - [[caching]]
  - [[fast-path-slow-path]]
  - [[latency-percentiles]]
  - [[model-classify-intervene]]

