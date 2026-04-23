# Systems Performance — Ch.9 Disks — Intro, chapter map, §9.1 terminology

Source: `systems-performance-ch9-scout-p460-520.txt`, lines **40–181** (PDF ~424–425).

## Summary

- **Chapter role:** Disk I/O drives **tail latency** and can **idle CPUs** under load; SSDs help but **capacity and rate demands** still create bottlenecks.
- **Six parts:** Background (terminology, models, concepts) → **Architecture** → **Methodology** → **Observability Tools** → **Experimentation** → **Tuning**—last three emphasize **Linux** practice.
- **/fs vs disk:** Prior chapter (**file systems**) is the usual place to interpret **application** behavior; this chapter stresses **devices and block path**.

### §9.1 Terminology (bullets)

- **Virtual disk:** logical LUN-like object that may span **fractions or aggregates** of physical disks.
- **Transport:** physical bus/link for **data + control**.
- **Sector:** traditionally **512 B**, often **4 KiB** today.
- **I/O:** reads/writes with **direction, disk address/offset, size**; excludes some **non-transfer** disk commands unless stated.
- **Disk commands:** e.g. **cache flush**, **unmap/TRIM**.
- **Throughput:** current **data transfer rate** (bytes/s context).
- **Bandwidth:** **maximum** sustainable transfer ceiling for controller/transport (**hardware bound**).
- **I/O latency:** **start-to-complete** time for one operation (**networking “latency”** wording may mean **TTFA + transfer**—stay explicit).
- **Latency outliers:** unusually slow disk ops.

Further terms (disk, controller, array, …) defer to glossary / Ch.2–3 terminology sections.
