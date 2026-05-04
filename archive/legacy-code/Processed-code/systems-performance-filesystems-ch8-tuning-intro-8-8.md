# Systems Performance — Ch.8 §8.8 Tuning (intro)

Source: `systems-performance-ch8-scout-p398-460.txt` (print ~pp. 414–415), lines ~4600–4613.

## Summary

- Tuning here means **concrete tunables**; much of the *method* (workload characterization, cache thinking) already lives in **§8.5 Methodology**.
- **What to set** depends on **OS build**, **file system type**, and **intended workload**—treat tables in the book as **examples**, not a universal recipe.
- Scope of this section: **application-level calls** that influence cache/prefetch behavior, then **ext4** and **ZFS** as **illustrative** families. **Page cache** sysctl-style tuning points to **Ch.7 Memory**.

## Notes

- Full narrative: *Systems Performance* 2e, Chapter 8.
