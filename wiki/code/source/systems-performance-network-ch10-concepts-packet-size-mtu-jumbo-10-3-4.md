# Systems Performance — Ch.10 §10.3.4 Packet size (MTU/jumbo/fragmentation) (scout PDF 520–640)

## Source

- Title: *Systems Performance: Enterprise and the Cloud* (Second Edition)
- Scout: `processed/code/systems-performance-ch10-scout-p520-640.txt` (lines **1071–1108**; file rebuilt 2026-04-20)
- Scope: packet-size choices as a throughput/latency and reliability trade

## Processed artifacts

- `processed/code/systems-performance-network-ch10-concepts-packet-size-mtu-jumbo-10-3-4.md`

## Extracted ideas

- Packet size is a coupled knob: larger units reduce per-packet overhead (throughput win) but increase compatibility and drop/fragmentation risk ([[throughput-latency-metrics]]).
- Misconfigured middleboxes (e.g., blocking ICMP) can make MTU changes look like “random loss,” so treat MTU as a **scope boundary** when debugging sudden retransmits ([[cross-component-interactions]]).

## Application validation

If enabling jumbo frames increases retransmits/timeouts, suspect **path MTU/ICMP handling** before tuning application retries.

## Decision clarity

**Decision:** choose **MTU/path validation** over “increase timeouts” when latency spikes coincide with packet-size changes and show loss/retransmit symptoms (queueing/loss rather than CPU) ([[cross-component-interactions]]).

## Concepts reused / refined / created

- Reused: [[throughput-latency-metrics]], [[cross-component-interactions]], [[systems-performance]]
- Refined: none
- **Created:** none

## Links

- Concepts: [[throughput-latency-metrics]], [[cross-component-interactions]], [[systems-performance]]

