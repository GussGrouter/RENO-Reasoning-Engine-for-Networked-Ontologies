# Systems Performance — chapter 5 exercises: under-load lab (latency → workload → static → sync) (5.7 partial) (PDF ~231–285)

## Source

- Title: *Systems Performance: Enterprise and the Cloud* (Second Edition)
- Author: Brendan Gregg
- Raw: `raw/code/pdf/Systems.Performance.Enterprise.and.the.Cloud.pdf`
- Batch scope: Chapter 5, Section 5.7 Exercises, item 4 (caches through synchronization), plus optional item 5 (thread-state tool aspiration)

## Processed artifacts

- Converted slice: `processed/code/systems-performance-chapter-5-exercises-under-load-lab-b-5-7.md`
- Chunks:
  - `processed/code/systems-performance-chapter-5-exercises-under-load-lab-b-5-7-chunk-000001.md`

## Extracted ideas (with classification)

- (measurement) **Caches need hit rate + size**, not only existence—otherwise “we have a cache” is a non-measurement ([[caching]], [[counters-statistics-metrics]]).
- (measurement) **Latency distribution** (not only mean) decides whether the drill-down target is tails or central tendency ([[latency-analysis]], [[latency-percentiles]]).
- (heuristic) **Drill-down follows dominant latency mass**; **workload characterization** (“who/what”) prevents optimizing the wrong tenants ([[drill-down-analysis]], [[resource-analysis-vs-workload-analysis]]).
- (heuristic) **Static tuning checklist** belongs in the same lab sequence as dynamic tracing—misconfigurations mimic hot code ([[static-performance-tuning]]).
- (diagnosis) **Concurrency primitives audit** closes the loop from CPU/off-CPU stories to real serialization points ([[resource-vs-implementation-bottleneck]], [[context-switching]]).
- (abstraction) Optional **thread-state columnar tooling** is framed as a **measurement product gap**, not a mandate—feasibility vs maintainer cost still applies ([[known-unknowns-framework]]).

## Application validation

- **Capacity review**: require cache hit/size, latency histogram, workload owner, static checklist, and lock profile sections filled—same structure as this exercise tail.

## Concepts reused / refined / created

- Reused (mechanism): [[caching]]
- Reused (measurement): [[counters-statistics-metrics]]
- Reused (measurement): [[latency-analysis]]
- Reused (measurement): [[latency-percentiles]]
- Reused (heuristic): [[drill-down-analysis]]
- Reused (abstraction): [[resource-analysis-vs-workload-analysis]]
- Reused (heuristic): [[static-performance-tuning]]
- Reused (structure): [[resource-vs-implementation-bottleneck]]
- Reused (mechanism): [[context-switching]]
- Reused (diagnosis): [[known-unknowns-framework]]
- Reused: [[systems-performance]]

## Links

- Concepts:
  - [[caching]]
  - [[counters-statistics-metrics]]
  - [[latency-analysis]]
  - [[latency-percentiles]]
  - [[drill-down-analysis]]
  - [[resource-analysis-vs-workload-analysis]]
  - [[static-performance-tuning]]
  - [[resource-vs-implementation-bottleneck]]
  - [[context-switching]]
  - [[known-unknowns-framework]]
  - [[systems-performance]]
- Related sources:
  - [[systems-performance-chapter-5-exercises-under-load-lab-a-5-7]]
  - [[systems-performance-bpftrace-custom-aggregation-probe-ladder-5-5-7]]
