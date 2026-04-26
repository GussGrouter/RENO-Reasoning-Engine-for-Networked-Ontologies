# Systems Performance — Ch.9 §9.4.1.2 SSD / flash (scout PDF 460–520)

## Source

- Title: *Systems Performance: Enterprise and the Cloud* (Second Edition)
- Scout: `processed/code/systems-performance-ch9-scout-p460-520.txt`
- Scope: **SSD**, **FTL**, **write amplification**, **TRIM**, **endurance / pathologies**

## Processed artifacts

- `processed/code/systems-performance-disks-ch9-architecture-ssd-flash-9-4-1c.md`

## Extracted ideas

- **FTL** maps **block SCSI** to **flash erase geometry**—performance is **firmware + free space + write shape** ([[caching]], [[throughput-latency-metrics]]).
- **Cell taxonomy** is procurement **trade space**, not a new abstract concept here.

## Application validation

Before accepting **flash for write-heavy DB:** model **WA** + **DWPD** using **vendor tools + fio**, not **random-read IOPS** alone.

## Decision clarity

**Decision:** choose **discard/TRIM-capable stack + spare provisioning review** over **naïve full-disk fill** when **sustained random write** defines risk.

## Concepts reused / refined / created

- Reused: [[throughput-latency-metrics]], [[caching]], [[micro-benchmarking]], [[measurement-validity]], [[systems-performance]]
- **Created:** none

## Links

- Concepts: [[throughput-latency-metrics]], [[caching]], [[micro-benchmarking]], [[measurement-validity]], [[systems-performance]]
