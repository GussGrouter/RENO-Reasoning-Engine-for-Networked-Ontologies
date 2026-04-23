# Systems Performance — CPU models: topology and caches (6.2.1–6.2.2) (PDF ~231–285)

## Source

- Title: *Systems Performance: Enterprise and the Cloud* (Second Edition)
- Author: Brendan Gregg
- Raw: `raw/code/pdf/Systems.Performance.Enterprise.and.the.Cloud.pdf`
- Batch scope: Chapter 6, Section 6.2 Models — CPU architecture (logical CPUs from hardware threads) and CPU memory caches (size/speed tradeoff ladder)

## Processed artifacts

- Converted slice: `processed/code/systems-performance-cpu-models-architecture-and-caches-6-2-1-2.md`
- Chunks:
  - `processed/code/systems-performance-cpu-models-architecture-and-caches-6-2-1-2-chunk-000001.md`

## Extracted ideas (with classification)

- (abstraction) **Topology-aware scheduling** uses knowledge of **shared caches and sibling threads** to pick runnable CPUs—performance is not independent of *where* a thread runs ([[caching]], [[context-switching]]).
- (mechanism) **Cache hierarchy** trades **capacity vs proximity**: closer caches are faster but smaller—later “memory wall” symptoms should be read through this ladder, not as random noise ([[caching]], [[throughput-latency-metrics]]).
- (abstraction) OS view of “many CPUs” may be **hardware threads** on fewer cores—parallelism ceilings and coherency costs depend on physical packaging ([[universal-scalability-law]], [[resource-vs-implementation-bottleneck]]).

## Application validation

- **NUMA later, caches now**: when debating “add cores,” check whether threads are already **sibling-packed** on SMT pairs—vertical scale may not add independent execution units.

## Concepts reused / refined / created

- Reused (mechanism): [[caching]]
- Reused (mechanism): [[context-switching]]
- Reused (structure): [[throughput-latency-metrics]]
- Reused (abstraction): [[universal-scalability-law]]
- Reused (structure): [[resource-vs-implementation-bottleneck]]
- Reused: [[systems-performance]]

## Links

- Concepts:
  - [[caching]]
  - [[context-switching]]
  - [[throughput-latency-metrics]]
  - [[universal-scalability-law]]
  - [[resource-vs-implementation-bottleneck]]
  - [[systems-performance]]
- Related sources:
  - [[systems-performance-cpu-terminology-6-1]]
  - [[systems-performance-cpu-models-run-queues-scheduler-latency-6-2-3]]
