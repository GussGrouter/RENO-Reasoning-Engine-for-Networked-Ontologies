# Systems Performance — Ch.10 §10.7.3 pathchar / pchar (bandwidth-per-hop probing)

Source: `systems-performance-ch10-scout-p520-640.txt`, lines **3993–4015** (PDF 520–640 extract; scout rebuilt 2026-04-20).

## Summary

- `pathchar`-style tools estimate **per-hop bandwidth** by sending many **varied-size probes** and doing statistical analysis (example output shows Mb/s and delay per hop, bottleneck summary).
- Practical limitations: original `pathchar` did not become widely available/maintained; **`pchar(8)`** noted as more accessible alternative.
- Operational cost: can be **very time-consuming** (tens of minutes depending on hops); research exists on speeding probe schedules.
