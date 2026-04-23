# Systems Performance — programming languages performance framing (5.3 intro) (PDF ~182–230)

## Source

- Title: *Systems Performance: Enterprise and the Cloud* (Second Edition)
- Author: Brendan Gregg
- Raw: `raw/code/pdf/Systems.Performance.Enterprise.and.the.Cloud.pdf`
- Batch scope: Chapter 5, Section 5.3 introduction

## Processed artifacts

- Converted slice: `processed/code/systems-performance-programming-languages-intro-5-3.md`
- Chunks:
  - `processed/code/systems-performance-programming-languages-intro-5-3-chunk-000001.md`

## Extracted ideas (with classification)

- (abstraction) **Language vs runtime**: “performance features” usually belong to **executing software** (VM, JIT, GC), not the grammar—decisions about observability and tuning attach to the **stack you ship**, not the brochure bullet.
- (diagnosis) Quick wins often come from **runtime-visible** pathologies (GC CPU, known bugs) checked against release notes and bug DBs—same loop as [[problem-statement-method]] “what changed / known defects.”

## Application validation

- **Runtime selection**: when comparing two language stacks for a latency-sensitive service, treat missing GC/runtime metrics hooks as a **ship risk** comparable to missing SLO dashboards—not a footnote after microbenchmark scores.

## Concepts reused / refined / created

- Reused (abstraction): [[observability-vs-experimentation]]
- Reused (heuristic): [[problem-statement-method]]
- Reused (diagnosis): [[known-unknowns-framework]]
- Reused: [[systems-performance]]

## Links

- Concepts:
  - [[observability-vs-experimentation]]
  - [[problem-statement-method]]
  - [[known-unknowns-framework]]
  - [[systems-performance]]
