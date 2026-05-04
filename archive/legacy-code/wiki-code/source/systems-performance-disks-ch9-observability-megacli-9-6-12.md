# Systems Performance — Ch.9 §9.6.12 MegaCli

## Source

- Title: *Systems Performance: Enterprise and the Cloud* (Second Edition)
- Scout: `processed/code/systems-performance-ch9-scout-p482-560.txt`
- Scope: **§9.6.12**

## Processed artifacts

- `processed/code/systems-performance-disks-ch9-observability-megacli-9-6-12.md`
- Chunks: `*-chunk-000001.md`

## Extracted ideas

- **Firmware boundary:** HBAs expose **partial truth** via **vendor CLIs**—combine with **kernel-visible I/O** experiments, not instead of them ([[measurement-validity]], [[resource-vs-implementation-bottleneck]]).

## Application hook

Seeing **patrol-read** intervals in **`MegaCli` logs** explains **silent periodic slowdowns** that **pure `iostat`** blames on “disk busy” without **schedule**.

## Concepts reused / refined / created

- Reused: [[measurement-validity]], [[resource-vs-implementation-bottleneck]], [[systems-performance]]
- **Created:** none

## Links

- Concepts: [[measurement-validity]], [[resource-vs-implementation-bottleneck]], [[systems-performance]]
