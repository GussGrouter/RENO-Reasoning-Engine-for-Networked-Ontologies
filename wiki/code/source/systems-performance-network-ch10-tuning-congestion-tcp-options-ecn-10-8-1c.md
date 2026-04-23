# Systems Performance — Ch.10 §10.8.1 system-wide tuning — congestion/options/ECN (scout PDF 520–640)

## Source

- Title: *Systems Performance: Enterprise and the Cloud* (Second Edition)
- Scout: `processed/code/systems-performance-ch10-scout-p520-640.txt` (lines **4621–4655**; file rebuilt 2026-04-20)
- Scope: **how congestion control + a few TCP behaviors change loss/latency trade-offs**

## Processed artifacts

- `processed/code/systems-performance-network-ch10-tuning-congestion-tcp-options-ecn-10-8-1c.md`

## Extracted ideas

- **Congestion control is a policy choice** over how aggressively to probe bandwidth vs react to loss/delay; wrong choice shows up as **throughput cliffs** or **bufferbloat inflation** ([[throughput-latency-metrics]]).
- **Slow start after idle** can reintroduce **burstiness** after quiet periods—useful for safety, harmful for steady micro-latency if idle is common ([[queueing-theory]] tails).
- **SACK** changes how loss is repaired (fewer go-back-N episodes); turning it off usually hurts tails on lossy/wide paths ([[queueing-theory]]).
- **ECN** moves some congestion signals earlier (mark vs drop), but requires **end-to-end support**; mis-scoped enablement is a **representation risk** if you interpret “no drops” as “no congestion” ([[measurement-validity]] **representation**).

## Decision clarity

**Decision:** choose **ECN experiments** over **blind cwnd inflation** when you can validate switches/queues mark correctly and your metrics distinguish **marks vs drops** ([[measurement-validity]]).

## Application validation

- **Idle-sensitive APIs:** if p99 spikes after quiet seconds, test `tcp_slow_start_after_idle` behavior as a hypothesis before rewriting app code ([[queueing-theory]]).

## Concepts reused / refined / created

- Reused: [[throughput-latency-metrics]], [[queueing-theory]], [[measurement-validity]], [[systems-performance]]
- Refined: none
- **Created:** none

## Links

- Concepts: [[throughput-latency-metrics]], [[queueing-theory]], [[measurement-validity]], [[systems-performance]]
