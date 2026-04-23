# Systems Performance — uprobes (4.3.7) (PDF pages 171–220 extract)

## Source

- Title: *Systems Performance: Enterprise and the Cloud* (Second Edition)
- Author: Brendan Gregg
- Raw: `raw/code/pdf/Systems.Performance.Enterprise.and.the.Cloud.pdf`
- Batch scope: Chapter 4, Section 4.3.7 (user-space dynamic instrumentation)

## Processed artifacts

- Converted slice: `processed/code/systems-performance-uprobes-4-3-7.md`
- Chunks:
  - `processed/code/systems-performance-uprobes-4-3-7-chunk-000001.md`

## Extracted ideas (with classification)

- (abstraction) User-space mirrors the kernel split: uprobes give **unlimited function-level** reach with an **unstable** contract (private functions, changing ABIs), similar in *role* to kprobes but across the [[kernel-user-boundary]].
- (measurement) Execution is trap-heavy versus in-kernel probes; absolute nanosecond floors are typically **much larger**, so micro-timing of short user functions needs skepticism—especially with **uretprobes**, where trampoline costs dominate.

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
