# Systems Performance — Ch.9 §9.5.10 Scaling (capacity planning sketch)

Source: `systems-performance-ch9-scout-p460-520.txt`, lines **1986–2027** (PDF ~457–458).

## Summary

- **Micro-benchmarks** reveal **device/controller ceilings**; **tuning** cannot exceed those without **architecture change**.
- **Five-step sketch:** (1) **target workload** IOPS/BW from **capacity planning** or **scaled user model**—note **cache-per-user** shrink if cache not scaled; (2) **count disks** using **derated util** (~**50%** example) **not** 100% peaks; **fold in RAID overhead**; (3) **count controllers**; (4) **check transports**; (5) **CPU cycles per I/O** for host overhead.
- **IOPS equality:** reuse **§9.3.7**—pick limits using **workload-relevant** **size/type** microbench results (**[[factor-analysis-capacity-planning]]**, **[[micro-benchmarking]]**).
- Modern slogan shift: **“more spindles” → “more flash”**—same **scale-out** logic, different media.

## Decision clarity

**Decision:** choose **horizontal disk/flash scaling with target utilization headroom** over **running devices at benchmark peak** when **latency SLOs** must survive **variance + queue growth**.
