# Systems Performance — Ch.9 §9.6.8 iotop, biotop

Source: `systems-performance-ch9-scout-p460-520.txt`, lines **3967–4290** (PDF ~473–474).

## Summary

- **`iotop`:** kernel **accounting**-based “top for disk”; batch mode (`-b`) for logs; columns include **DISK READ/WRITE**, **SWAPIN**, **IO %** wait.
- **Calibration:** author found **`iotop` undercounted writes** vs a known workload—**cross-check** with **`biotop`** (different instrumentation).
- **`biotop`:** BPF-based per-interval **read/write counts**, **Kbytes**, **avg ms** latency (issue→complete); **PID/COMM best-effort** when real issuer already off CPU.

## Measurement-validity

- **Representation:** **accounting-based tops** vs **BPF block taps** can **disagree** on the same workload—treat as **validation**, not oracle.
