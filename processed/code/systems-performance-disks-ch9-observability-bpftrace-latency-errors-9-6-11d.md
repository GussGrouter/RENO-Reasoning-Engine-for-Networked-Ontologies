# Systems Performance — Ch.9 §9.6.11 bpftrace (disk I/O latency + errors)

Source: `systems-performance-ch9-scout-p482-560.txt`, lines **1862–1963** (printed ~482–484).

## Summary

- **Disk I/O latency script:** pair **`block_rq_issue`** timestamps with **`block_rq_complete`** via BPF map keyed by **`(dev, sector)`**—unlike **VFS** tracing where **TID** works because **disk completions interrupt arbitrary CPUs**.
- **Assumption:** **at most one in-flight I/O per sector** at a time—if violated, latency math collides.
- **Optional:** add **`rwbs`** to map key for **per-flavor** histograms.
- **`bioerr`:** filter **`block_rq_complete`** where **`args->error != 0`** for actionable **error lines** (full script).
- **Bridge:** deep disk errors may still need **controller/drive vendor tools** next.

## Measurement-validity

- **Scope/semantics:** **(dev, sector)** identity differs from **thread-based** latency pairing used in **§8.6.15**—pick keying to match **subsystem concurrency** (**representation** if sector reused concurrently).
