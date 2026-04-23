# Systems Performance — nine-state thread model (5.4.5 partial) (PDF ~231–285)

## Source

- Title: *Systems Performance: Enterprise and the Cloud* (Second Edition)
- Author: Brendan Gregg
- Raw: `raw/code/pdf/Systems.Performance.Enterprise.and.the.Cloud.pdf`
- Batch scope: Chapter 5, Section 5.4.5 Thread State Analysis (intro through nine-state model and performance objective)

## Processed artifacts

- Converted slice: `processed/code/systems-performance-thread-state-nine-state-model-5-4-5.md`
- Chunks:
  - `processed/code/systems-performance-thread-state-nine-state-model-5-4-5-chunk-000001.md`

## Extracted ideas (with classification)

- (abstraction) **State decomposition** refines “on-CPU vs off-CPU” into categories that imply **different diagnostic families** (scheduler pressure, memory, disk, network, voluntary sleeps, locks, intentional idle) ([[model-classify-intervene]], [[context-switching]]).
- (diagnosis) Treat **idle as the only non-costly sink**: shrinking every other state (ceteris paribus) improves latency and throughput headroom ([[throughput-latency-metrics]]).
- (mechanism) The model sits on top of **threads as the schedulable unit** the OS moves between states ([[process-abstraction]]).

## Application validation

- **Worker pool “mostly waiting”**: if much time is classified as network or lock wait but offered load is low, reclassify mentally as **idle disguised as blocking primitives** before optimizing protocol parsers.

## Concepts reused / refined / created

- Reused (abstraction): [[model-classify-intervene]]
- Reused (mechanism): [[context-switching]]
- Reused (measurement): [[throughput-latency-metrics]]
- Reused (mechanism): [[process-abstraction]]
- Reused: [[systems-performance]]

## Links

- Concepts:
  - [[model-classify-intervene]]
  - [[context-switching]]
  - [[throughput-latency-metrics]]
  - [[process-abstraction]]
  - [[systems-performance]]
- Related sources:
  - [[systems-performance-use-method-software-resources-5-4-4]]
  - [[systems-performance-thread-state-investigation-and-measurement-5-4-5]]
