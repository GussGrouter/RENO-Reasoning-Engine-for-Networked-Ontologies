# Systems Performance — Ch.9 §9.4.4 Operating system disk I/O stack (Linux focus)

Source: `systems-performance-ch9-scout-p460-520.txt`, lines **1293–1409** (PDF ~447–449).

## Summary

- **Generic stack** (Fig. 9.7) + **Linux** figures **9.8–9.9** omitted—see PDF; path spans **FS → block → driver → device**.
- **Block interface:** **512 B lineage**, **buffer cache** role partly superseded by **FS page cache** (**Ch.8**); **`iostat`** observes here; **BPF/static probes** common.
- **Raw I/O** historically bypassed buffer cache—parallel **O_DIRECT** mental model (**Ch.8**).
- **I/O merging:** **front/back merge + coalesce** reduces **kernel CPU** and **device ops** (**throughput-latency** coupling).
- **Schedulers:** classic (**noop/deadline/CFQ**) vs **blk-mq** multi-queue stack (**Linux ≥5** defaults)—goals include **fairness**, **latency deadlines**, **starvation avoidance**, **parallel issue** for **flash/IOPS**.
- **Examples:** **deadline** mitigates **elevator starvation**; **Kyber** targets **read/write latency knobs**—treat as **policy layer** atop queueing.

## Measurement-validity

- **Perturbation/representation:** scheduler **reordering** changes **completion order** vs **issue order**—tail latency attribution needs **trace**, not **average queue depth alone**.

## Notes

- Next section in book: **§9.5 Methodology** (starts PDF page ~449 after Table 9.4).
