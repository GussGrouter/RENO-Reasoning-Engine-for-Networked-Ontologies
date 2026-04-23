# Systems Performance — Ch.9 §9.6.9 biostacks

## Source

- Title: *Systems Performance: Enterprise and the Cloud* (Second Edition)
- Scout: `processed/code/systems-performance-ch9-scout-p460-520.txt`
- Scope: **§9.6.9**

## Processed artifacts

- `processed/code/systems-performance-disks-ch9-observability-biostacks-9-6-9.md`
- Chunks: `*-chunk-000001.md`

## Extracted ideas

- **Init stack + latency histogram** ties **which code path started I/O** to **how long that class waited**—surfaces **metadata / scrub / journal** “ghost” traffic ([[drill-down-analysis]], [[latency-analysis]], [[extended-bpf]]).

## Application hook

If **`pidstat` shows no obvious culprit** but disks churn: **`biostacks`** often reveals **filesystem housekeeping** or **volume/crypto paths**, not a misbehaving app tier.

## Concepts reused / refined / created

- Reused: [[drill-down-analysis]], [[latency-analysis]], [[extended-bpf]], [[event-tracing]], [[systems-performance]]
- **Created:** none

## Links

- Concepts: [[drill-down-analysis]], [[latency-analysis]], [[extended-bpf]], [[event-tracing]], [[systems-performance]]
