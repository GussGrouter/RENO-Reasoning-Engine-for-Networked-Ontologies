# Systems Performance — tracepoints: arguments, interfaces, overhead; kprobes intro (PDF pages 186–194)

## Source

- Title: *Systems Performance: Enterprise and the Cloud* (Second Edition)
- Author: Brendan Gregg
- Raw: `raw/code/pdf/Systems.Performance.Enterprise.and.the.Cloud.pdf`
- Batch scope: PDF pages 186–194 (Chapter 4 observability sources: tracepoints details + overhead; kprobes intro)

## Processed artifacts

- Converted slice: `processed/code/systems-performance-tracing-profiling-p186-194.md`
- Chapter-section slice (§4.3.5 overlap): `processed/code/systems-performance-tracepoints-4-3-5.md`
- Chunks:
  - `processed/code/systems-performance-tracepoints-overhead-kprobes-chunk-000001.md`
  - `processed/code/systems-performance-tracepoints-overhead-kprobes-chunk-000002.md`
  - `processed/code/systems-performance-tracepoints-overhead-kprobes-chunk-000003.md`

## Extracted ideas (with classification)

- (measurement) Trace events expose contextual arguments via per-event format strings (names + typed fields + print format), enabling structured filtering and custom output.
- (measurement) Instrumentation interface choices (tracefs vs `perf_event_open(2)`) affect concurrency/operational behavior and how tools enable/consume event streams.
- (measurement) Instrumentation overhead has enabled-cost and disabled-cost components; whether it perturbs production depends on event rate and CPU count.
- (measurement) Stable event sources (tracepoints/TRACE_EVENT) provide a stable API surface (name + arguments), whereas dynamic instrumentation (kprobes) is an unstable API because it targets raw kernel functions/arguments that can change.
- (diagnosis) Measurement design must account for perturbation risk (high-rate events can distort the observed workload), so “what you can safely trace” constrains diagnosis tactics.

## Promoted concepts (from this batch)

- [[instrumentation-overhead-and-perturbation]]

## Links

- Concepts:
  - [[instrumentation-overhead-and-perturbation]]

## Related sections

- [[systems-performance-tracepoints-4-3-5]]

