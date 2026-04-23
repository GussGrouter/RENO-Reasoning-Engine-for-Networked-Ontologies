# Systems Performance — Ch.9 §9.4.4 OS block I/O stack (scout PDF 460–520)

## Source

- Title: *Systems Performance: Enterprise and the Cloud* (Second Edition)
- Scout: `processed/code/systems-performance-ch9-scout-p460-520.txt`
- Scope: **block layer**, **merge**, **Linux schedulers / blk-mq**

## Processed artifacts

- `processed/code/systems-performance-disks-ch9-architecture-os-block-stack-9-4-4.md`

## Extracted ideas

- **Merge + scheduler** reshape **I/O stream** before device—explains **reordering**, **fairness**, **MQ scalability** ([[kernel-user-boundary]], [[queueing-theory]]).

## Decision clarity

**Decision:** choose **latency-aware schedulers / mq tuning** over **noop on HDD** when **starvation** or **unfair queue hogging** shows in **trace histograms**.

## Concepts reused / refined / created

- Reused: [[kernel-user-boundary]], [[queueing-theory]], [[throughput-latency-metrics]], [[measurement-validity]], [[systems-performance]]
- **Created:** none

## Links

- Concepts: [[kernel-user-boundary]], [[queueing-theory]], [[throughput-latency-metrics]], [[measurement-validity]], [[systems-performance]]
