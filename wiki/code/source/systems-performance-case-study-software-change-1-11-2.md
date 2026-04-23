# Systems Performance — case study: software change (1.11.2) (PDF pages 56–64)

## Source

- Title: *Systems Performance: Enterprise and the Cloud* (Second Edition)
- Author: Brendan Gregg
- Raw: `raw/code/pdf/Systems.Performance.Enterprise.and.the.Cloud.pdf`
- Batch scope: Chapter 1, Section 1.11.2 (case study)

## Processed artifacts

- Converted slice: `processed/code/systems-performance-case-study-software-change-1-11-2.md`
- Chunks:
  - `processed/code/systems-performance-case-study-software-change-1-11-2-chunk-000001.md`

## Extracted ideas (with classification)

- (diagnosis) Non-regression testing is an experimentation-driven approach: compare current vs new version under controlled load to detect performance regressions.
- (diagnosis) A throughput ceiling requires checking all components in the datapath (server, client, network, generator) rather than assuming the server is limiting.
- (measurement) Workload characterization matters: a simulator that matches only the average can miss variance-driven issues; workload mismatch is a measurement risk.
- (diagnosis) If resource checks show idle servers but throughput is capped, consider constraints outside the server (e.g., client generator limits) and confirm via drill-down.
- (measurement) Normalizing resource usage per unit work (e.g., CPU utilization at a fixed request rate) can reveal regressions even when throughput ceilings are identical.
- (measurement) Profiling can be used after regression detection to localize increased CPU cost to code paths (visualization mentioned, tool specifics omitted).

## Concepts reused / refined / created

- Reused (measurement): [[observability-vs-experimentation]] (controlled experiments for regression testing).
- Reused (measurement): [[throughput-latency-metrics]] (throughput ceilings and per-request normalization framing).
- Reused (diagnosis): [[resource-vs-implementation-bottleneck]] (distinguishing “server resource limit” vs “elsewhere in system” bottleneck).
- Reused (diagnosis): [[cross-component-interactions]] (datapath components interact; the limiter may not be where you first look).

## Links

- Concepts:
  - [[observability-vs-experimentation]]
  - [[throughput-latency-metrics]]
  - [[resource-vs-implementation-bottleneck]]
  - [[cross-component-interactions]]

