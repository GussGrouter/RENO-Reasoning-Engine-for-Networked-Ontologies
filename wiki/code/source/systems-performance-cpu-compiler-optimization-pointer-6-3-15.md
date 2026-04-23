# Systems Performance — Compiler generation as a static performance lever (6.3.15) (PDF ~231–285)

## Source

- Title: *Systems Performance: Enterprise and the Cloud* (Second Edition)
- Author: Brendan Gregg
- Raw: `raw/code/pdf/Systems.Performance.Enterprise.and.the.Cloud.pdf`
- Batch scope: Chapter 6, Section 6.3.15 (compiler options/updates; pointer to Chapter 5 compiled languages)

## Processed artifacts

- Converted slice: `processed/code/systems-performance-cpu-compiler-optimization-pointer-6-3-15.md`
- Chunks:
  - `processed/code/systems-performance-cpu-compiler-optimization-pointer-6-3-15-chunk-000001.md`

## Extracted ideas (with classification)

- (measurement) **Toolchain is part of the workload’s performance envelope**: newer compilers can exploit **ISA features** and optimization passes—**rebuild** can move the baseline more than micro-tuning hot paths ([[static-performance-tuning]], [[measurement-validity]]).
- (abstraction) **Word size / codegen flags** interact with **ABI and register conventions**—this ties CPU runtime to **build-time configuration**, not only algorithmic complexity ([[static-performance-tuning]], [[throughput-latency-metrics]]).

## Application validation

- **LTS distro packages**: upgrading **GCC/Clang major** on the same hardware → treat as a **controlled experiment** (same inputs, same flags) before attributing wins to app code.

## Decision clarity

- **Decision**: choose **compiler/ISA baseline upgrade + flag audit** over **kernel tuning** when profiles show **instruction selection / autovec gaps** rather than **scheduler or IO waits**.

## Concepts reused / refined / created

- Reused (heuristic): [[static-performance-tuning]]
- Reused (abstraction): [[measurement-validity]]
- Reused (structure): [[throughput-latency-metrics]]
- Reused: [[systems-performance]]

## Links

- Concepts:
  - [[static-performance-tuning]]
  - [[measurement-validity]]
  - [[throughput-latency-metrics]]
  - [[systems-performance]]
- Related sources:
  - [[systems-performance-cpu-parallelism-footprint-and-word-size-6-3-14]]
  - [[systems-performance-cpu-hardware-processor-subsystems-intro-6-4-1]]
