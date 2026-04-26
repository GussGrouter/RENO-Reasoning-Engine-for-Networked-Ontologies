# Systems Performance — Ch.10 §10.4.2 Hardware (switches/routers, buffering, rate transitions)

Source: `systems-performance-ch10-scout-p520-640.txt`, lines **1614–1736** (PDF 520–640 extract; scout rebuilt 2026-04-20).

## Summary

- Switches reduce host-to-host contention vs hubs; collision counters today usually indicate errors (negotiation/wiring).
- Router paths can change dynamically; uncertain path + out-of-order delivery can hurt TCP performance.
- Switches/routers have **buffers + CPUs** and can bottleneck under load.
- **Rate transitions** (fast link into slower link) require buffering; over-buffering can cause **bufferbloat**. Source pacing can reduce burstiness.

