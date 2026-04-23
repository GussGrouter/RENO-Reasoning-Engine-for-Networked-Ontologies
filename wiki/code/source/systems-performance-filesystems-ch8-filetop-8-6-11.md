# Systems Performance — filetop (§8.6.11) (scout PDF 398–460)

## Source

- Title: *Systems Performance: Enterprise and the Cloud* (Second Edition)
- Author: Brendan Gregg
- Raw: `raw/code/pdf/Systems.Performance.Enterprise.and.the.Cloud.pdf`
- Batch scope: **§8.6.11** — **top-for-files** + **`-a`** mixes sockets/devices with regular files

## Processed artifacts

- Scout: `processed/code/systems-performance-ch8-scout-p398-460.txt`
- Converted slice: `processed/code/systems-performance-filesystems-ch8-filetop-8-6-11.md`
- Chunks: `processed/code/systems-performance-filesystems-ch8-filetop-8-6-11-chunk-000001.md`

## Extracted ideas (with classification)

- **Workload steering:** surfaces **unexpected hot files** analogously to CPU top—supports eliminate-work / relocate-data decisions ([[resource-analysis-vs-workload-analysis]]).
- **Regular vs all:** default hides non-regular nodes; **`-a`** reveals when “file” heat is actually **sockets or device special files**.

## Application validation

- **Surprise leader is `TCP` row:** you are no longer in “disk file tuning”—switch diagnosis to **network/session** framing before tuning ext4.

## Decision clarity

- **Decision:** choose **`filetop` default (regular files)** over **`-a`** when **hunting tablespace/log hot spots**; choose **`-a`** when **diagnosing mixed FD types** masquerading as FS load.

## Concepts reused / refined / created

- Reused: [[resource-analysis-vs-workload-analysis]], [[event-tracing]], [[extended-bpf]], [[systems-performance]]
- **Created:** none

## Links

- Concepts: [[resource-analysis-vs-workload-analysis]], [[event-tracing]], [[extended-bpf]], [[systems-performance]]
- Related sources: [[systems-performance-filesystems-ch8-opensnoop-8-6-10]], [[systems-performance-filesystems-ch8-cachestat-8-6-12]]
