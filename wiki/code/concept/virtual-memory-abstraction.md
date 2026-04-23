# Virtual memory abstraction

- Tag: abstraction

## Definition

The **virtual memory abstraction** presents programs with a contiguous address space that is mapped to physical memory (and optionally disk) via translation structures.

## Scope note

This is an OS/hardware abstraction boundary: it changes which memory costs are explicit vs hidden to the programmer.
Operating systems also commonly partition virtual address space into distinct regions such as kernel space vs user space, even though the core abstraction is still “virtual addresses → physical backing”.

## Relation

- Realized via page table translation and mechanisms like [[demand-paging]].
- Can hide performance-relevant costs (e.g., translation misses, paging), relating to [[abstraction-design-principles]].

## Links

- Source: [[network-algorithmics-2-4-2-virtual-memory]]
- Source: [[systems-performance-operating-systems-terminology-3-1]]
- Source: [[systems-performance-kernels-bsd-3-3-2]]
- Source: [[systems-performance-kernels-solaris-3-3-3]]
- Source: [[systems-performance-exercises-3-7]]
- Source: [[systems-performance-memory-terminology-7-1]]
- Source: [[systems-performance-memory-concepts-virtual-memory-7-2-1]]
- Source: [[systems-performance-memory-concepts-demand-paging-7-2-3]]
- Source: [[systems-performance-memory-concepts-overcommit-7-2-4]]
- Source: [[systems-performance-memory-concepts-word-size-7-2-11]]
- Source: [[systems-performance-memory-architecture-mmu-tlb-7-3-1e]]
- Source: [[systems-performance-memory-architecture-free-lists-reaping-scan-7-3-2c]]
- Source: [[systems-performance-memory-process-address-space-segments-7-3-3a]]
- Source: [[systems-performance-memory-heap-growth-vs-leak-7-3-3b]]
- Source: [[systems-performance-memory-kernel-slab-and-magazines-7-3-3d]]
- Source: [[systems-performance-memory-slab-adoption-and-slub-7-3-3e]]
- Related concepts:
  - [[demand-paging]]
  - [[abstraction-design-principles]]

