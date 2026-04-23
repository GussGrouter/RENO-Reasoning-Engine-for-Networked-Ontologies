# Systems Performance — Ch.10 §10.7.4 iperf (TCP/UDP throughput micro-benchmark)

Source: `systems-performance-ch10-scout-p520-640.txt`, lines **4259–4273** (PDF 520–640 extract; scout rebuilt 2026-04-20).

## Summary

- `iperf` needs **client + server**; parallel client threads (`-P`) can be required to **drive very fast links** to their limit.
- Example shows **larger socket buffers** (`-l`) on server vs client defaults—buffer asymmetry affects what you are *actually* measuring.
- Output includes **per-interval rows** (`-i`) with **Transfer** and **Bandwidth** per interval (rates over each interval) plus a **final average** summed across parallel flows (`[SUM]`).
- `--reportstyle C` enables **CSV export** for plotting variance over time.
