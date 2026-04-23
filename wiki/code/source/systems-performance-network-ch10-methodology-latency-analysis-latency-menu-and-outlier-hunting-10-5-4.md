# Systems Performance — Ch.10 §10.5.4 Latency analysis (network) (scout PDF 520–640)

## Source

- Title: *Systems Performance: Enterprise and the Cloud* (Second Edition)
- Scout: `processed/code/systems-performance-ch10-scout-p520-640.txt` (lines **2187–2259**; file rebuilt 2026-04-20)
- Scope: pick latency measures that localize the delay source

## Processed artifacts

- `processed/code/systems-performance-network-ch10-methodology-latency-analysis-latency-menu-and-outlier-hunting-10-5-4.md`

## Extracted ideas

- Latency analysis works by measuring multiple latency types and subdividing: isolate network-path latency vs endpoint think time vs kernel/interrupt/stack delay ([[latency-analysis]], [[throughput-latency-metrics]]).
- Retransmit-driven outliers require distribution views or per-op traces with threshold filters ([[latency-outliers]]).

## Decision clarity

**Decision:** choose **multi-latency decomposition (DNS/ping/connect/TTFB)** over a single “network latency” number when you need to separate path RTT from endpoint overload and kernel stack delay ([[latency-analysis]]).

## Concepts reused / refined / created

- Reused: [[latency-analysis]], [[throughput-latency-metrics]], [[latency-outliers]], [[metric-visualization]], [[systems-performance]]
- Refined: none
- **Created:** none

## Links

- Concepts: [[latency-analysis]], [[throughput-latency-metrics]], [[latency-outliers]], [[metric-visualization]], [[systems-performance]]

