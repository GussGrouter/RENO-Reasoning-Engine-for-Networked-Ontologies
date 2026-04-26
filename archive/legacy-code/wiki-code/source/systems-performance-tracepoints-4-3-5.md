# Systems Performance — tracepoints (4.3.5) (PDF pages 171–220 extract)

## Source

- Title: *Systems Performance: Enterprise and the Cloud* (Second Edition)
- Author: Brendan Gregg
- Raw: `raw/code/pdf/Systems.Performance.Enterprise.and.the.Cloud.pdf`
- Batch scope: Chapter 4, Section 4.3.5 (static kernel trace hooks + stable event surface)

## Processed artifacts

- Converted slice: `processed/code/systems-performance-tracepoints-4-3-5.md`
- Chunks:
  - `processed/code/systems-performance-tracepoints-4-3-5-chunk-000001.md`

## Overlap note

Much of the argument-level and interface-level detail here is captured in [[systems-performance-tracepoints-overhead-kprobes-p186-194]] (overlapping PDF pages). This page anchors the same material to the **§4.3.5** heading and captures a few naming/availability wrinkles that affect interpretation.

## Extracted ideas (with classification)

- (abstraction) **Hook vs exported event**: kernel “tracepoints” are often implemented as TRACE_EVENT-generated *trace events* exposed by name; tools and `perf` may still label multiple attachment styles as “Tracepoint event,” so category decisions should follow the attachment mechanism, not only the UI label.
- (measurement) Some events exist only when the kernel is built with relevant Kconfig options; “missing tracepoint” can mean **disabled compile-time instrumentation**, not necessarily “this path never fires.”
- (measurement) Stable static tracing competes with function-based tracing (Section 4.3.6) on power, but differs in **API stability**: names/fields are intended to stay consistent for tool builders.
- (measurement) Raw tracepoints (post-4.7) trade structured argument materialization for lower per-event CPU when you only need coarse attachment.

## Concepts reused / refined / created

- Reused (measurement): [[event-tracing]]
- Reused (measurement): [[instrumentation-overhead-and-perturbation]]
- Reused (structure): [[counters-statistics-metrics]]
- Reused (mechanism): [[extended-bpf]]
- Related extraction: [[systems-performance-tracepoints-overhead-kprobes-p186-194]]
- Reused: [[systems-performance]]

## Links

- Concepts:
  - [[event-tracing]]
  - [[instrumentation-overhead-and-perturbation]]
  - [[counters-statistics-metrics]]
  - [[extended-bpf]]
  - [[systems-performance]]
