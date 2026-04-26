# Systems Performance — bpftrace one-liners for FS work (§8.6.15 beginning) (scout PDF 398–460)

## Source

- Title: *Systems Performance: Enterprise and the Cloud* (Second Edition)
- Author: Brendan Gregg
- Raw: `raw/code/pdf/Systems.Performance.Enterprise.and.the.Cloud.pdf`
- Batch scope: **§8.6.15** — **bpftrace** intro + **One-Liners** catalogue (verbatim lines in PDF)

## Processed artifacts

- Scout: `processed/code/systems-performance-ch8-scout-p398-460.txt`
- Converted slice: `processed/code/systems-performance-filesystems-ch8-bpftrace-oneliners-8-6-15a.md`
- Chunks: `processed/code/systems-performance-filesystems-ch8-bpftrace-oneliners-8-6-15a-chunk-000001.md`

## Extracted ideas (with classification)

- **Composable probes:** syscall entry/exit, tracepoint wildcards, `vfs_*` kprobe fan-out, FS-specific probes, stacks—same engine, different **questions** ([[extended-bpf]]).

## Application validation

- Need **“which syscall variants fire?”**—use `sys_enter_*read*` wildcard counts before writing a bespoke tool.

## Decision clarity

- **Decision:** choose **bpftrace histogram of read sizes / return bytes** over **vendor APM averages** when **you must know I/O shape** (`count`/`ret` distributions) behind a latency spike.

## Concepts reused / refined / created

- Reused: [[extended-bpf]], [[systems-performance]]
- **Created:** none

## Links

- Concepts: [[extended-bpf]], [[kernel-user-boundary]], [[systems-performance]]
- Related sources: [[systems-performance-filesystems-ch8-ext4slower-8-6-14]], [[systems-performance-filesystems-ch8-bpftrace-syscall-semantics-8-6-15b]]
