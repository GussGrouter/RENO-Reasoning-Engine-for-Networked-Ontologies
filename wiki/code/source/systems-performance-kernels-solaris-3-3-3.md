# Systems Performance — Solaris kernel developments (3.3.3) (PDF pages 118–170)

## Source

- Title: *Systems Performance: Enterprise and the Cloud* (Second Edition)
- Author: Brendan Gregg
- Raw: `raw/code/pdf/Systems.Performance.Enterprise.and.the.Cloud.pdf`
- Batch scope: Chapter 3, Section 3.3.3 Solaris

## Processed artifacts

- Converted slice: `processed/code/systems-performance-kernels-solaris-3-3-3.md`
- Chunks:
  - `processed/code/systems-performance-kernels-solaris-3-3-3-chunk-000001.md`

## Extracted ideas (with classification)

- (abstraction) A virtual file system layer is an interface strategy to host multiple filesystems concurrently (coexistence vs “one monolithic FS implementation”).
- (mechanism) Kernel preemption and early SMP support change scheduling/latency tradeoffs for mixed-priority workloads on multiprocessors.
- (mechanism) Slab-style kernel allocators trade memory for allocator fast-path performance via reuse of fixed-size objects.
- (measurement) Deep production observability (historically DTrace-shaped) is an evidence strategy: preserve per-event detail across the stack rather than relying only on coarse counters.

## Concepts reused / refined / created

- Reused (abstraction): [[kernel-architecture-models]]
- Reused (mechanism): [[context-switching]]
- Reused (structure): [[resource-vs-implementation-bottleneck]]
- Reused (measurement): [[event-tracing]]
- Reused (mechanism): [[extended-bpf]]

## Links

- Concepts:
  - [[kernel-architecture-models]]
  - [[context-switching]]
  - [[resource-vs-implementation-bottleneck]]
  - [[event-tracing]]
  - [[extended-bpf]]
