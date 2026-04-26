# Systems Performance — Ch.10 §10.1 Terminology (network)

Source: `systems-performance-ch10-scout-p520-640.txt`, lines **892–919** (PDF 520–640 extract; scout rebuilt 2026-04-20).

## Summary

- **Interface** has a **physical port** vs OS **logical interface** distinction (virtual interfaces exist).
- Distinguish message units: **frame** (L2) vs **packet** (L3) vs API endpoint **socket**.
- Distinguish rate terms: **bandwidth** (max possible) vs **throughput** (current achieved) vs **latency** (time cost, with multiple meanings like RTT vs connect).

## Application validation

If a link is “100 GbE” but transfers are slow, treat **bandwidth** as a ceiling and use **throughput + latency** to decide whether you have a **capacity** problem or a **delay** problem.

