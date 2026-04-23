# Systems Performance — Ch.10 §10.4.3 Software (device drivers: ring buffer + NAPI/coalescing)

Source: `systems-performance-ch10-scout-p520-640.txt`, lines **1737–1931** (PDF 520–640 extract; scout rebuilt 2026-04-20).

## Summary

- Drivers add a **ring buffer** queue between kernel memory and NIC.
- **Interrupt coalescing** increases throughput by batching (fewer interrupts) but can increase latency.
- Linux **NAPI** switches behavior by rate: interrupts at low rate; polling at high rate (coalescing).
- Extra NAPI features: throttling drops during storms; fairness quotas; optional busy polling for lower latency (CPU trade).

