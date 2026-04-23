# Systems Performance — Ch.9 §9.6.5 perf (block tracepoints)

Source: `systems-performance-ch9-scout-p460-520.txt`, lines **2900–3108** (PDF ~465–467).

## Summary

- **`perf list 'block:*'`** enumerates **block layer tracepoints** (queue, remap, plug, completion, …).
- **Stack capture:** `perf record -e block:block_rq_issue -a -g` ties **issues** to **user/kernel stacks** (example: **`fsync` → ext4 → blk-mq**).
- **Attribution caveat:** many I/Os are **issued later** by **kernel threads**—**`block_rq_issue`** may miss **originating process**; **`block_rq_insert`** alternative sees **queue insertion** but misses **direct-issue** paths.
- **Latency pairing:** record **issue + complete** then **diff timestamps** offline; overlaps with BPF tools that compute latency **in kernel**.

## Measurement-validity

- **Perturbation:** **`perf record`** volume can be heavy—bounded **`sleep`** windows and careful **event filtering**.
