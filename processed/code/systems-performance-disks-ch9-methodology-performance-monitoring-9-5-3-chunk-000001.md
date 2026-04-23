# Systems Performance — Ch.9 §9.5.3 Performance monitoring

Source: `systems-performance-ch9-scout-p460-520.txt`, lines **1606–1632** (PDF ~452).

## Summary

- **Key rolling metrics:** **disk utilization**, **response time** (often **interval averages** + max/stdev in tools).
- **Heuristics:** **100% sustained** suspicious; **>60%** may correlate with **queue pain** depending on workload/SLO—**micro-benchmark “known good vs bad”** helps calibrate (**[[micro-benchmarking]]**).
- **Per-disk** views expose **skew** and **bad disks**.
- **Prefer full latency distribution** (histogram/heatmap) over **avg-only** when hunting **tails** (**[[metric-visualization]]**, **[[multimodal-latency-distribution]]**).
- **Resource controls:** if **I/O caps** active, bottleneck may be **policy**, not raw device capability (**[[measurement-validity]]** **scope/semantics**).

## Measurement-validity

- **Representation:** **per-second average response time** **collapses** multimodal mixes.
