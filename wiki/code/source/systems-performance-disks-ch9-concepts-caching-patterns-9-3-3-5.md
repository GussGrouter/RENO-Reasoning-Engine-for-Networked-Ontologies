# Systems Performance — Ch.9 §9.3.3–§9.3.5 (scout PDF 460–520)

## Source

- Title: *Systems Performance: Enterprise and the Cloud* (Second Edition)
- Raw: `raw/code/pdf/Systems.Performance.Enterprise.and.the.Cloud.pdf`
- Scout: `processed/code/systems-performance-ch9-scout-p460-520.txt`
- Scope: **Caching** + **random vs sequential** + **read/write ratio**; Table 9.2 summarized

## Processed artifacts

- `processed/code/systems-performance-disks-ch9-concepts-caching-patterns-9-3-3-5.md`
- Chunks: `systems-performance-disks-ch9-concepts-caching-patterns-9-3-3-5-chunk-000001.md`

## Extracted ideas

- **Tiered caches** below the FS make **disk** the last resort; **random** historically **amplification-prone** on HDD; **flash** shifts **pattern** importance to **RMW**, **erase**, **FTL**.
- **OS offset** may not equal **physical** placement—infer **randomness** from **service time** when **mapping opaque**.

## Application validation

**High read ratio:** invest in **cache / more RAM / read path**; **high write ratio:** invest in **backend bandwidth and write durability path**—not interchangeable.

## Decision clarity

**Decision:** choose **read-path cache expansion** over **adding spindles/flash bandwidth** when **dominant cost** is **read misses** at **metrics** not **write commit**.

## Concepts reused / refined / created

- Reused: [[caching]], [[cache-tuning]], [[throughput-latency-metrics]], [[resource-analysis-vs-workload-analysis]], [[cross-component-interactions]], [[systems-performance]]
- **Created:** none

## Links

- Concepts: [[caching]], [[cache-tuning]], [[throughput-latency-metrics]], [[resource-analysis-vs-workload-analysis]], [[cross-component-interactions]], [[systems-performance]]
