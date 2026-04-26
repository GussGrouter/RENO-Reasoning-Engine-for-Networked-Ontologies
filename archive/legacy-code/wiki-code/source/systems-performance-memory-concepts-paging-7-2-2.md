# Systems Performance — Paging: file cache vs anonymous swap (7.2.2) (PDF 321–360 extract)

## Source

- Title: *Systems Performance: Enterprise and the Cloud* (Second Edition)
- Author: Brendan Gregg
- Raw: `raw/code/pdf/Systems.Performance.Enterprise.and.the.Cloud.pdf`
- Batch scope: Chapter 7, **§7.2.2** — **page movement**, **file-system paging** vs **anonymous paging (“swap”)**, and **clean vs dirty** eviction semantics

## Processed artifacts

- Converted slice: `processed/code/systems-performance-memory-concepts-paging-7-2-2.md`
- Chunks:
  - `processed/code/systems-performance-memory-concepts-paging-7-2-2-chunk-000001.md`

## Extracted ideas (with classification)

- (structure) **Two paging species** imply **two latency stories**: **file cache** churn can be “normal,” while **anonymous swap-ins** usually mean **hard memory shortage** with **user-visible stalls** ([[throughput-latency-metrics]], [[utilization-and-saturation]]).
- (mechanism) **“Page-out” includes non-write frees** for clean cache pages—**representation** of “disk writes” metrics can miss that memory was still reclaimed ([[measurement-validity]], [[caching]]).
- (structure) **Fast swap media** reframes anonymous paging from “always bad” to **intentional tiering**—the decision is whether your **SLO + economics** endorse that trade ([[throughput-latency-metrics]], [[cross-component-interactions]]).

## Application validation

- **High page-out rate but low app latency**: separate **clean cache reclaim** from **anonymous swap** before buying more **DRAM** or faster **disks**.

## Decision clarity

- **Decision**: choose **anonymous paging / PSI memory stall** investigation over **file cache eviction tuning** when **application RSS** grows into **swap** but **disk cache** is not the dominant allocator story.

## Concepts reused / refined / created

- Reused (structure): [[throughput-latency-metrics]]
- Reused (structure): [[utilization-and-saturation]]
- Reused (abstraction): [[measurement-validity]]
- Reused (mechanism): [[caching]]
- Reused (structure): [[cross-component-interactions]]
- Reused: [[systems-performance]]

## Links

- Concepts:
  - [[throughput-latency-metrics]]
  - [[utilization-and-saturation]]
  - [[measurement-validity]]
  - [[caching]]
  - [[cross-component-interactions]]
  - [[systems-performance]]
- Related sources:
  - [[systems-performance-memory-concepts-virtual-memory-7-2-1]]
  - [[systems-performance-memory-concepts-demand-paging-7-2-3]]
