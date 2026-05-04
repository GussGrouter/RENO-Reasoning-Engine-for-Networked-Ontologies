# Systems Performance — tracing tool roles (4.5) (PDF pages 171–220 extract)

## Source

- Title: *Systems Performance: Enterprise and the Cloud* (Second Edition)
- Author: Brendan Gregg
- Raw: `raw/code/pdf/Systems.Performance.Enterprise.and.the.Cloud.pdf`
- Batch scope: Chapter 4, Section 4.5 Tracing Tools (survey of major Linux tracers—roles, not tutorials)

## Processed artifacts

- Converted slice: `processed/code/systems-performance-tracing-tools-survey-4-5.md`
- Chunks:
  - `processed/code/systems-performance-tracing-tools-survey-4-5-chunk-000001.md`

## Extracted ideas (with classification)

- (abstraction) **Complementary tracer classes** map to complementary questions: **stack/PMC-oriented sampling**, **built-in kernel trace control surfaces**, **programmable in-kernel aggregation**—pick by evidence type, overhead budget, and dependency tolerance, same as choosing among query engines in a platform.
- (diagnosis) **Pedagogical ordering** (symptom/use chapters before tracer-internals chapters) mirrors good incident practice: anchor on *what you are trying to prove* before expanding surface area into low-level mechanisms.
- (mechanism) Long-session / high-volume **black-box recording** emphasizes capture fidelity and later analysis—another point on the **volume vs immediacy** spectrum next to [[event-tracing]] uses.

## Concepts reused / refined / created

- Reused (measurement): [[sampling-based-profiling]]
- Reused (measurement): [[event-tracing]]
- Reused (mechanism): [[extended-bpf]]
- Reused (measurement): [[instrumentation-overhead-and-perturbation]]
- Reused: [[systems-performance]]

## Links

- Concepts:
  - [[sampling-based-profiling]]
  - [[event-tracing]]
  - [[extended-bpf]]
  - [[instrumentation-overhead-and-perturbation]]
  - [[systems-performance]]
