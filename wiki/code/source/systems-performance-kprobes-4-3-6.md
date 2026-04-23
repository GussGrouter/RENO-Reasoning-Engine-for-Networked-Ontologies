# Systems Performance — kprobes (4.3.6) (PDF pages 171–220 extract)

## Source

- Title: *Systems Performance: Enterprise and the Cloud* (Second Edition)
- Author: Brendan Gregg
- Raw: `raw/code/pdf/Systems.Performance.Enterprise.and.the.Cloud.pdf`
- Batch scope: Chapter 4, Section 4.3.6 (kernel dynamic instrumentation)

## Processed artifacts

- Converted slice: `processed/code/systems-performance-kprobes-4-3-6.md`
- Chunks:
  - `processed/code/systems-performance-kprobes-4-3-6-chunk-000001.md`

## Extracted ideas (with classification)

- (abstraction) **Depth vs stability tradeoff**: kprobes expose **raw** kernel entry points and memory; the symbol/argument contract is not a stable external API, so tools can break across kernel versions even when workloads are unchanged.
- (mechanism) Implementations mix **instruction patching**, **breakpoint-style offsets**, **Ftrace fast path** on function entry, and **return trampolines** for kretprobes—each path changes the overhead floor and what can be measured safely at high frequency.
- (measurement) Empirical minimum costs differ by probe style (example narrative: higher floor for return probes due to trampolines), so “dynamic tracing overhead” is not one number.
- (diagnosis) Role as **last-resort observability**: when stable static probes do not exist, dynamic attachment is often the only way to make invisible kernel paths visible in production—at acceptability/latency risk.

## Concepts reused / refined / created

- Reused (measurement): [[event-tracing]]
- Reused (measurement): [[instrumentation-overhead-and-perturbation]]
- Reused (measurement): [[sampling-based-profiling]]
- Reused (structure): [[kernel-user-boundary]]
- Reused (mechanism): [[extended-bpf]]
- Reused: [[systems-performance]]

## Links

- Concepts:
  - [[event-tracing]]
  - [[instrumentation-overhead-and-perturbation]]
  - [[sampling-based-profiling]]
  - [[kernel-user-boundary]]
  - [[extended-bpf]]
  - [[systems-performance]]
