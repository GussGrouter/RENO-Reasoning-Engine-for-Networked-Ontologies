# Systems Performance — kernels overview (3.3) (PDF pages 118–170)

## Source

- Title: *Systems Performance: Enterprise and the Cloud* (Second Edition)
- Author: Brendan Gregg
- Raw: `raw/code/pdf/Systems.Performance.Enterprise.and.the.Cloud.pdf`
- Batch scope: Chapter 3, Section 3.3 Kernels

## Processed artifacts

- Converted slice: `processed/code/systems-performance-kernels-3-3.md`
- Chunks:
  - `processed/code/systems-performance-kernels-3-3-chunk-000001.md`

## Extracted ideas (with classification)

- (abstraction) “Kernel differences” show up as different syscall surfaces, network stack shapes, scheduling policies, and filesystem stacks—i.e., different privileged implementation choices behind the same user-facing goals.
- (measurement) Documented syscall counts are a crude comparability signal across kernels/versions (useful as orientation, not as a full complexity model).
- (diagnosis) Growing syscall/API surface area increases learning, programming, and debugging time when performance work must cross the privilege boundary.

## Concepts reused / refined / created

- Reused (abstraction): [[kernel-architecture-models]]
- Reused (structure): [[kernel-user-boundary]]
- Reused (mechanism): [[system-call]]
- Reused (measurement): [[counters-statistics-metrics]]
- Reused (structure): [[resource-vs-implementation-bottleneck]]

## Links

- Concepts:
  - [[kernel-architecture-models]]
  - [[kernel-user-boundary]]
  - [[system-call]]
  - [[counters-statistics-metrics]]
  - [[resource-vs-implementation-bottleneck]]
