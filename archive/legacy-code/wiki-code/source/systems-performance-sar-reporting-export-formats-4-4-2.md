# Systems Performance — sar reporting + machine-readable exports (4.4.2 part) (PDF pages 171–220 extract)

## Source

- Title: *Systems Performance: Enterprise and the Cloud* (Second Edition)
- Author: Brendan Gregg
- Raw: `raw/code/pdf/Systems.Performance.Enterprise.and.the.Cloud.pdf`
- Batch scope: Chapter 4, Section 4.4.2 — reporting combinations, `sar -A`, `sadf` structured exports

## Processed artifacts

- Converted slice: `processed/code/systems-performance-sar-reporting-export-formats-4-4-2.md`
- Chunks:
  - `processed/code/systems-performance-sar-reporting-export-formats-4-4-2-chunk-000001.md`

## Extracted ideas (with classification)

- (diagnosis) **Correlated rollups**: combining statistic groups (example narrative: CPU plus TCP families) supports cross-domain triage without bouncing between disjoint dashboards—same decision pattern as joining signals in [[model-classify-intervene]]-style workflows.
- (measurement) **Export as integration contract**: machine-parsable serializations are the bridge from host-local collection to **automation and central stores**; the design question is parse stability and field semantics, not a specific file format.
- (abstraction) “All statistics” (`-A`) is a **completeness vs noise** switch: more columns can help corner cases and can also drown ad hoc reading—choose based on question, not habit.

## Concepts reused / refined / created

- Reused (measurement): [[counters-statistics-metrics]]
- Reused (abstraction): [[centralized-monitoring-architecture]]
- Reused (measurement): [[time-series-monitoring]]
- Reused: [[model-classify-intervene]]
- Reused: [[systems-performance]]

## Links

- Concepts:
  - [[counters-statistics-metrics]]
  - [[centralized-monitoring-architecture]]
  - [[time-series-monitoring]]
- Insights:
  - [[model-classify-intervene]]
- Also:
  - [[systems-performance]]
