# Systems Performance — Memory tools method caveats (7.4.1) (PDF ~320–380 extract)

## Source

- Title: *Systems Performance: Enterprise and the Cloud* (Second Edition)
- Author: Brendan Gregg
- Raw: `raw/code/pdf/Systems.Performance.Enterprise.and.the.Cloud.pdf`
- Batch scope: Chapter 7, **§7.4.1** — **tools iteration** risks + Linux-oriented **saturation / pressure** checks (book lists commands; retained as **patterns**, not endorsements)

## Processed artifacts

- Scout: `processed/code/systems-performance-ch7-scout-p320-380.txt`
- Converted slice: `processed/code/systems-performance-memory-methodology-tools-method-7-4-1.md`
- Chunks:
  - `processed/code/systems-performance-memory-methodology-tools-method-7-4-1-chunk-000001.md`

## Extracted ideas (with classification)

- (heuristic) **Tools ladder** can miss entire failure classes when **inventory is thin**—explicitly track **visibility gaps** as [[known-unknowns-framework]] items ([[streetlight-anti-method]]).
- (measurement) **Allocation tracing vs CPU sampling** trades **precision for perturbation**—choose mode by **production safety** and **rate of allocations** ([[instrumentation-overhead-and-perturbation]], [[measurement-validity]]).

## Application validation

- **Only vmstat free + top**: if **PSI / scan rate** are absent from the checklist, add **one saturation witness** before declaring “memory fine.”

## Decision clarity

- **Decision**: choose **cheap saturation witnesses first (PSI/scan/swap/OOM)** over **deep allocation stacks** when **customer pain is intermittent** and **tracing cost** could distort the race.

## Concepts reused / refined / created

- Reused (heuristic): [[streetlight-anti-method]]
- Reused (abstraction): [[known-unknowns-framework]]
- Reused (measurement): [[instrumentation-overhead-and-perturbation]]
- Reused (abstraction): [[measurement-validity]]
- Reused: [[systems-performance]]

## Links

- Concepts:
  - [[streetlight-anti-method]]
  - [[known-unknowns-framework]]
  - [[instrumentation-overhead-and-perturbation]]
  - [[measurement-validity]]
  - [[systems-performance]]
- Related sources:
  - [[systems-performance-memory-methodology-ch7-intro-and-order-7-4]]
