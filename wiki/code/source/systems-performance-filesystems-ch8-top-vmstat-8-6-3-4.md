# Systems Performance — top + vmstat page/buffer cache columns (§8.6.3–§8.6.4) (scout PDF 398–460)

## Source

- Title: *Systems Performance: Enterprise and the Cloud* (Second Edition)
- Author: Brendan Gregg
- Raw: `raw/code/pdf/Systems.Performance.Enterprise.and.the.Cloud.pdf`
- Batch scope: **§8.6.3 top** + **§8.6.4 vmstat** (sample **omitted** in processed extract)

## Processed artifacts

- Scout: `processed/code/systems-performance-ch8-scout-p398-460.txt`
- Converted slice: `processed/code/systems-performance-filesystems-ch8-top-vmstat-8-6-3-4.md`
- Chunks: `processed/code/systems-performance-filesystems-ch8-top-vmstat-8-6-3-4-chunk-000001.md`

## Extracted ideas (with classification)

- (same signal, different surface) **top** and **vmstat** both expose **buffer vs page cache** sizes—**representation** choice (parseable row vs live TUI) not a different physical truth ([[counters-statistics-metrics]]).
- (scope) **vmstat** memory columns are the same Ch.7 story with an FS angle: they help connect **block cache growth** to I/O wait without yet opening a syscall tracer.

## Application validation

- **Rising `wa` with flat `bi/bo`:** triage **not** as “disks idle” if **cache columns** show large retained read working sets—**semantics of what “I/O wait” means** may need VFS-level evidence.

## Decision clarity

- **Decision:** choose **vmstat 1s + mem column triage** over **diving into `iostat` first** when **suspecting page cache / read path** as the stateful player.

## Concepts reused / refined / created

- Reused: [[counters-statistics-metrics]], [[utilization-and-saturation]], [[caching]], [[measurement-validity]], [[systems-performance]]
- **Created:** none

## Links

- Concepts: [[counters-statistics-metrics]], [[caching]], [[utilization-and-saturation]], [[measurement-validity]], [[use-method]], [[systems-performance]]
- Related sources: [[systems-performance-filesystems-ch8-mount-free-8-6-1-2]], [[systems-performance-filesystems-ch8-sar-cache-dentry-8-6-5]]
