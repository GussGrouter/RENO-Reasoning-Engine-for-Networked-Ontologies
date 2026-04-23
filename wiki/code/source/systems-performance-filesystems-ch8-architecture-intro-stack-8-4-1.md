# Systems Performance — File system architecture + I/O stack (§8.4 + §8.4.1) (scout PDF 398–460)

## Source

- Title: *Systems Performance: Enterprise and the Cloud* (Second Edition)
- Author: Brendan Gregg
- Raw: `raw/code/pdf/Systems.Performance.Enterprise.and.the.Cloud.pdf`
- Batch scope: **§8.4** intro + **§8.4.1** I/O stack (figures in book) — **raw** vs **VFS path** distinction

## Processed artifacts

- Scout: `processed/code/systems-performance-ch8-scout-p398-460.txt`
- Converted slice: `processed/code/systems-performance-filesystems-ch8-architecture-intro-stack-8-4-1.md`
- Chunks: `processed/code/systems-performance-filesystems-ch8-architecture-intro-stack-8-4-1-chunk-000001.md`

## Extracted ideas (with classification)

- (structure) **Layered stack** sets where to instrument: **syscall → VFS → FS → block**; “**raw**” bypasses VFS/FS cache path ([[kernel-architecture-models]], [[resource-vs-implementation-bottleneck]], [[measurement-validity]]).

## Application validation

- **eBPF on block device only:** you may **miss** VFS coalescing / credit for app work—**add VFS/FS tracepoints** when classifying **logical vs physical** stories.

## Decision clarity

- **Decision:** choose **VFS/FS-level probes** over **block-device–only metrics** when **the question is application syscall latency**, not **array queue depth in isolation**.

## Concepts reused / refined / created

- Reused: [[kernel-architecture-models]], [[resource-vs-implementation-bottleneck]], [[measurement-validity]], [[systems-performance]]
- **Created:** none

## Links

- Concepts: [[kernel-architecture-models]], [[resource-vs-implementation-bottleneck]], [[measurement-validity]], [[systems-performance]]
- Related sources: [[systems-performance-filesystems-ch8-vfs-8-4-2]]
