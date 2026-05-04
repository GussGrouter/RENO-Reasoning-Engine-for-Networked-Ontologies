# Systems Performance — Ch.9 §9.4.3 Arrays + NAS (scout PDF 460–520)

## Source

- Title: *Systems Performance: Enterprise and the Cloud* (Second Edition)
- Scout: `processed/code/systems-performance-ch9-scout-p460-520.txt`
- Scope: **storage arrays**, **NAS/iSCSI** boundary

## Processed artifacts

- `processed/code/systems-performance-disks-ch9-architecture-arrays-nas-9-4-3c.md`

## Extracted ideas

- **Arrays:** **large caches** + **policy flips** on **battery failure** → **step-change** latency ([[cross-component-interactions]]).
- **NAS:** treat as **distributed system**—**network RTT/congestion** is part of **disk story** ([[measurement-validity]] **scope**).

## Decision clarity

**Decision:** choose **block/path analytics on array + network** over **only host `iostat`** when **latency** tracks **WAN/NFS** symptoms.

## Concepts reused / refined / created

- Reused: [[cross-component-interactions]], [[measurement-validity]], [[throughput-latency-metrics]], [[systems-performance]]
- **Created:** none

## Links

- Concepts: [[cross-component-interactions]], [[measurement-validity]], [[throughput-latency-metrics]], [[systems-performance]]
