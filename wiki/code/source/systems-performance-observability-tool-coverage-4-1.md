# Systems Performance — observability tool coverage (4.1) (PDF pages 118–170)

## Source

- Title: *Systems Performance: Enterprise and the Cloud* (Second Edition)
- Author: Brendan Gregg
- Raw: `raw/code/pdf/Systems.Performance.Enterprise.and.the.Cloud.pdf`
- Batch scope: Chapter 4, Section 4.1 Tool Coverage

## Processed artifacts

- Converted slice: `processed/code/systems-performance-observability-tool-coverage-4-1.md`
- Chunks:
  - `processed/code/systems-performance-observability-tool-coverage-4-1-chunk-000001.md`

## Extracted ideas (with classification)

- (diagnosis) Annotating an OS diagram with “what observes what” is a coverage map: it makes missing observability for a subsystem explicit before you commit to an investigation path.
- (abstraction) Tool coverage is not uniform across CPU/memory/disk/network; deep tracing stacks (perf/Ftrace/BCC/bpftrace) are called out as cross-cutting capabilities introduced later in the chapter.

## Concepts reused / refined / created

- Reused (insight): [[model-classify-intervene]]
- Reused (abstraction): [[resource-analysis-vs-workload-analysis]]
- Reused (structure): [[counters-statistics-metrics]]
- Reused (measurement): [[event-tracing]]
- Reused (measurement): [[metric-visualization]]
- Reused: [[systems-performance]]

## Links

- Concepts:
  - [[model-classify-intervene]]
  - [[resource-analysis-vs-workload-analysis]]
  - [[counters-statistics-metrics]]
  - [[event-tracing]]
  - [[metric-visualization]]
  - [[systems-performance]]
