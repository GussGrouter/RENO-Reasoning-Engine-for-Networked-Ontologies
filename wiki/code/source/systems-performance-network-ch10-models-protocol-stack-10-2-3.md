# Systems Performance — Ch.10 §10.2.3 Protocol stack (model) (scout PDF 520–640)

## Source

- Title: *Systems Performance: Enterprise and the Cloud* (Second Edition)
- Scout: `processed/code/systems-performance-ch10-scout-p520-640.txt` (lines **957–998**; file rebuilt 2026-04-20)
- Scope: protocol layers as performance scope boundaries

## Processed artifacts

- `processed/code/systems-performance-network-ch10-models-protocol-stack-10-2-3.md`

## Extracted ideas

- Layering changes what “latency” means (connect vs RTT vs first-byte); use the right layer for the claim ([[throughput-latency-metrics]]).
- Extra layers (tunnel/security) introduce extra work; treat them as **cross-component interactions** when performance changes after enabling them ([[cross-component-interactions]]).

## Decision clarity

**Decision:** choose **layer-specific measurement** over a single “network latency” metric when the hypothesis depends on *where* delay is introduced (handshake vs transfer vs tunnel overhead) ([[throughput-latency-metrics]]).

## Concepts reused / refined / created

- Reused: [[throughput-latency-metrics]], [[cross-component-interactions]], [[systems-performance]]
- Refined: none
- **Created:** none

## Links

- Concepts: [[throughput-latency-metrics]], [[cross-component-interactions]], [[systems-performance]]

