# Systems Performance — NUMA binding (§7.6.4) (PDF scout 381–400)

## Source

- Title: *Systems Performance: Enterprise and the Cloud* (Second Edition)
- Author: Brendan Gregg
- Raw: `raw/code/pdf/Systems.Performance.Enterprise.and.the.Cloud.pdf`
- Batch scope: Chapter 7, **§7.6.4** — **numactl** memory/CPU bind; **fail if cannot allocate on node** semantics

## Processed artifacts

- Scout: `processed/code/systems-performance-ch7-scout-p381-400.txt`
- Converted slice: `processed/code/systems-performance-memory-tuning-numa-bind-7-6-4.md`
- Chunks: `processed/code/systems-performance-memory-tuning-numa-bind-7-6-4-chunk-000001.md`

## Extracted ideas (with classification)

- (decision) **Socket isolation** reduces **remote memory access** at the cost of **harder OOM/alloc failure** if the working set outgrows the node—**bind memory and CPU together** for coherent locality stories ([[cross-component-interactions]], [[measurement-validity]]).
- (scope) **`--membind` without matching CPU affinity** can recreate **cross-socket traffic**—the book pairs **physcpubind** ([[cross-component-interactions]]).

## Application validation

- **Latency improves when pinned to one socket:** verify **allocation failures / unexpected remote fallbacks** aren’t masked—check **errno paths** when the heap exceeds **local DRAM**.

## Decision clarity

- **Decision:** choose **paired NUMA memory + CPU binding** over **memory-only binding** when **you are optimizing for local DRAM latency** and **scheduler placement** could otherwise undo locality.

## Concepts reused / refined / created

- Reused: [[cross-component-interactions]], [[measurement-validity]], [[systems-performance]]
- **Created:** none

## Links

- Concepts: [[cross-component-interactions]], [[measurement-validity]], [[systems-performance]]
- Related sources: [[systems-performance-memory-tuning-cgroup-limits-7-6-5]]
