# Systems Performance — Ch.9 §9.6.10 blktrace (btt + visualization)

Source: `systems-performance-ch9-scout-p460-520.txt`, lines **4679–4869** (PDF ~478–479).

## Summary

- **`btt`:** turns traces into **stage timing stats**—notable intervals include **Q2C** (queue→complete, **block-layer total**), **D2C** (**issue→complete**, **device latency**), **I2D** (**insert→issue**, queue wait), **M2D** (**merge→issue**).
- **Outliers:** **max** stage times can explain **tail latency** even when **averages** look mild.
- **Visualization:** **`iowatcher`** (blktrace package), **seekwatcher**—offline views of captured traces.

## Measurement-validity

- **Scope/semantics:** each **btt abbreviation** measures a **different sub-interval**—compare like-to-like before blaming “the disk.”
