# Systems Performance — systemd (3.4.2) (PDF pages 118–170)

## Source

- Title: *Systems Performance: Enterprise and the Cloud* (Second Edition)
- Author: Brendan Gregg
- Raw: `raw/code/pdf/Systems.Performance.Enterprise.and.the.Cloud.pdf`
- Batch scope: Chapter 3, Section 3.4.2 systemd

## Processed artifacts

- Converted slice: `processed/code/systems-performance-systemd-3-4-2.md`
- Chunks:
  - `processed/code/systems-performance-systemd-3-4-2-chunk-000001.md`

## Extracted ideas (with classification)

- (diagnosis) Boot-time performance work benefits from a dependency-aware critical path view: the slowest serial chain dominates end-to-end startup latency.
- (measurement) Service manager timing outputs expose kernel vs userspace time and per-unit latency contributions (treat as structured latency evidence, not as “the tool itself” as a concept).

## Concepts reused / refined / created

- Reused (heuristic): [[latency-analysis]]
- Reused (heuristic): [[static-performance-tuning]]
- Reused (measurement): [[throughput-latency-metrics]]

## Links

- Concepts:
  - [[latency-analysis]]
  - [[static-performance-tuning]]
  - [[throughput-latency-metrics]]
