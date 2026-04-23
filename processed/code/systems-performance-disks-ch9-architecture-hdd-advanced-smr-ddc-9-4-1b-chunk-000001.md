# Systems Performance — Ch.9 §9.4 Architecture — HDD tuning topics, SMR, disk data controller

Source: `systems-performance-ch9-scout-p460-520.txt`, lines **783–892** (PDF ~436–438).

## Summary

- **Short-stroking:** restrict workload to **outer tracks** → smaller **seek envelope** + often **higher MB/s** (zoning); **benchmark fraud** risk when **price/density** omitted.
- **Sector zoning:** outer tracks hold **more sectors** at same RPM → **higher sequential MB/s** at edge.
- **Advanced Format / 512e:** **4 KiB** physical sectors with **512 B emulation** can trigger **RMW**; **misaligned 4 KiB** logical I/O can **span sectors** and inflate ops.
- **On-disk RAM:** **read cache + write buffering**; **TCQ/NCQ** expose **queue + reorder** to reduce mechanical cost.
- **Elevator seeking:** completion **order ≠ issue order** on traces; **starvation parable**—steady stream near **offset A** delays isolated work at **offset B** (**queueing + fairness** concern).
- **ECC / retries:** **long latency tail** without app-visible error—watch **soft error rates**.
- **Vibration:** environmental mechanical coupling can **burst slow I/O** (author anecdote—**environment** as variable).
- **Sloth disks:** **multi-second** latency **without clean error**—hard to spot behind **virtual disks**; timeouts/offlining trade vs tail risk.
- **SMR:** **shingled** writes → **rewrite amplification** / poor **random write**—**archive / write-once** fit; awkward under **heavy RAID write**.
- **Disk data controller (DDC):** firmware **remaps** LBAs to physical layout—**OS cannot introspect** true placement (**measurement-validity**: **scope**—offset-space “randomness” is **not** physical randomness).

## Measurement-validity

- **Scope/semantics:** **LBA sequentiality** vs **physical head motion**; vendor **geometry** vs **flash/zone** reality.
