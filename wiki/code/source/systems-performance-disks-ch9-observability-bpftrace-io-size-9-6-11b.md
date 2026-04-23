# Systems Performance — Ch.9 §9.6.11 bpftrace (disk I/O size)

## Source

- Title: *Systems Performance: Enterprise and the Cloud* (Second Edition)
- Scout: `processed/code/systems-performance-ch9-scout-p460-520.txt`
- Scope: **§9.6.11** (part **b** of **c**—size distributions)

## Processed artifacts

- `processed/code/systems-performance-disks-ch9-observability-bpftrace-io-size-9-6-11b.md`
- Chunks: `*-chunk-000001.md`

## Extracted ideas

- **Size histograms by issuer** distinguish **few huge I/Os** from **many tiny I/Os**—different fixes (**aggregation**, **app batching**, **crypto block size**) ([[throughput-latency-metrics]], [[measurement-validity]] **scope/semantics** on **`comm`** at **`rq_issue`**).

## Concepts reused / refined / created

- Reused: [[throughput-latency-metrics]], [[measurement-validity]], [[extended-bpf]], [[systems-performance]]
- **Created:** none

## Links

- Concepts: [[throughput-latency-metrics]], [[measurement-validity]], [[extended-bpf]], [[systems-performance]]
