# Systems Performance — VFS latency typing + FS internals probe inventory (§8.6.15 tail) (scout PDF 398–460)

## Source

- Title: *Systems Performance: Enterprise and the Cloud* (Second Edition)
- Author: Brendan Gregg
- Raw: `raw/code/pdf/Systems.Performance.Enterprise.and.the.Cloud.pdf`
- Batch scope: **§8.6.15** — **VFS counts/latency by superblock type**, **async vs request-path caveat**, **ext4 tracepoint vs kprobe breadth**

## Processed artifacts

- Scout: `processed/code/systems-performance-ch8-scout-p398-460.txt`
- Converted slice: `processed/code/systems-performance-filesystems-ch8-bpftrace-vfs-fs-internals-8-6-15c.md`
- Chunks: `processed/code/systems-performance-filesystems-ch8-bpftrace-vfs-fs-internals-8-6-15c-chunk-000001.md`

## Extracted ideas (with classification)

- **Typing latency:** derive **filesystem class** (`ext4`, `sockfs`, …) from kernel structures—reduces socket/proc confusion inherent at raw `read` ([[latency-analysis]]).
- **Applicability caveat:** VFS latency may be **background**—add **`ustack`** keys when proving **request-path** stalls ([[throughput-latency-metrics]] timing semantics).
- **Internals ladder:** prefer **stable tracepoints**, fall back to **kprobes**—inventory scale (example: **105** ext4 tracepoints vs **538** `ext4_*` kprobes on cited kernel) guides maintenance cost ([[extended-bpf]]).

## Application validation

- **Histogram says `sockfs` slow but app fine:** attach **user stack keying**—you may be watching **kernel helper** traffic, not the customer request.

## Decision clarity

- **Decision:** choose **tracepoint-first custom tools** over **spray-and-pray `kprobe:ext4_*`** when **you must ship probes across kernel minor versions**.

## Concepts reused / refined / created

- Reused: [[latency-analysis]], [[extended-bpf]], [[throughput-latency-metrics]], [[kernel-architecture-models]], [[systems-performance]]
- **Created:** none

## Links

- Concepts: [[latency-analysis]], [[extended-bpf]], [[throughput-latency-metrics]], [[kernel-architecture-models]], [[systems-performance]]
- Related sources: [[systems-performance-filesystems-ch8-bpftrace-syscall-semantics-8-6-15b]], [[systems-performance-filesystems-ch8-latency-layers-table-8-5-2a]]
