# Systems Performance — Ch.9 §9.6 Observability Tools (intro + Table 9.5)

## Source

- Title: *Systems Performance: Enterprise and the Cloud* (Second Edition)
- Scout: `processed/code/systems-performance-ch9-scout-p460-520.txt`
- Scope: **§9.6** framed + **Table 9.5** tool index (**stops before §9.6.1 detail**)

## Processed artifacts

- `processed/code/systems-performance-disks-ch9-observability-intro-table-9-6.md`
- Chunks: `*-chunk-000001.md`

## Extracted ideas

- **Tool catalog follows methodology:** stats → **BPF tracing** → controller introspection—still need **§9.5 methods** so tooling does not become **comfort-first** investigation ([[streetlight-anti-method]], [[drill-down-analysis]], [[systems-performance]]).

## Decision clarity

**Decision:** choose **latency/workload methods + the smallest stat tool that answers the question** over **jumping to BPF** when **`iostat`/`sar` still falsify the hypothesis space**.

## Concepts reused / refined / created

- Reused: [[streetlight-anti-method]], [[drill-down-analysis]], [[extended-bpf]], [[systems-performance]]
- **Created:** none

## Links

- Concepts: [[streetlight-anti-method]], [[drill-down-analysis]], [[extended-bpf]], [[systems-performance]]
