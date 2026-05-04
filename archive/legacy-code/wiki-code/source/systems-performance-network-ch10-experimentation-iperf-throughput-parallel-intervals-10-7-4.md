# Systems Performance — Ch.10 §10.7.4 iperf (scout PDF 520–640)

## Source

- Title: *Systems Performance: Enterprise and the Cloud* (Second Edition)
- Scout: `processed/code/systems-performance-ch10-scout-p520-640.txt`
- Scope: **controlled throughput experiment** + how to read **interval rates vs run averages**

## Processed artifacts

- `processed/code/systems-performance-network-ch10-experimentation-iperf-throughput-parallel-intervals-10-7-4.md`

## Extracted ideas

- **Per-interval bandwidth** exposes **variance / stability**; the **final average** can hide short stalls that matter for **tails**—treat interval rows as first-class evidence ([[throughput-latency-metrics]]).
- **Parallelism** is often a **generator-side limiter**: if adding `-P` changes the ceiling, you may have measured **client stack saturation**, not “WAN speed” ([[resource-vs-implementation-bottleneck]]).
- **Buffer settings change the experiment’s queueing environment** on the hosts—misaligned client/server buffers can create **queueing/backpressure** that dominates results ([[queueing-theory]]).
- This is [[micro-benchmarking]] discipline: falsify “is the path capable?” before deep app tracing ([[observability-vs-experimentation]]).

## Decision clarity

**Decision:** choose **`iperf` with interval rows + parallelism sweep** over a **single headline number** when you must distinguish **stable line rate** from **burst then collapse** behavior ([[throughput-latency-metrics]]).

## Application validation

- **“100G can’t fill”:** if `-P 1` plateaus but `-P 8` jumps, your next decision is **host threading/driver**, not buying more WAN ([[resource-vs-implementation-bottleneck]]).

## Concepts reused / refined / created

- Reused: [[micro-benchmarking]], [[throughput-latency-metrics]], [[queueing-theory]], [[resource-vs-implementation-bottleneck]], [[observability-vs-experimentation]], [[systems-performance]]
- Refined: none
- **Created:** none

## Links

- Concepts: [[micro-benchmarking]], [[throughput-latency-metrics]], [[queueing-theory]], [[resource-vs-implementation-bottleneck]], [[observability-vs-experimentation]], [[systems-performance]]
