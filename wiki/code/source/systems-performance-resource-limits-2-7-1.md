# Systems Performance — resource limits (2.7.1) (PDF pages 108–116)

## Source

- Title: *Systems Performance: Enterprise and the Cloud* (Second Edition)
- Author: Brendan Gregg
- Raw: `raw/code/pdf/Systems.Performance.Enterprise.and.the.Cloud.pdf`
- Batch scope: Chapter 2, Section 2.7.1 Resource Limits

## Processed artifacts

- Converted slice: `processed/code/systems-performance-resource-limits-2-7-1.md`
- Chunks:
  - `processed/code/systems-performance-resource-limits-2-7-1-chunk-000001.md`

## Extracted ideas (with classification)

- (method) Find the resource that will bottleneck under load by measuring request rate and resource usage, expressing requests in resource terms, then extrapolating to known/experimental limits.
- (measurement) Use multiple data points over time (throughput vs utilization) to improve extrapolation accuracy.
- (diagnosis) Capacity predictions depend on peak patterns (averages can hide peaks); additional limits may appear before the extrapolated resource reaches 100%.

## Concepts reused / refined / created

- Created (method): [[resource-limits-method]]
- Reused (measurement): [[throughput-latency-metrics]] (request rate framing).
- Reused (diagnosis): [[utilization-and-saturation]] (utilization as proximity to limit).
- Reused (insight): [[model-classify-intervene]]

## Links

- Concepts:
  - [[resource-limits-method]]
  - [[throughput-latency-metrics]]
  - [[utilization-and-saturation]]
  - [[model-classify-intervene]]

