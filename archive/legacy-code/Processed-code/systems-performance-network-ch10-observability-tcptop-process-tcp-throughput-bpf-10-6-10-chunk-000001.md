# Systems Performance — Ch.10 §10.6.10 tcptop (per-process TCP throughput)

Source: `systems-performance-ch10-scout-p520-640.txt`, lines **3240–3274** (PDF 520–640 extract; scout rebuilt 2026-04-20).

## Summary

- Ranks processes by **TCP RX/TX KB per interval** (default ~1s refresh)—fast way to attribute **who is moving bulk bytes** on a host.
- Implemented by tracing **TCP send/receive paths** into BPF maps; **high throughput ⇒ high event rates**, so overhead may become measurable on saturated systems.
- Options narrow scope (`-p PID`, interval/count, `-C` screen behavior).
