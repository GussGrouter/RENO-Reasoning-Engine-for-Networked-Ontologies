# Systems Performance — Ch.9 §9.5.5 Latency analysis (stack drill-down)

Source: `systems-performance-ch9-scout-p460-520.txt`, lines **1782–1819** (PDF ~454–455).

## Summary

- **Goal:** locate **origin** of latency—often stop at **disk interface** (issue→completion) when it **matches** app-visible latency.
- **Mismatch across layers:** measure **each stack hop**; **FS locking/queueing** may dominate while **lower layers look calm** (**Figure 9.10** in book).
- **Inflation/deflation:** **count/size/latency** differ per layer—**one slow op** at block layer may pair with **many hidden ops** for one logical FS op (**metadata** story).
- **Presentation:** interval **averages** vs **histograms/heatmaps** vs **per-I/O trace** for **outliers** and **split/coalesce** detection (**[[latency-analysis]]**, **§9.7.3** pointer).

## Decision clarity

**Decision:** choose **layered latency comparison** over **disk-only investigations** when **application/block latencies diverge** materially.
