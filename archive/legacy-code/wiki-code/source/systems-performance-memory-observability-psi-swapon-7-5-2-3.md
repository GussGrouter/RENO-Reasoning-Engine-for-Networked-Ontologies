# Systems Performance — PSI + swapon (§7.5.2–§7.5.3) (PDF scout 320–380)

## Source

- Title: *Systems Performance: Enterprise and the Cloud* (Second Edition)
- Author: Brendan Gregg
- Raw: `raw/code/pdf/Systems.Performance.Enterprise.and.the.Cloud.pdf`
- Batch scope: Chapter 7, **§7.5.2–§7.5.3** — **PSI memory** stall lines + **swapon** inventory

## Processed artifacts

- Scout: `processed/code/systems-performance-ch7-scout-p320-380.txt`
- Converted slice: `processed/code/systems-performance-memory-observability-psi-swapon-7-5-2-3.md`
- Chunks: `processed/code/systems-performance-memory-observability-psi-swapon-7-5-2-3-chunk-000001.md`

## Extracted ideas (with classification)

- (structure) **PSI exposes saturation as time-stalled**, not just **occupancy**: **some vs full** answers **partial vs complete** memory stalls—match the line to **SLO cohort semantics** ([[utilization-and-saturation]], [[measurement-validity]]).
- (scope) **PSI can be tracked per cgroup2**: pressure may be **local to a service** while **host free** looks fine ([[cross-component-interactions]], [[measurement-validity]]).
- (measurement) **Swap configured vs active**: swapon shows **capacity**; **si/so / PSI** show **whether swap is on the critical path** ([[throughput-latency-metrics]]).

## Application validation

- **Microservice latency spikes:** compare **PSI “some” for the service cgroup** with **host-wide free**—if only the former spikes, fix **limits/working set**, not **DRAM purchase**.

## Decision clarity

- **Decision:** choose **cgroup-level PSI + swap usage** over **datacenter “memory utilization %” charts** when **software-enforced caps** can stall threads **before** the machine runs out of DIMMs.

## Concepts reused / refined / created

- Reused (structure): [[utilization-and-saturation]], [[cross-component-interactions]]
- Reused (measurement): [[measurement-validity]], [[throughput-latency-metrics]]
- Reused: [[systems-performance]]
- **Created:** none

## Links

- Concepts: [[utilization-and-saturation]], [[cross-component-interactions]], [[measurement-validity]], [[throughput-latency-metrics]], [[systems-performance]]
- Related sources: [[systems-performance-memory-observability-vmstat-7-5-1]], [[systems-performance-memory-observability-sar-7-5-4]]
