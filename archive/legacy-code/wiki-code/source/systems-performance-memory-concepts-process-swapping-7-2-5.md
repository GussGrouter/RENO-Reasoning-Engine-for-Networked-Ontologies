# Systems Performance — Historical process swapping vs Linux paging (7.2.5) (PDF 321–360 extract)

## Source

- Title: *Systems Performance: Enterprise and the Cloud* (Second Edition)
- Author: Brendan Gregg
- Raw: `raw/code/pdf/Systems.Performance.Enterprise.and.the.Cloud.pdf`
- Batch scope: Chapter 7, **§7.2.5** — **whole-process swap** (historical Unix) vs **Linux paging-only** reality (terminology / saturation signal hygiene)

## Processed artifacts

- Converted slice: `processed/code/systems-performance-memory-concepts-process-swapping-7-2-5.md`
- Chunks:
  - `processed/code/systems-performance-memory-concepts-process-swapping-7-2-5-chunk-000001.md`

## Extracted ideas (with classification)

- (measurement) **“Swap” in runbooks** may mean **process migration** (old Unix) or **anonymous paging** (Linux)—incident commands and metrics must be read with **OS semantics**, not folklore ([[measurement-validity]], [[demand-paging]]).
- (abstraction) Linux **does not** whole-process swap; performance work should anchor on **page-level reclaim**, not imaginary **“swap the process out”** states ([[virtual-memory-abstraction]]).

## Application validation

- **Vendor doc says “swap thrashing”**: translate to **Linux: scan/reclaim + swap I/O + PSI** signals before mirroring 1980s tuning advice.

## Decision clarity

- **Decision**: choose **Linux paging/reclaim vocabulary** over **classic swap-out-the-process mental model** when writing **cross-team runbooks** that must match **what the kernel actually does**.

## Concepts reused / refined / created

- Reused (abstraction): [[measurement-validity]]
- Reused (mechanism): [[demand-paging]]
- Reused (abstraction): [[virtual-memory-abstraction]]
- Reused: [[systems-performance]]

## Links

- Concepts:
  - [[measurement-validity]]
  - [[demand-paging]]
  - [[virtual-memory-abstraction]]
  - [[systems-performance]]
- Related sources:
  - [[systems-performance-memory-concepts-paging-7-2-2]]
  - [[systems-performance-memory-terminology-7-1]]
