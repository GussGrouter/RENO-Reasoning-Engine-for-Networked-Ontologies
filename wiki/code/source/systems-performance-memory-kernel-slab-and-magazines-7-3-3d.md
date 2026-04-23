# Systems Performance — Kernel slab + magazines (7.3.3) (PDF ~320–380 extract)

## Source

- Title: *Systems Performance: Enterprise and the Cloud* (Second Edition)
- Author: Brendan Gregg
- Raw: `raw/code/pdf/Systems.Performance.Enterprise.and.the.Cloud.pdf`
- Batch scope: Chapter 7, **§7.3.3** — **slab caches** for fixed-size kernel objects; **kmem_alloc** vs **kmem_cache_alloc** pattern; **magazine** per-CPU caching idea

## Processed artifacts

- Scout: `processed/code/systems-performance-ch7-scout-p320-380.txt`
- Converted slice: `processed/code/systems-performance-memory-kernel-slab-and-magazines-7-3-3d.md`
- Chunks:
  - `processed/code/systems-performance-memory-kernel-slab-and-magazines-7-3-3d-chunk-000001.md`

## Extracted ideas (with classification)

- (structure) **Object caches** move kernel allocation hot paths off the **page allocator**—performance work shifts to **cache sizing / churn**, not only **DRAM bytes** ([[resource-vs-implementation-bottleneck]], [[virtual-memory-abstraction]]).
- (structure) **Per-CPU magazines** are the same **composition pattern** as userland **per-thread caches**: locality wins, **rebalance / migration** costs apply ([[cross-component-interactions]]).

## Application validation

- **Kernel subsystems allocating tiny structs at high rate**: if CPU is in **slab fastpath**, **tuning page reclaim** alone will not help—profile **object cache churn** and **magazine refill**.

## Decision clarity

- **Decision**: choose **dedicated kmem caches + tuned object sizes** over **generic kmalloc hot paths** when a **kernel module** allocates the **same struct** at **millions/sec**.

## Concepts reused / refined / created

- Reused (structure): [[resource-vs-implementation-bottleneck]]
- Reused (abstraction): [[virtual-memory-abstraction]]
- Reused (structure): [[cross-component-interactions]]
- Reused: [[systems-performance]]

## Links

- Concepts:
  - [[resource-vs-implementation-bottleneck]]
  - [[virtual-memory-abstraction]]
  - [[cross-component-interactions]]
  - [[systems-performance]]
- Related sources:
  - [[systems-performance-memory-slab-adoption-and-slub-7-3-3e]]
