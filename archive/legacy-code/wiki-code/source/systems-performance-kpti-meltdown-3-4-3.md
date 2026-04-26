# Systems Performance — KPTI (Meltdown) (3.4.3) (PDF pages 118–170)

## Source

- Title: *Systems Performance: Enterprise and the Cloud* (Second Edition)
- Author: Brendan Gregg
- Raw: `raw/code/pdf/Systems.Performance.Enterprise.and.the.Cloud.pdf`
- Batch scope: Chapter 3, Section 3.4.3 KPTI (Meltdown)

## Processed artifacts

- Converted slice: `processed/code/systems-performance-kpti-meltdown-3-4-3.md`
- Chunks:
  - `processed/code/systems-performance-kpti-meltdown-3-4-3-chunk-000001.md`

## Extracted ideas (with classification)

- (tradeoff) Security mitigations can shift an implementation from “fast on paper” to “slower in practice” by adding extra privileged work on syscall/mode transitions and address-space switches.
- (diagnosis) The performance impact of such mitigations often scales with syscall rate and TLB behavior, so measurement should emphasize boundary-crossing frequency and memory/TLB warm-up—not only CPU utilization.
- (mechanism) Hardware features (e.g., PCID) can partially restore performance by avoiding some TLB flush work, changing the cost model of context/mode switches under mitigation.

## Concepts reused / refined / created

- Reused (structure): [[resource-vs-implementation-bottleneck]]
- Reused (structure): [[kernel-user-boundary]]
- Reused (mechanism): [[system-call]]
- Reused (mechanism): [[context-switching]]
- Reused (abstraction): [[virtual-memory-abstraction]]
- Reused (measurement): [[event-tracing]]
- Reused (mechanism): [[extended-bpf]]
- Reused (heuristic): [[static-performance-tuning]]

## Links

- Concepts:
  - [[resource-vs-implementation-bottleneck]]
  - [[kernel-user-boundary]]
  - [[system-call]]
  - [[context-switching]]
  - [[virtual-memory-abstraction]]
  - [[event-tracing]]
  - [[extended-bpf]]
  - [[static-performance-tuning]]
- Related sources:
  - [[systems-performance-cpu-security-mitigations-boot-6-9-9]]
