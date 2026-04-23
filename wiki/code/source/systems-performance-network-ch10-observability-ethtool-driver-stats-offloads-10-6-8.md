# Systems Performance — Ch.10 §10.6.8 ethtool (scout PDF 520–640)

## Source

- Title: *Systems Performance: Enterprise and the Cloud* (Second Edition)
- Scout: `processed/code/systems-performance-ch10-scout-p520-640.txt` (lines **3122–3185**; file rebuilt 2026-04-20)
- Scope: NIC-level static facts + saturation/error counters that vary by driver

## Processed artifacts

- `processed/code/systems-performance-network-ch10-observability-ethtool-driver-stats-offloads-10-6-8.md`

## Extracted ideas

- **Vendor-specific `-S` counters** are strongest as **localized evidence** (queue stops, DMA errors, per-queue drops) pointing to **which NIC queue path** is hurting—combine with stack/interface counters so drops/retransmits stay framed as [[queueing-theory]] consequences, then narrow the queue ([[resource-vs-implementation-bottleneck]] often “implementation/driver path”).
- **Offload state (`-k`) shapes where work runs** (NIC vs CPU): mismatches can look like “slow network” while the real constraint is **host CPU segmentation/interrupt load**—decide using [[use-method]] (CPU saturation + NIC throughput ceilings) rather than folklore.
- **`[fixed]` offload lines** imply **representation limits** on what you can change live—don’t assume `ethtool -K` will fix throughput if the ecosystem locked the setting ([[measurement-validity]] **scope/semantics**: tunable visibility vs capability).

## Decision clarity

**Decision:** choose **`ethtool -k/-S` sanity** over application tuning when throughput is capped and **`ss`/stack stats hint “needs segmentation/GRO/GSO alignment” or driver-queue stops** ([[static-performance-tuning]]).

## Application validation

- **Low line rate + high CPU on networking stack threads:** inspect `-k` for segmentation/offload mismatches **before** blaming WAN loss—otherwise you chase **retransmit tails** that are partly **CPU/software path** artifacts ([[resource-vs-implementation-bottleneck]]).

## Concepts reused / refined / created

- Reused: [[static-performance-tuning]], [[queueing-theory]], [[use-method]], [[resource-vs-implementation-bottleneck]], [[measurement-validity]], [[systems-performance]]
- Refined: none
- **Created:** none

## Links

- Concepts: [[static-performance-tuning]], [[queueing-theory]], [[use-method]], [[resource-vs-implementation-bottleneck]], [[measurement-validity]], [[systems-performance]]
