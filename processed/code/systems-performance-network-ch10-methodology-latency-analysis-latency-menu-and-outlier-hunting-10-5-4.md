# Systems Performance — Ch.10 §10.5.4 Latency analysis (latency menu + outlier hunting)

Source: `systems-performance-ch10-scout-p520-640.txt`, lines **2187–2259** (PDF 520–640 extract; scout rebuilt 2026-04-20).

## Summary

- Use a **menu of latency measures** to localize where time comes from: DNS, ping, TCP connect, TTFB, retransmits, TIME_WAIT, lifespan, syscall send/recv/connect, RTT, interrupt latency, inter-stack latency.
- Present latency as averages (per pair), full distributions (hist/heatmap), or per-operation traces with endpoints.
- Retransmits are a common outlier cause; identify via distributions or per-op tracing with minimum-latency filters.
- Some extra latency appears only under load; measure latency under realistic load, not only idle.

