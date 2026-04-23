# Systems Performance — Ch.10 §10.2.1 Network interface (model) (scout PDF 520–640)

## Source

- Title: *Systems Performance: Enterprise and the Cloud* (Second Edition)
- Scout: `processed/code/systems-performance-ch10-scout-p520-640.txt` (lines **925–938**; file rebuilt 2026-04-20)
- Scope: interface as a measurement boundary

## Processed artifacts

- `processed/code/systems-performance-network-ch10-models-network-interface-10-2-1.md`

## Extracted ideas

- Use the **interface boundary** to avoid mixing populations (per-link TX/RX behavior vs system-wide) ([[counters-statistics-metrics]], [[measurement-validity]] only if conflicting definitions arise).

## Decision clarity

**Decision:** choose **per-interface** counters over **system-wide** aggregates when symptoms are localized (single VLAN/ENI/NIC) and aggregate views hide contention ([[counters-statistics-metrics]]).

## Concepts reused / refined / created

- Reused: [[counters-statistics-metrics]], [[systems-performance]]
- Refined: none
- **Created:** none

## Links

- Concepts: [[counters-statistics-metrics]], [[systems-performance]]

