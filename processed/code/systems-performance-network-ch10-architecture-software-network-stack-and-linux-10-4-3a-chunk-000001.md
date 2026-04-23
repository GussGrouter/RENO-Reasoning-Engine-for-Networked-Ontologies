# Systems Performance — Ch.10 §10.4.3 Software (network stack + Linux model)

Source: `systems-performance-ch10-scout-p520-640.txt`, lines **1737–1931** (PDF 520–640 extract; scout rebuilt 2026-04-20).

## Summary

- The network stack is layered and OS-dependent; modern stacks can process inbound packets on multiple CPUs.
- Linux specifics: kernel stack + drivers; packets move as `sk_buff`; there can be queueing in IP reassembly.
- Use this model to decide where queueing and CPU cost can arise (queues, buffers, drivers, softirq paths).

