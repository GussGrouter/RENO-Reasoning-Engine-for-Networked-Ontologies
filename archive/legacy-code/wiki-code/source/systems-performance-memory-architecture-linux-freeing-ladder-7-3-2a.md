# Systems Performance — Linux memory freeing ladder (7.3.2) (PDF 321–360 extract)

## Source

- Title: *Systems Performance: Enterprise and the Cloud* (Second Edition)
- Author: Brendan Gregg
- Raw: `raw/code/pdf/Systems.Performance.Enterprise.and.the.Cloud.pdf`
- Batch scope: Chapter 7, **§7.3.2** open — **reclaim stack** (free list, **page cache** vs **swap**, **reaping**, **OOM killer**) in **pressure order** (Figure 7.6 narrative)

## Processed artifacts

- Converted slice: `processed/code/systems-performance-memory-architecture-linux-freeing-ladder-7-3-2a.md`
- Chunks:
  - `processed/code/systems-performance-memory-architecture-linux-freeing-ladder-7-3-2a-chunk-000001.md`

## Extracted ideas (with classification)

- (structure) **Saturation signals differ by stage**—**scan/reclaim** vs **swap I/O** vs **OOM** are not interchangeable “memory errors” ([[utilization-and-saturation]], [[caching]]).
- (measurement) **Dashboards that collapse the ladder** into one “memory pressure” LED cause **wrong interventions** (e.g. tuning cache when you are already in **swap-in**) ([[measurement-validity]]).

## Application validation

- **Incident: “memory OK” but OOMs**: check **cgroup memory.max** vs **host free**—the ladder runs **per limit**, not only **global free**.

## Decision clarity

- **Decision**: choose **which rung fired (cache reclaim vs swap vs OOM vs cgroup cap)** over **aggregate “low memory”** when picking among **application fix**, **quota change**, and **DRAM purchase**.

## Concepts reused / refined / created

- Reused (structure): [[utilization-and-saturation]]
- Reused (mechanism): [[caching]]
- Reused (abstraction): [[measurement-validity]]
- Reused: [[systems-performance]]

## Links

- Concepts:
  - [[utilization-and-saturation]]
  - [[caching]]
  - [[measurement-validity]]
  - [[systems-performance]]
- Related sources:
  - [[systems-performance-memory-architecture-swappiness-swap-cgroups-7-3-2b]]
