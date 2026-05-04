# Systems Performance — Memory overcommit policy (7.2.4) (PDF 321–360 extract)

## Source

- Title: *Systems Performance: Enterprise and the Cloud* (Second Edition)
- Author: Brendan Gregg
- Raw: `raw/code/pdf/Systems.Performance.Enterprise.and.the.Cloud.pdf`
- Batch scope: Chapter 7, **§7.2.4** — **Linux overcommit**: virtual allocations beyond **DRAM+swap**, interaction with **demand paging** and **OOM** behavior

## Processed artifacts

- Converted slice: `processed/code/systems-performance-memory-concepts-overcommit-7-2-4.md`
- Chunks:
  - `processed/code/systems-performance-memory-concepts-overcommit-7-2-4-chunk-000001.md`

## Extracted ideas (with classification)

- (abstraction) **Overcommit** moves failure from **allocation time** to **pressure time**—success of `malloc` is a **weak promise** about future **fault + reclaim** costs ([[virtual-memory-abstraction]], [[demand-paging]]).
- (measurement) **“OOM killer vs ENOMEM”** splits by **policy knobs**—comparing hosts requires matching **overcommit mode**, not only **RSS** ([[measurement-validity]], [[utilization-and-saturation]]).

## Application validation

- **Spiky batch jobs**: if allocations always succeed until random kills, you are likely in **overcommit + pressure** territory—fix with **quota/limit + working-set discipline**, not only heap profilers on the victim.

## Decision clarity

- **Decision**: choose **strict commit accounting / cgroup memory limits** over **default overcommit** when **silent eviction or OOM** is unacceptable for **multi-tenant** or **safety-critical** services.

## Concepts reused / refined / created

- Reused (abstraction): [[virtual-memory-abstraction]]
- Reused (mechanism): [[demand-paging]]
- Reused (abstraction): [[measurement-validity]]
- Reused (structure): [[utilization-and-saturation]]
- Reused: [[systems-performance]]

## Links

- Concepts:
  - [[virtual-memory-abstraction]]
  - [[demand-paging]]
  - [[measurement-validity]]
  - [[utilization-and-saturation]]
  - [[systems-performance]]
- Related sources:
  - [[systems-performance-memory-concepts-virtual-memory-7-2-1]]
  - [[systems-performance-memory-concepts-demand-paging-7-2-3]]
