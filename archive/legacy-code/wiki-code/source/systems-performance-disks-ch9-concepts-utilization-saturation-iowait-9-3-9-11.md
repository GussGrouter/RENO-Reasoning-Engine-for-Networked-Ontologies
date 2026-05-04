# Systems Performance — Ch.9 §9.3.9–§9.3.11 Utilization / saturation / iowait (scout PDF 460–520)

## Source

- Title: *Systems Performance: Enterprise and the Cloud* (Second Edition)
- Raw: `raw/code/pdf/Systems.Performance.Enterprise.and.the.Cloud.pdf`
- Scout: `processed/code/systems-performance-ch9-scout-p460-520.txt`
- Scope: **utilization caveats**, **virtual disk**, **saturation**, **CPU iowait**

## Processed artifacts

- `processed/code/systems-performance-disks-ch9-concepts-utilization-saturation-iowait-9-3-9-11.md`
- Chunks: `systems-performance-disks-ch9-concepts-utilization-saturation-iowait-9-3-9-11-chunk-000001.md`

## Extracted ideas

- **Disk utilization** is **interval busy time**—can mislead under **async I/O**, **burst writes**, **virtualization** of queues (**measurement-validity** **scope/semantics**).
- **Saturation** requires **queue depth signal**, not util alone (**[[utilization-and-saturation]]**).
- **%iowait** mixes **CPU scheduling** with **disk blocking**—falls when **other CPU load** appears.

## Application validation

“**iowait jumped after upgrade**” investigation: separate **CPU efficiency change** from **disk regression** using **blocked-time** probes.

## Decision clarity

**Decision:** choose **per-thread blocked-on-I/O accounting** over **raw iowait %** when **CPU utilization is volatile** across the fleet.

## Concepts reused / refined / created

- Reused: [[utilization-and-saturation]], [[measurement-validity]], [[throughput-latency-metrics]], [[latency-analysis]], [[cross-component-interactions]], [[systems-performance]]
- **Created:** none

## Links

- Concepts: [[utilization-and-saturation]], [[measurement-validity]], [[throughput-latency-metrics]], [[latency-analysis]], [[cross-component-interactions]], [[systems-performance]]
