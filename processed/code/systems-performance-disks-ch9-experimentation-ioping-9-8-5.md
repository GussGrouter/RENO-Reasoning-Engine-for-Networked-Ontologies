# Systems Performance — Ch.9 §9.8.5 ioping

Source: `systems-performance-ch9-scout-p482-560.txt`, lines **2339–2372** (printed ~492–493).

## Summary

- **Ping-like** periodic **4KB reads** with **microsecond** latency prints—**low duty cycle** (example **`iostat`** shows **~0.4% util** vs **100%** saturating benches).
- **Use case:** **gentle probing** where **heavy micro-benchmarks** would be unsafe—still an **experiment**, not passive monitoring.

## Measurement-validity

- **Perturbation:** far lower **load-induced distortion** than saturation tests—trade **signal strength** vs **production safety**.
