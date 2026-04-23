# Systems Performance — /sys observability interface (4.3.2) (PDF pages 171–220)

## Source

- Title: *Systems Performance: Enterprise and the Cloud* (Second Edition)
- Author: Brendan Gregg
- Raw: `raw/code/pdf/Systems.Performance.Enterprise.and.the.Cloud.pdf`
- Batch scope: Chapter 4, Section 4.3.2 /sys

## Processed artifacts

- Converted slice: `processed/code/systems-performance-sysfs-observability-4-3-2.md`
- Chunks:
  - `processed/code/systems-performance-sysfs-observability-4-3-2-chunk-000001.md`

## Extracted ideas (with classification)

- (mechanism) `sysfs` provides a **directory-oriented** view of many device and subsystem statistics, often with a very large surface area (tens of thousands of files), mixing read-only telemetry and writable controls.
- (abstraction) Compared to `/proc`, `sysfs` reflects a different historical evolution: a structured tree for kernel/driver objects rather than “mostly top-level misc stats.”

## Concepts reused / refined / created

- Reused (structure): [[kernel-user-boundary]]
- Reused (mechanism): [[system-call]]
- Reused (structure): [[counters-statistics-metrics]]
- Reused: [[systems-performance]]

## Links

- Concepts:
  - [[kernel-user-boundary]]
  - [[system-call]]
  - [[counters-statistics-metrics]]
  - [[systems-performance]]
