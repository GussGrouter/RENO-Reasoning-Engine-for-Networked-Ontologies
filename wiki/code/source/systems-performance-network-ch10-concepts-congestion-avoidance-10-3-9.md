# Systems Performance — Ch.10 §10.3.9 Congestion avoidance (scout PDF 520–640)

## Source

- Title: *Systems Performance: Enterprise and the Cloud* (Second Edition)
- Scout: `processed/code/systems-performance-ch10-scout-p520-640.txt` (lines **1261–1277**; file rebuilt 2026-04-20)
- Scope: congestion as queueing + loss behavior under load

## Processed artifacts

- `processed/code/systems-performance-network-ch10-concepts-congestion-avoidance-10-3-9.md`

## Extracted ideas

- Under load, performance collapse often comes from **queueing + drops + retransmits**, not just raw bandwidth; treat it as a queueing system and look for backlog and delay propagation ([[queueing-theory]]).

## Decision clarity

**Decision:** choose **queueing/backlog reasoning** over “increase bandwidth” when throughput degrades with increasing load and retransmit-like symptoms appear (drop-driven delay amplification) ([[queueing-theory]], [[throughput-latency-metrics]]).

## Concepts reused / refined / created

- Reused: [[queueing-theory]], [[throughput-latency-metrics]], [[cross-component-interactions]], [[systems-performance]]
- Refined: none
- **Created:** none

## Links

- Concepts: [[queueing-theory]], [[throughput-latency-metrics]], [[cross-component-interactions]], [[systems-performance]]

