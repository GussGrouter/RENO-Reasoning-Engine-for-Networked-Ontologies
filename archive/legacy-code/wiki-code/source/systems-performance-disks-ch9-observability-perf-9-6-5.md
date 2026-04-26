# Systems Performance — Ch.9 §9.6.5 perf (block tracepoints)

## Source

- Title: *Systems Performance: Enterprise and the Cloud* (Second Edition)
- Scout: `processed/code/systems-performance-ch9-scout-p460-520.txt`
- Scope: **§9.6.5**

## Processed artifacts

- `processed/code/systems-performance-disks-ch9-observability-perf-9-6-5.md`
- Chunks: `*-chunk-000001.md`

## Extracted ideas

- **Tracepoints are the vocabulary** for **block-layer causality**; **`perf`** turns them into **stack-bearing evidence** ([[event-tracing]], [[drill-down-analysis]]).
- **`rq_issue` vs `rq_insert` tradeoff:** async paths break naive “who issued” stories—pick the probe matching **your attribution question** ([[measurement-validity]] **scope/semantics**).
- **Offline latency:** pair **issue + complete** when BPF latency tools are not available—mind **capture overhead** ([[instrumentation-overhead-and-perturbation]] **perturbation**).

## Concepts reused / refined / created

- Reused: [[event-tracing]], [[drill-down-analysis]], [[measurement-validity]], [[instrumentation-overhead-and-perturbation]], [[systems-performance]]
- **Created:** none

## Links

- Concepts: [[event-tracing]], [[drill-down-analysis]], [[measurement-validity]], [[instrumentation-overhead-and-perturbation]], [[systems-performance]]
