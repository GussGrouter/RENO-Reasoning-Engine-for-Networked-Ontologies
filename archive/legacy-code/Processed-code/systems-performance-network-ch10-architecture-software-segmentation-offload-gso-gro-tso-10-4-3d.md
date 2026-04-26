# Systems Performance — Ch.10 §10.4.3 Software (segmentation offload: GSO/GRO/TSO)

Source: `systems-performance-ch10-scout-p520-640.txt`, lines **1737–1931** (PDF 520–640 extract; scout rebuilt 2026-04-20).

## Summary

- Large “super packets” reduce stack overheads; Linux can split near the device boundary (GSO) or offload splitting to NIC hardware (TSO).
- Receive offload (GRO) complements segmentation offload.
- These features increase throughput by reducing per-packet processing overhead, without changing the on-wire MSS.

