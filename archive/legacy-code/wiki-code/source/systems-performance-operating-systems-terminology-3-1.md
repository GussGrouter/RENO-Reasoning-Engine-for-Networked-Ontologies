# Systems Performance — operating systems terminology (3.1) (PDF pages 118–134)

## Source

- Title: *Systems Performance: Enterprise and the Cloud* (Second Edition)
- Author: Brendan Gregg
- Raw: `raw/code/pdf/Systems.Performance.Enterprise.and.the.Cloud.pdf`
- Batch scope: Chapter 3, Section 3.1 Terminology (plus chapter introduction on the same PDF pages)

## Processed artifacts

- Converted slice: `processed/code/systems-performance-operating-systems-terminology-3-1.md`
- Chunks:
  - `processed/code/systems-performance-operating-systems-terminology-3-1-chunk-000001.md`

## Extracted ideas (with classification)

- (abstraction) The chapter frames OS/kernel knowledge as the substrate for performance hypotheses (syscalls, scheduling, memory, file system I/O paths).
- (abstraction) “Operating system” spans bootable user-facing software: kernel, admin tooling, and system libraries—not only the kernel.
- (abstraction) Core entities: kernel vs user land; processes vs threads vs Linux tasks as schedulable units.
- (mechanism) Crossing privilege is organized around traps/syscalls/interrupts; context switches vs mode switches are distinct costs.
- (abstraction) Virtual memory is presented as the multitasking/oversubscription abstraction; kernel vs user address spaces partition visibility.
- (mechanism) BPF programs are first-class kernel-mode programs in a dedicated execution environment (naming note: “BPF” is treated as a name, not an acronym).

## Concepts reused / refined / created

- Created (mechanism): [[extended-bpf]]
- Reused (abstraction): [[process-abstraction]]
- Reused (mechanism): [[context-switching]]
- Reused (mechanism): [[system-call]]
- Reused (structure): [[kernel-user-boundary]]
- Reused (abstraction): [[virtual-memory-abstraction]]

## Links

- Concepts:
  - [[extended-bpf]]
  - [[process-abstraction]]
  - [[context-switching]]
  - [[system-call]]
  - [[kernel-user-boundary]]
  - [[virtual-memory-abstraction]]
