# Systems Performance — standard deviation, percentiles, median (2.8.3) (PDF pages 110–120)

## Source

- Title: *Systems Performance: Enterprise and the Cloud* (Second Edition)
- Author: Brendan Gregg
- Raw: `raw/code/pdf/Systems.Performance.Enterprise.and.the.Cloud.pdf`
- Batch scope: Chapter 2, Section 2.8.3 Standard Deviation, Percentiles, Median

## Processed artifacts

- Converted slice: `processed/code/systems-performance-standard-deviation-percentiles-median-2-8-3.md`
- Chunks:
  - `processed/code/systems-performance-standard-deviation-percentiles-median-2-8-3-chunk-000001.md`

## Extracted ideas (with classification)

- (measurement) Standard deviation summarizes variance around the mean; higher values imply greater spread.
- (measurement) Percentiles locate points in the distribution (e.g., p99 includes 99% of values).
- (measurement) High percentiles (p90/p95/p99/p99.9) are used for latency monitoring and can be specified in SLAs/SLOs to capture tail performance.
- (measurement) p50 (median) shows the “bulk”/typical location and can differ materially from mean in skewed distributions.

## Concepts reused / refined / created

- Created (measurement): [[latency-percentiles]]
- Reused (measurement): [[throughput-latency-metrics]]
- Reused (measurement): [[counters-statistics-metrics]]

## Links

- Concepts:
  - [[latency-percentiles]]
  - [[throughput-latency-metrics]]
  - [[counters-statistics-metrics]]

