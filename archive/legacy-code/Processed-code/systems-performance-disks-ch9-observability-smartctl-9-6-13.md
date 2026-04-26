# Systems Performance — Ch.9 §9.6.13 smartctl

Source: `systems-performance-ch9-scout-p482-560.txt`, lines **2007–2077** (printed ~485–486).

## Summary

- **Drive firmware** is another **black box**; OS sees **requests/latency**; **SMART** exposes **health/counters** (temperature, **grown defects**, **ECC-corrected reads**, hours, self-tests).
- **Virtual RAID paths:** **`smartctl --all -d megaraid,N`** reaches **physical disk behind HBA**.
- **Use:** **predictive failure** / **confirm failing device**—**not** microsecond **per-I/O forensics** (that stays with **kernel/BPF**).

## Measurement-validity

- **Representation:** SMART **aggregate health** vs **trace timelines**—different questions (**failure risk** vs **tail latency causes**).
