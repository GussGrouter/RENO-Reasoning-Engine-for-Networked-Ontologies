# Systems Performance — Ch.9 §9.5 intro + §9.5.1 Tools method (scout PDF 460–520)

## Source

- Title: *Systems Performance: Enterprise and the Cloud* (Second Edition)
- Scout: `processed/code/systems-performance-ch9-scout-p460-520.txt`
- Scope: **Table 9.4** summarized; investigation order; **§9.5.1**

## Processed artifacts

- `processed/code/systems-performance-disks-ch9-methodology-intro-tools-9-5-1.md`
- Chunks: `*-chunk-000001.md`

## Extracted ideas

- **Tools-first** is **cheap entry** but **coverage-limited**—pair with structured methods ([[streetlight-anti-method]], [[drill-down-analysis]]).

## Decision clarity

**Decision:** choose **USE + workload characterization** over **only `iostat` iteration** when **symptoms involve tails or per-tenant skew** the basic tools hide.

## Concepts reused / refined / created

- Reused: [[streetlight-anti-method]], [[drill-down-analysis]], [[throughput-latency-metrics]], [[measurement-validity]], [[systems-performance]]
- **Created:** none

## Links

- Concepts: [[streetlight-anti-method]], [[drill-down-analysis]], [[throughput-latency-metrics]], [[measurement-validity]], [[systems-performance]]
