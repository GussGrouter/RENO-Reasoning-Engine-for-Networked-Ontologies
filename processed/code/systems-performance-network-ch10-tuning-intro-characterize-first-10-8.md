# Systems Performance — Ch.10 §10.8 Tuning (intro)

Source: `systems-performance-ch10-scout-p520-640.txt`, lines **4518–4521** (PDF 520–640 extract; scout rebuilt 2026-04-20).

## Summary

- Defaults are usually already “high performance”; stack is often **adaptive** to workload.
- Recommends **workload characterization + static performance tuning** before knob twiddling—eliminating unnecessary work beats marginal sysctl wins.
- Warns tunables differ by OS/version/docs; following sections are **starting points**, not recipes.
