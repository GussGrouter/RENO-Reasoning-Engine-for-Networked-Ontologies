# Systems Performance — observability tools chapter framing (5.5 intro) (PDF ~231–285)

## Source

- Title: *Systems Performance: Enterprise and the Cloud* (Second Edition)
- Author: Brendan Gregg
- Raw: `raw/code/pdf/Systems.Performance.Enterprise.and.the.Cloud.pdf`
- Batch scope: Chapter 5, Section 5.5 Observability Tools (introduction; excludes Table 5.3 as a catalog—see book for the inventory)

## Processed artifacts

- Converted slice: `processed/code/systems-performance-observability-tools-chapter-framing-5-5.md`
- Chunks:
  - `processed/code/systems-performance-observability-tools-chapter-framing-5-5-chunk-000001.md`

## Extracted ideas (with classification)

- (abstraction) **Methodology precedes tooling**: the prior application methodology sections define *what to look for*; this chapter supplies Linux-oriented mechanisms—order matters for blast radius and interpretability ([[drill-down-analysis]], [[observability-vs-experimentation]]).
- (diagnosis) **Tooling is layered**: domain-specific and resource-oriented observability remain valid complements; no single table replaces workload judgment ([[resource-analysis-vs-workload-analysis]]).
- (measurement) **Stack/symbol quality is a prerequisite**: broken stacks make every downstream profile or trace misleading—treat “unknown frames” as a measurement defect class, not a cosmetic UI issue ([[instrumentation-overhead-and-perturbation]], [[sampling-based-profiling]]).

## Application validation

- **Incident bridge**: when rotating from “which subsystem?” (methodology) to “which commands?,” keep the §5.4 hypothesis explicit so you do not simultaneously turn on CPU, off-CPU, and syscall firehoses without a rollback order.

## Decision clarity

- **Decision**: choose **deferring heavy tracer enablement** until **methodology-scoped questions** are written down when an incident is still in the **classification** phase.

## Concepts reused / refined / created

- Reused (heuristic): [[drill-down-analysis]]
- Reused (abstraction): [[observability-vs-experimentation]]
- Reused (abstraction): [[resource-analysis-vs-workload-analysis]]
- Reused (measurement): [[instrumentation-overhead-and-perturbation]]
- Reused (measurement): [[sampling-based-profiling]]
- Reused: [[systems-performance]]

## Links

- Concepts:
  - [[drill-down-analysis]]
  - [[observability-vs-experimentation]]
  - [[resource-analysis-vs-workload-analysis]]
  - [[instrumentation-overhead-and-perturbation]]
  - [[sampling-based-profiling]]
  - [[systems-performance]]
- Related sources:
  - [[systems-performance-distributed-request-trace-sampling-5-4-8]]
  - [[systems-performance-perf-profiling-syscall-trace-and-io-5-5-1]]
  - [[systems-performance-bcc-profile-kernel-side-aggregation-5-5-2]]
