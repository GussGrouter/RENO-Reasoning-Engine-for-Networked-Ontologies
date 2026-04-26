# Systems Performance — USDT (4.3.8) (PDF pages 171–220 extract)

## Source

- Title: *Systems Performance: Enterprise and the Cloud* (Second Edition)
- Author: Brendan Gregg
- Raw: `raw/code/pdf/Systems.Performance.Enterprise.and.the.Cloud.pdf`
- Batch scope: Chapter 4, Section 4.3.8 (static user-level probes)

## Processed artifacts

- Converted slice: `processed/code/systems-performance-usdt-4-3-8.md`
- Chunks:
  - `processed/code/systems-performance-usdt-4-3-8-chunk-000001.md`

## Extracted ideas (with classification)

- (abstraction) USDT repeats the kernel pattern: **documented stable probe surface** versus **raw uprobes**. It exists so application-level semantics can join kernel-level timelines in one tracer without bespoke log scraping.
- (diagnosis) Log lines answer “what happened”; paired tracing answers “what else happened concurrently on kernel paths” (locks, I/O attribution), narrowing mistaken blame (example narrative: slow query attributed to disk vs filesystem lock).
- (mechanism) Build-time probes may be absent in packaged binaries; JIT languages often need **dynamic USDT** shims because probes cannot always be baked into JIT-generated code paths.

## Concepts reused / refined / created

- Reused (measurement): [[event-tracing]]
- Reused (measurement): [[instrumentation-overhead-and-perturbation]]
- Reused (structure): [[kernel-user-boundary]]
- Reused (mechanism): [[extended-bpf]]
- Reused: [[systems-performance]]

## Links

- Concepts:
  - [[event-tracing]]
  - [[instrumentation-overhead-and-perturbation]]
  - [[kernel-user-boundary]]
  - [[extended-bpf]]
  - [[systems-performance]]
