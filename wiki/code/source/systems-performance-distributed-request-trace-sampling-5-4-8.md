# Systems Performance — distributed request tracing and sampling (5.4.8) (PDF ~231–285)

## Source

- Title: *Systems Performance: Enterprise and the Cloud* (Second Edition)
- Author: Brendan Gregg
- Raw: `raw/code/pdf/Systems.Performance.Enterprise.and.the.Cloud.pdf`
- Batch scope: Chapter 5, Section 5.4.8 Distributed Tracing (end-to-end correlation intent and sampling tradeoffs; not a product survey)

## Processed artifacts

- Converted slice: `processed/code/systems-performance-distributed-request-trace-sampling-5-4-8.md`
- Chunks:
  - `processed/code/systems-performance-distributed-request-trace-sampling-5-4-8-chunk-000001.md`

## Extracted ideas (with classification)

- (measurement) **Distributed diagnosis** needs **per-request correlation** across services so latency and errors map to dependency edges, not isolated node averages ([[event-tracing]], [[latency-analysis]]).
- (measurement) **Trace volume** forces an explicit **sampling policy trade**: early uniform sampling describes bulk behavior cheaply; **deferred keep decisions** improve capture of rare tails and errors at higher retention cost ([[sampling-based-profiling]], [[instrumentation-overhead-and-perturbation]]).

## Application validation

- **Intermittent 99.9% checkout spikes**: uniform 0.01% head sampling may never see the path; bias retention toward completed slow traces or error-linked traces so capacity engineering has evidence.

## Decision clarity

- **Decision**: choose **tail-biased trace retention** over **head-only uniform sampling** when the primary risk is **sparse high-latency tails or rare errors**, not steady-state average latency.

## Concepts reused / refined / created

- Reused (measurement): [[event-tracing]]
- Reused (measurement): [[latency-analysis]]
- Reused (measurement): [[sampling-based-profiling]]
- Reused (measurement): [[instrumentation-overhead-and-perturbation]]
- Reused: [[systems-performance]]

## Links

- Concepts:
  - [[event-tracing]]
  - [[latency-analysis]]
  - [[sampling-based-profiling]]
  - [[instrumentation-overhead-and-perturbation]]
  - [[systems-performance]]
- Related sources:
  - [[systems-performance-static-performance-tuning-application-checklist-5-4-7]]
  - [[systems-performance-application-methodology-overview-5-4]]
