# Systems Performance — Ch.10 §10.6.12 bpftrace (part C — TCP tracepoints, kprobes, tcpsynbl)

Source: `systems-performance-ch10-scout-p520-640.txt`, lines **3325–3735** (PDF 520–640 extract; scout rebuilt 2026-04-20).

## Summary

- TCP-level analysis can use **stable `t:tcp:*` tracepoints** (retransmit, resets, probe, etc.); broad `k:tcp_*` counting attaches hundreds of probes and may add noticeable overhead—alternatives suggested for “count all TCP calls” style profiling (Ftrace/funccount elsewhere).
- Example `tcpsynbl.bt` histograms **listen backlog depth** and prints timestamps when SYNs drop due to backlog overflow—early warning for **SYN loss** driven by backlog saturation.
- Histogram bucket semantics: default `hist()` log-scaling skews perception; linear `lhist()` alternative discussed.
