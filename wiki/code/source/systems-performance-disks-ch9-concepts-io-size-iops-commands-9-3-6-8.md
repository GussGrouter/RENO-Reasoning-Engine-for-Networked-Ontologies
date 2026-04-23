# Systems Performance — Ch.9 §9.3.6–§9.3.8 (scout PDF 460–520)

## Source

- Title: *Systems Performance: Enterprise and the Cloud* (Second Edition)
- Raw: `raw/code/pdf/Systems.Performance.Enterprise.and.the.Cloud.pdf`
- Scout: `processed/code/systems-performance-ch9-scout-p460-520.txt`
- Scope: **I/O size**, **IOPS comparability**, **non-data commands** (flush, TRIM)

## Processed artifacts

- `processed/code/systems-performance-disks-ch9-concepts-io-size-iops-commands-9-3-6-8.md`
- Chunks: `systems-performance-disks-ch9-concepts-io-size-iops-commands-9-3-6-8-chunk-000001.md`

## Extracted ideas

- **IOPS** without **randomness, size, R/W, depth, buffering** is not comparable across systems ([[measurement-validity]] **scope/semantics**).
- **Flash** often needs **different** optimal **read vs write sizes**—[[micro-benchmarking]] with vendor reality.
- **Flush/unmap** drive **busy time** without matching **application byte throughput**.

## Application validation

Procurement compares **300k IOPS** boxes: demand **full workload tuple** + **latency distribution**—else [[counters-statistics-metrics]] apples-to-oranges.

## Decision clarity

**Decision:** choose **latency- and size-qualified IOPS / bandwidth** over **headline peak IOPS** when **tail latency SLOs** apply.

## Concepts reused / refined / created

- Reused: [[throughput-latency-metrics]], [[measurement-validity]], [[micro-benchmarking]], [[counters-statistics-metrics]], [[systems-performance]]
- **Created:** none

## Links

- Concepts: [[throughput-latency-metrics]], [[measurement-validity]], [[micro-benchmarking]], [[counters-statistics-metrics]], [[systems-performance]]
