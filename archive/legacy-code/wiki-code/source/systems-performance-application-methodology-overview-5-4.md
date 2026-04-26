# Systems Performance — application methodology overview (5.4 intro) (PDF ~182–230)

## Source

- Title: *Systems Performance: Enterprise and the Cloud* (Second Edition)
- Author: Brendan Gregg
- Raw: `raw/code/pdf/Systems.Performance.Enterprise.and.the.Cloud.pdf`
- Batch scope: Chapter 5, Section 5.4 Methodology (table of application-focused methods + ordering guidance)

## Processed artifacts

- Converted slice: `processed/code/systems-performance-application-methodology-overview-5-4.md`
- Chunks:
  - `processed/code/systems-performance-application-methodology-overview-5-4-chunk-000001.md`

## Extracted ideas (with classification)

- (abstraction) **Method portfolio** lists complementary observational tactics (CPU, off-CPU, syscalls, USE, threads, locks, static tuning, distributed traces)—choice is **sequencing** under uncertainty, not maximal simultaneous measurement.
- (diagnosis) Suggested **order** biases early cheap signal (CPU profile, workload framing) before heavier cross-layer captures—mirrors staged [[drill-down-analysis]].
- (diagnosis) **Domain-specific playbooks** (known logical bugs) can short-circuit months of generic profiling—keep them adjacent to formal methods in the same decision system ([[known-unknowns-framework]]).

## Application validation

- **New on-call runbook**: for “slow microservice,” default the first two steps to **CPU profile + request/workload characterization** before enabling system-wide off-CPU tracing—table order is about controlling blast radius of overhead.

## Concepts reused / refined / created

- Reused (heuristic): [[drill-down-analysis]]
- Reused (heuristic): [[use-method]]
- Reused (diagnosis): [[known-unknowns-framework]]
- Reused (measurement): [[sampling-based-profiling]]
- Reused: [[systems-performance]]

## Links

- Concepts:
  - [[drill-down-analysis]]
  - [[use-method]]
  - [[known-unknowns-framework]]
  - [[sampling-based-profiling]]
  - [[systems-performance]]
- Related sources:
  - [[systems-performance-workload-characterization-2-5-11]]
