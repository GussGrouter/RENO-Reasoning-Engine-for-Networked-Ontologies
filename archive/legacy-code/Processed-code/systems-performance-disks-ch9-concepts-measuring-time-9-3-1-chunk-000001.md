# Systems Performance — Ch.9 §9.3.1 Measuring time (kernel vs disk decomposition)

Source: `systems-performance-ch9-scout-p460-520.txt`, lines **239–337** (PDF ~427–428).

## Summary

**Generic intervals**

- **I/O request / response time:** issue → completion (**full stack** where applicable).
- **Wait time:** **queued**, not actively serviced.
- **Service time:** actively processed (**may still include hidden queues** on modern devices).

**From the kernel (block path)**

- **Block I/O wait time (“OS wait”):** **creation → leaves final kernel queue → issued to device** (may span **multiple software queues**).
- **Block I/O service time:** **issue to device → completion interrupt** (author notes OS “service time” today often **includes internal device queueing**).
- **Block I/O request time:** **wait + service** end-to-end from kernel creation.

**From the disk**

- **Disk wait / service / request time** analogs on **on-disk queues**; **disk request time** aligns with **block I/O service time** in the layered diagram.

**Interpretation hazards**

- **“Service time”** from **`iostat`** historically treated as **disk performance proxy**—**oversimplified** when **multiple parallel ops** or **deep queues** exist; **inferring** avg service time as **utilization/IOPS** assumes **single-server** semantics and breaks on **parallelism**.
- **Tracing** (issue/completion timestamps) gives **ground-truth intervals** per I/O.

## Measurement-validity

- **Scope/semantics:** **“Latency”** and **“service time”** labels **shift by observer** (kernel block path vs disk engineer vs **`iostat` column**).
