# Systems Performance — chapter 5 exercises: conceptual review (5.7 partial) (PDF ~231–285)

## Source

- Title: *Systems Performance: Enterprise and the Cloud* (Second Edition)
- Author: Brendan Gregg
- Raw: `raw/code/pdf/Systems.Performance.Enterprise.and.the.Cloud.pdf`
- Batch scope: Chapter 5, Section 5.7 Exercises, item 2 (I/O size tradeoffs; lock hashing; language runtimes + GC—prompts only; answers map to prior chapter concepts)

## Processed artifacts

- Converted slice: `processed/code/systems-performance-chapter-5-exercises-conceptual-review-5-7.md`
- Chunks:
  - `processed/code/systems-performance-chapter-5-exercises-conceptual-review-5-7-chunk-000001.md`

## Extracted ideas (with classification)

- (abstraction) **Large I/O units** trade transfer efficiency against **unit latency**—the exercise restates the throughput/latency coupling already used for batching decisions ([[throughput-latency-metrics]], [[cross-component-interactions]]).
- (structure) **Lock hashing / striping** is a scaling pattern for reducing contention on a single mutex namespace—implementation bottleneck class, not “more GHz” ([[resource-vs-implementation-bottleneck]]).
- (mechanism) **Runtime + GC** questions anchor performance work in **allocation/churn and pause** axes rather than micro-ops alone ([[caching]], [[throughput-latency-metrics]]).

## Application validation

- **Service batching knob review**: when PM asks for “bigger writes,” answer using the I/O-size/latency coupling frame before changing defaults.

## Decision clarity

- **Decision**: choose **smaller I/O units / less batching** over **larger transfers** when tail latency SLOs dominate average throughput goals.

## Concepts reused / refined / created

- Reused (structure): [[throughput-latency-metrics]]
- Reused (structure): [[cross-component-interactions]]
- Reused (structure): [[resource-vs-implementation-bottleneck]]
- Reused (mechanism): [[caching]]
- Reused: [[systems-performance]]

## Links

- Concepts:
  - [[throughput-latency-metrics]]
  - [[cross-component-interactions]]
  - [[resource-vs-implementation-bottleneck]]
  - [[caching]]
  - [[systems-performance]]
- Related sources:
  - [[systems-performance-chapter-5-exercises-terminology-scaffold-5-7]]
  - [[systems-performance-chapter-5-exercises-application-profile-role-and-metrics-5-7]]
