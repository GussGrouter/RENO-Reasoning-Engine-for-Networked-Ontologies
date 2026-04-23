# Systems Performance — Extended BPF (3.4.4) (PDF pages 118–170)

## Source

- Title: *Systems Performance: Enterprise and the Cloud* (Second Edition)
- Author: Brendan Gregg
- Raw: `raw/code/pdf/Systems.Performance.Enterprise.and.the.Cloud.pdf`
- Batch scope: Chapter 3, Section 3.4.4 Extended BPF

## Processed artifacts

- Converted slice: `processed/code/systems-performance-extended-bpf-3-4-4.md`
- Chunks:
  - `processed/code/systems-performance-extended-bpf-3-4-4-chunk-000001.md`

## Extracted ideas (with classification)

- (mechanism) BPF programs attach to event sources (tracepoints, k/uprobes, perf events, sockets) and move programmable kernel-side work next to those events.
- (mechanism) Safety is enforced by verification (plus type information like BTF), constraining what loaded programs can do before they run in kernel mode.
- (measurement) Outputs can be streaming (ring buffer per event detail) or aggregated (maps/histograms), choosing between fidelity and overhead.

## Concepts reused / refined / created

- Reused (mechanism): [[extended-bpf]]
- Reused (measurement): [[event-tracing]]
- Reused (measurement): [[instrumentation-overhead-and-perturbation]]
- Reused (structure): [[kernel-user-boundary]]

## Links

- Concepts:
  - [[extended-bpf]]
  - [[event-tracing]]
  - [[instrumentation-overhead-and-perturbation]]
  - [[kernel-user-boundary]]
