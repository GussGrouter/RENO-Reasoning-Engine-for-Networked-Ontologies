# Systems Performance — Ch.8 §8.9 Exercises (scaffold)

Source: `systems-performance-ch8-scout-p398-460.txt`, lines ~5108–5206 (print ~pp. 419–420).

## Summary

Exercise list retained as a **study checklist** (answers not transcribed):

1. **Terminology:** logical vs physical I/O, random vs sequential, direct I/O, non-blocking I/O, **WSS**.
2. **Concepts:** VFS role, where **FS latency** can be measured, purpose of **prefetch** and **direct I/O**.
3. **Deeper:** **fsync** vs **O_SYNC**; **mmap** vs **read/write**; **inflation/deflation** logical→physical I/O; **CoW** performance upside.
4. **Procedures:** build **FS cache tuning checklist** (caches, sizes, hit rates); **workload characterization** for FS ops using **OS observability first**.
5. **Tasks:** measure FS op **latency distribution** (not just mean) + **time-in-FS per thread**; **micro-benchmark** to estimate **cache effective size** and show degradation when **WSS** exceeds cache.
6. **Advanced (optional):** tool sketch for **sync vs async** FS writes with rates/latency/**PID**.
7. **Advanced (optional):** tool for **indirect/inflated** I/O breakdown by cause.

## Notes

- Numbered prompts reference earlier chapter sections; use as self-test against [[micro-benchmarking]], [[latency-analysis]], [[event-tracing]], [[caching]].
