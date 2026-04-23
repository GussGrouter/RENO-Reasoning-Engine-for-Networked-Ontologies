# Systems Performance — Ch.10 §10.4.2 Hardware: interfaces + controllers (scout PDF 520–640)

## Source

- Title: *Systems Performance: Enterprise and the Cloud* (Second Edition)
- Scout: `processed/code/systems-performance-ch10-scout-p520-640.txt` (lines **1614–1736**; file rebuilt 2026-04-20)
- Scope: capacity ceilings beyond “line rate”

## Processed artifacts

- `processed/code/systems-performance-network-ch10-architecture-hardware-interfaces-and-controllers-10-4-2a.md`

## Extracted ideas

- Treat “network bandwidth” as multi-stage: **port**, **controller**, and **I/O transport** can each be the limiter ([[resource-vs-implementation-bottleneck]], [[cross-component-interactions]]).

## Decision clarity

**Decision:** choose **controller/transport ceiling checks** over “optimize TCP” when throughput caps below aggregate port bandwidth and matches a known bus limit (e.g., PCIe generation/lanes) ([[resource-vs-implementation-bottleneck]]).

## Concepts reused / refined / created

- Reused: [[resource-vs-implementation-bottleneck]], [[cross-component-interactions]], [[systems-performance]]
- Refined: none
- **Created:** none

## Links

- Concepts: [[resource-vs-implementation-bottleneck]], [[cross-component-interactions]], [[systems-performance]]

