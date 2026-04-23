# Systems Performance — Why read(2) is a poor standalone FS signal (§8.6.15) (scout PDF 398–460)

## Source

- Title: *Systems Performance: Enterprise and the Cloud* (Second Edition)
- Author: Brendan Gregg
- Raw: `raw/code/pdf/Systems.Performance.Enterprise.and.the.Cloud.pdf`
- Batch scope: **§8.6.15** *Syscall Tracing* — **`openat` works**, **`read` is ambiguous** + remediation ladder

## Processed artifacts

- Scout: `processed/code/systems-performance-ch8-scout-p398-460.txt`
- Converted slice: `processed/code/systems-performance-filesystems-ch8-bpftrace-syscall-semantics-8-6-15b.md`
- Chunks: `processed/code/systems-performance-filesystems-ch8-bpftrace-syscall-semantics-8-6-15b-chunk-000001.md`

## Extracted ideas (with classification)

- **Scope/semantics:** `read(2)` counts **files, sockets, /proc, …** identically—high counts do not imply disk reads ([[measurement-validity]]: **misleading aggregation**).
- **Representation gap:** tracepoint exposes **FD as integer**, not type; **BPF cannot consult `/proc`** from the restricted context as naïvely as shell tools ([[kernel-user-boundary]]).
- **Escalation path:** post-process FD→path, future FD-path helper, **VFS-level** tracing, or **FS-function** tools (`*dist`/`*slower`) that exclude non-file traffic.

## Application validation

- **Java dominates `read` counts:** do **not** conclude “disk-heavy” until FD typing or FS-layer probes prove file-backed reads.

## Decision clarity

- **Decision:** choose **FS-specific BPF tools or VFS-typed histograms** over **raw `read` syscall totals by process** when **socket vs file separation** decides your scaling lever.

## Concepts reused / refined / created

- Reused: [[measurement-validity]], [[kernel-user-boundary]], [[extended-bpf]], [[latency-analysis]], [[systems-performance]]
- **Created:** none

## Links

- Concepts: [[measurement-validity]], [[kernel-user-boundary]], [[extended-bpf]], [[latency-analysis]], [[systems-performance]]
- Related sources: [[systems-performance-filesystems-ch8-bpftrace-oneliners-8-6-15a]], [[systems-performance-filesystems-ch8-bpftrace-vfs-fs-internals-8-6-15c]]
