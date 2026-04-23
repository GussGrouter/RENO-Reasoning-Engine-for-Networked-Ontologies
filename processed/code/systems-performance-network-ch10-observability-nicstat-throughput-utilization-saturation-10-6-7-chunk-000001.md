# Systems Performance — Ch.10 §10.6.7 nicstat (interface throughput + utilization)

Source: `systems-performance-ch10-scout-p520-640.txt`, lines **3076–3121** (PDF 520–640 extract; scout rebuilt 2026-04-20).

## Summary

- `nicstat` follows iostat/mpstat style: per-interval **KB/s**, packet rates, avg packet sizes, **`%Util`**, and **`Sat`** (saturation-oriented field per tool’s reporting).
- Example output distinguishes **idle vs active interfaces** (`-z` trims zero lines).
- Interpretation note: `%Util` reports **max direction utilization** among RX/TX at a sampling instant (paired example shows high read throughput with utilization ~35%).
- Explicit tie-in: especially helpful for USE—provides utilization and saturation-ish signals on NICs without building ad-hoc parsers.
