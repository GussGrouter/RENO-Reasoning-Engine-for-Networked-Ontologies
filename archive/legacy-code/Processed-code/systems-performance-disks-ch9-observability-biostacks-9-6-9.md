# Systems Performance — Ch.9 §9.6.9 biostacks

Source: `systems-performance-ch9-scout-p460-520.txt`, lines **4291–4365** (PDF ~474–475).

## Summary

- **`biostacks`:** **bpftrace** tool combining **initialization stack** with **histogram of block I/O request time** (enqueue→complete).
- **Interpretation:** stacks often show **non read/write** paths—**permission checks**, **metadata**, **journal**, **scrubbers** explaining “mystery” disk traffic (example: **ZFS scrub**).

## Links to methodology

- Answers **why disk is busy** when **no obvious app reader/writer**—narrows to **kernel/FS housekeeping** vs mis-blaming tenants.
