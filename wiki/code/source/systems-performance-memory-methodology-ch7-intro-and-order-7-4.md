# Systems Performance — Chapter 7 memory methodologies: intro and ordering (§7.4 open) (PDF ~320–380 extract)

## Source

- Title: *Systems Performance: Enterprise and the Cloud* (Second Edition)
- Author: Brendan Gregg
- Raw: `raw/code/pdf/Systems.Performance.Enterprise.and.the.Cloud.pdf`
- Batch scope: Chapter 7, **§7.4** — methodology map (**Table 7.3 omitted** in processed extract); suggested **investigation order** before tool survey (**§7.5**)

## Processed artifacts

- Scout: `processed/code/systems-performance-ch7-scout-p320-380.txt`
- Converted slice: `processed/code/systems-performance-memory-methodology-ch7-intro-and-order-7-4.md`
- Chunks:
  - `processed/code/systems-performance-memory-methodology-ch7-intro-and-order-7-4-chunk-000001.md`

## Extracted ideas (with classification)

- (heuristic) **Breadth-first screen**: **performance monitoring → USE → characterize usage** before diving into allocators—mirrors narrowing unknowns without locking onto one dashboard ([[use-method]], [[resource-analysis-vs-workload-analysis]]).
- (abstraction) **Methodology ordering is a scope choice**: skipping **characterization** early often produces **beautiful traces** answering the wrong capacity question ([[scientific-method]]).

## Application validation

- **New memory incident**: time-box **15 minutes** on **saturation signals + top consumers + cache vs RSS split** before installing heavy **allocation tracers**.

## Decision clarity

- **Decision**: choose **monitoring + USE + usage characterization** over **immediate deep allocator tracing** when **symptoms are systemic** (swap/PSI/OOM) rather than **one suspicious process**.

## Concepts reused / refined / created

- Reused (heuristic): [[use-method]]
- Reused (abstraction): [[resource-analysis-vs-workload-analysis]]
- Reused (abstraction): [[scientific-method]]
- Reused: [[systems-performance]]

## Links

- Concepts:
  - [[use-method]]
  - [[resource-analysis-vs-workload-analysis]]
  - [[scientific-method]]
  - [[systems-performance]]
- Related sources:
  - [[systems-performance-memory-methodology-use-method-7-4-2]]
  - [[systems-performance-memory-methodology-characterizing-usage-7-4-3a]]
