# Systems Performance — Ch.8 §8.8.2 ext4 (kernel atime defaults, tune2fs, common noatime)

Source: `systems-performance-ch8-scout-p398-460.txt`, lines ~4798–4887 (print ~pp. 417–418).

## Summary

- **Default behavior drift:** since **Linux 2.6.30**, generic behavior matches **relatime-style** updates unless **`noatime`** or **`strictatime`** is chosen; **atime** older than ~**1 day** may still be refreshed—**semantics depend on kernel version and mount flags**.
- **Documentation split:** generic flags in **`mount(8)`**, **ext4-specific** flags in **`ext4(5)`** (journal options, checksums, compatibility flags—see source man page grids).
- **Inspect current settings:** **`tune2fs -l device`**, **`mount`** output.
- **`tune2fs(8)`** can set/clear some persisted mount-related flags per filesystem metadata (details in its man page).
- **Performance lever:** **`noatime`** avoids **access timestamp** updates when applications do not need them → fewer **metadata writes** on read-heavy workloads.

## Measurement-validity (conditional)

- **Scope/semantics:** treating “we mounted **noatime**” as “zero atime cost” without checking **application assumptions** (mailers, backup, audit patterns) can mis-scope user-visible correctness vs I/O savings.
