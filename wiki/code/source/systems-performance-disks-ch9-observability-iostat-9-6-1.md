# Systems Performance — Ch.9 §9.6.1 iostat

## Source

- Title: *Systems Performance: Enterprise and the Cloud* (Second Edition)
- Scout: `processed/code/systems-performance-ch9-scout-p460-520.txt`
- Scope: **§9.6.1**

## Processed artifacts

- `processed/code/systems-performance-disks-ch9-observability-iostat-9-6-1.md`
- Chunks: `*-chunk-000001.md`

## Extracted ideas

- **Block-device lens:** FS-heavy work may **hide** behind cache—**absence on `iostat` is not absence of I/O pain** ([[measurement-validity]] **scope/semantics**).
- **USE columns:** **`await`**, **`aqu-sz`**, **`%util`**—but **`%util`** is **not** a universal capacity scalar for **virtual/aggregated** devices ([[use-method]], [[utilization-and-saturation]], [[measurement-validity]] **representation**).
- **Split reads/writes** in extended output to avoid **write-back noise** diluting **read SLO tracking** ([[throughput-latency-metrics]]).

## Application hook

When **`%util` looks fine** but apps stall: **verify whether you are measuring the same layer the app waits on** before buying disks.

## Decision clarity

**Decision:** choose **read/write-separated extended stats** over **blended disk averages** when **writes are mostly cached** but **reads dominate tail latency**.

## Concepts reused / refined / created

- Reused: [[counters-statistics-metrics]], [[throughput-latency-metrics]], [[use-method]], [[utilization-and-saturation]], [[measurement-validity]], [[systems-performance]]
- **Created:** none

## Links

- Concepts: [[counters-statistics-metrics]], [[throughput-latency-metrics]], [[use-method]], [[utilization-and-saturation]], [[measurement-validity]], [[systems-performance]]
