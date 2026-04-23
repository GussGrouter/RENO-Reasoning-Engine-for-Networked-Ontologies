# Systems Performance — PMC challenges and documentation pointers (4.3.9 cont.) (PDF pages 171–220 extract)

## Source

- Title: *Systems Performance: Enterprise and the Cloud* (Second Edition)
- Author: Brendan Gregg
- Raw: `raw/code/pdf/Systems.Performance.Enterprise.and.the.Cloud.pdf`
- Batch scope: Chapter 4, Section 4.3.9 (PMC sampling accuracy, cloud availability, vendor manuals, PAPI note)

## Processed artifacts

- Converted slice: `processed/code/systems-performance-pmc-challenges-and-docs-4-3-9.md`
- Chunks:
  - `processed/code/systems-performance-pmc-challenges-and-docs-4-3-9-chunk-000001.md`

## Extracted ideas (with classification)

- (measurement) **Attribution hazard**: interrupt-based sampling of fine-grained hardware events can mis-assign costs to instructions due to skid, reordering, and interrupt latency—so “which line of code caused this LLC miss?” needs **precision aids** when the question is micro-level.
- (abstraction) **Environment gating**: many hosted environments disallow guest PMC access; architectural counter stories that assume bare metal may fail silently in cloud—this is an [[observability-vs-experimentation]] and [[known-unknowns-framework]] hazard (you may need provider features, bare-metal SKUs, or alternate evidence).
- (diagnosis) Cross-vendor naming remains messy; portability efforts (example: PAPI-style schemes) fight mapping churn and still need OS maintenance—another “standardized surface vs operational reality” tradeoff.

## Concepts reused / refined / created

- Reused (measurement): [[sampling-based-profiling]]
- Reused (measurement): [[counters-statistics-metrics]]
- Reused (abstraction): [[observability-vs-experimentation]]
- Reused (diagnosis): [[known-unknowns-framework]]
- Reused: [[systems-performance]]

## Links

- Concepts:
  - [[sampling-based-profiling]]
  - [[counters-statistics-metrics]]
  - [[observability-vs-experimentation]]
  - [[known-unknowns-framework]]
  - [[systems-performance]]
