# Systems Performance — Ch.9 §9.4.1.3 PMEM + §9.4.2 Interfaces (scout PDF 460–520)

## Source

- Title: *Systems Performance: Enterprise and the Cloud* (Second Edition)
- Scout: `processed/code/systems-performance-ch9-scout-p460-520.txt`
- Scope: **persistent memory** pointer + **SCSI/SAS/SATA/FC/NVMe** decision summary

## Processed artifacts

- `processed/code/systems-performance-disks-ch9-architecture-interfaces-pmem-9-4-2.md`

## Extracted ideas

- **Interface choice** = **bandwidth ceiling**, **contention model**, **queue depth**, **CPU locality** (**NVMe mq**)—not “**which acronym is trendy**.”

## Decision clarity

**Decision:** choose **NVMe + adequate PCIe lanes** over **legacy SAS/SATA attachment** when **µs-scale flash latency** is the bottleneck and **CPU-side queue locks** show up in profiles.

## Concepts reused / refined / created

- Reused: [[throughput-latency-metrics]], [[measurement-validity]], [[cross-component-interactions]], [[systems-performance]]
- **Created:** none

## Links

- Concepts: [[throughput-latency-metrics]], [[measurement-validity]], [[cross-component-interactions]], [[systems-performance]]
