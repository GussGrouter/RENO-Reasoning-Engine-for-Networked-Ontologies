# Systems Performance — models (2.2) (PDF pages 61–63)

## Source

- Title: *Systems Performance: Enterprise and the Cloud* (Second Edition)
- Author: Brendan Gregg
- Raw: `raw/code/pdf/Systems.Performance.Enterprise.and.the.Cloud.pdf`
- Batch scope: Chapter 2, Section 2.2 Models (SUT + queueing system)

## Processed artifacts

- Converted slice: `processed/code/systems-performance-models-2-2.md`
- Chunks:
  - `processed/code/systems-performance-models-2-2-chunk-000001.md`

## Extracted ideas (with classification)

- (diagnosis) A system under test (SUT) can be modeled with a simple block diagram to bound what is “in” vs “out” of analysis.
- (measurement) Perturbations/interference (scheduled activity, other workloads/users, tenant activity) can affect results and may not be directly observable from within the SUT.
- (diagnosis) Modern environments are multi-component; mapping the environment can reveal overlooked perturbation sources and supports whole-system reasoning.
- (diagnosis) Queueing systems are a basic model for predicting response time degradation under load; systems can be modeled as networks of queues.

## Concepts reused / refined / created

- Refined (measurement): [[instrumentation-overhead-and-perturbation]] (broadened perturbation scope beyond tool overhead to include concurrent system activity/tenancy).
- Reused (diagnosis): [[cross-component-interactions]] (multi-component environments motivate composition-aware reasoning).

## Links

- Concepts:
  - [[systems-performance]]
  - [[instrumentation-overhead-and-perturbation]]
  - [[cross-component-interactions]]

