# Systems Performance — Ch.10 §10.6.1 ss (socket statistics)

Source: `systems-performance-ch10-scout-p520-640.txt`, lines **2502–2602** (PDF 520–640 extract; scout rebuilt 2026-04-20).

## Summary

- Default `ss` output is a **socket inventory**: protocol, state, **Recv-Q / Send-Q** (queue backlog hints), endpoints—enough for **workload characterization** (how many clients, how many deps, concurrency).
- Extended flags expose **TCP internal snapshot** (RTO/RTT/MSS/cwnd, BBR fields, pacing, bytes in flight): use to classify whether the connection looks **application-limited**, **receive-window-limited**, or **send-buffer-limited** vs purely “network slow.”
- **RTT vs min RTT**: compare average RTT/mdev to **minrtt** to reason about **delay variance** (queueing/congestion) vs stable path—important for **tail latency** stories.
- **Mechanism note:** `ss` reads extended TCP info via **netlink** (`SOCK_DIAG` family); contrast with legacy **`/proc/net/tcp`** text paths used by older tooling—different plumbing, same *kind* of metrics but not identical freshness/coverage (**measurement-validity**: **scope/semantics** when correlating across tools).
