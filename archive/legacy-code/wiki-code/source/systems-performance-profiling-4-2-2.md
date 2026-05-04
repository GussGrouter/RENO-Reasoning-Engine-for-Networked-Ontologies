# Systems Performance — profiling (4.2.2) (PDF pages 171–220)

## Source

- Title: *Systems Performance: Enterprise and the Cloud* (Second Edition)
- Author: Brendan Gregg
- Raw: `raw/code/pdf/Systems.Performance.Enterprise.and.the.Cloud.pdf`
- Batch scope: Chapter 4, Section 4.2.2 Profiling

## Processed artifacts

- Converted slice: `processed/code/systems-performance-profiling-4-2-2.md`
- Chunks:
  - `processed/code/systems-performance-profiling-4-2-2-chunk-000001.md`

## Extracted ideas (with classification)

- (measurement) Profiling builds a picture from **samples/snapshots** (timer-based or event-triggered), trading completeness for controlled overhead compared to full event capture.
- (mechanism) Hardware-event profiling (e.g., cache miss counters) attributes memory-related costs to code paths without requiring explicit per-access tracing.
- (abstraction) Profiling is typically **on-demand** because sampling rate and storage scale with observability cost; “negligible overhead” is a rate/configuration claim, not a law.

## Concepts reused / refined / created

- Reused (measurement): [[sampling-based-profiling]]
- Reused (measurement): [[instrumentation-overhead-and-perturbation]]
- Reused (measurement): [[event-tracing]]
- Reused (structure): [[counters-statistics-metrics]]
- Reused (abstraction): [[observability-vs-experimentation]]
- Reused: [[systems-performance]]

## Links

- Concepts:
  - [[sampling-based-profiling]]
  - [[instrumentation-overhead-and-perturbation]]
  - [[event-tracing]]
  - [[counters-statistics-metrics]]
  - [[observability-vs-experimentation]]
  - [[systems-performance]]
