# Systems Performance — Other FS observability tools (index) (§8.6.17) (scout PDF 398–460)

## Source

- Title: *Systems Performance: Enterprise and the Cloud* (Second Edition)
- Author: Brendan Gregg
- Raw: `raw/code/pdf/Systems.Performance.Enterprise.and.the.Cloud.pdf`
- Batch scope: **§8.6.17** — **Table 8.7** (**omitted**); **df** / **inotify** / **FS-specific tooling** pointers

## Processed artifacts

- Scout: `processed/code/systems-performance-ch8-scout-p398-460.txt`
- Converted slice: `processed/code/systems-performance-filesystems-ch8-other-tools-8-6-17.md`
- Chunks: `processed/code/systems-performance-filesystems-ch8-other-tools-8-6-17-chunk-000001.md`

## Extracted ideas (with classification)

- **External catalog:** many BPF/experimental tools live in **other chapters** or **[Gregg 19]**—this section is a **reading map**, not a new measurement theory ([[extended-bpf]], [[drill-down-analysis]]).

## Application validation

- When stuck after Ch.8 basics, search **BPFT book + Ch.5 tools** before writing custom BPF—often a **named script** already encodes the right probe surface.

## Decision clarity

- **Decision:** choose **published tool + man page contract** over **forking your own tracer** when **your question matches an existing syscall/VFS/tracepoint axis** documented in the table.

## Concepts reused / refined / created

- Reused: [[extended-bpf]], [[event-tracing]], [[drill-down-analysis]], [[systems-performance]]
- **Created:** none

## Links

- Concepts: [[extended-bpf]], [[event-tracing]], [[drill-down-analysis]], [[systems-performance]]
- Related sources: [[systems-performance-filesystems-ch8-bpftrace-vfs-fs-internals-8-6-15c]], [[systems-performance-filesystems-ch8-zfs-arc-iostat-8-6-zfs]]
