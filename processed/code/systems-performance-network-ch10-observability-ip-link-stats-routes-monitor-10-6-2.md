# Systems Performance — Ch.10 §10.6.2 ip (link/address/route observability)

Source: `systems-performance-ch10-scout-p520-640.txt`, lines **2603–2659** (PDF 520–640 extract; scout rebuilt 2026-04-20).

## Summary

- `ip -s link` adds **RX/TX counters** plus **errors, drops, overruns, collisions/carrier**—classic inputs for interface-level **errors + drops/saturation** screening (USE-style screening).
- Counters are typically **since interface came up** (cumulative): interpret **rates** via deltas over time or tooling that prints intervals—not the instantaneous “Mbps” reading.
- **Route observability**: `ip route` helps catch **misroutes** that look like poor performance (suboptimal paths vs stale static entries).
- **Live changes**: `ip monitor` watches **netlink events**—useful when problems correlate with churn (routes/interfaces flapping).
