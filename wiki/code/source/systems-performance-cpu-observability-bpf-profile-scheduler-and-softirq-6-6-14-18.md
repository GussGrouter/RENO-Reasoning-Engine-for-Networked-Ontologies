# Systems Performance — BPF sampling, scheduler latency, and softirq CPU time (6.6.14–6.6.18) (PDF 286–320)

## Source

- Title: *Systems Performance: Enterprise and the Cloud* (Second Edition)
- Author: Brendan Gregg
- Raw: `raw/code/pdf/Systems.Performance.Enterprise.and.the.Cloud.pdf`
- Batch scope: Chapter 6, **§6.6.14–6.6.18** — sample-based stack tools, **on-CPU duration**, **run-queue latency/length**, **softirq time** (interrupt-path CPU consumers often absent from plain on-CPU profiles)

## Processed artifacts

- Converted slice: `processed/code/systems-performance-cpu-observability-bpf-profile-scheduler-and-softirq-6-6-14-18.md`
- Chunks:
  - `processed/code/systems-performance-cpu-observability-bpf-profile-scheduler-and-softirq-6-6-14-18-chunk-000001.md`

## Extracted ideas (with classification)

- (measurement) **Scheduler wait histograms** separate **runnable delay** from **on-CPU work**—critical for “CPU looks fine” stories ([[utilization-and-saturation]], [[throughput-latency-metrics]]).
- (diagnosis) **Softirq/hardirq time** can dominate cycles **without appearing** in typical user/kernel stack profiles—treat interrupt planes as **first-class CPU consumers** ([[measurement-validity]], [[throughput-latency-metrics]]).
- (mechanism) **In-kernel aggregation (BPF)** is the recurring pattern to keep **high-rate sampling** production-safe ([[extended-bpf]], [[instrumentation-overhead-and-perturbation]]).

## Application validation

- **DB tail latency**: run-queue latency grows while **user stacks idle** → capacity story is **scheduling/CPU quota**, not query plans alone.

## Decision clarity

- **Decision**: choose **run-queue latency + throttle metrics** over **mean CPU%** when **p99** tracks **runnable queuing** more than **instruction hotspots**.

## Concepts reused / refined / created

- Reused (structure): [[utilization-and-saturation]]
- Reused (structure): [[throughput-latency-metrics]]
- Reused (abstraction): [[measurement-validity]]
- Reused (mechanism): [[extended-bpf]]
- Reused (abstraction): [[instrumentation-overhead-and-perturbation]]
- Reused (measurement): [[sampling-based-profiling]]
- Reused: [[systems-performance]]

## Links

- Concepts:
  - [[utilization-and-saturation]]
  - [[throughput-latency-metrics]]
  - [[measurement-validity]]
  - [[extended-bpf]]
  - [[instrumentation-overhead-and-perturbation]]
  - [[sampling-based-profiling]]
  - [[systems-performance]]
- Related sources:
  - [[systems-performance-cpu-observability-perf-profiling-and-pmcs-6-6-13]]
  - [[systems-performance-cpu-interrupt-gpu-tools-and-distribution-visualizations-6-6-19-6-7-4]]
