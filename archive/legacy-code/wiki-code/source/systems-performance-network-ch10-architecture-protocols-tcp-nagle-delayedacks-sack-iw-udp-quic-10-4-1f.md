# Systems Performance — Ch.10 §10.4.1 Protocols: TCP tuning knobs; UDP/QUIC tradeoffs (scout PDF 520–640)

## Source

- Title: *Systems Performance: Enterprise and the Cloud* (Second Edition)
- Scout: `processed/code/systems-performance-ch10-scout-p520-640.txt` (lines **2149–2186**; file rebuilt 2026-04-20)
- Scope: protocol-level throughput/latency tradeoffs and tuning risks

## Processed artifacts

- `processed/code/systems-performance-network-ch10-architecture-protocols-tcp-nagle-delayedacks-sack-iw-udp-quic-10-4-1f.md`

## Extracted ideas

- Small-packet reduction (Nagle/delayed ACK) is a **throughput vs latency** trade; disable only when it conflicts with workload latency requirements ([[throughput-latency-metrics]], [[static-performance-tuning]]).
- Protocol choice changes reliability/congestion behavior (UDP vs TCP/QUIC) and thus changes queueing dynamics under load ([[queueing-theory]]).

## Application validation

If RPC p99 is dominated by “small message waits,” consider whether coalescing behavior (Nagle/delayed ACK) is inflating latency before scaling hardware.

## Decision clarity

**Decision:** choose **disable Nagle (or adjust delayed ACK)** over “increase timeouts” when workload is latency-sensitive, messages are small, and evidence indicates coalescing delays dominate ([[static-performance-tuning]], [[throughput-latency-metrics]]).

## Concepts reused / refined / created

- Reused: [[static-performance-tuning]], [[throughput-latency-metrics]], [[queueing-theory]], [[systems-performance]]
- Refined: none
- **Created:** none

## Links

- Concepts: [[static-performance-tuning]], [[throughput-latency-metrics]], [[queueing-theory]], [[systems-performance]]

