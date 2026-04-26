# Systems Performance — observing observability / metric skepticism (4.6) (PDF pages 171–220 extract)

## Source

- Title: *Systems Performance: Enterprise and the Cloud* (Second Edition)
- Author: Brendan Gregg
- Raw: `raw/code/pdf/Systems.Performance.Enterprise.and.the.Cloud.pdf`
- Batch scope: Chapter 4, Section 4.6 Observing Observability

## Processed artifacts

- Converted slice: `processed/code/systems-performance-observing-observability-4-6.md`
- Chunks:
  - `processed/code/systems-performance-observing-observability-4-6-chunk-000001.md`

## Extracted ideas (with classification)

- (diagnosis) **Metrics stack is software**: compilers, parsers, collectors, and doc strings all fail—treat surprising numbers like any other production defect: reproduce, isolate layer, compare independent paths.
- (diagnosis) **Independent cross-checks** when coverage overlaps (ideally different instrumentation families) reduce the chance a single buggy framework dominates your story—same epistemic pattern as triangulating telemetry in distributed systems.
- (measurement) **Collectors are part of the signal**: pipeline bugs (example narrative: unit-stripping regex ruining throughput figures) create **false bottlenecks** in dashboards—blame neither the service nor the kernel until the plumbing is ruled out.
- (abstraction) **Known-workload oracle tests** (including micro-benchmark harnesses with their own counters) bridge [[observability-vs-experimentation]]: synthesis when neither pure observe nor pure bench alone is authoritative.
- (diagnosis) **Absence is harder than incorrect presence**: sparse instrumentation often reflects developer debugging history, not user needs—connects directly to expanding [[known-unknowns-framework]] deliberately.

## Concepts reused / refined / created

- Reused (abstraction): [[scientific-method]]
- Reused (diagnosis): [[known-unknowns-framework]]
- Reused (abstraction): [[observability-vs-experimentation]]
- Reused (heuristic): [[micro-benchmarking]]
- Reused (measurement): [[counters-statistics-metrics]]
- Reused (measurement): [[instrumentation-overhead-and-perturbation]]
- Reused: [[systems-performance]]

## Links

- Concepts:
  - [[scientific-method]]
  - [[known-unknowns-framework]]
  - [[observability-vs-experimentation]]
  - [[micro-benchmarking]]
  - [[counters-statistics-metrics]]
  - [[instrumentation-overhead-and-perturbation]]
  - [[systems-performance]]
