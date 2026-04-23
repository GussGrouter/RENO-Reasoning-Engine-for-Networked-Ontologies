# Systems Performance — Ch.10 §10.4.3 Software: CPU scaling for packets (scout PDF 520–640)

## Source

- Title: *Systems Performance: Enterprise and the Cloud* (Second Edition)
- Scout: `processed/code/systems-performance-ch10-scout-p520-640.txt` (lines **1737–1931**; file rebuilt 2026-04-20)
- Scope: avoid single-CPU softirq bottlenecks under packet load

## Processed artifacts

- `processed/code/systems-performance-network-ch10-architecture-software-cpu-scaling-rss-rps-rfs-xps-irqbalance-10-4-3h.md`

## Extracted ideas

- Packet processing can be CPU-saturated on one core even when aggregate CPU looks fine; USE-style CPU saturation must include softirq hotspots and load distribution ([[use-method]], [[utilization-and-saturation]]).

## Application validation

If overall CPU is ~30% but one core shows high softirq and throughput caps, prioritize steering/IRQ distribution before tuning TCP.

## Decision clarity

**Decision:** choose **packet steering / IRQ balancing** over “add more cores” when one CPU is saturated (softirq) and traffic can be distributed across queues/CPUs ([[utilization-and-saturation]]).

## Concepts reused / refined / created

- Reused: [[use-method]], [[utilization-and-saturation]], [[cross-component-interactions]], [[systems-performance]]
- Refined: none
- **Created:** none

## Links

- Concepts: [[use-method]], [[utilization-and-saturation]], [[cross-component-interactions]], [[systems-performance]]

