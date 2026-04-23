# Systems Performance — chapter 5 exercises: terminology scaffold (5.7 partial) (PDF ~231–285)

## Source

- Title: *Systems Performance: Enterprise and the Cloud* (Second Edition)
- Author: Brendan Gregg
- Raw: `raw/code/pdf/Systems.Performance.Enterprise.and.the.Cloud.pdf`
- Batch scope: Chapter 5, Section 5.7 Exercises, item 1 (terminology prompts only; wiki does not duplicate textbook definitions—see book)

## Processed artifacts

- Converted slice: `processed/code/systems-performance-chapter-5-exercises-terminology-scaffold-5-7.md`
- Chunks:
  - `processed/code/systems-performance-chapter-5-exercises-terminology-scaffold-5-7-chunk-000001.md`

## Extracted ideas (with classification)

- (diagnosis) A **shared performance vocabulary** (caches, buffers, locks, affinity, concurrency vs parallelism) is an **operational contract**: mismatched terms between dev/SRE/data create false disagreements during incidents ([[known-unknowns-framework]], [[resource-analysis-vs-workload-analysis]]).
- (abstraction) Treat exercise-1 style prompts as a **coverage checklist** for “what words might still be unknown-unknowns on this team,” not as trivia to memorize in isolation ([[known-unknowns-framework]]).

## Application validation

- **Postmortem template**: require each subsystem owner to label their bottleneck claims with the book’s concurrency vs parallelism and affinity vocabulary before accepting a “CPU-bound” verdict.

## Concepts reused / refined / created

- Reused (diagnosis): [[known-unknowns-framework]]
- Reused (abstraction): [[resource-analysis-vs-workload-analysis]]
- Reused: [[systems-performance]]

## Links

- Concepts:
  - [[known-unknowns-framework]]
  - [[resource-analysis-vs-workload-analysis]]
  - [[systems-performance]]
- Related sources:
  - [[systems-performance-gotchas-missing-stacks-remedies-and-unwinder-5-6-2]]
  - [[systems-performance-chapter-5-exercises-conceptual-review-5-7]]
