# Systems Performance — Chapter 9 Disks — Intro + §9.1 terminology (scout PDF 460–520)

## Source

- Title: *Systems Performance: Enterprise and the Cloud* (Second Edition)
- Author: Brendan Gregg
- Raw: `raw/code/pdf/Systems.Performance.Enterprise.and.the.Cloud.pdf`
- Scout: `processed/code/systems-performance-ch9-scout-p460-520.txt`
- Scope: **Chapter opening** + **six-part map** + **§9.1 terminology**

## Processed artifacts

- Converted slice: `processed/code/systems-performance-disks-ch9-intro-parts-terminology-9-1.md`
- Chunks: `processed/code/systems-performance-disks-ch9-intro-parts-terminology-9-1-chunk-000001.md`

## Extracted ideas

- Disks remain a **latency and throughput bottleneck** despite SSDs; chapter balances **models, architecture, methodology**, then **Linux observability/experimentation/tuning**.
- Terminology distinguishes **throughput vs bandwidth**, **I/O vs arbitrary disk commands**, and warns **network “latency”** wording vs **storage end-to-end time**.

## Application validation

Planning **SLO review:** anchor **latency** definitions to **layer** (application vs block vs device) before comparing to **Table 9.1** style scales in later sections.

## Decision clarity

**Decision:** choose **filesystem-level diagnosis first** over **disk tuning** when **symptoms** match **syscall/VFS/cache** narratives from Chapter 8.

## Concepts reused / refined / created

- Reused: [[throughput-latency-metrics]], [[resource-analysis-vs-workload-analysis]], [[latency-outliers]], [[systems-performance]]
- **Created:** none

## Links

- Concepts: [[throughput-latency-metrics]], [[resource-analysis-vs-workload-analysis]], [[latency-outliers]], [[systems-performance]]
