# Systems Performance — Ch.10 §10.6.15 other tools — Linux sources (scout PDF 520–640)

## Source

- Title: *Systems Performance: Enterprise and the Cloud* (Second Edition)
- Scout: `processed/code/systems-performance-ch10-scout-p520-640.txt` (lines **3835–3838**; file rebuilt 2026-04-20)
- Scope: **where else signals live** + **fleet monitoring** reality

## Processed artifacts

- `processed/code/systems-performance-network-ch10-observability-other-tools-linux-sources-monitoring-10-6-15b.md`

## Extracted ideas

- **`/proc/net` + BPF iterators** are often the durable way to ship metrics; text tools are for humans—mind **parser brittleness** vs canonical sources ([[measurement-validity]] **scope/semantics** when dashboards disagree with `ss`/netlink).
- **strace** is explicitly high-overhead: classify as **perturbation** risk when used under load ([[instrumentation-overhead-and-perturbation]]).
- **Sniffer-style iftop** produces **rates/aggregates over a window**, not totals since boot—state the window when interpreting “who is busy” ([[counters-statistics-metrics]]).

## Decision clarity

**Decision:** choose **`/proc/net` + agent counters** over **interactive sniffers** when you need **continuous SLO-grade visibility** without per-second human operators ([[counters-statistics-metrics]]).

## Application validation

- **Fleet-wide “who hits this dependency”:** export stable counters from **BPF iterators** or agents; avoid scraping fragile CLI output as “truth” ([[measurement-validity]]).

## Concepts reused / refined / created

- Reused: [[measurement-validity]], [[instrumentation-overhead-and-perturbation]], [[counters-statistics-metrics]], [[systems-performance]]
- Refined: none
- **Created:** none

## Links

- Concepts: [[measurement-validity]], [[instrumentation-overhead-and-perturbation]], [[counters-statistics-metrics]], [[systems-performance]]
