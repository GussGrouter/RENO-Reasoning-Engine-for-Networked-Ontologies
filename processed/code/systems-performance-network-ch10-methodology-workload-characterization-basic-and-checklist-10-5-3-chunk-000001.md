# Systems Performance — Ch.10 §10.5.3 Workload characterization (basic + checklist)

Source: `systems-performance-ch10-scout-p520-640.txt`, lines **2137–2148** (PDF 520–640 extract; scout rebuilt 2026-04-20).

## Summary

- Basic workload dimensions:
  - **Throughput** (bytes/s) per direction (RX/TX)
  - **IOPS/pps** (frames/s) per direction
  - **Connection rate** (active/passive connections/s)
- Express per-interface to find line-rate bottlenecks; account for imposed bandwidth limits.
- Checklist emphasizes packet size, protocol breakdown, active ports, multicast/broadcast rates, and which processes generate traffic.

