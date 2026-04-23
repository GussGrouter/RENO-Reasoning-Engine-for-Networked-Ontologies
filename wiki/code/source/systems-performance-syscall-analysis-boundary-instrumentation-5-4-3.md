# Systems Performance — syscall analysis as boundary instrumentation (5.4.3) (PDF ~231–285)

## Source

- Title: *Systems Performance: Enterprise and the Cloud* (Second Edition)
- Author: Brendan Gregg
- Raw: `raw/code/pdf/Systems.Performance.Enterprise.and.the.Cloud.pdf`
- Batch scope: Chapter 5, Section 5.4.3 Syscall Analysis (intent and targets; tool names treated as pointers, not concepts)

## Processed artifacts

- Converted slice: `processed/code/systems-performance-syscall-analysis-boundary-instrumentation-5-4-3.md`
- Chunks:
  - `processed/code/systems-performance-syscall-analysis-boundary-instrumentation-5-4-3-chunk-000001.md`

## Extracted ideas (with classification)

- (mechanism) Syscalls are a **documented, synchronous boundary**: events align with application stacks, so attribution stays tied to responsible code paths ([[system-call]], [[kernel-user-boundary]]).
- (diagnosis) Elevated **kernel CPU** prompts syscall investigation, but **not all kernel time is syscalls**—keep explicit “remaining mass” hypotheses ([[known-unknowns-framework]]).
- (measurement) Syscall-level study supports **I/O shape** questions (sizes, flags, call sites), bridging resource symptoms to workload structure ([[resource-analysis-vs-workload-analysis]], [[event-tracing]]).

## Application validation

- **High %sys on a stateless API tier**: rank syscalls by time, then walk stacks at those sites—if stacks point at `sendmsg` with tiny buffers, fix coalescing before buying faster NICs.

## Concepts reused / refined / created

- Reused (mechanism): [[system-call]]
- Reused (structure): [[kernel-user-boundary]]
- Reused (diagnosis): [[known-unknowns-framework]]
- Reused (abstraction): [[resource-analysis-vs-workload-analysis]]
- Reused (measurement): [[event-tracing]]
- Reused: [[systems-performance]]

## Links

- Concepts:
  - [[system-call]]
  - [[kernel-user-boundary]]
  - [[known-unknowns-framework]]
  - [[resource-analysis-vs-workload-analysis]]
  - [[event-tracing]]
  - [[systems-performance]]
- Related sources:
  - [[systems-performance-off-cpu-narrowing-filters-5-4-2]]
  - [[systems-performance-use-method-software-resources-5-4-4]]
