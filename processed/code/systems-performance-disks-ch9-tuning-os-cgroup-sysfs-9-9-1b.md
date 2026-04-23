# Systems Performance — Ch.9 §9.9.1 OS tunables (cgroups blkio + sysfs queues)

Source: `systems-performance-ch9-scout-p482-560.txt`, lines **2428–2450** (printed ~494).

## Summary

- **`blkio` cgroup controls:** **weights vs hard caps**, separate **read/write**, **IOPS vs B/s**—cross-ref **Ch.11** cloud context.
- ** sysfs queue knobs:** **scheduler policy**, **`nr_requests`**, **`read_ahead_kb`**—tie back to **§9.4** architecture explanations; **`Documentation/block/queue-sysfs.txt`** cited as authoritative.

## Measurement-validity

- **Scope/semantics:** ** cgroup limits** measure/enforce **policy throughput**, not raw **device physics**—misinterpretation drives **wrong “disk slow” narratives**.
