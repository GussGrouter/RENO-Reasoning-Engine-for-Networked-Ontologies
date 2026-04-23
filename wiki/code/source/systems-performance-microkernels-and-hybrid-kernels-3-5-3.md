# Systems Performance — microkernels and hybrid kernels (3.5.3) (PDF pages 118–170)

## Source

- Title: *Systems Performance: Enterprise and the Cloud* (Second Edition)
- Author: Brendan Gregg
- Raw: `raw/code/pdf/Systems.Performance.Enterprise.and.the.Cloud.pdf`
- Batch scope: Chapter 3, Section 3.5.3 Microkernels and Hybrid Kernels

## Processed artifacts

- Converted slice: `processed/code/systems-performance-microkernels-and-hybrid-kernels-3-5-3.md`
- Chunks:
  - `processed/code/systems-performance-microkernels-and-hybrid-kernels-3-5-3-chunk-000001.md`

## Extracted ideas (with classification)

- (abstraction) Microkernels push filesystems/drivers/network stacks to user mode, trading IPC steps and context for modularity and fault isolation.
- (abstraction) Hybrid kernels selectively re-inline performance-critical paths to recover monolithic-style fast calls while keeping modular boundaries elsewhere.

## Concepts reused / refined / created

- Reused (abstraction): [[kernel-architecture-models]]
- Reused (structure): [[resource-vs-implementation-bottleneck]]
- Reused (mechanism): [[context-switching]]

## Links

- Concepts:
  - [[kernel-architecture-models]]
  - [[resource-vs-implementation-bottleneck]]
  - [[context-switching]]
