# Systems Performance — Ch.9 §9.6.6 biolatency

## Source

- Title: *Systems Performance: Enterprise and the Cloud* (Second Edition)
- Scout: `processed/code/systems-performance-ch9-scout-p460-520.txt`
- Scope: **§9.6.6**

## Processed artifacts

- `processed/code/systems-performance-disks-ch9-observability-biolatency-9-6-6.md`
- Chunks: `*-chunk-000001.md`

## Extracted ideas

- **Histogram first:** multimodal shape drives **different hypotheses** than **mean `await`** alone ([[multimodal-latency-distribution]], [[metric-visualization]]).
- **Flag-split (`-F`):** separates **policy paths** (sync write vs readahead) that share a device but not a tuning lever ([[throughput-latency-metrics]]).
- **`-Q` widens the interval:** OS queue vs device—compare definitions before optimizing the wrong queue ([[measurement-validity]] **scope/semantics**).
- BPF implementation note: ties **kernel-space aggregation** pattern to [[extended-bpf]].

## Application hook

Seeing **two peaks** pushes you to ask **which I/O flavors** land in each—not just “disk slow”.

## Concepts reused / refined / created

- Reused: [[multimodal-latency-distribution]], [[metric-visualization]], [[throughput-latency-metrics]], [[measurement-validity]], [[extended-bpf]], [[systems-performance]]
- **Created:** none

## Links

- Concepts: [[multimodal-latency-distribution]], [[metric-visualization]], [[throughput-latency-metrics]], [[measurement-validity]], [[extended-bpf]], [[systems-performance]]
