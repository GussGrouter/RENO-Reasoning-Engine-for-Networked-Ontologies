# Systems Performance — terminology (2.1) (PDF pages 61–63)

## Source

- Title: *Systems Performance: Enterprise and the Cloud* (Second Edition)
- Author: Brendan Gregg
- Raw: `raw/code/pdf/Systems.Performance.Enterprise.and.the.Cloud.pdf`
- Batch scope: Chapter 2, Section 2.1 Terminology (key terms)

## Processed artifacts

- Converted slice: `processed/code/systems-performance-terminology-2-1.md`
- Chunks:
  - `processed/code/systems-performance-terminology-2-1-chunk-000001.md`

## Extracted ideas (with classification)

- (measurement) Distinguish workload rate metrics (IOPS, throughput) from time metrics (response time, latency) to avoid mismatched comparisons.
- (measurement) Response time includes both waiting and service time; “latency” can mean waiting time and is sometimes used ambiguously as total time, so definitions should be explicit.
- (diagnosis) Utilization (busy) and saturation (queued work) are distinct signals for diagnosing whether a resource is limiting performance.
- (diagnosis) A bottleneck is the resource that limits system performance; identifying and removing systemic bottlenecks is a central activity.
- (diagnosis) Workload is the applied input/load; understanding the workload is part of interpreting performance.
- (mechanism) Cache as a performance structure: a fast limited storage tier that avoids direct access to a slower tier.

## Concepts reused / refined / created

- Reused (measurement): [[throughput-latency-metrics]] (terminology anchors throughput/latency meanings).
- Created (diagnosis): [[utilization-and-saturation]]

## Links

- Concepts:
  - [[systems-performance]]
  - [[throughput-latency-metrics]]
  - [[utilization-and-saturation]]

