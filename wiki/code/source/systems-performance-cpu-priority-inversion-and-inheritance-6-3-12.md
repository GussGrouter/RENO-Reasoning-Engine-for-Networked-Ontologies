# Systems Performance — Priority inversion as a scheduling composition failure (6.3.12) (PDF ~231–285)

## Source

- Title: *Systems Performance: Enterprise and the Cloud* (Second Edition)
- Author: Brendan Gregg
- Raw: `raw/code/pdf/Systems.Performance.Enterprise.and.the.Cloud.pdf`
- Batch scope: Chapter 6, Section 6.3.12 (priority inversion pattern; inheritance as mitigation)

## Processed artifacts

- Converted slice: `processed/code/systems-performance-cpu-priority-inversion-and-inheritance-6-3-12.md`
- Chunks:
  - `processed/code/systems-performance-cpu-priority-inversion-and-inheritance-6-3-12-chunk-000001.md`

## Extracted ideas (with classification)

- (diagnosis) **Priority inversion** is when **scheduling priority ordering is violated by lock ownership**: high-priority runnable work waits on a resource held by **lower-priority** runnable/interleaved work, so “priority” stops predicting latency ([[process-abstraction]], [[cross-component-interactions]]).
- (mechanism) **Priority inheritance** temporarily **elevates the lock holder** so it can finish and release—restoring composability between **mutex graphs** and **CPU scheduling** (OS-specific mutex flavors are implementation detail; the decision pattern is portable) ([[process-abstraction]], [[throughput-latency-metrics]]).

## Application validation

- **Realtime + admin tooling**: a background monitor holds a DB address-space lock while a batch job runs; production queries block → **inheritance or lock partitioning** beats “raise nice(5) on the batch job” alone.

## Decision clarity

- **Decision**: choose **inheritance-capable locks / shorter critical sections** over **more CPU or higher base priorities** when **high-priority runnable threads** stall on **mutexes held by lower-priority** partners.

## Concepts reused / refined / created

- Reused (abstraction): [[process-abstraction]]
- Reused (structure): [[cross-component-interactions]]
- Reused (structure): [[throughput-latency-metrics]]
- Reused: [[systems-performance]]

## Links

- Concepts:
  - [[process-abstraction]]
  - [[cross-component-interactions]]
  - [[throughput-latency-metrics]]
  - [[systems-performance]]
- Related sources:
  - [[systems-performance-cpu-saturation-preemption-and-quotas-6-3-10-11]]
  - [[systems-performance-cpu-multiprocess-multithreading-tradeoffs-6-3-13]]
