# Systems Performance — Ch.9 §9.8 Experimentation (intro + §9.8.1 Ad hoc `dd`)

Source: `systems-performance-ch9-scout-p482-560.txt`, lines **2244–2284** (printed ~491).

## Summary

- **§9.8** frames **active tests** under **§9.5.9 micro-benchmarking** methodology—keep **`iostat`** open to **sanity-check** numbers.
- **`dd` sequential tests:** easy **throughput** experiments; **kernel cache can dominate** unless you use **raw device**, **`oflag=direct` / `iflag=direct`**, or accept **FS overhead**.
- **Safety:** raw **`dd` to devices** can **destroy data**—prefer **direct I/O to files** when possible.

## Measurement-validity

- **Scope/semantics:** measured **MB/s** may be **cache+disk**, **disk only**, or **disk+FS**—state which path your flags implemented (**representation**).
