# Systems Performance — Ch.9 §9.6 Observability Tools (intro + Table 9.5)

Source: `systems-performance-ch9-scout-p460-520.txt`, lines **2028–2132** (PDF ~459).

## Summary

- **Ordering:** classic **statistics** tools first, then **tracing** (many **BPF**/BCC/bpftrace—see Ch.15), then **controller/disk introspection** utilities (**Table 9.5**).
- **Companion to §9.5:** tools implement the methodology—not a substitute for **USE**, **workload characterization**, or **latency analysis**.
- **Cross-Unix:** `iostat`, `sar` originate broadly; BPF-backed tools are **Linux-shaped**.

## Table 9.5 (indexed)

| § | Tool | Role |
|---|------|------|
| 9.6.1 | iostat | Per-disk stats |
| 9.6.2 | sar | Historical disk stats |
| 9.6.3 | PSI | Disk pressure / stall |
| 9.6.4 | pidstat | Per-process disk I/O |
| 9.6.5 | perf | Block tracepoints + stacks |
| 9.6.6 | biolatency | Latency histogram |
| 9.6.7 | biosnoop | Per-I/O trace + latency |
| 9.6.8 | iotop, biotop | Top processes by disk I/O |
| 9.6.9 | biostacks | Init stacks + latency |
| 9.6.10 | blktrace | Verbose block trace |
| 9.6.11 | bpftrace | Custom disk tracing |
| 9.6.12 | MegaCli | LSI controller stats |
| 9.6.13 | smartctl | SMART / device health |

*(Table continues in scout; remainder of chapter covers 9.6.1ff in detail.)*
