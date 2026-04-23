# Systems Performance — Ch.10 §10.7.5 netperf (request/response micro-benchmark)

Source: `systems-performance-ch10-scout-p520-640.txt`, lines **4409–4476** (PDF 520–640 extract; scout rebuilt 2026-04-20).

## Summary

- Positions `netperf` as a richer micro-benchmark than raw throughput tests; example focuses on **TCP request/response** (`TCP_RR`) to measure **round-trip latency** at transaction granularity.
- Requires `netserver` on the far host; client flags include verbosity and port selection.
- Example output highlights **usec/Tran** latency column and a transaction rate / throughput column family—interpret as **experimental RTT samples** for that workload shape, not your full app’s mixed traffic.
