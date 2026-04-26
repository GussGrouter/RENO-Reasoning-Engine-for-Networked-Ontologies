# Systems Performance — Ch.9 §9.3.9–§9.3.11 Utilization, saturation, %iowait

Source: `systems-performance-ch9-scout-p460-520.txt`, lines **562–642** (PDF ~433–434).

## Summary

### §9.3.9 Utilization

- **% busy time** in interval for **active work + non-transfer commands**; **any** util can hurt if **latency SLO** tight; **queueing** can bite **before** literal **100%** (see **Ch.2 queueing / ~60%** narrative).
- **Async I/O:** high disk util may **not** block apps—validate **response time + app wait path**.
- **Interval aggregation:** **bursts** (e.g. **write flush**) **flatten** in long windows (**Ch.2 utilization caveats**).

**Virtual disk utilization**

- OS may see **virtual disk busy** while **backing disks** differ: **striped load**, **write-back cache** hiding backend work, **RAID rebuild**—**reported util** can be **counterintuitive** vs **physical** reality.

### §9.3.10 Saturation

- **Queue length** beyond what device can deliver; **100% util** may have **little or lots** of saturation—need **queue stats / tracing** for truth.

### §9.3.11 %iowait (CPU)

- **Idle CPU** while **runnable threads block on disk**—**drops** when **CPU becomes busy elsewhere** even if **disk pain unchanged**—classic **confound**.
- Prefer **thread-blocked-on-I/O time** when possible; **iowait** still useful as **first hint** (“disks busy, CPUs idle”).

## Measurement-validity

- **Scope/semantics:** **virtual disk util** vs **physical util**; **iowait** vs **application pain**.
