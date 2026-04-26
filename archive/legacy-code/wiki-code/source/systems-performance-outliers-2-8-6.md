# Systems Performance — outliers (2.8.6) (PDF pages 110–120)

## Source

- Title: *Systems Performance: Enterprise and the Cloud* (Second Edition)
- Author: Brendan Gregg
- Raw: `raw/code/pdf/Systems.Performance.Enterprise.and.the.Cloud.pdf`
- Batch scope: Chapter 2, Section 2.8.6 Outliers

## Processed artifacts

- Converted slice: `processed/code/systems-performance-outliers-2-8-6.md`
- Chunks:
  - `processed/code/systems-performance-outliers-2-8-6-chunk-000001.md`

## Extracted ideas (with classification)

- (diagnosis) Outliers are rare extreme values that do not fit the expected distribution (unimodal or multimodal).
- (diagnosis) Latency outliers can dominate performance while being invisible to many summary metrics except extremes (e.g., max).
- (measurement) Median may be more stable than mean under outliers; standard deviation and high percentiles can help detect outliers depending on frequency.
- (method) Inspect full distributions (e.g., histograms) to understand multimodality and outliers; visualization helps.

## Concepts reused / refined / created

- Created (diagnosis): [[latency-outliers]]
- Reused (diagnosis): [[multimodal-latency-distribution]]
- Reused (measurement): [[latency-percentiles]]
- Reused (method): [[metric-visualization]]

## Links

- Concepts:
  - [[latency-outliers]]
  - [[multimodal-latency-distribution]]
  - [[latency-percentiles]]
  - [[metric-visualization]]
