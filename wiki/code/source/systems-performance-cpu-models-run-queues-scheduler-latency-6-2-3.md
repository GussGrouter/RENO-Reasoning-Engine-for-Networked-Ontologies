# Systems Performance — CPU models: run queues, affinity, scheduler latency (6.2.3) (PDF ~231–285)

## Source

- Title: *Systems Performance: Enterprise and the Cloud* (Second Edition)
- Author: Brendan Gregg
- Raw: `raw/code/pdf/Systems.Performance.Enterprise.and.the.Cloud.pdf`
- Batch scope: Chapter 6, Section 6.2.3 CPU Run Queues (scheduler latency, per-CPU queues, cache warmth, CPU affinity, NUMA locality vs global queue locking)

## Processed artifacts

- Converted slice: `processed/code/systems-performance-cpu-models-run-queues-scheduler-latency-6-2-3.md`
- Chunks:
  - `processed/code/systems-performance-cpu-models-run-queues-scheduler-latency-6-2-3-chunk-000001.md`

## Extracted ideas (with classification)

- (structure) **Runnable depth** on a CPU is **saturation signal** for compute: threads ready but not running implies **scheduler latency** cost to throughput and tail latency ([[utilization-and-saturation]], [[throughput-latency-metrics]]).
- (mechanism) **Per-CPU run queues** trade **migration flexibility** for **cache warmth and NUMA locality**, and avoid a **global queue mutex** that would serialize scaling ([[context-switching]], [[cross-component-interactions]]).
- (abstraction) **CPU affinity** is a deliberate **pin-threads-to-where-data-warmed** policy—not the same thing as “never move threads,” but a response to memory hierarchy economics ([[caching]]).

## Application validation

- **Latency tail on a NUMA host**: if runnable depth is low but migrations are high, test **sticky scheduling** before buying faster cores—queue latency may be cache/NUMA cold-start, not GHz.

## Decision clarity

- **Decision**: choose **per-CPU queue locality (affinity-aware placement)** over **frequent cross-socket migration** when profiles show hot data resident to a node and scheduler latency tracks migration rate.

## Concepts reused / refined / created

- Reused (structure): [[utilization-and-saturation]]
- Reused (structure): [[throughput-latency-metrics]]
- Reused (mechanism): [[context-switching]]
- Reused (structure): [[cross-component-interactions]]
- Reused (mechanism): [[caching]]
- Reused: [[systems-performance]]

## Links

- Concepts:
  - [[utilization-and-saturation]]
  - [[throughput-latency-metrics]]
  - [[context-switching]]
  - [[cross-component-interactions]]
  - [[caching]]
  - [[systems-performance]]
- Related sources:
  - [[systems-performance-cpu-models-architecture-and-caches-6-2-1-2]]
  - [[systems-performance-cpu-concepts-clock-rate-and-stalls-6-3-1]]
  - [[systems-performance-processor-affinity-locality-5-2-7]]