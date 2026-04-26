# Systems Performance — Ch.10 §10.4.2 Hardware: switches/routers + rate transitions (scout PDF 520–640)

## Source

- Title: *Systems Performance: Enterprise and the Cloud* (Second Edition)
- Scout: `processed/code/systems-performance-ch10-scout-p520-640.txt` (lines **1614–1736**; file rebuilt 2026-04-20)
- Scope: shared devices as queueing + bottleneck sources

## Processed artifacts

- `processed/code/systems-performance-network-ch10-architecture-hardware-switches-routers-rate-transitions-10-4-2b.md`

## Extracted ideas

- Switch/router buffering and CPU limits create queueing latency; treat shared infrastructure as part of the bottleneck graph ([[queueing-theory]], [[cross-component-interactions]]).
- Rate transitions are a classic queue growth trigger; diagnose via backlog/delay propagation before changing endpoints ([[queueing-theory]]).

## Application validation

If traffic bursts from 10G into a 1G segment and p99 inflates, suspect queue growth at the transition point (bufferbloat) before tuning TCP on hosts.

## Decision clarity

**Decision:** choose **queueing diagnosis at rate transitions** over “increase host buffers” when latency inflation correlates with bursts and a known link-speed step-down exists ([[queueing-theory]]).

## Concepts reused / refined / created

- Reused: [[queueing-theory]], [[cross-component-interactions]], [[systems-performance]]
- Refined: none
- **Created:** none

## Links

- Concepts: [[queueing-theory]], [[cross-component-interactions]], [[systems-performance]]

