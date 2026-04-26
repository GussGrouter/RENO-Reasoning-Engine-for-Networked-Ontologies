# Systems Performance — Ch.9 §9.3.2 Time scales (Table 9.1)

Source: `systems-performance-ch9-scout-p460-520.txt`, lines **339–430** (PDF ~428–430).

## Summary

- Latency spans **µs to seconds** depending on **cache tier**, **media**, **queue depth**, **RAID path**; a **single slow** I/O can dominate **app latency**, or **many fast** I/Os can sum to the same pain.
- **Table 9.1** (book) orders events from **on-disk cache hit** through **worst-case virtual disk / RAID-5 / queueing**—**scaled** column is a **pedagogical analogy** (“if cache hit = 1 s…”) not a literal instrument readout.
- **Enterprise** vs **cloud / web** heuristics differ (e.g. author’s **>10 ms** vs **>50 ms** rule-of-thumb as **investigation thresholds**—environment-specific).
- **Bimodal device behavior:** **cache hit** vs **miss** populations → **average** latency (as in some **`iostat`** views) can **misrepresent** user-visible mix—tie to **[[multimodal-latency-distribution]]** and Ch.2 histogram figure reference.

## Measurement-validity

- **Representation:** collapsing **hit+miss** into **one average** hides **two modes** (and **tails**).

## Notes

- **NVMe** footnote: **10–20 µs** class for some devices—use **vendor + measure**, not table alone.
