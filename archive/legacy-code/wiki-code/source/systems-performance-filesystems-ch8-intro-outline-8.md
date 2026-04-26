# Systems Performance — Chapter 8 File Systems: intro (scout PDF 398–460 extract)

## Source

- Title: *Systems Performance: Enterprise and the Cloud* (Second Edition)
- Author: Brendan Gregg
- Raw: `raw/code/pdf/Systems.Performance.Enterprise.and.the.Cloud.pdf`
- Batch scope: Chapter 8 opening — **why FS matters vs disks**, learning objectives, **six-part chapter map**

## Processed artifacts

- Scout: `processed/code/systems-performance-ch8-scout-p398-460.txt` (**pdftotext -f 398 -l 460**)
- Converted slice: `processed/code/systems-performance-filesystems-ch8-intro-outline-8.md`
- Chunks: `processed/code/systems-performance-filesystems-ch8-intro-outline-8-chunk-000001.md`

## Extracted ideas (with classification)

- (structure) Applications wait on the **file system interface**, not raw devices—**latency and attribution** questions route through FS behavior ([[throughput-latency-metrics]], [[resource-vs-implementation-bottleneck]]).
- (heuristic) Historical tooling bias toward **disk counters** leaves FS as a **blind spot**—explicit **logical-operation** framing is required ([[measurement-validity]], [[drill-down-analysis]]).

## Application validation

- **“Disk is idle” while app stalls:** treat **FS queue + syscall path + cache** as the primary hypothesis plane before expanding storage arrays.

## Decision clarity

- **Decision:** choose **file-system–level latency and operation tracing** over **disk throughput dashboards alone** when **application threads block on read/write/stat paths** but **device utilization looks unrelated**.

## Concepts reused / refined / created

- Reused: [[throughput-latency-metrics]], [[resource-vs-implementation-bottleneck]], [[measurement-validity]], [[drill-down-analysis]], [[systems-performance]]
- **Created:** none

## Links

- Concepts: [[throughput-latency-metrics]], [[resource-vs-implementation-bottleneck]], [[measurement-validity]], [[drill-down-analysis]], [[systems-performance]]
- Related sources: [[systems-performance-filesystems-ch8-models-8-2]]
