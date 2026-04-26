# Systems Performance — Ch.9 §9.8.3 Micro-benchmark tools (hdparm example)

Source: `systems-performance-ch9-scout-p482-560.txt`, lines **2295–2311** (printed ~492).

## Summary

- **`hdparm -Tt`:** **`-T`** hits **buffered/cache path**; **`-t`** exercises **device reads**—side-by-side shows **cache vs media** gap.
- Points to **Ch.12** benchmarking background and **Ch.8** FS-oriented disk tests for broader tool landscape.

## Measurement-validity

- **Representation:** **cached read** throughput is **not** “disk sustained”—label dashboards and conclusions accordingly.
