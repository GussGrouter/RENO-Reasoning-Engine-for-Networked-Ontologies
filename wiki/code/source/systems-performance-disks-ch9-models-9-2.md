# Systems Performance — Ch.9 §9.2 Models (scout PDF 460–520)

## Source

- Title: *Systems Performance: Enterprise and the Cloud* (Second Edition)
- Raw: `raw/code/pdf/Systems.Performance.Enterprise.and.the.Cloud.pdf`
- Scout: `processed/code/systems-performance-ch9-scout-p460-520.txt`
- Scope: **§9.2** — queued disk, caching disk, controller/HBA

## Processed artifacts

- `processed/code/systems-performance-disks-ch9-models-9-2.md`
- Chunks: `systems-performance-disks-ch9-models-9-2-chunk-000001.md`

## Extracted ideas

- **Queue + server** abstraction matches [[queueing-theory]] intuition; controllers may reorder (**elevator**, **split RW queues**).
- **On-disk cache** splits **hit vs miss** latency; **write-back vs write-through** affects **completion semantics** vs **durability**.
- **HBA** introduces **multiple choke points** (host bus vs storage fabric vs drives).

## Application validation

Before blaming “slow disks,” check whether **completion** reflects **DRAM on device** (**write-back**) versus **persistent** latency.

## Decision clarity

**Decision:** choose **latency instrumentation at issue vs completion** over **average “service time” ratios** when the device can **parallelize or deeply queue**.

## Concepts reused / refined / created

- Reused: [[queueing-theory]], [[caching]], [[throughput-latency-metrics]], [[cross-component-interactions]], [[systems-performance]]
- **Created:** none

## Links

- Concepts: [[queueing-theory]], [[caching]], [[throughput-latency-metrics]], [[cross-component-interactions]], [[systems-performance]]
