# Systems Performance — observability sources (4.3 intro) (PDF pages 171–220)

## Source

- Title: *Systems Performance: Enterprise and the Cloud* (Second Edition)
- Author: Brendan Gregg
- Raw: `raw/code/pdf/Systems.Performance.Enterprise.and.the.Cloud.pdf`
- Batch scope: Chapter 4, Section 4.3 Observability Sources (introductory framing + source taxonomy lead-in)

## Processed artifacts

- Converted slice: `processed/code/systems-performance-observability-sources-intro-4-3.md`
- Chunks:
  - `processed/code/systems-performance-observability-sources-intro-4-3-chunk-000001.md`

## Extracted ideas (with classification)

- (abstraction) Linux observability is not “one API”; it is a **menu of source families** (/proc, /sys, cgroup accounting, tracing attachment points, PMC channels, packet capture paths) that tools compose differently.
- (diagnosis) Knowing the **source family** behind a metric or trace is part of validating whether a signal is system-wide vs per-process, counter-like vs event-like, and whether it is cheap to read at fleet scale.

## Concepts reused / refined / created

- Reused (abstraction): [[resource-analysis-vs-workload-analysis]]
- Reused (diagnosis): [[known-unknowns-framework]]
- Reused (structure): [[counters-statistics-metrics]]
- Reused (measurement): [[event-tracing]]
- Reused: [[systems-performance]]

## Links

- Concepts:
  - [[resource-analysis-vs-workload-analysis]]
  - [[known-unknowns-framework]]
  - [[counters-statistics-metrics]]
  - [[event-tracing]]
  - [[systems-performance]]
