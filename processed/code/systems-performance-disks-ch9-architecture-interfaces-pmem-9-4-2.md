# Systems Performance — Ch.9 §9.4.2 Interfaces + §9.4.1.3 Persistent memory (scout excerpt)

Source: `systems-performance-ch9-scout-p460-520.txt`, lines **1022–1116** (PDF ~441–443).

## Summary

### §9.4.1.3 Persistent memory (short)

- **Controller NVRAM caches:** orders faster than flash; **battery/supercap** bounds.
- **3D XPoint / Optane class:** **byte-addressable** PMEM—latency **between DRAM and NAND** in cited example; treat as **different failure/latency model** when present.

### §9.4.2 Interfaces

- **Decision axis:** **bandwidth**, **contention model** (shared parallel SCSI bus vs **point-to-point serial**), **encoding overhead** (e.g. **8b/10b → ~80%** effective data rate), **queue depth** (**NVMe** deep queues + **multi-queue** vs legacy **32–256** limits), **PCIe lane width** caps **NVMe** throughput.
- **NVMe:** **<20 µs** class latency expectation in text—always **re-verify** on SKU.

## Measurement-validity

- **Scope/semantics:** **link-line-rate** vs **delivered application throughput**; **parallel SCSI bus contention** vs **SAS/NVMe point-to-point**.

## Notes

- Historical speed tables omitted—use **current spec sheets**.
