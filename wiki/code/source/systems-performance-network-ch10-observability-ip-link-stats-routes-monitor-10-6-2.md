# Systems Performance — Ch.10 §10.6.2 ip (scout PDF 520–640)

## Source

- Title: *Systems Performance: Enterprise and the Cloud* (Second Edition)
- Scout: `processed/code/systems-performance-ch10-scout-p520-640.txt` (lines **2603–2659**; file rebuilt 2026-04-20)
- Scope: interface + routing observability as static/sanity + USE inputs

## Processed artifacts

- `processed/code/systems-performance-network-ch10-observability-ip-link-stats-routes-monitor-10-6-2.md`

## Extracted ideas

- **Drops/overruns/errors** on an interface are **saturation/error signals** at the NIC/driver boundary: they usually create **retransmits and tail latency downstream**—classify as [[queueing-theory]] consequences until you identify the bounded resource (buffers, scheduler, bandwidth).
- **Cumulative counters** demand **delta math** for “how bad right now?”; comparing two snapshots answers rate questions ([[counters-statistics-metrics]]).
- **Routing mistakes** can dominate latency/loss without “CPU problems”; this pairs with [[static-performance-tuning]] (correct path selection) before micro-optimizing TCP.

## Decision clarity

**Decision:** choose **`ip -s link` + route review** over socket tracing when symptoms match **misconfigured NIC state**, **link errors**, or **wrong route precedence** ([[static-performance-tuning]]).

## Application validation

- **Incumbent route regression:** after infra changes, compare **`ip route`** to golden expectations; a worse-than-default static can raise RTT and inflate **timeouts/retransmits** as **queueing-on-the-wrong-path** symptoms ([[cross-component-interactions]]).

## Concepts reused / refined / created

- Reused: [[use-method]], [[queueing-theory]], [[counters-statistics-metrics]], [[static-performance-tuning]], [[cross-component-interactions]], [[systems-performance]]
- Refined: none
- **Created:** none

## Links

- Concepts: [[use-method]], [[queueing-theory]], [[counters-statistics-metrics]], [[static-performance-tuning]], [[cross-component-interactions]], [[systems-performance]]
