# Systems Performance — tracing (4.2.3) (PDF pages 171–220)

## Source

- Title: *Systems Performance: Enterprise and the Cloud* (Second Edition)
- Author: Brendan Gregg
- Raw: `raw/code/pdf/Systems.Performance.Enterprise.and.the.Cloud.pdf`
- Batch scope: Chapter 4, Section 4.2.3 Tracing

## Processed artifacts

- Converted slice: `processed/code/systems-performance-tracing-4-2-3.md`
- Chunks:
  - `processed/code/systems-performance-tracing-4-2-3-chunk-000001.md`

## Extracted ideas (with classification)

- (measurement) Tracing aims to capture **(near-)every occurrence** of an event class, preserving per-event detail for later analysis or summarized rollups.
- (abstraction) “Logging” is framed as **low-frequency tracing** enabled by default—same shape (event records), different rate and retention assumptions.
- (diagnosis) Debuggers can inspect per-event state but often impose **stop/start** costs that disqualify them as production tracing substitutes when low overhead matters.

## Concepts reused / refined / created

- Reused (measurement): [[event-tracing]]
- Reused (measurement): [[instrumentation-overhead-and-perturbation]]
- Reused (abstraction): [[observability-vs-experimentation]]
- Reused (measurement): [[sampling-based-profiling]]
- Reused: [[systems-performance]]

## Links

- Concepts:
  - [[event-tracing]]
  - [[instrumentation-overhead-and-perturbation]]
  - [[observability-vs-experimentation]]
  - [[sampling-based-profiling]]
  - [[systems-performance]]
