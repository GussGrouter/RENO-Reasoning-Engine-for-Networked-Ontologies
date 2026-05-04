# Systems Performance — Ch.9 §9.7.2 Latency scatter plots

Source: `systems-performance-ch9-scout-p482-560.txt`, lines **2160–2184** (printed ~488).

## Summary

- **Per-event** scatter (**time** vs **latency**) surfaces **rare tails** missed by dashboard means.
- **Causal sketch:** **read outliers** after **write bursts**—writes **return from controller cache** quickly while **later reads queue behind destaging** to disk (**cross-component-interactions** / queueing intuition).

## Measurement-validity

- **Scope/semantics:** scatter shows **event-level** reality—contrasts with **interval-averaged** charts.
