# Systems Performance — Cycle analysis + CPU performance monitoring (6.5.5–6.5.6) (PDF 286–320)

## Source

- Title: *Systems Performance: Enterprise and the Cloud* (Second Edition)
- Author: Brendan Gregg
- Raw: `raw/code/pdf/Systems.Performance.Enterprise.and.the.Cloud.pdf`
- Batch scope: Chapter 6, **§6.5.5** cycle analysis (IPC first, stall typing, overflow sampling caveats) + **§6.5.6** monitoring (per-CPU utilization, quota-aware recording, interval vs burst)

## Processed artifacts

- Converted slice: `processed/code/systems-performance-cpu-cycle-analysis-and-performance-monitoring-6-5-5-6.md`
- Chunks:
  - `processed/code/systems-performance-cpu-cycle-analysis-and-performance-monitoring-6-5-5-6-chunk-000001.md`

## Extracted ideas (with classification)

- (diagnosis) **IPC gates the next question**: low IPC → **stall taxonomy**; high IPC → **instruction reduction / algorithm**—thresholds are **SKU-relative**, learn them with **known workloads** ([[throughput-latency-metrics]], [[counters-statistics-metrics]]).
- (measurement) **Overflow-triggered attribution** trades **sparse interrupts** for **approximate instruction blame** (skid / OOO)—tight claims need **precise-event mechanisms** when available ([[sampling-based-profiling]], [[measurement-validity]]).
- (measurement) **Monitoring interval hides microbursts**—use **per-CPU series** and **saturation-adjacent signals**; sub-second forensics is a **different instrument class** than 5-minute archives ([[measurement-validity]], [[utilization-and-saturation]]).

## Application validation

- **Dashboard shows <20% CPU but p99 spikes**: raise **collection resolution** or add **run-queue / throttling** signals before concluding “not CPU.”

## Decision clarity

- **Decision**: choose **1s (or finer) per-CPU utilization + saturation sidecars** over **5-minute rollups only** when defending **latency SLOs** against **short CPU bursts**.

## Concepts reused / refined / created

- Reused (structure): [[throughput-latency-metrics]]
- Reused (structure): [[counters-statistics-metrics]]
- Reused (measurement): [[sampling-based-profiling]]
- Reused (abstraction): [[measurement-validity]]
- Reused (structure): [[utilization-and-saturation]]
- Reused: [[systems-performance]]

## Links

- Concepts:
  - [[throughput-latency-metrics]]
  - [[counters-statistics-metrics]]
  - [[sampling-based-profiling]]
  - [[measurement-validity]]
  - [[utilization-and-saturation]]
  - [[systems-performance]]
- Related sources:
  - [[systems-performance-cpu-profiling-methodology-sampling-vs-instrumentation-6-5-4]]
  - [[systems-performance-cpu-static-performance-tuning-checklist-6-5-7]]
