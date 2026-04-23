# Systems Performance — Ch.10 §10.5.3 Workload characterization (network) (scout PDF 520–640)

## Source

- Title: *Systems Performance: Enterprise and the Cloud* (Second Edition)
- Scout: `processed/code/systems-performance-ch10-scout-p520-640.txt` (lines **2137–2148**; file rebuilt 2026-04-20)
- Scope: describe network load in a decision-usable way

## Processed artifacts

- `processed/code/systems-performance-network-ch10-methodology-workload-characterization-basic-and-checklist-10-5-3.md`

## Extracted ideas

- Network workload needs at least three axes: **bytes/s**, **packets/s**, **connections/s**; each can dominate different bottlenecks (bandwidth, per-packet CPU, backlog/state) ([[resource-analysis-vs-workload-analysis]]).

## Decision clarity

**Decision:** choose **packets/s + connection-rate analysis** over “bandwidth upgrade” when throughput is modest but CPU/softirq or backlog symptoms indicate per-packet or per-connection overhead dominates ([[resource-analysis-vs-workload-analysis]]).

## Concepts reused / refined / created

- Reused: [[resource-analysis-vs-workload-analysis]], [[throughput-latency-metrics]], [[counters-statistics-metrics]], [[systems-performance]]
- Refined: none
- **Created:** none

## Links

- Concepts: [[resource-analysis-vs-workload-analysis]], [[throughput-latency-metrics]], [[counters-statistics-metrics]], [[systems-performance]]

