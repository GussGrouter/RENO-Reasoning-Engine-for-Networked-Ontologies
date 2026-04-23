# Systems Performance — Volumes vs pools (§8.4.6) (scout PDF 398–460)

## Source

- Title: *Systems Performance: Enterprise and the Cloud* (Second Edition)
- Author: Brendan Gregg
- Raw: `raw/code/pdf/Systems.Performance.Enterprise.and.the.Cloud.pdf`
- Batch scope: **§8.4.6** — virtualization of backing devices (**LVM / hardware RAID** named as examples; **striping/parity/rebuild bullets kept** as decision hazards)

## Processed artifacts

- Scout: `processed/code/systems-performance-ch8-scout-p398-460.txt`
- Converted slice: `processed/code/systems-performance-filesystems-ch8-volumes-pools-8-4-6.md`
- Chunks: `processed/code/systems-performance-filesystems-ch8-volumes-pools-8-4-6-chunk-000001.md`

## Extracted ideas (with classification)

- (composition) **Volumes** (virtual disks) vs **pools**: a **flexibility / isolation** trade—pools multiplex all spindles for every FS; volumes can **silo** workloads on device groups.
- (measurement validity) **Virtual device % busy** can mislead—must reconcile to **physical devices** and parity/rebuild paths.
- (capacity scaling risk) **Rebuild windows** lengthen as device capacity outpaces sequential throughput—failure/rebuild becomes a **dominant tail risk** for production.

## Application validation

- **“The LVM volume is 100% busy”** triangulate with **underlying PVs**, **RAID parity cost**, and **resilver progress**—otherwise you optimize the wrong layer.

## Decision clarity

- **Decision:** choose **multiple smaller pools / volume groups** over **one massive pool** when **latency-sensitive tenants must not inherit neighbor rebuild / scrub amplification** (accepting reduced flexibility).

## Concepts reused / refined / created

- Reused: [[cross-component-interactions]], [[measurement-validity]], [[resource-analysis-vs-workload-analysis]], [[throughput-latency-metrics]], [[systems-performance]]
- **Created:** none

## Links

- Concepts: [[cross-component-interactions]], [[measurement-validity]], [[resource-analysis-vs-workload-analysis]], [[use-method]], [[systems-performance]]
- Related sources: [[systems-performance-filesystems-ch8-fs-types-zfs-8-4-5d]], [[systems-performance-filesystems-ch8-methodology-intro-8-5]]
