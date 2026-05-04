# Systems Performance — Ch.10 §10.4.1 Protocols: IP DSCP/ECN (scout PDF 520–640)

## Source

- Title: *Systems Performance: Enterprise and the Cloud* (Second Edition)
- Scout: `processed/code/systems-performance-ch10-scout-p520-640.txt` (lines **2149–2186**; file rebuilt 2026-04-20)
- Scope: protocol-layer signals for congestion handling

## Processed artifacts

- `processed/code/systems-performance-network-ch10-architecture-protocols-ip-dscp-ecn-10-4-1a.md`

## Extracted ideas

- Congestion can be signaled without drops (ECN), changing the queueing/loss story and therefore latency behavior under load ([[queueing-theory]]).

## Decision clarity

**Decision:** choose **congestion signaling investigation (ECN path support)** over “assume random loss” when drops/retransmits appear but the environment claims ECN-enabled behavior ([[queueing-theory]]).

## Concepts reused / refined / created

- Reused: [[queueing-theory]], [[cross-component-interactions]], [[systems-performance]]
- Refined: none
- **Created:** none

## Links

- Concepts: [[queueing-theory]], [[cross-component-interactions]], [[systems-performance]]

