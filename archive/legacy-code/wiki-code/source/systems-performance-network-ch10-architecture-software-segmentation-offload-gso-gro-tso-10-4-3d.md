# Systems Performance — Ch.10 §10.4.3 Software: segmentation offload (GSO/GRO/TSO) (scout PDF 520–640)

## Source

- Title: *Systems Performance: Enterprise and the Cloud* (Second Edition)
- Scout: `processed/code/systems-performance-ch10-scout-p520-640.txt` (lines **1737–1931**; file rebuilt 2026-04-20)
- Scope: reduce per-packet overhead without changing MTU/MSS

## Processed artifacts

- `processed/code/systems-performance-network-ch10-architecture-software-segmentation-offload-gso-gro-tso-10-4-3d.md`

## Extracted ideas

- Offload is an implementation-level throughput lever: it reduces CPU/stack overhead per byte, which can shift bottlenecks from CPU to link or vice versa ([[resource-vs-implementation-bottleneck]]).

## Decision clarity

**Decision:** choose **enable/verify segmentation offload** over “raise MTU” when you need higher throughput but MTU changes are risky and the bottleneck is per-packet processing overhead ([[resource-vs-implementation-bottleneck]]).

## Concepts reused / refined / created

- Reused: [[resource-vs-implementation-bottleneck]], [[throughput-latency-metrics]], [[systems-performance]]
- Refined: none
- **Created:** none

## Links

- Concepts: [[resource-vs-implementation-bottleneck]], [[throughput-latency-metrics]], [[systems-performance]]

