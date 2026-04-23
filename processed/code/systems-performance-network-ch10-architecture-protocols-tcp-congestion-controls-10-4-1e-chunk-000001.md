# Systems Performance — Ch.10 §10.4.1 Protocols (TCP congestion control algorithms)

Source: `systems-performance-ch10-scout-p520-640.txt`, lines **2149–2186** (PDF 520–640 extract; scout rebuilt 2026-04-20).

## Summary

- Congestion control algorithm choice can materially change throughput/latency under loss and varying paths.
- Different algorithms embody different models (window-based vs explicit path-model like BBR; datacenter-specific ECN assumptions like DCTCP).
- Some systems allow algorithm selection as part of tuning.

