# Systems Performance — Kernel scheduler: time sharing, preemption, load balance (6.4.2) (PDF ~231–285)

## Source

- Title: *Systems Performance: Enterprise and the Cloud* (Second Edition)
- Author: Brendan Gregg
- Raw: `raw/code/pdf/Systems.Performance.Enterprise.and.the.Cloud.pdf`
- Batch scope: Chapter 6, Section 6.4.2 — **Scheduler** overview (portable functions) plus Linux implementation notes and **migration vs cache warmth** tradeoff

## Processed artifacts

- Converted slice: `processed/code/systems-performance-cpu-kernel-scheduler-functions-and-locality-6-4-2.md`
- Chunks:
  - `processed/code/systems-performance-cpu-kernel-scheduler-functions-and-locality-6-4-2-chunk-000001.md`

## Extracted ideas (with classification)

- (mechanism) **Three scheduler responsibilities** recur across kernels: **time sharing**, **preemption of runnable higher priority**, and **load balancing** across CPUs—latency under load is often “where runnable waits” plus “how often you migrate” ([[process-abstraction]], [[throughput-latency-metrics]]).
- (abstraction) **Mental model vs data structure**: “run queue” is the **operational picture** even when the implementation is a **tree keyed by virtual runtime**—debugging requires both views ([[measurement-validity]]).
- (diagnosis) **Migration cost tradeoff**: kernels **suppress moves** when **cache warmth** likely beats **idle CPU elsewhere**—symptoms can look like **uneven utilization** while improving tail latency ([[caching]], [[cross-component-interactions]]).

## Application validation

- **Container on NUMA node “wrong” socket**: forced rebalance can improve **mean CPU** but hurt **p99** if hot caches are abandoned—measure **migrations + LLC MPKI** together.

## Decision clarity

- **Decision**: choose **explicit CPU affinity / topology hints** over **global rebalance defaults** when **working-set locality** is proven and **latency SLO** dominates average utilization.

## Concepts reused / refined / created

- Reused (abstraction): [[process-abstraction]]
- Reused (structure): [[throughput-latency-metrics]]
- Reused (abstraction): [[measurement-validity]]
- Reused (mechanism): [[caching]]
- Reused (structure): [[cross-component-interactions]]
- Reused (mechanism): [[context-switching]]
- Reused: [[systems-performance]]

## Links

- Concepts:
  - [[process-abstraction]]
  - [[throughput-latency-metrics]]
  - [[measurement-validity]]
  - [[caching]]
  - [[cross-component-interactions]]
  - [[context-switching]]
  - [[systems-performance]]
- Related sources:
  - [[systems-performance-cpu-heterogeneous-accelerators-observability-6-4-1]]
  - [[systems-performance-cpu-scheduling-classes-policies-workload-shape-6-4-2]]
  - [[systems-performance-cpu-models-run-queues-scheduler-latency-6-2-3]]
