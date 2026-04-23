# Systems Performance — Ch.9 §9.8.6 fio + §9.8.7 blkreplay

Source: `systems-performance-ch9-scout-p482-560.txt`, lines **2373–2389** (printed ~493).

## Summary

- **`fio`:** flexible loads; **`--direct=true`** when FS supports **non-buffered** I/O—ties disk chapter back to **Ch.8** micro-bench material.
- **`blkreplay`:** replay **blktrace** (or **DiskMon**) captures—useful for **hard-to-synthesize** production shapes.
- **Caveat:** replays can **mislead** if **target system geometry/capacity** differs—see **Ch.12 §12.2.3**.

## Measurement-validity

- **Scope/semantics:** replay **validity** depends on **environment parity**—not a portable “same speed” guarantee.
