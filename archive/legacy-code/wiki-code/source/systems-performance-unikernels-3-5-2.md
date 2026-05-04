# Systems Performance — unikernels (3.5.2) (PDF pages 118–170)

## Source

- Title: *Systems Performance: Enterprise and the Cloud* (Second Edition)
- Author: Brendan Gregg
- Raw: `raw/code/pdf/Systems.Performance.Enterprise.and.the.Cloud.pdf`
- Batch scope: Chapter 3, Section 3.5.2 Unikernels

## Processed artifacts

- Converted slice: `processed/code/systems-performance-unikernels-3-5-2.md`
- Chunks:
  - `processed/code/systems-performance-unikernels-3-5-2-chunk-000001.md`

## Extracted ideas (with classification)

- (abstraction) Unikernels collapse kernel/library/app into one deployable image, often in a single address space—an extreme point on the same “where does privileged code live?” spectrum as monolithic vs microkernel designs.
- (abstraction) Fewer moving parts can improve locality and attack surface, but can remove standard interactive/debug tooling assumptions unless observability is rebuilt for that execution model.

## Concepts reused / refined / created

- Reused (abstraction): [[kernel-architecture-models]]
- Reused (measurement): [[instrumentation-overhead-and-perturbation]]
- Reused (measurement): [[event-tracing]]

## Links

- Concepts:
  - [[kernel-architecture-models]]
  - [[instrumentation-overhead-and-perturbation]]
  - [[event-tracing]]
