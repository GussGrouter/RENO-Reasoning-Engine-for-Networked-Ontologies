# Systems Performance — Ch.10 §10.3.11 Local connections (loopback vs UDS)

Source: `systems-performance-ch10-scout-p520-640.txt`, lines **1299–1613** (PDF 520–640 extract; scout rebuilt 2026-04-20).

## Summary

- Localhost connections use a virtual interface (**loopback**).
- **Unix domain sockets (UDS)** can outperform localhost TCP/IP by bypassing TCP/IP stack overheads.
- Some systems attempt to optimize localhost TCP/IP paths, but behavior is implementation-specific.

