# Systems Performance — sysctl VM tunables (§7.6.1) (PDF scout 381–400)

## Source

- Title: *Systems Performance: Enterprise and the Cloud* (Second Edition)
- Author: Brendan Gregg
- Raw: `raw/code/pdf/Systems.Performance.Enterprise.and.the.Cloud.pdf`
- Batch scope: Chapter 7, **§7.6.1** — **vm.* / kernel memory-related sysctl** patterns; **Table 7.7 omitted** (see kernel docs / book)

## Processed artifacts

- Scout: `processed/code/systems-performance-ch7-scout-p381-400.txt`
- Converted slice: `processed/code/systems-performance-memory-tuning-sysctl-vm-7-6-1.md`
- Chunks: `processed/code/systems-performance-memory-tuning-sysctl-vm-7-6-1-chunk-000001.md`

## Extracted ideas (with classification)

- (decision) **Dirty cache controls** trade **writer latency vs background flush**—**mutually exclusive byte vs ratio knobs** must be interpreted as one **representation** ([[measurement-validity]], [[caching]], [[throughput-latency-metrics]]).
- (tradeoff) **min_free_kbytes** raises **reserve headroom** vs **usable app RAM**—lowering it can accelerate **OOM** under pressure ([[static-performance-tuning]], [[measurement-validity]]).
- (tradeoff) **swappiness** tilts reclaim between **page cache** and **anonymous pages**—**not** “disable swap,” but **preference under pressure** ([[caching]], [[utilization-and-saturation]]).
- (scope) **NUMA balancing toggles** trade **automatic locality** vs **scanner CPU**—history matters for aggressiveness claims ([[cross-component-interactions]], [[measurement-validity]]).

## Application validation

- **Writers stall after tuning dirty ratios:** verify you didn’t set **bytes + ratio pairs** inconsistently—**representation drift** across hosts misorders “disk vs memory” blame.

## Decision clarity

- **Decision:** choose **raising `vm.min_free_kbytes` / tightening overcommit policy** over **raising service replica count** when **OOM kills correlate with atomic-allocation storms** and **marginal free RAM** is the repeated pattern—not when **RSS is simply too large for the SKU**.

## Concepts reused / refined / created

- Reused: [[static-performance-tuning]], [[measurement-validity]], [[caching]], [[throughput-latency-metrics]], [[utilization-and-saturation]], [[cross-component-interactions]], [[systems-performance]]
- **Created:** none

## Links

- Concepts: [[static-performance-tuning]], [[measurement-validity]], [[caching]], [[throughput-latency-metrics]], [[utilization-and-saturation]], [[cross-component-interactions]], [[systems-performance]]
- Related sources: [[systems-performance-memory-tuning-huge-pages-7-6-2]]
