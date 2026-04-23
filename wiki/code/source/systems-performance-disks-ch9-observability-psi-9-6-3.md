# Systems Performance — Ch.9 §9.6.3 PSI (I/O)

## Source

- Title: *Systems Performance: Enterprise and the Cloud* (Second Edition)
- Scout: `processed/code/systems-performance-ch9-scout-p460-520.txt`
- Scope: **§9.6.3**

## Processed artifacts

- `processed/code/systems-performance-disks-ch9-observability-psi-9-6-3.md`
- Chunks: `*-chunk-000001.md`

## Extracted ideas

- **Pressure windows** expose **direction** (**short avg > long avg** ⇒ worsening stall regime)—good **pager-scale** signal before **`pidstat`/`iostat`** drill-down ([[utilization-and-saturation]], [[measurement-validity]] **scope/semantics**).

## Decision clarity

**Decision:** choose **PSI-style stall pressure** over **disk throughput graphs** when **symptoms are thread stalls** but **MB/s looks healthy**.

## Concepts reused / refined / created

- Reused: [[utilization-and-saturation]], [[measurement-validity]], [[systems-performance]]
- **Created:** none

## Links

- Concepts: [[utilization-and-saturation]], [[measurement-validity]], [[systems-performance]]
