# Systems Performance — Percent of transaction time in the file system (§8.5.2) (scout PDF 398–460)

## Source

- Title: *Systems Performance: Enterprise and the Cloud* (Second Edition)
- Author: Brendan Gregg
- Raw: `raw/code/pdf/Systems.Performance.Enterprise.and.the.Cloud.pdf`
- Batch scope: **§8.5.2** *Transaction Cost* — fraction of blocking time in FS vs transaction (Figure 8.12 in book)

## Processed artifacts

- Scout: `processed/code/systems-performance-ch8-scout-p398-460.txt`
- Converted slice: `processed/code/systems-performance-filesystems-ch8-transaction-cost-fs-8-5-2c.md`
- Chunks: `processed/code/systems-performance-filesystems-ch8-transaction-cost-fs-8-5-2c-chunk-000001.md`

## Extracted ideas (with classification)

- (scope) **Blocking FS time / transaction time** ties storage work to **application SLO units**—a **semantic bridge** between user operations and kernel wait, not raw IOPS.
- (semantics) **Non-blocking I/O:** the metric counts only **blocking** waits; async work changes what “percent in FS” means ([[measurement-validity]]: same formula, different population).

## Application validation

- **90% of 200 ms transaction blocked in FS** → storage work is plausibly on the critical path; **1%** → redirect effort away from disk/Fs fire drills unless evidence shows non-blocking debt elsewhere.

## Decision clarity

- **Decision:** choose **deep file system / disk investigation** over **application CPU profiling** when **blocking FS fraction of the business transaction is high**; choose the **reverse** when **FS share is negligible** even if disks look busy in the aggregate.

## Concepts reused / refined / created

- Reused: [[measurement-validity]], [[resource-analysis-vs-workload-analysis]], [[throughput-latency-metrics]], [[systems-performance]]
- **Created:** none

## Links

- Concepts: [[measurement-validity]], [[resource-analysis-vs-workload-analysis]], [[throughput-latency-metrics]], [[latency-analysis]], [[systems-performance]]
- Related sources: [[systems-performance-filesystems-ch8-latency-presentation-drilldown-8-5-2b]], [[systems-performance-filesystems-ch8-workload-char-basic-8-5-3a]]
