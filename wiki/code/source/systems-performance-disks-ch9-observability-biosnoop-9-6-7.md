# Systems Performance — Ch.9 §9.6.7 biosnoop

## Source

- Title: *Systems Performance: Enterprise and the Cloud* (Second Edition)
- Scout: `processed/code/systems-performance-ch9-scout-p460-520.txt`
- Scope: **§9.6.7**

## Processed artifacts

- `processed/code/systems-performance-disks-ch9-observability-biosnoop-9-6-7.md`
- Chunks: `*-chunk-000001.md`

## Extracted ideas

- **Per-I/O timeline** exposes **queue ladder** patterns (**same start time, rising completion latency**) that averages erase ([[latency-analysis]], [[queueing-theory]] as intuition, not formal modeling).
- **Outlier triage:** sort by **latency**, then **rewind wall-clock** to see **precursors** vs **reordering** vs **supervisor-delay-like gaps** ([[drill-down-analysis]]).
- **Guests:** extreme tails may be **hypervisor scheduling**, not storage—validate environment ([[measurement-validity]] **representation**).
- **`-Q`:** splits **OS queue** vs **device** latency—same decision axis as **biolatency -Q** ([[measurement-validity]] **scope/semantics**).

## Decision clarity

**Decision:** choose **per-event tracing + sort-by-tail** over **dashboard means** when **SLO hits are rare** but expensive.

## Concepts reused / refined / created

- Reused: [[latency-analysis]], [[drill-down-analysis]], [[queueing-theory]], [[measurement-validity]], [[extended-bpf]], [[systems-performance]]
- **Created:** none

## Links

- Concepts: [[latency-analysis]], [[drill-down-analysis]], [[queueing-theory]], [[measurement-validity]], [[extended-bpf]], [[systems-performance]]
