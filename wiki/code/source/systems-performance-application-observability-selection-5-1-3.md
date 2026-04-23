# Systems Performance — observability vs headline benchmark wins (5.1.3) (Chapter 5 extract)

## Source

- Title: *Systems Performance: Enterprise and the Cloud* (Second Edition)
- Author: Brendan Gregg
- Raw: `raw/code/pdf/Systems.Performance.Enterprise.and.the.Cloud.pdf`
- Batch scope: Chapter 5, Section 5.1.3 Observability

## Processed artifacts

- Converted slice: `processed/code/systems-performance-application-observability-selection-5-1-3.md`
- Chunks:
  - `processed/code/systems-performance-application-observability-selection-5-1-3-chunk-000001.md`

## Extracted ideas (with classification)

- (diagnosis) **Eliminating unnecessary work** dominates marginal micro-optimizations; opaque stacks hide that class of win even when synthetic benchmarks look better.
- (abstraction) **Vendor/runtime selection** under uncertainty: short-term throughput deltas can be swamped by long-run ability to observe, eliminate, and retune—this is an [[observability-vs-experimentation]] and toolchain maturity tradeoff expressed at the *platform choice* layer, not only at measurement time.

## Concepts reused / refined / created

- Reused (abstraction): [[observability-vs-experimentation]]
- Reused (diagnosis): [[known-unknowns-framework]]
- Reused (measurement): [[instrumentation-overhead-and-perturbation]]
- Reused (measurement): [[throughput-latency-metrics]]
- Reused: [[systems-performance]]

## Links

- Concepts:
  - [[observability-vs-experimentation]]
  - [[known-unknowns-framework]]
  - [[instrumentation-overhead-and-perturbation]]
  - [[throughput-latency-metrics]]
  - [[systems-performance]]
