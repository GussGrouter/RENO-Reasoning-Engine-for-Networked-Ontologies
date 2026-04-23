# Systems Performance — Ch.10 §10.5.10 Micro-benchmarking (network)

Source: `systems-performance-ch10-scout-p520-640.txt`, lines **2434–2501** (PDF 520–640 extract; scout rebuilt 2026-04-20).

## Summary

- Network micro-benchmarks are most valuable as a **simpler isolation step** when a distributed app looks throughput-limited: confirm the network can hit expected rates before debugging application complexity.
- Factorize the experiment: direction, protocol/port, thread count, buffer sizes, MTU—especially because very fast links may need **multiple client threads** to actually saturate the path.
- Treat “cannot reach line rate in a microbench” as a **queueing/capacity/configuration** problem first (alignment with Chapter 10 methodology), not an automatic app defect.
