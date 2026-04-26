# Systems Performance — Ch.9 §9.6.1 iostat

Source: `systems-performance-ch9-scout-p460-520.txt`, lines **2133–2616** (PDF ~459–463).

## Summary

- **Role:** default CLI **per-disk** counters—workload (**tps**, **kB/s**), **USE-oriented** columns in **`-x`** mode (**await**, **aqu-sz**, **`%util`**), comparable to what many dashboards replay.
- **Name mismatch:** reports **block devices**, so **filesystem-heavy** apps may show little disk activity while doing lots of FS cache I/O (**visibility gap**).
- **Extended (`-x`) evolution:** column set grew very wide → **`-s`** “short” extended mode for readability.
- **Semantics highlights:**
  - **`await`:** total wait including **OS queue + device**—primary “how bad” signal for delivered latency.
  - **`%util`:** **busy time**, not necessarily throughput cap; **weak for virtual/LVM/RAID-backed** devices—pair with **load** (**tps**, **kB/s**).
  - **Read/write split (`-x` full):** avoids blending **write-back-cached writes** with **read latency** that often bounds apps.
  - **rqm/s / merges + areq-sz:** merger behavior hints **sequential vs random** and **effective I/O size**.
  - **Discard/flush** columns (newer kernels): helps narrow **trim/fsync** paths.
- **Gaps:** example laments **no disk error column** in `iostat`—USE “errors” may need another tool.

## Measurement-validity

- **Scope/semantics:** **block layer** metrics vs **application/FS** latency.
- **Representation:** **`%util`** as **idle inverse** can mislead on **virtual or parallel devices**.
