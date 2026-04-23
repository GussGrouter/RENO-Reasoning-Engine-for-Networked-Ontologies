# Systems Performance — Ch.10 §10.5.2 USE method (network) (scout PDF 520–640)

## Source

- Title: *Systems Performance: Enterprise and the Cloud* (Second Edition)
- Scout: `processed/code/systems-performance-ch10-scout-p520-640.txt` (lines **2093–2136**; file rebuilt 2026-04-20)
- Scope: fast bottleneck screening for network paths

## Processed artifacts

- `processed/code/systems-performance-network-ch10-methodology-use-method-network-interfaces-10-5-2.md`

## Extracted ideas

- USE works best when applied **per direction** (TX vs RX) and when utilization uses the right denominator (negotiated speed and/or imposed limit) ([[use-method]], [[utilization-and-saturation]]).
- Retransmits can indicate saturation, but they are path-scoped; treat them as a queueing hypothesis trigger rather than a definitive “interface saturated” claim ([[queueing-theory]]).

## Decision clarity

**Decision:** choose **per-interface, per-direction USE** over aggregate network charts when symptoms are localized (one host/link) and you need to isolate where queueing begins ([[use-method]]).

## Concepts reused / refined / created

- Reused: [[use-method]], [[utilization-and-saturation]], [[queueing-theory]], [[throughput-latency-metrics]], [[systems-performance]]
- Refined: none
- **Created:** none

## Links

- Concepts: [[use-method]], [[utilization-and-saturation]], [[queueing-theory]], [[throughput-latency-metrics]], [[systems-performance]]

