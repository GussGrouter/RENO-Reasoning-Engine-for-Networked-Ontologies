# Systems Performance — utilization + saturation (2.3.11–2.3.12) (PDF pages 70–75)

## Source

- Title: *Systems Performance: Enterprise and the Cloud* (Second Edition)
- Author: Brendan Gregg
- Raw: `raw/code/pdf/Systems.Performance.Enterprise.and.the.Cloud.pdf`
- Batch scope: Chapter 2, Sections 2.3.11–2.3.12 (utilization definitions; saturation/queueing)

## Processed artifacts

- Converted slice: `processed/code/systems-performance-utilization-and-saturation-2-3-11-2-3-12.md`
- Chunks:
  - `processed/code/systems-performance-utilization-and-saturation-2-3-11-2-3-12-chunk-000001.md`

## Extracted ideas (with classification)

- (measurement) Time-based utilization (“percent busy”) is \(U = B/T\) and is the utilization most commonly provided by OS tools.
- (diagnosis) High time-based utilization can correlate with contention and degraded performance, but “100% busy” does not necessarily mean “100% capacity”.
- (measurement) Capacity-based utilization defines utilization as proportion of deliverable throughput capacity; it implies inability to accept more work at 100%.
- (diagnosis) Saturation is excess requested work that must queue; any saturation increases latency (waiting).
- (diagnosis) Queueing/saturation may begin before 100% time-based utilization when resources can process work in parallel.

## Concepts reused / refined / created

- Refined (diagnosis): [[utilization-and-saturation]] (added explicit time-based vs capacity-based distinction and “100% busy ≠ 100% capacity”).

## Links

- Concepts:
  - [[utilization-and-saturation]]

