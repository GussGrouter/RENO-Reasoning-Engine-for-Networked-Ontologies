# Systems Performance — Ch.9 §9.4 Architecture — SSD / flash (9.4.1.2)

Source: `systems-performance-ch9-scout-p460-520.txt`, lines **894–1020** (PDF ~439–441).

## Summary

- **SSD:** generally **offset-stable**, **size-predictable** for planning; **internal pathologies** still complex (**FTL**, wear, GC).
- **NAND:** **erase block** larger than **page** → **asymmetric R/W**, **write amplification** when **writes < erase block**; **DRAM+cap** mitigates bursty write latency.
- **Cell technology list** (SLC/MLC/…/3D NAND): **trade density vs endurance vs performance**—treat vendor **TBW / DWPD** + workload as **capacity planning inputs**, not as new primitives here.
- **FTL:** maps **logical sectors** to flash **pages/blocks**—often **log-structured** internally; **TRIM/discard** helps **free block** pool (**scope**: OS knows deleted/extents).
- **Pathologies:** **tail latency** from **retries/aging**, **FTL fragmentation** (sometimes helped by **secure erase/rebuild maps**), **internal compression** changing **usable throughput**.

## Application validation

**Sustained random write** on **small blocks:** validate against **flash erase size** and **write amplification** metrics—not just peak **IOPS** marketing.

## Notes

- **Persistent memory / 3D XPoint** paragraph starts next slice.
