# Systems Performance — observability tool types (4.2 intro) (PDF pages 171–220)

## Source

- Title: *Systems Performance: Enterprise and the Cloud* (Second Edition)
- Author: Brendan Gregg
- Raw: `raw/code/pdf/Systems.Performance.Enterprise.and.the.Cloud.pdf`
- Batch scope: Chapter 4, Section 4.2 Tool Types (introductory framing before 4.2.1)

## Processed artifacts

- Converted slice: `processed/code/systems-performance-observability-tool-types-4-2.md`
- Chunks:
  - `processed/code/systems-performance-observability-tool-types-4-2-chunk-000001.md`

## Extracted ideas (with classification)

- (abstraction) A practical classification combines **scope** (system-wide vs per-process) with **signal shape** (counters vs events), because those two axes determine tool selection and interpretation pitfalls.
- (measurement) Profilers vs tracers are both “event-ish,” but differ in sampling density and completeness tradeoffs (coarse painting vs per-event capture).

## Concepts reused / refined / created

- Reused (structure): [[counters-statistics-metrics]]
- Reused (measurement): [[event-tracing]]
- Reused (measurement): [[sampling-based-profiling]]
- Reused (abstraction): [[observability-vs-experimentation]]
- Reused: [[systems-performance]]

## Links

- Concepts:
  - [[counters-statistics-metrics]]
  - [[event-tracing]]
  - [[sampling-based-profiling]]
  - [[observability-vs-experimentation]]
  - [[systems-performance]]
