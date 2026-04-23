# Systems Performance — Memory terminology (7.1) (PDF 321–360 extract)

## Source

- Title: *Systems Performance: Enterprise and the Cloud* (Second Edition)
- Author: Brendan Gregg
- Raw: `raw/code/pdf/Systems.Performance.Enterprise.and.the.Cloud.pdf`
- Batch scope: Chapter 7, **§7.1** — **definitions** tying **virtual**, **resident**, **anonymous**, **paging**, **swap**, **OOM** (terminology for consistent measurement language)

## Processed artifacts

- Converted slice: `processed/code/systems-performance-memory-terminology-7-1.md`
- Chunks:
  - `processed/code/systems-performance-memory-terminology-7-1-chunk-000001.md`

## Extracted ideas (with classification)

- (abstraction) **Virtual vs resident vs address space** is a **scope/semantics** triad: tools disagree most when **names reuse “memory”** for different populations ([[measurement-validity]], [[virtual-memory-abstraction]]).
- (structure) **Linux “swapping” = anonymous paging** (not whole-process swap) is a **definition trap** when comparing to other Unix literature or dashboards ([[measurement-validity]], [[demand-paging]]).
- (structure) **OOM** is an **error/liveness policy** signal, not a utilization average—use it as **hard saturation evidence** ([[utilization-and-saturation]]).

## Application validation

- **Dashboard says “high virtual, low RSS”**: translate to **fault / mapping / overcommit story** before blaming leaks—**virtual** counts **committed address ranges**, not necessarily **DRAM pressure**.

## Decision clarity

- **Decision**: choose **pressure metrics (scan/reclaim/swap/PSI/OOM)** over **“free memory” headline** when deciding if you are in **saturation** vs **healthy cache usage**.

## Concepts reused / refined / created

- Reused (abstraction): [[measurement-validity]]
- Reused (abstraction): [[virtual-memory-abstraction]]
- Reused (mechanism): [[demand-paging]]
- Reused (structure): [[utilization-and-saturation]]
- Reused (abstraction): [[process-abstraction]]
- Reused: [[systems-performance]]

## Links

- Concepts:
  - [[measurement-validity]]
  - [[virtual-memory-abstraction]]
  - [[demand-paging]]
  - [[utilization-and-saturation]]
  - [[process-abstraction]]
  - [[systems-performance]]
- Related sources:
  - [[systems-performance-memory-chapter-intro-and-parts-7]]
  - [[systems-performance-memory-concepts-virtual-memory-7-2-1]]
