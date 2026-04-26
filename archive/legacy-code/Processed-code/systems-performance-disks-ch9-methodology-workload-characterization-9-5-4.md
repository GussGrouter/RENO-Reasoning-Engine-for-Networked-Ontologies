# Systems Performance — Ch.9 §9.5.4 Workload characterization (+ advanced checklist)

Source: `systems-performance-ch9-scout-p460-520.txt`, lines **1633–1781** (PDF ~452–454).

## Summary

- **Core attributes:** **IOPS**, **throughput**, **size**, **read/write ratio**, **random vs sequential**—tie to **§9.3** definitions; capture **bursts** (writes flush), **max not only mean**, **distributions over time**.
- **Worked example** paragraph models **mixed random read + burst sequential write** story—use as **template** for internal **workload specs**.
- **Advanced checklist:** system/per-disk/per-controller **IOPS & BW**, **who** (apps/users), **which FS/files**, **errors**, **balance**, **per-bus throughput**, **non-data commands**, **syscall/kernel path**, **sync vs async**, **arrival-time distribution**.
- **Performance characterization** (result side): **util**, **saturation**, **avg service/wait**, **outliers**, **full latency distribution**, **throttling**, **non-transfer command latency**.
- **Event tracing:** richest **characterization** but **overhead**—disk writes **to the trace** can **perturb** and **feedback** (**[[instrumentation-overhead-and-perturbation]]**, **[[event-tracing]]**).

## Application validation

Capacity planning request: demand **workload paragraph + burst statistics**, not **“about 3000 IOPS”** alone.

## Measurement-validity

- **Perturbation:** high-rate tracing **feeding back** through **disk writes** or **CPU load**.
