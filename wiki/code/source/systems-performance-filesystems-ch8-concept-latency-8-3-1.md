# Systems Performance — File system latency concept (§8.3.1) (scout PDF 398–460)

## Source

- Title: *Systems Performance: Enterprise and the Cloud* (Second Edition)
- Author: Brendan Gregg
- Raw: `raw/code/pdf/Systems.Performance.Enterprise.and.the.Cloud.pdf`
- Batch scope: **§8.3.1** — definition of **FS latency**, blocking threads, exceptions (prefetch/async), **disk stats can mislead** when flush traffic isn’t on the app path

## Processed artifacts

- Scout: `processed/code/systems-performance-ch8-scout-p398-460.txt`
- Converted slice: `processed/code/systems-performance-filesystems-ch8-concept-latency-8-3-1.md`
- Chunks: `processed/code/systems-performance-filesystems-ch8-concept-latency-8-3-1-chunk-000001.md`

## Extracted ideas (with classification)

- (measurement) **Primary FS metric is end-to-end logical op latency**, including FS + block path—not “disk busy %” ([[throughput-latency-metrics]], [[latency-analysis]]).
- (scope) **Background flush bursts** may spike **disk** metrics without blocking **current** app threads—**semantic mismatch** vs user pain ([[measurement-validity]], [[resource-vs-implementation-bottleneck]]).

## Application validation

- **Disk latency spikes during backups:** check **whether user requests stall**—if not, chase **prefetch/write-back policy**, not **array upgrades**.

## Decision clarity

- **Decision:** choose **application-visible FS/latency instrumentation** over **storage device dashboards** when **prioritizing customer-visible stalls** vs **housekeeping I/O**.

## Concepts reused / refined / created

- Reused: [[throughput-latency-metrics]], [[latency-analysis]], [[measurement-validity]], [[resource-vs-implementation-bottleneck]], [[systems-performance]]
- **Created:** none

## Links

- Concepts: [[throughput-latency-metrics]], [[latency-analysis]], [[measurement-validity]], [[resource-vs-implementation-bottleneck]], [[systems-performance]]
- Related sources: [[systems-performance-filesystems-ch8-concept-caching-8-3-2]]
