# Systems Performance — CPU §6.5 methodology ordering and tools-method limits (6.5 intro + 6.5.1) (PDF 231–285 + 286–320)

## Source

- Title: *Systems Performance: Enterprise and the Cloud* (Second Edition)
- Author: Brendan Gregg
- Raw: `raw/code/pdf/Systems.Performance.Enterprise.and.the.Cloud.pdf`
- Batch scope: Chapter 6, **§6.5** — cookbook ordering for CPU work; **§6.5.1** tools method (coverage gaps vs convenience)

## Processed artifacts

- Converted slice: `processed/code/systems-performance-cpu-methodology-cookbook-and-tools-method-6-5-intro-6-5-1.md`
- Chunks:
  - `processed/code/systems-performance-cpu-methodology-cookbook-and-tools-method-6-5-intro-6-5-1-chunk-000001.md`

## Extracted ideas (with classification)

- (abstraction) **Suggested sequencing** (monitoring → USE → profiling → micro-benchmarking → static tuning) is a **risk-ordered ladder**: start with **cheap systemic screens** before expensive attribution ([[drill-down-analysis]], [[model-classify-intervene]]).
- (diagnosis) **Tools method** (iterate whatever exists) is **fast to start** but **coverage-bounded**: blind spots are expected when the platform’s metrics don’t surface the real constraint ([[streetlight-anti-method]], [[known-unknowns-framework]]).
- (measurement) **Per-CPU vs system-wide views** are part of method hygiene—hot CPUs are a **shape** signal for parallelism and scheduler imbalance, not only “high %” ([[measurement-validity]], [[utilization-and-saturation]]).

## Application validation

- **On-call playbook**: default to **USE + per-CPU utilization** before opening a flame graph when the incident window is short and data capture is constrained.

## Decision clarity

- **Decision**: choose **USE + saturation-first triage** over **tool-shopping every dashboard tile** when time-boxed and the failure mode is **unknown bottleneck class**.

## Concepts reused / refined / created

- Reused (heuristic): [[drill-down-analysis]]
- Reused (insight): [[model-classify-intervene]]
- Reused (heuristic): [[streetlight-anti-method]]
- Reused (abstraction): [[known-unknowns-framework]]
- Reused (abstraction): [[measurement-validity]]
- Reused (structure): [[utilization-and-saturation]]
- Reused: [[systems-performance]]

## Links

- Concepts:
  - [[drill-down-analysis]]
  - [[model-classify-intervene]]
  - [[streetlight-anti-method]]
  - [[known-unknowns-framework]]
  - [[measurement-validity]]
  - [[utilization-and-saturation]]
  - [[systems-performance]]
- Related sources:
  - [[systems-performance-cpu-idle-numa-topology-scheduler-awareness-6-4-2]]
  - [[systems-performance-cpu-use-method-cpu-checklist-6-5-2]]
