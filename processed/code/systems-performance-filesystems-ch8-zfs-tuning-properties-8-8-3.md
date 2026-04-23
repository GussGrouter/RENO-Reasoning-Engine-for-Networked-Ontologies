# Systems Performance — Ch.8 §8.8.3 ZFS (dataset properties + performance)

Source: `systems-performance-ch8-scout-p398-460.txt`, lines ~4962–5106 (print ~pp. 417–419). *Scout order places a page break before **Table 8.10**; content restored to logical narrative.*

## Summary

- **Inspect:** **`zfs get all <dataset>`** shows **property / value / source** (default, inherited, local).
- **Set:** **`zfs set property=value <dataset>`** (details in **`zfs(1)`** / platform docs).

### Table 8.10 (key performance-related properties, paraphrased)

| Parameter | Role |
|-----------|------|
| **recordsize** | 512 B–128 KiB **suggested** block size for **large** files; mismatch with **small random I/O** can waste space/bandwidth. **Smaller files** use **dynamic** size ≤ record size. |
| **compression** | Algorithms (e.g. **lzjb**, **lz4**, **gzip** levels) may **reduce backend I/O** when CPU is cheaper than storage latency/bandwidth. |
| **atime** | **On** can cause **writes after reads** for timestamp updates; **off** if unused. |
| **primarycache** | **ARC**: **`all` / `none` / `metadata`**—limit **ARC pollution** from low-value datasets (e.g. archives) with **`none`** or **`metadata`**. |
| **secondarycache** | **L2ARC** inclusion policy (**`all` / `none` / `metadata`**). |
| **logbias** | **`latency`** vs **`throughput`** for **sync-write** handling—**latency** favors **log devices**; **throughput** favors **pool** placement (see ZFS docs for exact behavior on your implementation). |
| **sync** | **standard / always / disabled**—**synchronous durability** semantics (risk/correctness trade). |

### Other

- **Tuning priority:** author highlights **recordsize** to **match application I/O shape** (default often **128 KiB**).
- **System-wide tunables** (examples named): **`zfs_txg_synctime_ms`**, **`zfs_txg_timeout`**, **`metaslab_df_free_pct`**—smaller **TXG** sync windows can reduce **contention** and **queueing** vs other I/O at the cost of different aggregation behavior—**always read current tunable docs**.

## Measurement-validity

- **Scope/semantics:** **`recordsize`** vs actual **object size** and **I/O pattern**—misalignment shows up as **space amplification** or **read/modify/write** behavior, not as a single “MB/s” headline.
