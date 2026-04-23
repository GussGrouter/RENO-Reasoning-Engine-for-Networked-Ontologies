# Systems Performance — chapter 4 observability tools (intro) (PDF pages 118–170)

## Source

- Title: *Systems Performance: Enterprise and the Cloud* (Second Edition)
- Author: Brendan Gregg
- Raw: `raw/code/pdf/Systems.Performance.Enterprise.and.the.Cloud.pdf`
- Batch scope: Chapter 4, introductory material (learning objectives + observability gaps narrative)

## Processed artifacts

- Converted slice: `processed/code/systems-performance-chapter-4-intro-4.md`
- Chunks:
  - `processed/code/systems-performance-chapter-4-intro-4-chunk-000001.md`

## Extracted ideas (with classification)

- (diagnosis) Historical tool abundance created an “everything is observable” illusion; experts still needed inference because many important paths were not directly instrumentable.
- (measurement) Modern Linux observability improves substantially with dynamic tracing (BPF-class tooling), changing which questions are cheap to answer in production versus which still require inference.
- (abstraction) Tooling discussion is framed around tool *types* (counters, profiling, tracing) and their overhead tradeoffs, aligning with earlier observability vocabulary in the book.

## Concepts reused / refined / created

- Reused (diagnosis): [[known-unknowns-framework]]
- Reused (structure): [[counters-statistics-metrics]]
- Reused (measurement): [[event-tracing]]
- Reused (measurement): [[sampling-based-profiling]]
- Reused (abstraction): [[observability-vs-experimentation]]
- Reused (measurement): [[instrumentation-overhead-and-perturbation]]
- Reused (mechanism): [[extended-bpf]]
- Reused: [[systems-performance]]

## Links

- Concepts:
  - [[known-unknowns-framework]]
  - [[counters-statistics-metrics]]
  - [[event-tracing]]
  - [[sampling-based-profiling]]
  - [[observability-vs-experimentation]]
  - [[instrumentation-overhead-and-perturbation]]
  - [[extended-bpf]]
  - [[systems-performance]]
