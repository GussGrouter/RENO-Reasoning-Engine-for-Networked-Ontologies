# Systems Performance — Ch.9 §9.4.3 RAID Table 9.3 + RMW + caches (scout PDF 460–520)

## Source

- Title: *Systems Performance: Enterprise and the Cloud* (Second Edition)
- Scout: `processed/code/systems-performance-ch9-scout-p460-520.txt`
- Scope: **Table 9.3** summarized in processed text; **RMW**, **controller cache**, **vendor background tasks**

## Processed artifacts

- `processed/code/systems-performance-disks-ch9-architecture-raid-table-rmw-9-4-3b.md`

## Extracted ideas

- **RAID level** sets **read parallelism vs write penalty**—parity schemes tax **small random writes** unless **full-stripe** aligned ([[throughput-latency-metrics]], [[caching]]).
- **Virtual disk** observability gap + **cache ACK** semantics ([[measurement-validity]] **representation**).

## Decision clarity

**Decision:** choose **mirror or dedicated log devices** over **parity RAID** when **sync random write tail latency** dominates and **stripe alignment** cannot be enforced.

## Concepts reused / refined / created

- Reused: [[throughput-latency-metrics]], [[caching]], [[cross-component-interactions]], [[measurement-validity]], [[static-performance-tuning]], [[systems-performance]]
- **Created:** none

## Links

- Concepts: [[throughput-latency-metrics]], [[caching]], [[cross-component-interactions]], [[measurement-validity]], [[static-performance-tuning]], [[systems-performance]]
