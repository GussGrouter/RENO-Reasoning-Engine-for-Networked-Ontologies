# Systems Performance — fatrace fanotify churn vs LatencyTOP aggregates (§8.6.8–§8.6.9) (scout PDF 398–460)

## Source

- Title: *Systems Performance: Enterprise and the Cloud* (Second Edition)
- Author: Brendan Gregg
- Raw: `raw/code/pdf/Systems.Performance.Enterprise.and.the.Cloud.pdf`
- Batch scope: **§8.6.8 fatrace** + **§8.6.9 LatencyTOP** (sample tables **omitted** in processed extract)

## Processed artifacts

- Scout: `processed/code/systems-performance-ch8-scout-p398-460.txt`
- Converted slice: `processed/code/systems-performance-filesystems-ch8-fatrace-latencytop-8-6-8-9.md`
- Chunks: `processed/code/systems-performance-filesystems-ch8-fatrace-latencytop-8-6-8-9-chunk-000001.md`

## Extracted ideas (with classification)

- (perturbation × rate) **fatrace** can emit **massive event volume**—CPU cost and log volume are first-class validity risks; **filtering** and **BPF alternatives** cited for relief ([[instrumentation-overhead-and-perturbation]], [[event-tracing]]).
- (representation) **LatencyTOP** aggregates **causes with percentages**—good for steering (“reading vs sync write”); **stale / kernel-option-gated** on modern kernels; author steers readers to **BPF latency tools** (§8.6.13–15) ([[extended-bpf]], [[measurement-validity]]).

## Application validation

- **Capture disk fills while running fanotify-wide tracing:** suspect **tool-induced CPU**, not workload growth—narrow event types or switch tracer class.

## Decision clarity

- **Decision:** choose **BPF latency stacks** over **LatencyTOP installs** when **kernel options aren’t already enabled** and **you cannot afford invasive rebuilds** on production-grade timelines.

## Concepts reused / refined / created

- Reused: [[event-tracing]], [[instrumentation-overhead-and-perturbation]], [[measurement-validity]], [[extended-bpf]], [[resource-analysis-vs-workload-analysis]], [[systems-performance]]
- **Created:** none

## Links

- Concepts: [[event-tracing]], [[instrumentation-overhead-and-perturbation]], [[measurement-validity]], [[extended-bpf]], [[resource-analysis-vs-workload-analysis]], [[systems-performance]]
- Related sources: [[systems-performance-filesystems-ch8-strace-syscall-latency-8-6-7]], [[systems-performance-filesystems-ch8-obs-tools-intro-8-6]]
