# Systems Performance — drsnoop + wss + bpftrace + other sources (§7.5.11–§7.5.14) (PDF scout 381–400)

## Source

- Title: *Systems Performance: Enterprise and the Cloud* (Second Edition)
- Author: Brendan Gregg
- Raw: `raw/code/pdf/Systems.Performance.Enterprise.and.the.Cloud.pdf`
- Batch scope: Chapter 7, **§7.5.11–§7.5.14** — **direct reclaim latency**, **experimental WSS**, **bpftrace** patterns + overhead warnings; **Table 7.6 omitted** in processed extract; misc `/proc`, **dmidecode** cloud caveat

## Processed artifacts

- Scout: `processed/code/systems-performance-ch7-scout-p381-400.txt`
- Converted slice: `processed/code/systems-performance-memory-observability-trace-other-7-5-11-14.md`
- Chunks: `processed/code/systems-performance-memory-observability-trace-other-7-5-11-14-chunk-000001.md`

## Extracted ideas (with classification)

- (measurement) **Direct reclaim tracing maps stall time to reclaim episodes**—expected **low frequency** ⇒ often **low perturbation**; still validate **burst behavior** on pathological workloads ([[instrumentation-overhead-and-perturbation]], [[measurement-validity]]).
- (tradeoff) **WSS via PTE accessed bits is experimental**: explicit **lab vs prod** boundary ([[observability-vs-experimentation]], [[scientific-method]]).
- (perturbation) **High-frequency memory events + uprobes** can **2× slow** targets—prefer **aggregation / fewer probes** ([[instrumentation-overhead-and-perturbation]], [[extended-bpf]]).
- (scope) **Hardware inventory (dmidecode) unavailable on many clouds**—don’t gate decisions on **static DRAM SKU** signals you cannot see ([[static-performance-tuning]], [[measurement-validity]]).

## Application validation

- **Latency aligns with reclaim:** use **direct-reclaim latency distribution** to justify **vertical scale / limits lift** vs **code change**—if ms-scale stalls cluster under load, **capacity policy** may win faster than micro-opts.

## Decision clarity

- **Decision:** choose **kernel-side aggregation (BPF maps / summaries) + rare tracepoints first** over **per-event malloc uprobes** when **allocation rate is millions/sec** and **observer effect** would dominate the profile.

## Concepts reused / refined / created

- Reused (measurement): [[instrumentation-overhead-and-perturbation]], [[measurement-validity]]
- Reused (tradeoff): [[observability-vs-experimentation]]
- Reused (method): [[scientific-method]]
- Reused (structure): [[extended-bpf]]
- Reused (heuristic): [[static-performance-tuning]]
- Reused: [[systems-performance]]
- **Created:** none

## Links

- Concepts: [[instrumentation-overhead-and-perturbation]], [[measurement-validity]], [[observability-vs-experimentation]], [[scientific-method]], [[extended-bpf]], [[static-performance-tuning]], [[systems-performance]]
- Related sources: [[systems-performance-memory-observability-perf-7-5-10]]
