# Systems Performance — when to stop analysis (2.3.6) (PDF pages 68–72)

## Source

- Title: *Systems Performance: Enterprise and the Cloud* (Second Edition)
- Author: Brendan Gregg
- Raw: `raw/code/pdf/Systems.Performance.Enterprise.and.the.Cloud.pdf`
- Batch scope: Chapter 2, Section 2.3.6 When to Stop Analysis (stopping criteria/ROI)

## Processed artifacts

- Converted slice: `processed/code/systems-performance-when-to-stop-analysis-2-3-6.md`
- Chunks:
  - `processed/code/systems-performance-when-to-stop-analysis-2-3-6-chunk-000001.md`

## Extracted ideas (with classification)

- (diagnosis) Stopping analysis is a decision: “found enough to explain the bulk of the problem” is a practical stopping criterion.
- (diagnosis) ROI matters: analysis effort should be bounded by potential benefit (and by higher-priority issues elsewhere).
- (measurement) Quantifying contribution (e.g., percent of CPU footprint) helps decide whether an identified cause is sufficient to explain observed slowdown.

## Concepts reused / refined / created

- Reused (diagnosis): [[utilization-and-saturation]] (quantification and thresholds depend on understanding utilization/saturation signals in practice).
- Reused (diagnosis): [[throughput-latency-metrics]] (quantification is often expressed in time/latency or time spent).

## Links

- Concepts:
  - [[systems-performance]]
  - [[utilization-and-saturation]]
  - [[throughput-latency-metrics]]

