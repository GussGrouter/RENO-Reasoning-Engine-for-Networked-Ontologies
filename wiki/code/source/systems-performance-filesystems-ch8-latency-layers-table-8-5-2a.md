# Systems Performance — Four layers for file system latency (§8.5.2) (scout PDF 398–460)

## Source

- Title: *Systems Performance: Enterprise and the Cloud* (Second Edition)
- Author: Brendan Gregg
- Raw: `raw/code/pdf/Systems.Performance.Enterprise.and.the.Cloud.pdf`
- Batch scope: **§8.5.2** — **Table 8.4** layer taxonomy (rewritten for `pdftotext` table damage; full grid in PDF)

## Processed artifacts

- Scout: `processed/code/systems-performance-ch8-scout-p398-460.txt`
- Converted slice: `processed/code/systems-performance-filesystems-ch8-latency-layers-table-8-5-2a.md`
- Chunks: `processed/code/systems-performance-filesystems-ch8-latency-layers-table-8-5-2a-chunk-000001.md`

## Extracted ideas (with classification)

- (representation / scope) **Same “file system,” different surfaces**—**application**, **syscall**, **VFS**, and **top-of-FS** each answer a different question: user-visible effect, portable interface, generic kernel path, or one storage implementation. **Non-storage** VFS/syscall traffic (e.g. `proc`, sockets) can **poison** naïve traces unless **filtered** (semantics of the “file system” label).
- (representation) **Many syscalls, one story**—`read` family variants can all need coverage if you equate “one logical op” to a single trace point.

## Application validation

- **Layer pick is an instrument-choice problem:** confirm you are not profiling **socket** syscall volume when you meant **block-backed** latency—tie filters to **object identity** ([[measurement-validity]]).

## Decision clarity

- **Decision:** choose **syscall or VFS instrumentation with FS-type/path filters** over **application-only timers** when **you need comparable numbers across apps** but **still want kernel-attributable splits**.

## Concepts reused / refined / created

- Reused: [[measurement-validity]], [[latency-analysis]], [[event-tracing]], [[systems-performance]]
- **Created:** none

## Links

- Concepts: [[measurement-validity]], [[latency-analysis]], [[event-tracing]], [[instrumentation-overhead-and-perturbation]], [[systems-performance]]
- Related sources: [[systems-performance-filesystems-ch8-disk-latency-analysis-open-8-5-1-2]], [[systems-performance-filesystems-ch8-latency-presentation-drilldown-8-5-2b]]
