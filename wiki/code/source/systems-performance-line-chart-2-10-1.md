# Systems Performance — line chart (2.10.1) (PDF pages 110–120)

## Source

- Title: *Systems Performance: Enterprise and the Cloud* (Second Edition)
- Author: Brendan Gregg
- Raw: `raw/code/pdf/Systems.Performance.Enterprise.and.the.Cloud.pdf`
- Batch scope: Chapter 2, Section 2.10.1 Line Chart

## Processed artifacts

- Converted slice: `processed/code/systems-performance-line-chart-2-10-1.md`
- Chunks:
  - `processed/code/systems-performance-line-chart-2-10-1-chunk-000001.md`

## Extracted ideas (with classification)

- (method) Line charts plot metrics over time (time on x-axis), useful for trends and comparing multiple series on shared axes.
- (diagnosis) Plotting distribution summaries (median, stddev, percentiles) over time can explain misleading averages (e.g., average latency high due to tail while median is low).

## Concepts reused / refined / created

- Reused (method): [[metric-visualization]]
- Reused (measurement): [[latency-percentiles]]
- Reused (diagnosis): [[latency-outliers]]

## Links

- Concepts:
  - [[metric-visualization]]
  - [[latency-percentiles]]
  - [[latency-outliers]]
