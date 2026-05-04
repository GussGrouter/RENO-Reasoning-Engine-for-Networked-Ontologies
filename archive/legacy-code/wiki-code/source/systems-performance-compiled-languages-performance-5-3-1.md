# Systems Performance — compiled languages: symbols, optimizations, observability tradeoffs (5.3.1) (PDF ~182–230)

## Source

- Title: *Systems Performance: Enterprise and the Cloud* (Second Edition)
- Author: Brendan Gregg
- Raw: `raw/code/pdf/Systems.Performance.Enterprise.and.the.Cloud.pdf`
- Batch scope: Chapter 5, Section 5.3.1 Compiled Languages

## Processed artifacts

- Converted slice: `processed/code/systems-performance-compiled-languages-performance-5-3-1.md`
- Chunks:
  - `processed/code/systems-performance-compiled-languages-performance-5-3-1-chunk-000001.md`

## Extracted ideas (with classification)

- (measurement) **Symbol lineage**: machine code maps to source when symbols/debuginfo exist—without them, profilers regress to address archaeology ([[sampling-based-profiling]] hygiene).
- (abstraction) **Compiler knobs trade future diagnosis for present cycles** (example narrative: frame-pointer omission speeds hot code but breaks stack walkers)—fits [[abstraction-design-principles]]: hidden constraints surface later as cost.
- (diagnosis) **“Just drop –O3”** is not a safe debugging dial: optimization level rewrites code enough to **move** the bug you are chasing—treat like any uncontrolled variable in [[observability-vs-experimentation]].

## Application validation

- **Release builds**: ship artifacts with **split debuginfo** (or preserved frame pointers) if production profiling is a contractual requirement—otherwise you are choosing compile-time wins over post-incident recoverability.

## Concepts reused / refined / created

- Reused (measurement): [[sampling-based-profiling]]
- Reused (abstraction): [[abstraction-design-principles]]
- Reused (abstraction): [[observability-vs-experimentation]]
- Reused (structure): [[resource-vs-implementation-bottleneck]]
- Reused: [[systems-performance]]

## Links

- Concepts:
  - [[sampling-based-profiling]]
  - [[abstraction-design-principles]]
  - [[observability-vs-experimentation]]
  - [[resource-vs-implementation-bottleneck]]
  - [[systems-performance]]
