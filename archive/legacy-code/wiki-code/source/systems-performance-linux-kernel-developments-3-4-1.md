# Systems Performance — Linux kernel developments (3.4.1) (PDF pages 118–170)

## Source

- Title: *Systems Performance: Enterprise and the Cloud* (Second Edition)
- Author: Brendan Gregg
- Raw: `raw/code/pdf/Systems.Performance.Enterprise.and.the.Cloud.pdf`
- Batch scope: Chapter 3, Section 3.4.1 Linux Kernel Developments

## Processed artifacts

- Converted slice: `processed/code/systems-performance-linux-kernel-developments-3-4-1.md`
- Chunks:
  - `processed/code/systems-performance-linux-kernel-developments-3-4-1-chunk-000001.md`

## Extracted ideas (with classification)

- (mechanism) Many Linux changes are explicit tradeoffs between throughput, tail latency, CPU overhead, and operational complexity (schedulers, block layer queues, TCP CC, NUMA placement, lock algorithms).
- (measurement) First-class static instrumentation (tracepoints) and perf-oriented tooling shift what is cheap to observe in production versus what requires heavier dynamic attachment.
- (mechanism) Extended BPF becomes a programmable fast path and policy/observability host inside the kernel, changing where work can live relative to syscalls and packet/stack processing.
- (abstraction) “Move work across boundaries” patterns recur (zero-copy paths, offload, bypass-ish interfaces), relevant when deciding whether a bottleneck is resource-limited vs implementation-limited.

## Concepts reused / refined / created

- Reused (mechanism): [[extended-bpf]]
- Reused (measurement): [[event-tracing]]
- Reused (structure): [[resource-vs-implementation-bottleneck]]
- Reused (abstraction): [[shift-computation-in-time]]
- Reused (measurement): [[counters-statistics-metrics]]
- Reused (measurement): [[instrumentation-overhead-and-perturbation]]

## Links

- Concepts:
  - [[extended-bpf]]
  - [[event-tracing]]
  - [[resource-vs-implementation-bottleneck]]
  - [[shift-computation-in-time]]
  - [[counters-statistics-metrics]]
  - [[instrumentation-overhead-and-perturbation]]
