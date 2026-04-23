# Systems Performance — Ch.10 §10.4.1 Protocols: TCP throughput + features (scout PDF 520–640)

## Source

- Title: *Systems Performance: Enterprise and the Cloud* (Second Edition)
- Scout: `processed/code/systems-performance-ch10-scout-p520-640.txt` (lines **2149–2186**; file rebuilt 2026-04-20)
- Scope: TCP mechanisms as performance levers (without turning them into concepts)

## Processed artifacts

- `processed/code/systems-performance-network-ch10-architecture-protocols-tcp-throughput-and-features-10-4-1b.md`

## Extracted ideas

- TCP performance is primarily a **queueing and control** story: windows/buffers hide RTT for throughput; congestion control prevents overload collapse ([[queueing-theory]], [[throughput-latency-metrics]]).

## Decision clarity

**Decision:** choose **queueing + congestion-control hypotheses** over “increase bandwidth” when throughput drops under load and symptoms include retransmits/ACK dynamics (control reacting to congestion) ([[queueing-theory]]).

## Concepts reused / refined / created

- Reused: [[queueing-theory]], [[throughput-latency-metrics]], [[systems-performance]]
- Refined: none
- **Created:** none

## Links

- Concepts: [[queueing-theory]], [[throughput-latency-metrics]], [[systems-performance]]

