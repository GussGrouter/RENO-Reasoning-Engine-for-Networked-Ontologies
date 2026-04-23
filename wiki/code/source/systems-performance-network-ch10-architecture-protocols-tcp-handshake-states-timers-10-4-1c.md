# Systems Performance — Ch.10 §10.4.1 Protocols: TCP handshake/states/timers (scout PDF 520–640)

## Source

- Title: *Systems Performance: Enterprise and the Cloud* (Second Edition)
- Scout: `processed/code/systems-performance-ch10-scout-p520-640.txt` (lines **2149–2186**; file rebuilt 2026-04-20)
- Scope: connection setup latency and state/timer effects

## Processed artifacts

- `processed/code/systems-performance-network-ch10-architecture-protocols-tcp-handshake-states-timers-10-4-1c.md`

## Extracted ideas

- Connection establishment latency can include loss/retransmit waits; treat it as a queueing/loss amplification problem under load, not just “RTT” ([[queueing-theory]], [[throughput-latency-metrics]]).

## Decision clarity

**Decision:** choose **handshake/retransmit investigation** over “optimize request handler” when the symptom is slow connects and evidence points to handshake delays (drops/timeouts), before application code runs ([[queueing-theory]]).

## Concepts reused / refined / created

- Reused: [[queueing-theory]], [[throughput-latency-metrics]], [[systems-performance]]
- Refined: none
- **Created:** none

## Links

- Concepts: [[queueing-theory]], [[throughput-latency-metrics]], [[systems-performance]]

