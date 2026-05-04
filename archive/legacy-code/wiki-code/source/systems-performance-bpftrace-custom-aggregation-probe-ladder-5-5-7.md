# Systems Performance — bpftrace: dimensional breakdown and internals ladder (5.5.7) (PDF ~231–285)

## Source

- Title: *Systems Performance: Enterprise and the Cloud* (Second Edition)
- Author: Brendan Gregg
- Raw: `raw/code/pdf/Systems.Performance.Enterprise.and.the.Cloud.pdf`
- Batch scope: Chapter 5, Section 5.5.7 `bpftrace` (signals, I/O histograms/latency, lock latency/holder stacks, USDT/uprobes guidance; tool names as examples only)

## Processed artifacts

- Converted slice: `processed/code/systems-performance-bpftrace-custom-aggregation-probe-ladder-5-5-7.md`
- Chunks:
  - `processed/code/systems-performance-bpftrace-custom-aggregation-probe-ladder-5-5-7-chunk-000001.md`

## Extracted ideas (with classification)

- (measurement) **Progressive dimensionalization**: start with a single latency or size map, then key histograms by **return value** or **`ustack`** only after a stable mode appears—controls cardinality and cognitive load ([[drill-down-analysis]], [[latency-analysis]]).
- (measurement) **Predicates** (`/comm == .../`, latency filters) keep custom programs shippable in incidents—measurement code is part of blast-radius management ([[instrumentation-overhead-and-perturbation]]).
- (abstraction) **Internals ladder**: prefer **USDT** when shipped, else **uprobes** on stable binary surfaces; JIT-heavy tiers may need **dynamic USDT** or runtime-specific symbol helpers—order is capability discovery, not taste ([[observability-vs-experimentation]], [[model-classify-intervene]]).
- (diagnosis) **Holder vs waiter** lock views echo the same causal split as other blocking investigations—pair latency histograms with “who held it” stacks before rewriting mutex code ([[resource-vs-implementation-bottleneck]]).

## Application validation

- **Bimodal RPC latency**: split latency histogram by `ustack` only after the base histogram shows two peaks—otherwise you pay map cardinality for noise.

## Concepts reused / refined / created

- Reused (heuristic): [[drill-down-analysis]]
- Reused (measurement): [[latency-analysis]]
- Reused (measurement): [[instrumentation-overhead-and-perturbation]]
- Reused (abstraction): [[observability-vs-experimentation]]
- Reused (insight): [[model-classify-intervene]]
- Reused (structure): [[resource-vs-implementation-bottleneck]]
- Reused (mechanism): [[extended-bpf]]
- Reused: [[systems-performance]]

## Links

- Concepts:
  - [[drill-down-analysis]]
  - [[latency-analysis]]
  - [[instrumentation-overhead-and-perturbation]]
  - [[observability-vs-experimentation]]
  - [[model-classify-intervene]]
  - [[resource-vs-implementation-bottleneck]]
  - [[extended-bpf]]
  - [[systems-performance]]
- Related sources:
  - [[systems-performance-syscount-ranking-and-follow-on-5-5-6]]
  - [[systems-performance-application-gotchas-missing-symbols-5-6-1]]
  - [[systems-performance-gotchas-missing-stacks-causes-5-6-2]]
