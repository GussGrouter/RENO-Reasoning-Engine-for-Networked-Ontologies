# Systems Performance — language virtual machines and observability depth (5.3.3) (PDF ~182–230)

## Source

- Title: *Systems Performance: Enterprise and the Cloud* (Second Edition)
- Author: Brendan Gregg
- Raw: `raw/code/pdf/Systems.Performance.Enterprise.and.the.Cloud.pdf`
- Batch scope: Chapter 5, Section 5.3.3 Virtual Machines

## Processed artifacts

- Converted slice: `processed/code/systems-performance-language-virtual-machines-5-3-3.md`
- Chunks:
  - `processed/code/systems-performance-language-virtual-machines-5-3-3-chunk-000001.md`

## Extracted ideas (with classification)

- (abstraction) **Bytecode portability** pairs with **staged execution** (interpret → JIT) so on-CPU behavior is several transformations away from source—evidence must often be gathered at **VM/tool boundaries** instead of generic OS profilers alone.
- (diagnosis) **Opaque stacks** push you toward VM-native probes and stable user-level trace points—same pattern as diagnosing managed services where the hypervisor/API is the real observability root ([[event-tracing]], [[instrumentation-overhead-and-perturbation]]).

## Application validation

- **Managed language services**: default to the runtime’s allocation/JIT/GC dashboards before opening a kernel-only profiler—otherwise you optimize the wrong translation layer.

## Concepts reused / refined / created

- Reused (abstraction): [[observability-vs-experimentation]]
- Reused (measurement): [[event-tracing]]
- Reused (measurement): [[instrumentation-overhead-and-perturbation]]
- Reused (structure): [[kernel-user-boundary]]
- Reused: [[systems-performance]]

## Links

- Concepts:
  - [[observability-vs-experimentation]]
  - [[event-tracing]]
  - [[instrumentation-overhead-and-perturbation]]
  - [[kernel-user-boundary]]
  - [[systems-performance]]
