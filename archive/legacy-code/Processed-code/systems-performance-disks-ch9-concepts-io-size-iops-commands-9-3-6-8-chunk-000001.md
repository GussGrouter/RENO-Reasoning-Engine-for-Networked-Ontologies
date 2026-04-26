# Systems Performance — Ch.9 §9.3.6–§9.3.8 I/O size, IOPS equivalence, non-data commands

Source: `systems-performance-ch9-scout-p460-520.txt`, lines **520–556** (PDF ~432).

## Summary

### §9.3.6 I/O size

- **Average or distribution** of **I/O sizes** characterizes workload; larger transfers raise **throughput** often at **higher per-op latency**.
- Sizes may be **quantized** (sector alignment), **inflated/deflated** through **FS / volume manager / driver** vs **application** intent (**Ch.8 §8.3.12**).
- **Flash** often **strongly prefers** certain **read/write sizes** (author example **4 KiB read / 1 MiB write** archetype)—discover via **vendor spec + microbench**.

### §9.3.7 IOPS are not equal

- **Raw IOPS count** insufficient: must bundle **randomness**, **size**, **read/write**, **buffering/direct**, **parallelism**; **latency-sensitive random** seeks **high IOPS headroom**; **streaming throughput** workloads may prefer **fewer larger** ops.

### §9.3.8 Non-data-transfer commands

- **Cache flush**, **TRIM/UNMAP** (**discard**) etc. consume **device time** without matching **application byte counts**—can drive **utilization** while apps see **different** bottlenecks.

## Measurement-validity

- **Scope/semantics:** comparing **IOPS** across devices/workloads without **shape** bundles is a **category error**.
