# Systems Performance — Ch.9 §9.6.2 sar (disk)

## Source

- Title: *Systems Performance: Enterprise and the Cloud* (Second Edition)
- Scout: `processed/code/systems-performance-ch9-scout-p460-520.txt`
- Scope: **§9.6.2**

## Processed artifacts

- `processed/code/systems-performance-disks-ch9-observability-sar-9-6-2.md`
- Chunks: `*-chunk-000001.md`

## Extracted ideas

- **`sar -d`** replays the **same conceptual metrics class** as **`iostat -x`** for **trend / historical** slices ([[time-series-monitoring]], [[counters-statistics-metrics]]).
- **Deprecated `svctm`:** naive **service-time split** misleading on **parallel devices**—align mental model with **issue→complete** latency ([[measurement-validity]] **representation**).

## Application hook

Use **`sar`** when you need **“what did disks look like last Tuesday”**—not different physics, **different retention**.

## Concepts reused / refined / created

- Reused: [[time-series-monitoring]], [[counters-statistics-metrics]], [[measurement-validity]], [[systems-performance]]
- **Created:** none

## Links

- Concepts: [[time-series-monitoring]], [[counters-statistics-metrics]], [[measurement-validity]], [[systems-performance]]
