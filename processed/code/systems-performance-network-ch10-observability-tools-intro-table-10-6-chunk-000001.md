# Systems Performance — Ch.10 §10.6 Observability tools (intro + Table 10.4 ladder)

Source: `systems-performance-ch10-scout-p520-640.txt`, lines **3839–3900** (PDF 520–640 extract; scout rebuilt 2026-04-20).

## Summary

- Positions observability as supporting **§10.5 methodology** (not a fishing expedition): progress from **cheap counters** → **tracing** → **packet capture** as cost/risk rises.
- **Table 10.4** is explicitly staged: traditional stats first, then BPF-style tracing tools, then sniffers.
- Notes engineering reality: some classic Unix tools are widely deployed but considered **deprecated** on Linux vs **iproute2**-family tools maintained alongside kernel features.
