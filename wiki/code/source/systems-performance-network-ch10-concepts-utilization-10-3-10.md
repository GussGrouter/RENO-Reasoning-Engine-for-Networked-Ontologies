# Systems Performance — Ch.10 §10.3.10 Utilization (network) (scout PDF 520–640)

## Source

- Title: *Systems Performance: Enterprise and the Cloud* (Second Edition)
- Scout: `processed/code/systems-performance-ch10-scout-p520-640.txt` (lines **1278–1298**; file rebuilt 2026-04-20)
- Scope: utilization as throughput/bandwidth with negotiation and unit caveats

## Processed artifacts

- `processed/code/systems-performance-network-ch10-concepts-utilization-10-3-10.md`

## Extracted ideas

- Utilization is a **throughput-derived** metric; it must be computed with the correct negotiated bandwidth and per-direction perspective ([[throughput-latency-metrics]], [[utilization-and-saturation]]).
- Packet-count-only tools can’t support byte-based utilization claims when packet sizes vary (this is a **representation** limitation; use bytes if you need utilization) ([[counters-statistics-metrics]]).

## Application validation

If a “pps” dashboard is flat but bytes/sec changes, don’t interpret pps as utilization; validate with byte counters before concluding “link saturated.”

## Decision clarity

**Decision:** choose **byte throughput** over **packet counts** when estimating link utilization and packet size can vary (e.g., mixed request sizes) ([[counters-statistics-metrics]]).

## Concepts reused / refined / created

- Reused: [[throughput-latency-metrics]], [[utilization-and-saturation]], [[counters-statistics-metrics]], [[systems-performance]]
- Refined: none
- **Created:** none

## Links

- Concepts: [[throughput-latency-metrics]], [[utilization-and-saturation]], [[counters-statistics-metrics]], [[systems-performance]]

