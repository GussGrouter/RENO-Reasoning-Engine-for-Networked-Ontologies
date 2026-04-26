# Systems Performance — Ch.9 §9.4.3 — Table 9.3 + RAID write path + caches

Source: `systems-performance-ch9-scout-p460-520.txt`, lines **1155–1274** (PDF ~444–446).

## Summary

- **Table 9.3** (book): RAID levels **0 concat/stripe, 1, 10, 5, 6** with **performance characterization**—transcribed only in PDF; here: **striped RAID-0** fastest **without redundancy**; **mirror** read parallelism vs **write limited by slowest leg**; **RAID-5/6** parity paths **write-costly**.
- **RAID-0 caveat:** **no redundancy**—only acceptable when **workload fault model** allows (**ephemeral cache**, **replaceable instances**).
- **Observability:** **hardware virtual disk** hides **physical disks**—echoes **virtual disk utilization** warnings (**cross-component**).
- **Parity RMW:** sub-stripe writes may **read strips + parity**, **XOR-update**, **rewrite**—mitigated by **full-stripe writes** and **stripe size vs mean write size** tuning.
- **RAID controller caches:** **write-back + BBU** mask **RMW pain** until **cache policy** changes.
- **Vendor background features** (example **patrol read**, **cache flush interval**): can **steal bandwidth** or **inject latency spikes**—read **vendor docs** (**static-performance-tuning** mindset).

## Measurement-validity

- **Representation:** **fast RAID writes** may be **ACK from cache**, not **platters committed**.
