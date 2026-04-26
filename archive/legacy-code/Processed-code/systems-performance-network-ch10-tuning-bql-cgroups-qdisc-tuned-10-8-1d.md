# Systems Performance — Ch.10 §10.8.1 System-wide tuning (part D — BQL, cgroup controls, default qdisc, tuned)

Source: `systems-performance-ch10-scout-p520-640.txt`, lines **4336–4439** (PDF 520–640 extract; scout rebuilt 2026-04-20).

## Summary

- **Byte Queue Limits (BQL)**: exposed under sysfs per TX queue (`byte_queue_limits/limit*`), auto-tuned in bytes; operators can clamp via **`limit_min` / `limit_max`** to bound driver queue depth.
- **Cgroup network controls**: **`net_prio`** for outbound priority; **`net_cls`** for tagging packets with a class ID consumable by qdisc shaping/limiting and BPF; notes moving classification/measurement/remarking to **tc egress** hooks to reduce pressure on the **root qdisc lock** (scalability story).
- **Queueing disciplines**: `man -k tc-` to discover qdisc man pages; **`net.core.default_qdisc`** selects the default (example shows **`fq_codel`**); many distributions already default to **`fq_codel`** for general cases.
- **Tuned**: profile bundles (`tuned-adm list`, `tuned-adm profile …`); **`network-latency`** example chains **`include=latency-performance`** and sets **`sysctl`** knobs such as **`net.core.busy_read` / `busy_poll`**, **`net.ipv4.tcp_fastopen`**, disables **`kernel.numa_balancing`**, and adds **`skew_tick=1`** via bootloader snippet—explicit trade of power/latency determinism.
