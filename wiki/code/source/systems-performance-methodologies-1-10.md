# Systems Performance — methodologies (1.10) (PDF page 54)

## Source

- Title: *Systems Performance: Enterprise and the Cloud* (Second Edition)
- Author: Brendan Gregg
- Raw: `raw/code/pdf/Systems.Performance.Enterprise.and.the.Cloud.pdf`
- Batch scope: Chapter 1, Section 1.10 Methodologies + 1.10.1 Linux Perf Analysis in 60 Seconds (tool-based checklist)

## Processed artifacts

- Converted slice: `processed/code/systems-performance-methodologies-1-10.md`
- Chunks:
  - `processed/code/systems-performance-methodologies-1-10-chunk-000001.md`

## Extracted ideas (with classification)

- (diagnosis) Methodologies are documented procedures that reduce “fishing expeditions” and help avoid overlooking important areas.
- (diagnosis) A first-pass tool-based checklist can be executed quickly to triage common bottleneck classes and guide deeper drill-down.
- (measurement) The checklist is grounded in readily available metrics (load averages, errors, CPU usage, disk I/O, memory, network stats) that provide fast situational awareness.

## Concepts reused / refined / created

- Reused (diagnosis): [[resource-vs-implementation-bottleneck]] (the checklist is explicitly aimed at quickly checking for bottlenecks before deeper analysis).
- Reused (measurement): [[counters-statistics-metrics]] (checklist consumes derived statistics/metrics).

## Links

- Concepts:
  - [[resource-vs-implementation-bottleneck]]
  - [[counters-statistics-metrics]]

