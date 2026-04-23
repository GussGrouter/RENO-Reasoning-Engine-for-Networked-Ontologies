# Systems Performance — Ch.9 §9.5.7–§9.5.9 Cache tuning, resource controls, micro-benchmarking

Source: `systems-performance-ch9-scout-p460-520.txt`, lines **1891–1985** (PDF ~456–457).

## Summary

### §9.5.7 Cache tuning

- Same **exist → working → sized → tune workload/cache** loop as **Ch.2 §2.5.18**, spanning **app → FS → controller → disk** tiers (**[[cache-tuning]]**, [[caching]]).

### §9.5.8 Resource controls

- **IOPS/BW caps** or **share-based** schedulers—implementation-specific (**§9.9 Tuning** forward ref); limits can **create** “disk-bound” symptoms (**scope**: policy vs hardware).

### §9.5.9 Micro-benchmarking

- Prefer **raw/block path** when isolating **disk** from **FS** (avoid FS **cache/coalesce/split**).
- **Axes:** R/W, **random vs seq**, **offset range**, **I/O size**, **concurrency**, **device count** (probe **controller/bus**).
- **Disk tests** (author recipes): **seq throughput** (large reads), **max IOPS** (tiny reads), **random IOPS**, **latency vs size sweeps**, **offset-0 “cached” read** to probe **on-device DRAM**.
- **Controller tests:** fan out across **many disks** until **controller saturates**.
- Footnote: **sector 0** “cache latency” tests may be **firmware-special-cased**—**verify vs other offsets** (**measurement-validity** **representation**).

## Measurement-validity

- **Representation:** **offset-0 microbench hero numbers** may not generalize.
