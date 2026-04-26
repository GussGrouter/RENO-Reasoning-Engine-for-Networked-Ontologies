# Systems Performance — Memory chapter intro and parts map (Ch. 7 open) (PDF 321–360 extract)

## Source

- Title: *Systems Performance: Enterprise and the Cloud* (Second Edition)
- Author: Brendan Gregg
- Raw: `raw/code/pdf/Systems.Performance.Enterprise.and.the.Cloud.pdf`
- Batch scope: **Chapter 7 Memory** — **problem framing** (pressure → paging/OOM), **CPU costs** of allocation/mapping, **NUMA locality**, and **chapter part map** (terminology → architecture → methodology → tools → tuning)

## Processed artifacts

- Converted slice: `processed/code/systems-performance-memory-chapter-intro-and-parts-7.md`
- Chunks:
  - `processed/code/systems-performance-memory-chapter-intro-and-parts-7-chunk-000001.md`

## Extracted ideas (with classification)

- (structure) **Memory pressure** is a **throughput → latency phase change**: once physical memory is exhausted, the system pays **orders-of-magnitude slower** paths (storage-backed movement, killer policies) ([[throughput-latency-metrics]], [[utilization-and-saturation]]).
- (structure) **Allocator + mapper work** is real **CPU service demand**—memory chapters are not “off-CPU only”; they interact with **run-queue time** and **fault handling** ([[cross-component-interactions]], [[throughput-latency-metrics]]).
- (abstraction) **NUMA locality** is the same **coupling** pattern as CPU chapters: “fast vs far” memory is a **topology** constraint on **valid comparisons** ([[cross-component-interactions]], [[measurement-validity]]).

## Application validation

- **“Disk slow” after traffic spike**: check **memory pressure first**—paging/saturation can **inflate I/O queues** even when disks are healthy.

## Decision clarity

- **Decision**: choose **memory pressure / reclaim / swap signals** over **disk vendor swaps** when latency blew up **after RSS growth** or **cache collapse**, until paging is ruled in or out.

## Concepts reused / refined / created

- Reused (structure): [[throughput-latency-metrics]]
- Reused (structure): [[utilization-and-saturation]]
- Reused (structure): [[cross-component-interactions]]
- Reused (abstraction): [[measurement-validity]]
- Reused: [[systems-performance]]

## Links

- Concepts:
  - [[throughput-latency-metrics]]
  - [[utilization-and-saturation]]
  - [[cross-component-interactions]]
  - [[measurement-validity]]
  - [[systems-performance]]
- Related sources:
  - [[systems-performance-cpu-interconnect-scalability-memory-system-6-4-1]]
  - [[systems-performance-memory-terminology-7-1]]
