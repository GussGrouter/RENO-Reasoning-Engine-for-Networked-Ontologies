# Systems Performance — Ch.9 §9.6.12 MegaCli

Source: `systems-performance-ch9-scout-p482-560.txt`, lines **1964–2006** (printed ~484).

## Summary

- **RAID/HBA controllers** are **opaque** to OS tracers—behavior must be **inferred** from **externally visible I/O** or **vendor CLIs** (example **LSI MegaCli** event log).
- **Patrol read** windows (verify checksums) show up as **time-bounded activity**—relate to **§9.4.3** storage types narrative.
- **Limits:** firmware introspection helps **configuration/health class** issues; may still not explain **single slow I/O** to millisecond precision.

## Measurement-validity

- **Scope/semantics:** vendor events describe **controller policy/work**, not **per-request OS view**—triangulate with **block-layer traces**.
