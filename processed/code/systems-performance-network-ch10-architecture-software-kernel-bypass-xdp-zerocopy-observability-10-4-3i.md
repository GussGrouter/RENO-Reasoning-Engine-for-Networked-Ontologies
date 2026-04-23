# Systems Performance — Ch.10 §10.4.3 Software (kernel bypass/XDP/zero-copy + observability trade)

Source: `systems-performance-ch10-scout-p520-640.txt`, lines **1737–1931** (PDF 520–640 extract; scout rebuilt 2026-04-20).

## Summary

- Kernel bypass (e.g., user-space packet processing) can increase packet rates and avoid copies.
- XDP provides a programmable fast path integrated with the kernel stack.
- Bypass reduces availability of traditional counters/tracing (instrumentation is bypassed), making analysis harder.
- Zero-copy send/receive features can reduce copy overhead without full stack bypass.

