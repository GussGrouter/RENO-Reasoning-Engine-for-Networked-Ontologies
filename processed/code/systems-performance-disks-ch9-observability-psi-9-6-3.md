# Systems Performance — Ch.9 §9.6.3 PSI (I/O)

Source: `systems-performance-ch9-scout-p460-520.txt`, lines **2701–2719** (PDF ~464).

## Summary

- **`/proc/pressure/io`:** **some** vs **full** stall percentages over **10s / 60s / 300s** windows—**directional pressure** indicator (rising short-window vs long-window means **getting worse now**).
- **Use:** coarse **saturation / stall alerting** akin to load averages—then drill to **`pidstat`**, **`iostat`**, traces.

## Measurement-validity

- **Scope/semantics:** percentage of time threads were **I/O stalled**—not throughput; pairs with deeper tools for **cause**.
