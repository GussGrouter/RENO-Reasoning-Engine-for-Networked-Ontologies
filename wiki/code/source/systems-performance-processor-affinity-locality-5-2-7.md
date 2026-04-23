# Systems Performance — CPU affinity and memory locality (5.2.7) (Chapter 5 extract)

## Source

- Title: *Systems Performance: Enterprise and the Cloud* (Second Edition)
- Author: Brendan Gregg
- Raw: `raw/code/pdf/Systems.Performance.Enterprise.and.the.Cloud.pdf`
- Batch scope: Chapter 5, Section 5.2.7 Processor Binding (NUMA locality / affinity framing)

## Processed artifacts

- Converted slice: `processed/code/systems-performance-processor-affinity-locality-5-2-7.md`
- Chunks:
  - `processed/code/systems-performance-processor-affinity-locality-5-2-7-chunk-000001.md`

## Extracted ideas (with classification)

- (measurement) **Sticky execution** after I/O can improve **memory locality** (fewer remote NUMA accesses / warmer caches)—same principle as sticky sessions or data-local batching when **distance to state** dominates cycles.
- (abstraction) OS **affinity** defaults are an implicit optimizer; explicit binding is the escape hatch when defaults fight your placement goals—decision belongs with **topology-aware** capacity planning, not micro-tuning alone.

## Concepts reused / refined / created

- Reused (mechanism): [[caching]]
- Reused (measurement): [[throughput-latency-metrics]]
- Reused (structure): [[resource-vs-implementation-bottleneck]]
- Reused (mechanism): [[context-switching]]
- Reused: [[systems-performance]]

## Related sections

- [[systems-performance-cpu-binding-risks-and-performance-mantras-5-2-7-8]]

## Links

- Concepts:
  - [[caching]]
  - [[throughput-latency-metrics]]
  - [[resource-vs-implementation-bottleneck]]
  - [[context-switching]]
  - [[systems-performance]]
