# Systems Performance — Ch.9 §9.4 HDD throughput + geometry caveat (scout PDF 460–520)

## Source

- Title: *Systems Performance: Enterprise and the Cloud* (Second Edition)
- Raw: `raw/code/pdf/Systems.Performance.Enterprise.and.the.Cloud.pdf`
- Scout: `processed/code/systems-performance-ch9-scout-p460-520.txt`
- Scope: **§9.4** intro + **§9.4.1.1** HDD basics + theoretical throughput

## Processed artifacts

- `processed/code/systems-performance-disks-ch9-architecture-hdd-throughput-9-4-1a.md`
- Chunks: `systems-performance-disks-ch9-architecture-hdd-throughput-9-4-1a-chunk-000001.md`

## Extracted ideas

- **Architecture vs load:** wrong **media/topology** mimics “mysterious slowness” under **innocent** load ([[factor-analysis-capacity-planning]], [[cross-component-interactions]]).
- **Throughput formula** needs **honest geometry**—modern drives **virtualize** ([[measurement-validity]] **scope/semantics**).

## Decision clarity

**Decision:** choose **SKU + firmware-level bandwidth evidence** over **paper formula using synthetic max sectors/track** when planning **streaming HDD throughput**.

## Concepts reused / refined / created

- Reused: [[throughput-latency-metrics]], [[measurement-validity]], [[factor-analysis-capacity-planning]], [[cross-component-interactions]], [[systems-performance]]
- **Created:** none

## Links

- Concepts: [[throughput-latency-metrics]], [[measurement-validity]], [[factor-analysis-capacity-planning]], [[cross-component-interactions]], [[systems-performance]]
