# Systems Performance — netlink observability interface (4.3.4) (PDF pages 171–220)

## Source

- Title: *Systems Performance: Enterprise and the Cloud* (Second Edition)
- Author: Brendan Gregg
- Raw: `raw/code/pdf/Systems.Performance.Enterprise.and.the.Cloud.pdf`
- Batch scope: Chapter 4, Section 4.3.4 netlink

## Processed artifacts

- Converted slice: `processed/code/systems-performance-netlink-observability-4-3-4.md`
- Chunks:
  - `processed/code/systems-performance-netlink-observability-4-3-4-chunk-000001.md`

## Extracted ideas (with classification)

- (mechanism) Netlink is a **binary request/response** channel for kernel information, typically more efficient than parsing textual `/proc` views and can support notification-style updates.
- (abstraction) The decision pattern is familiar: **human-friendly text interfaces** vs **machine-efficient structured interfaces**—choose based on rate, volume, automation needs, and integration cost.

## Concepts reused / refined / created

- Reused (structure): [[resource-vs-implementation-bottleneck]]
- Reused (measurement): [[instrumentation-overhead-and-perturbation]]
- Reused (structure): [[kernel-user-boundary]]
- Reused: [[systems-performance]]

## Links

- Concepts:
  - [[resource-vs-implementation-bottleneck]]
  - [[instrumentation-overhead-and-perturbation]]
  - [[kernel-user-boundary]]
  - [[systems-performance]]
