# Systems Performance — other observability sources (4.3.10) (PDF pages 171–220 extract)

## Source

- Title: *Systems Performance: Enterprise and the Cloud* (Second Edition)
- Author: Brendan Gregg
- Raw: `raw/code/pdf/Systems.Performance.Enterprise.and.the.Cloud.pdf`
- Batch scope: Chapter 4, Section 4.3.10 (miscellaneous interfaces + Solaris Kstat comparison)

## Processed artifacts

- Converted slice: `processed/code/systems-performance-other-observability-sources-4-3-10.md`
- Chunks:
  - `processed/code/systems-performance-other-observability-sources-4-3-10-chunk-000001.md`

## Extracted ideas (with classification)

- (abstraction) Beyond the headline families, kernels expose many **adjacent channels** (MSRs for power/thermal, accounted process lifetimes, netfilter hooks, packet capture paths, syscall trace tradeoffs vs `ptrace` breakpoints, software events such as page faults). The design question is whether a channel is **fit for purpose**—rate, safety, completeness—not whether it appears in a single “observability API.”
- (measurement) `ptrace`-class observation is flexible but can slow targets by orders of magnitude; prefer higher-efficiency syscall/static/dynamic tracing when continuous observation is needed.
- (abstraction) **Structured vs textual stats export** (example contrast: hierarchical Kstat tuples vs parsing `/proc` text) is the same recurring “machine interface vs human shell output” efficiency pattern as [[resource-vs-implementation-bottleneck]] framing: automation should favor low-parse-cost, stable shapes when volume is high.
- (diagnosis) Some measurements exist only because accounting features were historically aimed at **billing/chargeback**—still useful for spotting short-lived processes missed by sampled snapshots.

## Concepts reused / refined / created

- Reused (structure): [[resource-vs-implementation-bottleneck]]
- Reused (measurement): [[instrumentation-overhead-and-perturbation]]
- Reused (measurement): [[event-tracing]]
- Reused (measurement): [[counters-statistics-metrics]]
- Reused (diagnosis): [[known-unknowns-framework]]
- Reused: [[systems-performance]]

## Links

- Concepts:
  - [[resource-vs-implementation-bottleneck]]
  - [[instrumentation-overhead-and-perturbation]]
  - [[event-tracing]]
  - [[counters-statistics-metrics]]
  - [[known-unknowns-framework]]
  - [[systems-performance]]
