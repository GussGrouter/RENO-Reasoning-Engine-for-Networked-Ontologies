# Systems Performance — Ch.10 §10.6 Table 10.4 (BPF tracing tools)

Source: `systems-performance-ch10-scout-p520-640.txt`, lines **3839–3900** (PDF 520–640 extract; scout rebuilt 2026-04-20).

## Summary

- Tracing tools are positioned for **connection lifecycle**, **per-host/per-process TCP throughput**, **retransmit attribution**, and **stack-level events** (drops/latency), typically via BPF frontends.
- This layer is for when counters suggest **queueing or protocol dynamics** but you need **who/what/when** with more context than averages.
