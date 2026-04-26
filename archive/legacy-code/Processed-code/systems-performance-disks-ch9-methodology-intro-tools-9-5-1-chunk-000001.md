# Systems Performance — Ch.9 §9.5 Methodology — intro + Table 9.4 + §9.5.1 Tools Method

Source: `systems-performance-ch9-scout-p460-520.txt`, lines **1410–1530** (PDF ~449–451).

## Summary

- **Table 9.4** maps **§9.5.1–§9.5.10** to **observational vs experimentation vs capacity** flavors—see book for grid; methodologies mirror **Chapter 2**.
- **Suggested investigation order** (author): **USE → monitoring → workload characterization → latency analysis → micro-benchmarking → static analysis → event tracing**—then **§9.6** supplies Linux tools.
- **§9.5.1 Tools method:** iterate **available tools** and their headline metrics—**fast to start**, **risk of blind spots** where tools lack visibility (**[[streetlight-anti-method]]** adjacent).
- **Linux-oriented checklist** (names only in book): **`iostat`**, **`iotop/biotop`**, **`biolatency`**, **`biosnoop`**, **`perf`/BCC/bpftrace**, **vendor RAID tools**—threshold examples (**>60% busy**, **~10 ms service**, **100 ms+ tails**) are **heuristics**, not universal SLOs.

## Measurement-validity

- **Representation:** tool-default **summaries** may miss **multimodal** or **per-process** story until paired with distribution/trace tools.
