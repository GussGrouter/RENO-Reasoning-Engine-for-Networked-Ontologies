# Demand paging

- Tag: mechanism

## Definition

**Demand paging** loads a page into memory only when it is accessed; accessing a non-resident page triggers a fault/exception that brings the page in from slower storage.

## Scope note

This is a general “on-demand load” mechanism; it trades steady-state memory footprint against fault/latency costs under misses.

## Relation

- A key mechanism underlying the [[virtual-memory-abstraction]].
- A concrete instance of a time–space tradeoff: memory footprint vs access latency under misses (see [[time-space-tradeoff]]).

## Links

- Source: [[network-algorithmics-2-4-2-virtual-memory]]
- Source: [[systems-performance-kernels-bsd-3-3-2]]
- Source: [[systems-performance-exercises-3-7]]
- Source: [[systems-performance-memory-terminology-7-1]]
- Source: [[systems-performance-memory-concepts-virtual-memory-7-2-1]]
- Source: [[systems-performance-memory-concepts-demand-paging-7-2-3]]
- Source: [[systems-performance-memory-concepts-overcommit-7-2-4]]
- Source: [[systems-performance-memory-concepts-process-swapping-7-2-5]]
- Source: [[systems-performance-memory-heap-growth-vs-leak-7-3-3b]]
- Related concepts:
  - [[virtual-memory-abstraction]]
  - [[time-space-tradeoff]]

