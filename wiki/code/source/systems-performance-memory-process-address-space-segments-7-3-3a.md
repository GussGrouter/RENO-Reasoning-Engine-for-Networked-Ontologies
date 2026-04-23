# Systems Performance — Process virtual address space segments (7.3.3) (PDF ~320–380 extract)

## Source

- Title: *Systems Performance: Enterprise and the Cloud* (Second Edition)
- Author: Brendan Gregg
- Raw: `raw/code/pdf/Systems.Performance.Enterprise.and.the.Cloud.pdf`
- Batch scope: Chapter 7, **§7.3.3** — **segment model** (text, data, heap, stack), **shared library text**, **x86 vs SPARC** pointer semantics, **canonical** 64-bit ranges

## Processed artifacts

- Scout: `processed/code/systems-performance-ch7-scout-p320-380.txt` (**pdftotext -f 320 -l 380**)
- Converted slice: `processed/code/systems-performance-memory-process-address-space-segments-7-3-3a.md`
- Chunks:
  - `processed/code/systems-performance-memory-process-address-space-segments-7-3-3a-chunk-000001.md`

## Extracted ideas (with classification)

- (abstraction) **Segments partition responsibility**: **file-backed** vs **anonymous** regions drive different **reclaim, sharing, and observability** stories ([[virtual-memory-abstraction]], [[process-abstraction]]).
- (measurement) **“Is this pointer user or kernel?”** is **not portable**—debugging assumptions from **x86** can **invalidate** triage on other ABIs ([[measurement-validity]]).
- (structure) **Shared text / private data** per library is the **PSS vs RSS** pattern in address-space form ([[caching]] as read-mostly sharing).

## Application validation

- **Core dump from SPARC-era assumptions**: do not infer **ring** from **high bit pattern** alone—use **OS ABI rules** for that platform.

## Decision clarity

- **Decision**: choose **segment-aware maps (heap vs file maps vs stacks)** over **single “process bytes”** when attributing **which region** should shrink under **cgroup RSS** pressure.

## Concepts reused / refined / created

- Reused (abstraction): [[virtual-memory-abstraction]]
- Reused (abstraction): [[process-abstraction]]
- Reused (abstraction): [[measurement-validity]]
- Reused (mechanism): [[caching]]
- Reused: [[systems-performance]]

## Links

- Concepts:
  - [[virtual-memory-abstraction]]
  - [[process-abstraction]]
  - [[measurement-validity]]
  - [[caching]]
  - [[systems-performance]]
- Related sources:
  - [[systems-performance-memory-heap-growth-vs-leak-7-3-3b]]
