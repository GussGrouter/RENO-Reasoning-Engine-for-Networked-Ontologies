# Systems Performance — Ch.9 §9.3.3–§9.3.5 Caching, random vs sequential, read/write ratio

Source: `systems-performance-ch9-scout-p460-520.txt`, lines **431–512** (PDF ~431–432).

## Summary

### §9.3.3 Caching

- **Best I/O is none:** stack from app down to **disk** caches reads and buffers writes; **Ch.3 Table 3.2** enumerates layers; **Table 9.2** (book) lists **below-FS** examples: **vdev**, **buffer cache**, **RAID/HBA/array caches**, **on-disk DDC DRAM**.
- **Random I/O** historically **cache-sensitive** at **disk** tier.

### §9.3.4 Random vs sequential (offset space)

- **HDD:** **seek + rotation** penalize **random** vs **streaming** (Figure 9.6); mitigations include **cache**, **isolation**, **placement**—**mapping** from **OS LBA** to **physical geometry** may be **non-obvious** (**virtual disk**, **DDC remapping**) so “randomness” may be inferred from **long service time** rather than raw offset jumps.
- **Flash reads:** often **similar** seq vs rand; **small random writes** may hit **RMW**/erase **block** effects; **write** mechanics differ **by firmware**.

### §9.3.5 Read/write ratio

- Expressed over time (e.g. **% reads**); **high reads** → **cache** scaling; **high writes** → **more spindles/flash bandwidth** capacity; **read vs write** can differ in **random/seq** and **size**.

### Table 9.2

- Omitted verbatim; captured in §9.3.3 bullets.
