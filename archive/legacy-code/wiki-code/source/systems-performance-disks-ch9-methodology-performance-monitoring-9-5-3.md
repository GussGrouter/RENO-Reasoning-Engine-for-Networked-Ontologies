# Systems Performance — Ch.9 §9.5.3 Performance monitoring (scout PDF 460–520)

## Source

- Title: *Systems Performance: Enterprise and the Cloud* (Second Edition)
- Scout: `processed/code/systems-performance-ch9-scout-p460-520.txt`
- Scope: **§9.5.3** rolling metrics + calibration

## Processed artifacts

- `processed/code/systems-performance-disks-ch9-methodology-performance-monitoring-9-5-3.md`

## Extracted ideas

- **Rolling util + response time** are **service dashboards**—pair with **distributions** for **multimodal** disks ([[time-series-monitoring]], [[metric-visualization]], [[multimodal-latency-distribution]], [[measurement-validity]]).

## Decision clarity

**Decision:** choose **heatmap/histogram panels** over **mean response time only** when **SLO language is tail-based** or **devices mix cache hits and misses**.

## Concepts reused / refined / created

- Reused: [[time-series-monitoring]], [[throughput-latency-metrics]], [[metric-visualization]], [[multimodal-latency-distribution]], [[measurement-validity]], [[micro-benchmarking]], [[systems-performance]]
- **Created:** none

## Links

- Concepts: [[time-series-monitoring]], [[throughput-latency-metrics]], [[metric-visualization]], [[multimodal-latency-distribution]], [[measurement-validity]], [[micro-benchmarking]], [[systems-performance]]
