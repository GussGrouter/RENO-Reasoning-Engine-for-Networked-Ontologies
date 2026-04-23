# Systems Performance — Ch.9 §9.6.7 biosnoop

Source: `systems-performance-ch9-scout-p460-520.txt`, lines **3463–3967** (PDF ~470–473).

## Summary

- **One line per I/O** with **completion time**, **PID/COMM**, **disk**, **type**, **sector**, **bytes**, **latency** (issue→complete).
- **Queue ramp pattern:** simultaneous issues finish **in order** with **rising latency** → classic **device-side queueing** signature.
- **Outlier workflow:** capture file → **sort by latency** → inspect **slowest rows** → scroll earlier timeline for **precursors** (queue buildup vs reorder vs **VM scheduling** gaps inflating “I/O time”).
- **`-Q`:** adds **QUE(ms)** (**create→issue**) vs **LAT(ms)** (**issue→complete**) to separate **OS queue** vs **device**.

## Measurement-validity

- **Representation:** on **guests**, long gaps may include **hypervisor steal/deschedule**—not always disk alone.
