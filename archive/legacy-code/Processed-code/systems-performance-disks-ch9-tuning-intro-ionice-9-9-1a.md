# Systems Performance — Ch.9 §9.9 Tuning (intro + §9.9.1 `ionice`)

Source: `systems-performance-ch9-scout-p482-560.txt`, lines **2390–2426** (printed ~494).

## Summary

- **Framing:** **static** / **config** layer on top of **§9.5** method work—**defaults often fine**; change with **evidence** and **docs**.
- **`ionice` classes:** **none / RT / best-effort / idle**—**RT** can **starve** other tenants (analogous to **RT CPU** risk); **idle** for **low-priority** work (e.g. **backups**).

## Links (decision, not product)

- **I/O class choice** is a **fairness vs latency** lever—paired with **`cgroups`** when isolation must be **hard**.
