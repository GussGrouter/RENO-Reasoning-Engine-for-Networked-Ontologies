# Systems Performance — Slab adoption, UMA, SLUB simplification (7.3.3) (PDF ~320–380 extract)

## Source

- Title: *Systems Performance: Enterprise and the Cloud* (Second Edition)
- Author: Brendan Gregg
- Raw: `raw/code/pdf/Systems.Performance.Enterprise.and.the.Cloud.pdf`
- Batch scope: Chapter 7, **§7.3.3** — **BSD UMA**, Linux slab history, **SLUB** trade (complexity vs per-CPU caches; **NUMA** left to **page allocator**)

## Processed artifacts

- Scout: `processed/code/systems-performance-ch7-scout-p320-380.txt`
- Converted slice: `processed/code/systems-performance-memory-slab-adoption-and-slub-7-3-3e.md`
- Chunks:
  - `processed/code/systems-performance-memory-slab-adoption-and-slub-7-3-3e-chunk-000001.md`

## Extracted ideas (with classification)

- (structure) **Allocator evolution** shifts **where NUMA locality is enforced**—when SLUB **removes** some per-CPU layers, **page-level placement** matters more for the same workload ([[cross-component-interactions]], [[virtual-memory-abstraction]]).
- (structure) **“NUMA-aware slab” vs “NUMA-aware buddy”** is an **implementation split**, not a second **memory physics**—compare **end-to-end** before celebrating a name ([[resource-vs-implementation-bottleneck]], [[measurement-validity]]).

## Application validation

- **Kernel upgrade changes SLUB behavior**: re-baseline **cross-node allocation** tests—**locality guarantees** may have moved **up** the stack.

## Decision clarity

- **Decision**: choose **node-local allocation witnesses + fault/numa stats** over **allocator brand alone** when validating **kernel memory locality** after an **allocator or kernel** change.

## Concepts reused / refined / created

- Reused (structure): [[cross-component-interactions]]
- Reused (abstraction): [[virtual-memory-abstraction]]
- Reused (structure): [[resource-vs-implementation-bottleneck]]
- Reused (abstraction): [[measurement-validity]]
- Reused: [[systems-performance]]

## Links

- Concepts:
  - [[cross-component-interactions]]
  - [[virtual-memory-abstraction]]
  - [[resource-vs-implementation-bottleneck]]
  - [[measurement-validity]]
  - [[systems-performance]]
- Related sources:
  - [[systems-performance-memory-kernel-slab-and-magazines-7-3-3d]]
  - [[systems-performance-memory-allocator-glibc-dlmalloc-style-7-3-3f]]
