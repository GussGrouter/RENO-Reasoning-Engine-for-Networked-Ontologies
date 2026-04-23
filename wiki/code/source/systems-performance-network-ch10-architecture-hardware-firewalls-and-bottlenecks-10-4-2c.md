# Systems Performance — Ch.10 §10.4.2 Hardware: firewalls as bottlenecks (scout PDF 520–640)

## Source

- Title: *Systems Performance: Enterprise and the Cloud* (Second Edition)
- Scout: `processed/code/systems-performance-ch10-scout-p520-640.txt` (lines **1614–1736**; file rebuilt 2026-04-20)
- Scope: policy devices as hidden performance limiters

## Processed artifacts

- `processed/code/systems-performance-network-ch10-architecture-hardware-firewalls-and-bottlenecks-10-4-2c.md`

## Extracted ideas

- Firewalls can be the true limiting resource (CPU/memory/state tables), so treat “network slow” as cross-component until policy devices are exonerated ([[cross-component-interactions]], [[resource-vs-implementation-bottleneck]]).

## Decision clarity

**Decision:** choose **firewall bottleneck hypothesis** over “optimize services” when latency correlates with connection churn and the path includes stateful inspection (per-connection state pressure) ([[cross-component-interactions]]).

## Concepts reused / refined / created

- Reused: [[cross-component-interactions]], [[resource-vs-implementation-bottleneck]], [[systems-performance]]
- Refined: none
- **Created:** none

## Links

- Concepts: [[cross-component-interactions]], [[resource-vs-implementation-bottleneck]], [[systems-performance]]

