# Systems Performance — Ch.9 §9.6.11 bpftrace (issue vs insert + RWBS keys)

Source: `systems-performance-ch9-scout-p460-520.txt`, lines **5015–5080** (PDF ~481; **scout extract ends here**).

## Summary

- **Attribution trade:** **`rq_issue`** may show **scheduler/worker** names when real submitter is gone; **`rq_insert`** improves **process naming** sometimes but **misses** I/O that **never queues**.
- **`rwbs` as histogram key:** splits **sync vs async write**, etc.—aligns multimodal latency investigation with **I/O class**.
- **Scout gap:** chapter promises **“disk I/O latency”** bpftrace subsection **after** this material—**not present** in `systems-performance-ch9-scout-p460-520.txt` (PDF window ends ~481).

## Measurement-validity

- **Scope/semantics:** choice of **issue vs insert** probe is a **definition-of-latency / attribution** decision, not a syntax detail.
