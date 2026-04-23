# Systems Performance — drill-down analysis (2.5.12) (PDF pages 92–98)

## Source

- Title: *Systems Performance: Enterprise and the Cloud* (Second Edition)
- Author: Brendan Gregg
- Raw: `raw/code/pdf/Systems.Performance.Enterprise.and.the.Cloud.pdf`
- Batch scope: Chapter 2, Section 2.5.12 Drill-Down Analysis

## Processed artifacts

- Converted slice: `processed/code/systems-performance-drill-down-analysis-2-5-12.md`
- Chunks:
  - `processed/code/systems-performance-drill-down-analysis-2-5-12-chunk-000001.md`

## Extracted ideas (with classification)

- (diagnosis) Drill-down analysis narrows from high-level symptoms to root cause by repeatedly focusing on the most promising areas and digging deeper through the stack as needed.
- (abstraction) A common structure is monitoring → identification → analysis, moving from aggregated signals to resource suspects to deeper inspection (profiling/tracing/custom tools/source inspection).
- (diagnosis) “Five whys” can be used during drill-down to persistently question causes until reaching a core issue.

## Concepts reused / refined / created

- Created (method): [[drill-down-analysis]]
- Reused (cycle): [[diagnosis-cycle]]
- Reused (insight): [[model-classify-intervene]]
- Reused (measurement): [[sampling-based-profiling]]

## Links

- Concepts:
  - [[drill-down-analysis]]
  - [[diagnosis-cycle]]
  - [[model-classify-intervene]]
  - [[sampling-based-profiling]]

