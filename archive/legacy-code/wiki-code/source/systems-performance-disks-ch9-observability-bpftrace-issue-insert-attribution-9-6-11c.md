# Systems Performance — Ch.9 §9.6.11 bpftrace (issue vs insert + RWBS keys)

## Source

- Title: *Systems Performance: Enterprise and the Cloud* (Second Edition)
- Scout: `processed/code/systems-performance-ch9-scout-p460-520.txt`
- Scope: **§9.6.11** (part **c** of **d**); superseded tail text appears in **`…-bpftrace-latency-errors-9-6-11d`** (`systems-performance-ch9-scout-p482-560.txt`)

## Processed artifacts

- `processed/code/systems-performance-disks-ch9-observability-bpftrace-issue-insert-attribution-9-6-11c.md`
- Chunks: `*-chunk-000001.md`

## Extracted ideas

- **`rq_issue` vs `rq_insert`** repeats the **§9.6.5 perf** attribution trade—pick probe to match **whether you care about submitter identity** or **full queue coverage** ([[measurement-validity]] **scope/semantics**).
- **`rwbs` keys** separate **sync writes** from **buffered writes**—same decision primitive as **splitting blended disk averages** elsewhere.

## Decision clarity

**Decision:** choose **`block_rq_insert`**-based histograms over **`block_rq_issue`** when **`comm` shows only `kworker`** but you need **who queued** the work.

## Concepts reused / refined / created

- Reused: [[measurement-validity]], [[extended-bpf]], [[throughput-latency-metrics]], [[systems-performance]]
- **Created:** none

## Links

- Concepts: [[measurement-validity]], [[extended-bpf]], [[throughput-latency-metrics]], [[systems-performance]]
