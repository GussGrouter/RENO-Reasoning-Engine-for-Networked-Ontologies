# Systems Performance — Ch.9 §9.6.11 bpftrace (disk intro + one-liners)

Source: `systems-performance-ch9-scout-p460-520.txt`, lines **4870–4913** (PDF ~479–480).

## Summary

- **Role:** **bpftrace** as **high-level BPF script** surface for **custom disk investigations** (Ch.15 detail).
- **Examples:** count **`tracepoint:block:*`** hits; **`hist(bytes)`** on **`block_rq_issue`**; **user stacks** on **`rq_issue`/`rq_insert`**; **rwbs** histogram; **errors** on completion; **SCSI** opcode/result/driver probes.

## Scout boundary

- Section preview lists **disk I/O size**, **latency**, **one-liners**—this slice ends **before “Disk I/O Size.”**
