---
id: systems-performance-ch2-methodologies-continuation-p91-105
type: source
status: active
phase: phase-2-source-built
parent: systems-performance-hub
prev: systems-performance-ch2-methodologies-continuation-p76-90
next: systems-performance-ch2-methodologies-continuation-p106-120
source_id: systems-performance
raw_id: systems-performance-raw-001
processed_ids: ["systems-performance-processed-001"]
chunk_ids: ["systems-performance-chapter-2-methodologies-continuation-chunk-0023", "systems-performance-chapter-2-methodologies-continuation-chunk-0024", "systems-performance-chapter-2-methodologies-continuation-chunk-0025", "systems-performance-chapter-2-methodologies-continuation-chunk-0026", "systems-performance-chapter-2-methodologies-continuation-chunk-0027", "systems-performance-chapter-2-methodologies-continuation-chunk-0028"]
title: "Systems Performance Chapter 2 — Methodologies continuation (pages 91-105)"
source_kind: book-section
section_range: chapter-2-methodologies-continuation
---

# Systems Performance Chapter 2 — Methodologies continuation (pages 91-105)

## Source scope

- **Source:** Systems Performance: Enterprise and the Cloud, Second Edition (Brendan Gregg); bounded slice **pages 91–105**, `section_range` **chapter-2-methodologies-continuation**, `source_kind` **book-section**.
- **Chunk span:** `systems-performance-chapter-2-methodologies-continuation-chunk-0023` … `systems-performance-chapter-2-methodologies-continuation-chunk-0028` (linear chain; `slice_id` **chapter-2-methodologies-continuation-p91-105** in `manifest.json`).
- **Narrative role:** Continues **§2.5** after hardware USE: software USE, **RED**, workload characterization, drill-down, Five Whys, latency analysis / **Method R**, tracing, baselines, static tuning, cache tuning, micro-benchmarks, **mantras**, then **§2.6** through **Amdahl**, **USL**, and **queueing** (**Little's Law**).

## Graph navigation

- **Hub:** [[systems-performance]]
- **Previous bounded page:** [[systems-performance-ch2-methodologies-continuation-p76-90]] (pages 76–90).
- **Next bounded page:** [[systems-performance-ch2-methodologies-continuation-p106-120]] (pages 106–120).

## Section outline

1. **Software USE, RED, interpretation, controls** — mutex/pool/FD examples; RED triplet; tenant caps. (`systems-performance-chapter-2-methodologies-continuation-chunk-0023`)
2. **Workload characterization; drill-down** — who/why/what/how; monitor → identify → analyze; Netflix three-tool stack. (`systems-performance-chapter-2-methodologies-continuation-chunk-0024`)
3. **Five Whys; latency analysis; Method R; tracing** — MySQL bisection; tcpdump/biosnoop; queue-tail outliers. (`systems-performance-chapter-2-methodologies-continuation-chunk-0025`)
4. **Baselines; static tuning; cache; micro-benchmarks** — capture normal; config audit; cache steps; iperf. (`systems-performance-chapter-2-methodologies-continuation-chunk-0026`)
5. **Mantras; §2.6** — mantra ordering; knees; Amdahl/USL; Kendall + M/D/1 + Little. (`systems-performance-chapter-2-methodologies-continuation-chunk-0027`, `systems-performance-chapter-2-methodologies-continuation-chunk-0028`)

## Extracted source memory

### Software USE, RED, interpretation, tenant limits

USE extends to **software resources** (mutex hold vs wait queue; thread pool busy vs backlog; process/thread and FD caps with allocation failures as errors). **Heuristics:** 100% utilization usually needs saturation checked; >60% can hide bursts or non-preemptible devices; non-zero saturation or rising errors merit work; “all low” still **narrows** scope. **Tenant caps** mirror USE (usage vs cap; saturation via throttling or errors). **RED** adds **rate, errors, duration** per service—complements machine-side USE; steady rate + rising duration → **architecture**; both rise → **load**. **Chunk:** `systems-performance-chapter-2-methodologies-continuation-chunk-0023`

### Workload characterization and drill-down methodology

**Workload characterization** answers who/why/what/how-load-changes (DoS surprise example). Outcomes: remove unnecessary work or **throttle** via controls. **Drill-down:** monitor → identify → analyze (exporters/GUIs vs CLI; deep tools strace/perf/BCC/bpftrace/Ftrace). Example stack Atlas → perfdash → FlameCommander/SSH. **Chunk:** `systems-performance-chapter-2-methodologies-continuation-chunk-0024`

### Five Whys, latency analysis, Method R, event tracing

**Five Whys** chains questions during drill-down. **Latency analysis** bisects time toward a leaf; **Method R** formalizes DB query latency from trace events (portable pattern). **Tracing** shows discrete events (tcpdump, biosnoop columns); timestamps expose latency; **outliers** may be queue-tail artifacts. **Chunk:** `systems-performance-chapter-2-methodologies-continuation-chunk-0025`

### Baselines, static tuning, cache tuning, micro-benchmarking

**Baselines** snapshot “normal” when charts are thin (watch tool overhead); boot summaries are coarse. **Static tuning** checks config at rest (speeds, RAID, FS space, debug modes, routing mistakes). **Cache tuning:** enable → ratios → size → tune cache or workload; avoid **double caching**. **Micro-benchmarks** isolate syscalls, cached reads, TCP throughput vs macro tests. **Chunk:** `systems-performance-chapter-2-methodologies-continuation-chunk-0026`

### Performance mantras and §2.6 modeling (Amdahl, USL, queueing)

**Mantras** rank “don’t do it” … “do concurrently” … “buy faster HW.” **§2.6** ties modeling to measurement/simulation; **knees** mark contention/coherence ceilings; enterprise vs cloud contrasts theory vs rented experiments; visual knees (eight threads / eight cores). **Amdahl/USL** add α seriality and β coherence; regression tooling sketched. **Queueing:** Kendall A/S/m, M/M/1 family, **M/D/1** disk curve (**60%** story), **Little's Law** L = λW. **Chunks:** `systems-performance-chapter-2-methodologies-continuation-chunk-0027`, `systems-performance-chapter-2-methodologies-continuation-chunk-0028`

## Decision-relevant ideas

- Treat **software resources** and **tenant caps** as first-class USE targets when the host looks healthy but apps stall. **Chunk:** `systems-performance-chapter-2-methodologies-continuation-chunk-0023`
- Pair **USE** (machine) with **RED** (service) so cardinality and user-visible duration stay jointly bounded. **Chunk:** `systems-performance-chapter-2-methodologies-continuation-chunk-0023`
- Use **workload characterization** before expensive redesign to catch unnecessary or hostile load; stage **monitor → identify → analyze** to match risk. **Chunk:** `systems-performance-chapter-2-methodologies-continuation-chunk-0024`
- Prefer **latency bisection** over averaging when tails drive SLOs; treat **outliers** as possible queue artifacts. **Chunk:** `systems-performance-chapter-2-methodologies-continuation-chunk-0025`
- Invest in **baselines** and **static audits** when dashboards are green but behavior regressed. **Chunk:** `systems-performance-chapter-2-methodologies-continuation-chunk-0026`
- Read **scalability charts** for knees before buying hardware; apply **M/D/1 disk intuition** when latency rises below 100% utilization. **Chunks:** `systems-performance-chapter-2-methodologies-continuation-chunk-0027`, `systems-performance-chapter-2-methodologies-continuation-chunk-0028`

## Candidate concepts

- red-method-service-health
- software-resource-use-extensions
- workload-characterization-input-model
- drill-down-monitoring-identification-analysis
- latency-analysis-binary-split
- baseline-statistics-vs-line-charts
- amdahl-and-universal-scalability-law
- queueing-md1-utilization-latency

## Candidate insights

- RED’s request-rate line answers load-vs-architecture before you profile code.
- A drill-down chain is only as honest as the stage-1 telemetry feeding it.
- Disk mean latency can look fine while M/D/1 math says p99 danger past moderate utilization.
- Performance mantras put “buy faster hardware” last on purpose—cheaper levers should exhaust first.

## Contradictions / caveats

- **Forward references only:** cache tuning points ahead to **Chapter 3** for a full cache list—cross-reference, not Chapter 3 body in this slice. **Chunk:** `systems-performance-chapter-2-methodologies-continuation-chunk-0026`
- **Running headers:** `Chapter 2}}Methodologies` and footer page numbers are **layout noise** in chunk `text`. **Chunks:** `systems-performance-chapter-2-methodologies-continuation-chunk-0023`–`systems-performance-chapter-2-methodologies-continuation-chunk-0028`
- **Named deployments and products** in examples (e.g. Netflix stack, Atlas, Prometheus/Grafana mentions) are **illustrations**, not portable concepts—strip the pattern from the brand. **Chunks:** `systems-performance-chapter-2-methodologies-continuation-chunk-0023`, `systems-performance-chapter-2-methodologies-continuation-chunk-0024`, `systems-performance-chapter-2-methodologies-continuation-chunk-0027`

## Provenance

- **processed_id:** `systems-performance-processed-001` — `processed/systems-performance/manifest.json` (`slice_id` **chapter-2-methodologies-continuation-p91-105**)
- **raw_id:** `systems-performance-raw-001` — `raw/systems-performance/Systems.Performance.Enterprise.and.the.Cloud.pdf`
- **Chunk JSON (this page):** `systems-performance-chapter-2-methodologies-continuation-chunk-0023` … `systems-performance-chapter-2-methodologies-continuation-chunk-0028` under `processed/systems-performance/chunks/`
- **Page range (this slice):** 91–105 — **section_range:** `chapter-2-methodologies-continuation`
