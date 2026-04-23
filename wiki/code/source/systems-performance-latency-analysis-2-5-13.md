# Systems Performance — latency analysis (2.5.13) (PDF pages 92–98)

## Source

- Title: *Systems Performance: Enterprise and the Cloud* (Second Edition)
- Author: Brendan Gregg
- Raw: `raw/code/pdf/Systems.Performance.Enterprise.and.the.Cloud.pdf`
- Batch scope: Chapter 2, Section 2.5.13 Latency Analysis

## Processed artifacts

- Converted slice: `processed/code/systems-performance-latency-analysis-2-5-13.md`
- Chunks:
  - `processed/code/systems-performance-latency-analysis-2-5-13-chunk-000001.md`

## Extracted ideas (with classification)

- (diagnosis) Latency analysis decomposes an operation’s time into components and repeatedly subdivides the highest-latency component to identify and quantify root cause.
- (diagnosis) Analysis can drill down across layers (application → libraries → syscalls → kernel → drivers).
- (abstraction) A common procedure is repeatedly splitting latency into two parts and pursuing the slower part (a “binary search of latency”).

## Concepts reused / refined / created

- Created (method): [[latency-analysis]]
- Reused (measurement): [[throughput-latency-metrics]]
- Reused (cycle): [[diagnosis-cycle]]
- Reused (insight): [[model-classify-intervene]]

## Links

- Concepts:
  - [[latency-analysis]]
  - [[throughput-latency-metrics]]
  - [[diagnosis-cycle]]
  - [[model-classify-intervene]]

