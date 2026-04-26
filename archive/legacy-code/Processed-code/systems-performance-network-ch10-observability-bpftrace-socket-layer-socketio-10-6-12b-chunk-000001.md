# Systems Performance — Ch.10 §10.6.12 bpftrace (part B — socket syscall tracing + socketio)

Source: `systems-performance-ch10-scout-p520-640.txt`, lines **3325–3735** (PDF 520–640 extract; scout rebuilt 2026-04-20).

## Summary

- Socket-layer tracing favors **correct process attribution** because work is commonly in process context (`accept/connect` syscall paths, etc.).
- Shows **ustack slicing** on syscalls for “why is this connection happening?” investigations.
- Lists `sock:*` tracepoints (receive queue full, buffer limit exceeded, inet socket state changes)—direct queue/backpressure vocabulary.
- Longer programs move to `.bt` files; example `socketio.bt` aggregates socket read/write counts by process/protocol/port using `struct socket` fields (includes endianness caveat for ports).
