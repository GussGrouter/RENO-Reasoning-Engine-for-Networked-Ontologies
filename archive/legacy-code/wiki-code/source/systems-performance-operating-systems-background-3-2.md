# Systems Performance — operating systems background (3.2) (PDF pages 118–170)

## Source

- Title: *Systems Performance: Enterprise and the Cloud* (Second Edition)
- Author: Brendan Gregg
- Raw: `raw/code/pdf/Systems.Performance.Enterprise.and.the.Cloud.pdf`
- Batch scope: Chapter 3, Section 3.2 Background (through the end of 3.2.x before Section 3.3 Kernels)

## Processed artifacts

- Converted slice: `processed/code/systems-performance-operating-systems-background-3-2.md`
- Chunks:
  - `processed/code/systems-performance-operating-systems-background-3-2-chunk-000001.md`

## Extracted ideas (with classification)

- (abstraction) Unix-like systems commonly use a monolithic kernel model, but microkernel, unikernel, and hybrid models change where privileged code and IPC live.
- (mechanism) Linux extends the model with eBPF as a verified kernel-mode program type with helper APIs (ties forward to later BPF tooling chapters).
- (mechanism) Kernel work is often “on demand” (syscalls/interrupts) plus lightweight housekeeping threads; I/O-heavy workloads can spend substantial time in kernel context.
- (diagnosis) Even compute-heavy user workloads can be perturbed by kernel decisions (scheduler placement, contention), not only explicit syscalls.
- (mechanism) Kernel vs user modes are implemented with hardware privilege rings; syscalls mode-switch; blocking syscalls may also context-switch.
- (mechanism) Common optimizations reduce boundary crossings (vDSO user-mode syscalls, mmap I/O paths, kernel bypass frameworks, in-kernel or BPF-based approaches).

## Concepts reused / refined / created

- Created (abstraction): [[kernel-architecture-models]]
- Reused (mechanism): [[extended-bpf]]
- Reused (structure): [[kernel-user-boundary]]
- Reused (mechanism): [[system-call]]
- Reused (mechanism): [[context-switching]]
- Reused (abstraction): [[resource-vs-implementation-bottleneck]]

## Links

- Concepts:
  - [[kernel-architecture-models]]
  - [[extended-bpf]]
  - [[kernel-user-boundary]]
  - [[system-call]]
  - [[context-switching]]
  - [[resource-vs-implementation-bottleneck]]
