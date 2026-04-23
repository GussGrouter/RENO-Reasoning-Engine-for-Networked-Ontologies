# Systems Performance — Ch.9 §9.6.6 biolatency

Source: `systems-performance-ch9-scout-p460-520.txt`, lines **3109–3462** (PDF ~469–470).

## Summary

- **BPF histogram** of **device issue→complete** latency (aka **disk request time**).
- **Bi-modal example:** infer **different paths** (random vs large I/O, flags, **queueing tail** vs fast mode).
- **Flags:** **`-F`** splits histograms per **I/O flag** (sync write vs read-ahead, etc.)—often explains **merged multimodal** `await`.
- **`-Q`:** includes **OS queue time** (creation→issue), widening definition toward **full block I/O wait**.

## Measurement-validity

- **Scope/semantics:** default vs **`-Q`** measures **different intervals** along the path—compare definitions before tuning.
