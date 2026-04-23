# Systems Performance — scalability (2.3.9) (PDF pages 70–75)

## Source

- Title: *Systems Performance: Enterprise and the Cloud* (Second Edition)
- Author: Brendan Gregg
- Raw: `raw/code/pdf/Systems.Performance.Enterprise.and.the.Cloud.pdf`
- Batch scope: Chapter 2, Section 2.3.9 Scalability (throughput vs load; knee point; degradation)

## Processed artifacts

- Converted slice: `processed/code/systems-performance-scalability-2-3-9.md`
- Chunks:
  - `processed/code/systems-performance-scalability-2-3-9-chunk-000001.md`

## Extracted ideas (with classification)

- (measurement) Scalability is performance under increasing load; throughput vs load curves reveal scaling regimes.
- (diagnosis) A knee point marks departure from linear scalability as contention increases; beyond it, overheads can reduce completed work and decrease throughput.
- (diagnosis) Throughput degradation often correlates with rising response time/latency; saturation and queueing can begin as utilization approaches 100%.
- (mechanism) Contention/coherency overhead and increased context switching under high thread counts can consume resources and reduce useful work.
- (diagnosis) Different resources exhibit different degradation profiles (e.g., “fast” degradation for memory pressure/pageout, disk queueing; “slow” for CPU load).

## Concepts reused / refined / created

- Reused (measurement): [[throughput-latency-metrics]]
- Reused (diagnosis): [[utilization-and-saturation]]
- Created (diagnosis): [[scalability-knee-point]]

## Links

- Concepts:
  - [[throughput-latency-metrics]]
  - [[utilization-and-saturation]]
  - [[scalability-knee-point]]

