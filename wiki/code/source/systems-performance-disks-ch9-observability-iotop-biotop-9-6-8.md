# Systems Performance — Ch.9 §9.6.8 iotop, biotop

## Source

- Title: *Systems Performance: Enterprise and the Cloud* (Second Edition)
- Scout: `processed/code/systems-performance-ch9-scout-p460-520.txt`
- Scope: **§9.6.8**

## Processed artifacts

- `processed/code/systems-performance-disks-ch9-observability-iotop-biotop-9-6-8.md`
- Chunks: `*-chunk-000001.md`

## Extracted ideas

- **Two “tops,” two substrates:** **kernel accounting** (`iotop`) vs **BPF block taps** (`biotop`)—when they disagree on write load, **believe neither until calibrated** ([[measurement-validity]] **representation**).
- **Per-process disk blame** remains **best-effort** once I/O is **asynchronously issued** ([[resource-analysis-vs-workload-analysis]]).

## Application hook

Before tuning **cgroup I/O limits** from **`iotop`**: **spot-check with `biotop`** on a known workload so you do not chase **undercounted** numbers.

## Decision clarity

**Decision:** choose **`biotop`** over **`iotop`** as the **sanity reference** when **`iotop` write rates** fail a **simple reproducible experiment**.

## Concepts reused / refined / created

- Reused: [[measurement-validity]], [[resource-analysis-vs-workload-analysis]], [[throughput-latency-metrics]], [[systems-performance]]
- **Created:** none

## Links

- Concepts: [[measurement-validity]], [[resource-analysis-vs-workload-analysis]], [[throughput-latency-metrics]], [[systems-performance]]
