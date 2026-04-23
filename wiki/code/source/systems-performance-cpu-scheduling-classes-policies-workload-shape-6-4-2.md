# Systems Performance — Scheduling classes, policies, and workload-shape knobs (6.4.2) (PDF ~231–285)

## Source

- Title: *Systems Performance: Enterprise and the Cloud* (Second Edition)
- Author: Brendan Gregg
- Raw: `raw/code/pdf/Systems.Performance.Enterprise.and.the.Cloud.pdf`
- Batch scope: Chapter 6, Section 6.4.2 — **Scheduling classes** (RT, O(1), CFS, Idle, Deadline) and **policies** (RR/FIFO/NORMAL/BATCH/IDLE/DEADLINE) through research notes on HT/temperature-aware scheduling

## Processed artifacts

- Converted slice: `processed/code/systems-performance-cpu-scheduling-classes-policies-workload-shape-6-4-2.md`
- Chunks:
  - `processed/code/systems-performance-cpu-scheduling-classes-policies-workload-shape-6-4-2-chunk-000001.md`

## Extracted ideas (with classification)

- (abstraction) **Scheduling class chooses the optimization objective** (hard RT vs interactive fairness vs batch isolation)—misaligned class/policy is a **systemic latency** issue, not “bad threads” ([[throughput-latency-metrics]], [[process-abstraction]]).
- (mechanism) **Dynamic vs static priority split** (e.g., **nice** vs scheduler-computed weight) means **operator intent** and **kernel heuristics** can disagree—tune with that composition in mind ([[measurement-validity]]).
- (diagnosis) **Algorithm complexity mattered historically** (O(n) scan vs O(1) buckets)—modern issue is more often **coherence + NUMA + power** coupling than raw scheduler scan cost ([[universal-scalability-law]], [[cross-component-interactions]]).

## Application validation

- **Batch ETL on shared nodes**: `SCHED_BATCH`/`idle` class choices can reduce **interactive interference** more than raising **nice** alone—validate with **scheduler latency + runqueue** signals, not only CPU%.

## Decision clarity

- **Decision**: choose **SCHED_DEADLINE / RT class** over **CFS + priority games** when **hard per-period CPU guarantees** are part of the correctness contract.

## Concepts reused / refined / created

- Reused (structure): [[throughput-latency-metrics]]
- Reused (abstraction): [[process-abstraction]]
- Reused (abstraction): [[measurement-validity]]
- Reused (abstraction): [[universal-scalability-law]]
- Reused (structure): [[cross-component-interactions]]
- Reused (insight): [[model-classify-intervene]]
- Reused: [[systems-performance]]

## Links

- Concepts:
  - [[throughput-latency-metrics]]
  - [[process-abstraction]]
  - [[measurement-validity]]
  - [[universal-scalability-law]]
  - [[cross-component-interactions]]
  - [[model-classify-intervene]]
  - [[systems-performance]]
- Related sources:
  - [[systems-performance-cpu-kernel-scheduler-functions-and-locality-6-4-2]]
  - [[systems-performance-cpu-idle-numa-topology-scheduler-awareness-6-4-2]]
