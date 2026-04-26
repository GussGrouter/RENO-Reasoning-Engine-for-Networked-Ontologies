# Systems Performance — Ch.10 §10.1 Terminology (scout PDF 520–640)

## Source

- Title: *Systems Performance: Enterprise and the Cloud* (Second Edition)
- Scout: `processed/code/systems-performance-ch10-scout-p520-640.txt` (lines **892–919**; file rebuilt 2026-04-20)
- Scope: network vocabulary needed for performance claims

## Processed artifacts

- `processed/code/systems-performance-network-ch10-terminology-10-1.md`

## Extracted ideas

- Performance claims often fail because terms are mixed: **bandwidth (cap)** vs **throughput (observed)** vs **latency (time cost)** ([[throughput-latency-metrics]], [[counters-statistics-metrics]]).
- Unit discipline matters: **packet vs frame** boundaries and **socket** API scope can change what a measurement actually refers to ([[counters-statistics-metrics]]).

## Decision clarity

**Decision:** choose **latency decomposition** over “upgrade bandwidth” when **throughput is below link bandwidth but user-visible time is dominated by waits**, not transfer rate ([[throughput-latency-metrics]]).

## Concepts reused / refined / created

- Reused: [[throughput-latency-metrics]], [[counters-statistics-metrics]], [[systems-performance]]
- Refined: none
- **Created:** none

## Links

- Concepts: [[throughput-latency-metrics]], [[counters-statistics-metrics]], [[systems-performance]]

