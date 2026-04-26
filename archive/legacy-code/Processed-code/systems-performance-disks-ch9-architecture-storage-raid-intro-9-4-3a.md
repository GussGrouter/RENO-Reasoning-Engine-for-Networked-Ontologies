# Systems Performance — Ch.9 §9.4.3 Storage types — disk + RAID framing

Source: `systems-performance-ch9-scout-p460-520.txt`, lines **1118–1154** (PDF ~443–444).

## Summary

- **Four topologies:** **internal disks**, **RAID**, **arrays**, **NAS**—each changes **observability surface** and **bottleneck story**.
- **JBOD / passthrough:** simplest **per-disk** observability.
- **RAID:** presents **virtual disk**—often **cache + parity/mirror** work hidden from **simple OS counters**.
- **Hardware vs software RAID:** historical **offload + BBU** vs modern **CPU surplus** → **ZFS/md** style **software RAID** can improve **observability** and **repairability** at cost of **CPU** and **driver stack** complexity.
- **Stripe:** grouped blocks **striped across drives**—performance depends on **stripe size × workload**.

## Decision clarity

**Decision:** choose **software-defined RAID / FS-level redundancy** over **opaque hardware RAID** when **production debugging** requires **per-disk visibility** and **you can afford CPU/software complexity**.
