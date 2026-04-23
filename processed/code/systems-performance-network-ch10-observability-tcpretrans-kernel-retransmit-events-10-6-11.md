# Systems Performance — Ch.10 §10.6.11 tcpretrans (TCP retransmit events)

Source: `systems-performance-ch10-scout-p520-640.txt`, lines **3275–3324** (PDF 520–640 extract; scout rebuilt 2026-04-20).

## Summary

- Prints **kernel-side retransmit events** with endpoints + **TCP state**—contrasts with inferring retransmits indirectly from bulk packet capture + post-processing.
- Interprets rates qualitatively: sustained **ESTABLISHED** retransmits suggest **path/network pressure**; high **SYN_SENT** retransmits suggest **listen backlog/app accept pace** problems (SYN drops/backlog saturation narrative).
- Lower event frequency than packet capture typically implies **lower overhead** than sniff-all-packets workflows.
- Options add **tail-loss probes** (`-l`) or **count-by-flow** (`-c`) summaries.
