# Systems Performance — Ch.9 §9.4.3 Storage + RAID framing (scout PDF 460–520)

## Source

- Title: *Systems Performance: Enterprise and the Cloud* (Second Edition)
- Scout: `processed/code/systems-performance-ch9-scout-p460-520.txt`
- Scope: **disk/JBOD**, **hardware vs software RAID**, **stripe definition**

## Processed artifacts

- `processed/code/systems-performance-disks-ch9-architecture-storage-raid-intro-9-4-3a.md`

## Extracted ideas

- **Topology locks observability:** **JBOD** transparent; **hardware RAID** can **hide** disks ([[cross-component-interactions]], [[resource-vs-implementation-bottleneck]]).

## Decision clarity

**Decision:** choose **FS-level or OS-managed redundancy** over **opaque RAID card** when **incident response** requires **per-device telemetry** you cannot get from the controller.

## Concepts reused / refined / created

- Reused: [[cross-component-interactions]], [[resource-vs-implementation-bottleneck]], [[static-performance-tuning]], [[systems-performance]]
- **Created:** none

## Links

- Concepts: [[cross-component-interactions]], [[resource-vs-implementation-bottleneck]], [[static-performance-tuning]], [[systems-performance]]
