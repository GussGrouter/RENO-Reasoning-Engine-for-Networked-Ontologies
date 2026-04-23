# Systems Performance — P-states vs C-states: performance knobs vs idle depth (6.4.1) (PDF ~231–285)

## Source

- Title: *Systems Performance: Enterprise and the Cloud* (Second Edition)
- Author: Brendan Gregg
- Raw: `raw/code/pdf/Systems.Performance.Enterprise.and.the.Cloud.pdf`
- Batch scope: Chapter 6, Section 6.4.1 — **P-States and C-States** narrative through deep-idle coherency tradeoffs (extract stops before the **CPU Caches** section)

## Processed artifacts

- Converted slice: `processed/code/systems-performance-cpu-p-states-and-c-states-6-4-1.md`
- Chunks:
  - `processed/code/systems-performance-cpu-p-states-and-c-states-6-4-1-chunk-000001.md`

## Extracted ideas (with classification)

- (mechanism) **P-states reshape the time domain of execution** by changing **effective clock during active work**—this is a **throughput/latency knob** that can be driven by **firmware, thermals, or OS policy**, so “CPU busy” does not map linearly to “useful progress” ([[throughput-latency-metrics]], [[cross-component-interactions]]).
- (mechanism) **C-states trade idle power for wakeup latency**; deeper states can **alter coherency behavior** (e.g., reduced snooping)—idle optimization can become a **correctness/perf interaction** under concurrent memory traffic, not only a power story ([[throughput-latency-metrics]], [[caching]]).
- (measurement) **Named ACPI states are a vocabulary**, not the diagnosis: the engineering move is to connect **observed frequency/idle residency** to **tail latency and coherency stalls** under your workload ([[measurement-validity]]).

## Application validation

- **Microservice p99 spikes after power governor change** → compare **P0 residency + C-state distribution** against latency; deeper C-states often explain **wakeup tax** on bursty RPC servers.

## Decision clarity

- **Decision**: choose **shallower idle (C-state floor) / performance governor** over **more cores** when load is **sparse but latency-sensitive** and profiles show **idle-entry/wakeup** dominating short requests.

## Concepts reused / refined / created

- Reused (structure): [[throughput-latency-metrics]]
- Reused (structure): [[cross-component-interactions]]
- Reused (mechanism): [[caching]]
- Reused (abstraction): [[measurement-validity]]
- Reused: [[systems-performance]]

## Links

- Concepts:
  - [[throughput-latency-metrics]]
  - [[cross-component-interactions]]
  - [[caching]]
  - [[measurement-validity]]
  - [[systems-performance]]
- Related sources:
  - [[systems-performance-cpu-hardware-processor-subsystems-intro-6-4-1]]
  - [[systems-performance-cpu-on-chip-cache-hierarchy-and-llc-6-4-1]]
