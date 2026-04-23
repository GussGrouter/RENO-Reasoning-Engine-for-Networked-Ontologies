# Systems Performance — File system models (§8.2) (scout PDF 398–460)

## Source

- Title: *Systems Performance: Enterprise and the Cloud* (Second Edition)
- Author: Brendan Gregg
- Raw: `raw/code/pdf/Systems.Performance.Enterprise.and.the.Cloud.pdf`
- Batch scope: **§8.2** — interfaces diagram (figures in book), **cache hit/miss**, **second-level cache**, black-box latency stance

## Processed artifacts

- Scout: `processed/code/systems-performance-ch8-scout-p398-460.txt`
- Converted slice: `processed/code/systems-performance-filesystems-ch8-models-8-2.md`
- Chunks: `processed/code/systems-performance-filesystems-ch8-models-8-2-chunk-000001.md`

## Extracted ideas (with classification)

- (method) **Black-box FS study via operation latency** aligns with **latency decomposition** before opening internals ([[latency-analysis]], [[throughput-latency-metrics]]).
- (structure) **DRAM FS cache + optional flash tier** stack **multiple retention planes**—same symptom can be hit vs miss vs tier promotion ([[caching]], [[measurement-validity]]).

## Application validation

- **Warm-cache benchmark wins:** confirm whether production **cold starts** ever occur—otherwise **representation** of “fast FS” is wrong for rollout decisions.

## Decision clarity

- **Decision:** choose **operation-level latency probes on the syscall/VFS boundary** over **aggregate disk metrics** when **validating a new FS or mount option** for user-facing read paths.

## Concepts reused / refined / created

- Reused: [[latency-analysis]], [[throughput-latency-metrics]], [[caching]], [[measurement-validity]], [[systems-performance]]
- **Created:** none

## Links

- Concepts: [[latency-analysis]], [[throughput-latency-metrics]], [[caching]], [[measurement-validity]], [[systems-performance]]
- Related sources: [[systems-performance-filesystems-ch8-concept-latency-8-3-1]]
