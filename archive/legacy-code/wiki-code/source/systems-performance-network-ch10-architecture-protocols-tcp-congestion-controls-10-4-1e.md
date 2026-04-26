# Systems Performance — Ch.10 §10.4.1 Protocols: TCP congestion controls (scout PDF 520–640)

## Source

- Title: *Systems Performance: Enterprise and the Cloud* (Second Edition)
- Scout: `processed/code/systems-performance-ch10-scout-p520-640.txt` (lines **2149–2186**; file rebuilt 2026-04-20)
- Scope: algorithm choice as a workload/path-dependent performance lever

## Processed artifacts

- `processed/code/systems-performance-network-ch10-architecture-protocols-tcp-congestion-controls-10-4-1e.md`

## Extracted ideas

- Congestion control is a tunable intervention whose impact depends on path conditions; treat it as **static tuning** after you’ve characterized loss/RTT/bandwidth regime ([[static-performance-tuning]], [[queueing-theory]]).

## Decision clarity

**Decision:** choose **change congestion control algorithm** over “add bandwidth” when evidence indicates loss/RTT dynamics dominate and the current algorithm is a poor fit for the path regime ([[static-performance-tuning]]).

## Concepts reused / refined / created

- Reused: [[static-performance-tuning]], [[queueing-theory]], [[systems-performance]]
- Refined: none
- **Created:** none

## Links

- Concepts: [[static-performance-tuning]], [[queueing-theory]], [[systems-performance]]

