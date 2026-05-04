# Systems Performance — Unix kernel lineage (3.3.1) (PDF pages 118–170)

## Source

- Title: *Systems Performance: Enterprise and the Cloud* (Second Edition)
- Author: Brendan Gregg
- Raw: `raw/code/pdf/Systems.Performance.Enterprise.and.the.Cloud.pdf`
- Batch scope: Chapter 3, Section 3.3.1 Unix

## Processed artifacts

- Converted slice: `processed/code/systems-performance-kernels-unix-3-3-1.md`
- Chunks:
  - `processed/code/systems-performance-kernels-unix-3-3-1-chunk-000001.md`

## Extracted ideas (with classification)

- (abstraction) Early Unix philosophy pushes the kernel toward a small set of “real decisions,” favoring one strong default path over many optional privileged policy branches.
- (mechanism) Early performance-oriented kernel behaviors included scheduler priorities, larger disk I/O blocks with buffering, swapping idle work out of RAM, and multitasking for throughput.

## Concepts reused / refined / created

- Reused (abstraction): [[kernel-architecture-models]]
- Reused (abstraction): [[abstraction-design-principles]]
- Reused (abstraction): [[process-abstraction]]
- Reused (mechanism): [[context-switching]]
- Reused (abstraction): [[virtual-memory-abstraction]]
- Reused (mechanism): [[caching]]

## Links

- Concepts:
  - [[kernel-architecture-models]]
  - [[abstraction-design-principles]]
  - [[process-abstraction]]
  - [[context-switching]]
  - [[virtual-memory-abstraction]]
  - [[caching]]
