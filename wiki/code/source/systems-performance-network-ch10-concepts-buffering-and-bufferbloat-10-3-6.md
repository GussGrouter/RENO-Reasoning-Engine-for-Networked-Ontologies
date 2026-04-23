# Systems Performance — Ch.10 §10.3.6 Buffering (bufferbloat) (scout PDF 520–640)

## Source

- Title: *Systems Performance: Enterprise and the Cloud* (Second Edition)
- Scout: `processed/code/systems-performance-ch10-scout-p520-640.txt` (lines **1207–1228**; file rebuilt 2026-04-20)
- Scope: buffering as a throughput vs latency trade via queueing

## Processed artifacts

- `processed/code/systems-performance-network-ch10-concepts-buffering-and-bufferbloat-10-3-6.md`

## Extracted ideas

- Buffering can hide RTT for throughput, but it also creates **queues** that add latency; treat bufferbloat as a queueing-driven latency issue ([[queueing-theory]], [[throughput-latency-metrics]]).
- Intermediate buffers are cross-component: “network” may look slow because of queuing policy in switches/routers, not endpoint CPU ([[cross-component-interactions]]).

## Application validation

If throughput is fine but tail latency explodes under load, suspect **queue growth** (bufferbloat) before optimizing packet processing code.

## Decision clarity

**Decision:** choose **queueing diagnosis** over “increase buffers” when latency grows with load and symptoms match backlog/queue growth (delay propagation) ([[queueing-theory]]).

## Concepts reused / refined / created

- Reused: [[queueing-theory]], [[throughput-latency-metrics]], [[cross-component-interactions]], [[systems-performance]]
- Refined: none
- **Created:** none

## Links

- Concepts: [[queueing-theory]], [[throughput-latency-metrics]], [[cross-component-interactions]], [[systems-performance]]

