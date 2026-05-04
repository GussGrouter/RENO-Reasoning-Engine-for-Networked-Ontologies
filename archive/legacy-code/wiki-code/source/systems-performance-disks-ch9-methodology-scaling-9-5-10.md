# Systems Performance — Ch.9 §9.5.10 Scaling (scout PDF 460–520)

## Source

- Title: *Systems Performance: Enterprise and the Cloud* (Second Edition)
- Scout: `processed/code/systems-performance-ch9-scout-p460-520.txt`
- Scope: **§9.5.10** capacity sketch

## Processed artifacts

- `processed/code/systems-performance-disks-ch9-methodology-scaling-9-5-10.md`

## Extracted ideas

- **Scale-out** uses **derated device util**, **RAID overhead**, **controller/transport ceilings**, **CPU/IOP**—not **peak benchmark** ([[factor-analysis-capacity-planning]], [[utilization-and-saturation]], [[micro-benchmarking]]).

## Decision clarity

**Decision:** choose **scale media + controllers using 40–60% target util** over **dividing peak IOPS by required IOPS** when **queueing latency** is part of the **SLO**.

## Concepts reused / refined / created

- Reused: [[factor-analysis-capacity-planning]], [[utilization-and-saturation]], [[micro-benchmarking]], [[throughput-latency-metrics]], [[queueing-theory]], [[systems-performance]]
- **Created:** none

## Links

- Concepts: [[factor-analysis-capacity-planning]], [[utilization-and-saturation]], [[micro-benchmarking]], [[throughput-latency-metrics]], [[queueing-theory]], [[systems-performance]]
