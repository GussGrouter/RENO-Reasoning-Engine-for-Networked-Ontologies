# Systems Performance — CPU terminology (6.1) (PDF ~231–285)

## Source

- Title: *Systems Performance: Enterprise and the Cloud* (Second Edition)
- Author: Brendan Gregg
- Raw: `raw/code/pdf/Systems.Performance.Enterprise.and.the.Cloud.pdf`
- Batch scope: Chapter 6, Section 6.1 Terminology (processor/core/hardware thread/logical CPU/scheduler/run queue; book glossary for verbatim definitions)

## Processed artifacts

- Converted slice: `processed/code/systems-performance-cpu-terminology-6-1.md`
- Chunks:
  - `processed/code/systems-performance-cpu-terminology-6-1-chunk-000001.md`

## Extracted ideas (with classification)

- (abstraction) **Hardware parallelism vs OS schedulable units**: cores and hardware threads are packaging; **logical CPUs** are what the kernel schedules—capacity math must map between them or cgroup limits mis-sum ([[process-abstraction]], [[utilization-and-saturation]]).
- (mechanism) **Run queue** names a **scheduler-managed wait** for CPU time—distinct from disk/network queues but the same *saturation* family ([[utilization-and-saturation]], [[context-switching]]).
- (abstraction) “**Virtual CPU**” wording collision across virtualization vs logical CPU—scope the noun before comparing metrics across hosts ([[measurement-validity]], [[known-unknowns-framework]]).

## Application validation

- **Kubernetes `limits.cpu` incident**: convert “8 CPUs” into **logical CPU threads vs cores** before comparing node capacity to JVM `-XX:ActiveProcessorCount`.

## Decision clarity

- **Decision**: choose **topology-aware capacity accounting** over **raw hardware thread counts** when SMT is present and the scheduler may deliberately avoid packing both siblings.

## Concepts reused / refined / created

- Reused (mechanism): [[process-abstraction]]
- Reused (structure): [[utilization-and-saturation]]
- Reused (mechanism): [[context-switching]]
- Reused (abstraction): [[measurement-validity]]
- Reused (diagnosis): [[known-unknowns-framework]]
- Reused: [[systems-performance]]

## Links

- Concepts:
  - [[process-abstraction]]
  - [[utilization-and-saturation]]
  - [[context-switching]]
  - [[measurement-validity]]
  - [[known-unknowns-framework]]
  - [[systems-performance]]
- Related sources:
  - [[systems-performance-cpus-chapter-intro-and-parts-6]]
  - [[systems-performance-cpu-models-architecture-and-caches-6-2-1-2]]
