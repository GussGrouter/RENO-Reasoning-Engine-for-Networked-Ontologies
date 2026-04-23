# Systems Performance — Ch.8 §8.8.1 Application calls (posix_fadvise, madvise)

Source: `systems-performance-ch8-scout-p398-460.txt`, lines ~4614–4699 (print ~pp. 415–416).

## Summary

- **Synchronous write batching:** where **O_SYNC**-style per-op sync is expensive, **fsync(2) on a logical group** (per §8.3.7) can reduce round-trips; this is an **API contract** choice, not a mount knob.
- **Cache/prefetch hints:** **`posix_fadvise()`** (file range) and **`madvise(2)`** (mapped region) tell the kernel how the app *expects* to access data so it can **prefetch** and **retain or evict** pages with better policy.
- **Table 8.8 (posix_fadvise)** — advice values (see man page on target system): e.g. **SEQUENTIAL / RANDOM** (access order), **NOREUSE**, **WILLNEED** (likely soon), **DONTNEED** (not reused).
- **Table 8.9 (madvise)** — parallel vocabulary for mappings: **RANDOM**, **SEQUENTIAL**, **WILLNEED**, **DONTNEED**.
- Correctness does not rely on hints; wrong hints mainly waste **memory bandwidth** or **cache residency**.

## Measurement-validity

- Usually **not** a perturbation issue; misuse lands under **scope/semantics** if you infer “disk read amplification” from hinted residency alone without checking device/cache counters.
