# Systems Performance — Ch.9 §9.6.11 bpftrace (disk I/O size)

Source: `systems-performance-ch9-scout-p460-520.txt`, lines **4914–5014** (PDF ~480).

## Summary

- **Hypotheses:** **slow because large** (SSD **throughput-bound**) vs **death by tiny I/O** (**overhead-bound**)—attack with **`hist(bytes)`** distributions.
- **Example:** per-**comm** histogram at **`block_rq_issue`** exposes **who** emits **what sizes** (e.g., **`dmcrypt_write`** buckets).

## Measurement-validity

- **Scope/semantics:** **`rq_issue`** attributes **`comm`** at **issue time**—may reflect **kernel worker**, not original app (**same attribution caveat** as §9.6.5).
