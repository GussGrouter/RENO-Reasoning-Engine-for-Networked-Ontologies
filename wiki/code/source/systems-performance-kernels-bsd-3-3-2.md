# Systems Performance — BSD kernel developments (3.3.2) (PDF pages 118–170)

## Source

- Title: *Systems Performance: Enterprise and the Cloud* (Second Edition)
- Author: Brendan Gregg
- Raw: `raw/code/pdf/Systems.Performance.Enterprise.and.the.Cloud.pdf`
- Batch scope: Chapter 3, Section 3.3.2 BSD

## Processed artifacts

- Converted slice: `processed/code/systems-performance-kernels-bsd-3-3-2.md`
- Chunks:
  - `processed/code/systems-performance-kernels-bsd-3-3-2-chunk-000001.md`

## Extracted ideas (with classification)

- (mechanism) Paged virtual memory moves eviction granularity from “whole process” toward smaller units, changing the cost model of memory pressure vs CPU overhead.
- (mechanism) Demand paging defers committing physical pages until use, trading potential fault latency for lower upfront memory/time cost for unused regions.
- (diagnosis) BSD’s networking stack and sockets API became a long-lived performance baseline for Unix-like systems (relevant when comparing stack behavior, not as a “tool concept”).

## Concepts reused / refined / created

- Reused (mechanism): [[demand-paging]]
- Reused (abstraction): [[virtual-memory-abstraction]]
- Reused (mechanism): [[caching]]
- Reused (abstraction): [[kernel-architecture-models]]

## Links

- Concepts:
  - [[demand-paging]]
  - [[virtual-memory-abstraction]]
  - [[caching]]
  - [[kernel-architecture-models]]
