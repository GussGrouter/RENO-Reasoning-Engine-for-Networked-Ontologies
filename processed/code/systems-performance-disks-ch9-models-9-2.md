# Systems Performance — Ch.9 §9.2 Models (simple disk, caching disk, controller)

Source: `systems-performance-ch9-scout-p460-520.txt`, lines **182–237** (PDF ~425–426).

## Summary

### §9.2.1 Simple disk + queue

- Requests sit in an **on-device queue** before **service**—same abstract structure as **[[queueing-theory]]** checkout lines.
- Scheduling may **not** be FCFS: **elevator** on HDDs; **split read/write queues** on some flash controllers.

### §9.2.2 Caching disk

- **On-disk DRAM** satisfies some reads at **low latency**; misses pay **full device latency**.
- **Write-back** reports completion after **cache admit** (before **persistent** media); **write-through** waits for **next tier**.
- Production arrays often pair **write-back** with **battery/cap** for power-loss safety.

### §9.2.3 Controller / HBA

- **Host bus adapter** bridges **CPU-side transport** and **storage-side transport**; bottleneck may be **either bus**, **controller**, or **disks** (see §9.4).

## Notes

- Figures 9.1–9.3 omitted; see PDF.
