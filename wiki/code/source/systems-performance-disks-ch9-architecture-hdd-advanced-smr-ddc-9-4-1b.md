# Systems Performance — Ch.9 §9.4 HDD advanced topics, SMR, DDC (scout PDF 460–520)

## Source

- Title: *Systems Performance: Enterprise and the Cloud* (Second Edition)
- Scout: `processed/code/systems-performance-ch9-scout-p460-520.txt`
- Scope: **short-stroking**, **zoning**, **Advanced Format**, **elevator**, **ECC tails**, **vibration**, **sloth disks**, **SMR**, **DDC**

## Processed artifacts

- `processed/code/systems-performance-disks-ch9-architecture-hdd-advanced-smr-ddc-9-4-1b.md`
- Chunks: `*-chunk-000001.md`

## Extracted ideas

- **Hidden tails:** **retries**, **environmental vibration**, **sloth latency** invalidate “**disk healthy**” from **average util** alone ([[latency-outliers]], [[measurement-validity]]).
- **Elevator starvation** is a **queueing fairness** story ([[queueing-theory]]).
- **SMR / DDC:** **offset semantics** diverge from **physical behavior** ([[cross-component-interactions]]).

## Decision clarity

**Decision:** choose **SMR-aware or non-SMR disks** over **assuming HDD random-write parity** when **RAID5/6 heavy write** defines the workload.

## Concepts reused / refined / created

- Reused: [[queueing-theory]], [[latency-outliers]], [[measurement-validity]], [[cross-component-interactions]], [[caching]], [[systems-performance]]
- **Created:** none

## Links

- Concepts: [[queueing-theory]], [[latency-outliers]], [[measurement-validity]], [[cross-component-interactions]], [[caching]], [[systems-performance]]
