# Systems Performance — Hardirq time, BPF one-liners, GPU observability gap, distribution views (6.6.19–6.7.4) (PDF 321–360)

## Source

- Title: *Systems Performance: Enterprise and the Cloud* (Second Edition)
- Author: Brendan Gregg
- Raw: `raw/code/pdf/Systems.Performance.Enterprise.and.the.Cloud.pdf`
- Batch scope: Chapter 6, **§6.6.19–6.6.20** + “other tools” + **§6.7** through **FlameScope** — focuses on **what decisions these views enable**, not cataloging colors or vendor UIs

## Processed artifacts

- Converted slice: `processed/code/systems-performance-cpu-interrupt-gpu-tools-and-distribution-visualizations-6-6-19-6-7-4.md`
- Chunks:
  - `processed/code/systems-performance-cpu-interrupt-gpu-tools-and-distribution-visualizations-6-6-19-6-7-4-chunk-000001.md`

## Extracted ideas (with classification)

- (measurement) **Hardirq time by vector** answers “which device path burns CPU **outside** thread stacks?”—orthogonal to user-level profiling ([[measurement-validity]], [[throughput-latency-metrics]]).
- (abstraction) **GPU/server offload observability is fragmented**—end-to-end decisions require an explicit **second measurement plane** (device metrics + transfer boundaries) ([[cross-component-interactions]], [[observability-vs-experimentation]]).
- (measurement) **Utilization distributions and sub-second structure** exist because **means hide bimodality** and **within-second burstiness**—pick representations that preserve **multimodality** when fleets are large ([[latency-heatmap]], [[measurement-validity]]).
- (abstraction) **Time-range selection before aggregation** (FlameScope pattern) preserves **short perturbations** that disappear in full-window profiles ([[shift-computation-in-time]], [[sampling-based-profiling]]).

## Application validation

- **Cloud-wide CPU heat map**: a thin **100% line** with a dark mass near idle implies **a few hot shards**—shard placement/rebalance before cluster scale-out.

## Decision clarity

- **Decision**: choose **distribution / subsecond views + narrow-window flame summaries** over **single full-window flame graphs** when the hypothesis is **brief scheduler stalls or lock convoys**.

## Concepts reused / refined / created

- Reused (abstraction): [[measurement-validity]]
- Reused (structure): [[throughput-latency-metrics]]
- Reused (structure): [[cross-component-interactions]]
- Reused (abstraction): [[observability-vs-experimentation]]
- Reused (measurement): [[latency-heatmap]]
- Reused (abstraction): [[shift-computation-in-time]]
- Reused (measurement): [[sampling-based-profiling]]
- Reused: [[systems-performance]]

## Links

- Concepts:
  - [[measurement-validity]]
  - [[throughput-latency-metrics]]
  - [[cross-component-interactions]]
  - [[observability-vs-experimentation]]
  - [[latency-heatmap]]
  - [[shift-computation-in-time]]
  - [[sampling-based-profiling]]
  - [[systems-performance]]
- Related sources:
  - [[systems-performance-cpu-observability-bpf-profile-scheduler-and-softirq-6-6-14-18]]
  - [[systems-performance-cpu-experimentation-adhoc-and-sysbench-6-8]]
