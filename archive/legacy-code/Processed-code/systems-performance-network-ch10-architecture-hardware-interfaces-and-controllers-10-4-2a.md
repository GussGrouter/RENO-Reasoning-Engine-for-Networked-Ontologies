# Systems Performance — Ch.10 §10.4.2 Hardware (interfaces + controllers)

Source: `systems-performance-ch10-scout-p520-640.txt`, lines **1614–1736** (PDF 520–640 extract; scout rebuilt 2026-04-20).

## Summary

- Interface choice is a **cost vs bandwidth/latency** trade when designing systems; separate TX/RX channels matter in full duplex.
- Controller + I/O transport (e.g., PCIe) can cap throughput/IOPS even if port “line rate” suggests otherwise (port capacity ≠ system capacity).

