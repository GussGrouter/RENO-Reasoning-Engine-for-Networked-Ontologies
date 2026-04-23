# Systems Performance — Load averages and system-wide CPU statistics (6.6.1–6.6.4) (PDF 286–320)

## Source

- Title: *Systems Performance: Enterprise and the Cloud* (Second Edition)
- Author: Brendan Gregg
- Raw: `raw/code/pdf/Systems.Performance.Enterprise.and.the.Cloud.pdf`
- Batch scope: Chapter 6, **§6.6** observability framing + **§6.6.1–6.6.4** (uptime/load semantics, `vmstat`/`mpstat`/`sar` as *examples* of aggregate and per-CPU views)

## Processed artifacts

- Converted slice: `processed/code/systems-performance-cpu-observability-load-and-system-wide-stats-6-6-1-4.md`
- Chunks:
  - `processed/code/systems-performance-cpu-observability-load-and-system-wide-stats-6-6-1-4-chunk-000001.md`

## Extracted ideas (with classification)

- (measurement) **Load averages are a damped demand signal**, not a universal definition of “CPU queue depth”—**semantic portability** matters more than the three numbers themselves ([[measurement-validity]], [[utilization-and-saturation]]).
- (diagnosis) **Trend of 1/5/15** answers “is pressure building or fading?” faster than arguing absolute thresholds—use as a **coarse triage clock**, not a deep model ([[use-method]], [[throughput-latency-metrics]]).
- (measurement) **Per-CPU vs system-wide splits** expose **parallelism shape** (hot CPUs vs uniform utilization) that global averages hide ([[counters-statistics-metrics]], [[measurement-validity]]).

## Application validation

- **Incident triage**: if 1-min load ≫ 15-min load while user CPU looks flat, suspect **non-CPU contributors** to Linux load semantics before buying cores.

## Decision clarity

- **Decision**: choose **per-CPU utilization + run-queue/saturation sidecars** over **load-average-only dashboards** when diagnosing **scheduler imbalance** on multi-CPU hosts.

## Concepts reused / refined / created

- Reused (abstraction): [[measurement-validity]]
- Reused (structure): [[utilization-and-saturation]]
- Reused (heuristic): [[use-method]]
- Reused (structure): [[throughput-latency-metrics]]
- Reused (structure): [[counters-statistics-metrics]]
- Reused: [[systems-performance]]

## Links

- Concepts:
  - [[measurement-validity]]
  - [[utilization-and-saturation]]
  - [[use-method]]
  - [[throughput-latency-metrics]]
  - [[counters-statistics-metrics]]
  - [[systems-performance]]
- Related sources:
  - [[systems-performance-cpu-micro-benchmarking-decision-rules-6-5-11]]
  - [[systems-performance-cpu-observability-process-attribution-and-clock-tools-6-6-5-12]]
