# Systems Performance — Ch.10 §10.3.8 Interface negotiation (scout PDF 520–640)

## Source

- Title: *Systems Performance: Enterprise and the Cloud* (Second Edition)
- Scout: `processed/code/systems-performance-ch10-scout-p520-640.txt` (lines **1242–1260**; file rebuilt 2026-04-20)
- Scope: negotiated capacity as a prerequisite for utilization claims

## Processed artifacts

- `processed/code/systems-performance-network-ch10-concepts-interface-negotiation-10-3-8.md`

## Extracted ideas

- “Link bandwidth” is not always the advertised maximum; utilization calculations depend on the **negotiated** mode and directionality ([[throughput-latency-metrics]], [[counters-statistics-metrics]]).

## Decision clarity

**Decision:** choose **verify negotiated speed/duplex** over “tune TCP” when observed throughput caps at a round-number step (e.g., 1G → 100M) suggesting downshift, not congestion control ([[resource-vs-implementation-bottleneck]]).

## Concepts reused / refined / created

- Reused: [[throughput-latency-metrics]], [[counters-statistics-metrics]], [[resource-vs-implementation-bottleneck]], [[systems-performance]]
- Refined: none
- **Created:** none

## Links

- Concepts: [[throughput-latency-metrics]], [[counters-statistics-metrics]], [[resource-vs-implementation-bottleneck]], [[systems-performance]]

