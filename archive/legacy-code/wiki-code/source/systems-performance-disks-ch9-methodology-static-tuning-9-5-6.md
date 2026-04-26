# Systems Performance — Ch.9 §9.5.6 Static performance tuning (scout PDF 460–520)

## Source

- Title: *Systems Performance: Enterprise and the Cloud* (Second Edition)
- Scout: `processed/code/systems-performance-ch9-scout-p460-520.txt`
- Scope: **§9.5.6** checklist + ZFS RAID-Z story

## Processed artifacts

- `processed/code/systems-performance-disks-ch9-methodology-static-tuning-9-5-6.md`

## Extracted ideas

- **Misconfiguration** can cap performance **below** media limits—**inventory topology first** ([[static-performance-tuning]], [[resource-vs-implementation-bottleneck]]).

## Decision clarity

**Decision:** choose **topology/firmware/driver audit** over **kernel scheduler tuning** when **observed throughput matches “single spindle class”** on **multi-drive pools**.

## Concepts reused / refined / created

- Reused: [[static-performance-tuning]], [[resource-vs-implementation-bottleneck]], [[systems-performance]]
- **Created:** none

## Links

- Concepts: [[static-performance-tuning]], [[resource-vs-implementation-bottleneck]], [[systems-performance]]
