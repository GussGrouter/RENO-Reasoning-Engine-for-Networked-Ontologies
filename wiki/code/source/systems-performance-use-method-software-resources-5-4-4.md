# Systems Performance — USE method on software resources (5.4.4) (PDF ~231–285)

## Source

- Title: *Systems Performance: Enterprise and the Cloud* (Second Edition)
- Author: Brendan Gregg
- Raw: `raw/code/pdf/Systems.Performance.Enterprise.and.the.Cloud.pdf`
- Batch scope: Chapter 5, Section 5.4.4 USE Method (software resource examples: thread pools, file descriptors)

## Processed artifacts

- Converted slice: `processed/code/systems-performance-use-method-software-resources-5-4-4.md`
- Chunks:
  - `processed/code/systems-performance-use-method-software-resources-5-4-4-chunk-000001.md`

## Extracted ideas (with classification)

- (abstraction) **USE on logical resources** reuses utilization/saturation/error semantics where a component behaves like a **queueing server** (workers + backlog, FD table as finite capacity) ([[use-method]], [[utilization-and-saturation]], [[queueing-theory]]).
- (diagnosis) The deliverable is a **small repeatable checklist** of meaningful U/S/E per component—explicitly **skip** metrics that do not map to a decision ([[known-unknowns-framework]]).

## Application validation

- **Thread pool service**: define utilization as busy workers / pool size and saturation as mean queue length; if utilization is 30% but saturation grows under load, the bottleneck is admission/queue policy—not “CPU headroom.”

## Decision clarity

- **Decision**: choose **pool depth / queue policy** changes over **horizontal replica scaling** when worker utilization is low but request queue saturation is high.

## Concepts reused / refined / created

- Reused (heuristic): [[use-method]]
- Reused (structure): [[utilization-and-saturation]]
- Reused (abstraction): [[queueing-theory]]
- Reused (diagnosis): [[known-unknowns-framework]]
- Reused: [[systems-performance]]

## Links

- Concepts:
  - [[use-method]]
  - [[utilization-and-saturation]]
  - [[queueing-theory]]
  - [[known-unknowns-framework]]
  - [[systems-performance]]
- Related sources:
  - [[systems-performance-syscall-analysis-boundary-instrumentation-5-4-3]]
  - [[systems-performance-thread-state-nine-state-model-5-4-5]]
