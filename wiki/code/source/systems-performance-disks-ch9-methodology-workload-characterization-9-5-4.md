# Systems Performance — Ch.9 §9.5.4 Workload characterization (scout PDF 460–520)

## Source

- Title: *Systems Performance: Enterprise and the Cloud* (Second Edition)
- Scout: `processed/code/systems-performance-ch9-scout-p460-520.txt`
- Scope: **§9.5.4** + checklist + trace caveat

## Processed artifacts

- `processed/code/systems-performance-disks-ch9-methodology-workload-characterization-9-5-4.md`

## Extracted ideas

- **Who/why/what/how** for disk load—**eliminate unnecessary work** wins ([[resource-analysis-vs-workload-analysis]]).
- **Tracing** depth trades **fidelity vs perturbation** ([[event-tracing]], [[instrumentation-overhead-and-perturbation]]).

## Decision clarity

**Decision:** choose **sampling + periodic histograms** over **always-on full I/O trace to disk** when **event rate** risks **observer feedback loops**.

## Concepts reused / refined / created

- Reused: [[resource-analysis-vs-workload-analysis]], [[event-tracing]], [[instrumentation-overhead-and-perturbation]], [[counters-statistics-metrics]], [[systems-performance]]
- **Created:** none

## Links

- Concepts: [[resource-analysis-vs-workload-analysis]], [[event-tracing]], [[instrumentation-overhead-and-perturbation]], [[counters-statistics-metrics]], [[systems-performance]]
