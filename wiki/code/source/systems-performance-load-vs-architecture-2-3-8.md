# Systems Performance — load vs architecture (2.3.8) (PDF pages 68–72)

## Source

- Title: *Systems Performance: Enterprise and the Cloud* (Second Edition)
- Author: Brendan Gregg
- Raw: `raw/code/pdf/Systems.Performance.Enterprise.and.the.Cloud.pdf`
- Batch scope: Chapter 2, Section 2.3.8 Load vs. Architecture (queueing due to load vs inefficiency/constraints)

## Processed artifacts

- Converted slice: `processed/code/systems-performance-load-vs-architecture-2-3-8.md`
- Chunks:
  - `processed/code/systems-performance-load-vs-architecture-2-3-8-chunk-000001.md`

## Extracted ideas (with classification)

- (diagnosis) Poor performance can come from too much load (queueing/long latencies) or from architecture/implementation constraints; distinguishing them guides remedies (scale vs redesign).
- (diagnosis) Architecture examples include single-threaded limits and lock contention; load examples include all CPUs busy with queueing.
- (measurement) Queueing and latency under load are key evidence when deciding whether the issue is “load” rather than “architecture”.

## Concepts reused / refined / created

- Reused (diagnosis): [[resource-vs-implementation-bottleneck]] (a framing to separate capacity/resource limits from inefficient implementation).
- Reused (diagnosis): [[utilization-and-saturation]] (load manifests as saturation/queueing even before 100% utilization).

## Links

- Concepts:
  - [[systems-performance]]
  - [[resource-vs-implementation-bottleneck]]
  - [[utilization-and-saturation]]

