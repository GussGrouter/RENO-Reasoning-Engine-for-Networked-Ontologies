---
id: systems-performance-ch2-methodologies-p60-75
type: source
status: active
phase: phase-2-source-built
parent: systems-performance-hub
prev: systems-performance-ch1-case-studies-references-p56-59
next: systems-performance-ch2-methodologies-continuation-p76-90
source_id: systems-performance
raw_id: systems-performance-raw-001
processed_ids: ["systems-performance-processed-001"]
chunk_ids: ["systems-performance-chapter-2-methodologies-chunk-0010", "systems-performance-chapter-2-methodologies-chunk-0011", "systems-performance-chapter-2-methodologies-chunk-0012", "systems-performance-chapter-2-methodologies-chunk-0013", "systems-performance-chapter-2-methodologies-chunk-0014", "systems-performance-chapter-2-methodologies-chunk-0015", "systems-performance-chapter-2-methodologies-chunk-0016"]
title: "Systems Performance Chapter 2 — Methodologies (pages 60-75)"
source_kind: book-section
section_range: chapter-2-methodologies
---

# Systems Performance Chapter 2 — Methodologies (pages 60-75)

## Source scope

- **Source:** Systems Performance: Enterprise and the Cloud, Second Edition (Brendan Gregg); **pages 60–75**, `section_range` **chapter-2-methodologies**, `source_kind` **book-section**.
- **Chunk span:** `systems-performance-chapter-2-methodologies-chunk-0010` … `systems-performance-chapter-2-methodologies-chunk-0016` (linear chain; `slice_id` **chapter-2-methodologies-p60-75** in `manifest.json`).
- **Scope of slice:** **Background** thread through **§2.1** terminology, **§2.2** simple models (SUT, queueing), and deep **§2.3 Concepts** (latency, time scales, trade-offs, tuning depth, when to stop, load vs architecture, scalability, metrics, utilization, saturation, profiling, caching)—the **final chunk cuts off inside §2.3.14** (caching, cold/warm), not at chapter end.

## Graph navigation

- **Hub:** [[systems-performance]]
- **Previous bounded page:** [[systems-performance-ch1-case-studies-references-p56-59]] (pages 56–59).
- **Next bounded page:** [[systems-performance-ch2-methodologies-continuation-p76-90]] (Chapter 2 Methodologies continuation, pages 76–90).

## Section outline

1. **Ch.2 open; objectives; three parts; §2.1 terminology; §2.2** SUT and queueing figures. (`systems-performance-chapter-2-methodologies-chunk-0010`)
2. **§2.3.1–2.3.2** Latency semantics; Table 2.1 time units; Table 2.2 scaled latencies; trade-off “pick two” figure. (`systems-performance-chapter-2-methodologies-chunk-0011`)
3. **§2.3.3–2.3.5** Project and tuning trade-offs; tuning closest to the work (Table 2.3); level of appropriateness / ROI; Ch.1 callback. (`systems-performance-chapter-2-methodologies-chunk-0012`)
4. **§2.3.6–2.3.8** When to stop; point-in-time tunables; load vs architecture (Figure 2.5). (`systems-performance-chapter-2-methodologies-chunk-0013`)
5. **§2.3.9–2.3.11** Scalability knee; metrics types; observer effect; time-based **U = B/T** utilization. (`systems-performance-chapter-2-methodologies-chunk-0014`)
6. **§2.3.12–2.3.14 (partial)** Saturation; profiling; caching, hit ratio, **Figure 2.9**; miss rate; **MRU/LRU**; **cold** cache—text **ends mid-subsection**. (`systems-performance-chapter-2-methodologies-chunk-0015`, `systems-performance-chapter-2-methodologies-chunk-0016`)

## Extracted source memory

### Chapter frame: durable theory, then terminology and models

The chapter is positioned as **methodology and background** (terms, models, statistics, visualizations) before later implementation chapters. **Learning objectives** include **latency, utilization, saturation**, time scale intuition, **tuning trade-offs** and when to stop, **workload vs architecture**, and named methodologies (e.g. **USE**, **workload characterization**). The chapter’s **three parts** are **Background**, **Methodology**, and **Metrics**. **§2.1** defines **IOPS, throughput, response time, latency, utilization, saturation, bottleneck, workload**, etc. **§2.2** introduces **SUT** with a warning about **perturbations** and **multi-hop** systems; **queueing** models disks and links forward to **Section 2.6** modeling. **Chunk:** `systems-performance-chapter-2-methodologies-chunk-0010`

### Latency, time scales, and commensurate comparison

**§2.3.1** separates **wait** vs **service** and stresses **qualifying** the word *latency*; converting diverse work to **time** makes comparisons and speedup reasoning feasible where raw **IOPS** alone does not. **§2.3.2** uses **Table 2.1** (units) and **Table 2.2** (events from CPU cycle to long reboot) with a **scaled** metaphor to build intuition. A **good/fast/cheap** trade-off figure reframes **on-time, inexpensive, performant** for IT. **Chunk:** `systems-performance-chapter-2-methodologies-chunk-0011`

### Trade-offs, where to tune, and “how deep is enough”

**§2.3.3** gives CPU/memory and buffer-size examples. **§2.3.4** argues **largest wins** are often at the **application** layer, while **observation** may still be best from the **OS**; rapid deploy cadence can make **OS-level** analysis easy to skip but still valuable for app issues. **§2.3.5** ties **level of appropriateness** to **ROI** and org size, with extreme **latency** environments justifying **major** spend (e.g. trans-Atlantic **cable** cost vs **ms**). **Chunk:** `systems-performance-chapter-2-methodologies-chunk-0012`

### Stopping rules, moving targets, load vs structure

**§2.3.6** uses a **teaching** anecdote: stopping when the **bulk** of a problem is explained, when **ROI < cost**, or when **bigger ROI** exists elsewhere. **§2.3.7** warns **recommendations** are **point-in-time**; **Internet** tunables are like **borrowed medicine**; **VCS** history for changes is recommended. **§2.3.8** contrasts **load** (queueing under capacity) with **architecture** (single-thread, lock **contention**). **Chunk:** `systems-performance-chapter-2-methodologies-chunk-0013`

### Scalability curve, metrics cost, utilization definition start

**§2.3.9** describes **knee** / **contention** / **coherency** and **context-switch** overhead after peak. **§2.3.10** lists common **metric types** and warns **overhead** (**observer effect**) and **buggy** metrics. **§2.3.11** starts **utilization** with **time-based** **B/T** and **iostat** **%b**. **Chunk:** `systems-performance-chapter-2-methodologies-chunk-0014`

### Capacity vs time utilization, saturation, caching metrics

**Elevator** analogy: **100% busy ≠ 100% capacity**. **§2.3.12** defines **saturation** vs **100%** capacity. **§2.3.13** **profiling** as **sampling**. **§2.3.14** **hit ratio** **nonlinearity** (**Figure 2.9**), **miss rate/s**, **runtime** formula, **MRU/LRU**/**LFU** policies, begins **hot/cold/warm**—**incomplete in this chunk**. **Chunks:** `systems-performance-chapter-2-methodologies-chunk-0015`, `systems-performance-chapter-2-methodologies-chunk-0016`

## Decision-relevant ideas

- **SUT mapping** before micro-optimization: **perturbations** and **invisible** neighbors (e.g. **cloud** tenants) can dominate measurements. **Chunk:** `systems-performance-chapter-2-methodologies-chunk-0010`
- **Stop rules are economic:** “explain the bulk,” **ROI floor**, and **global priority** are explicit **halting** logic, not a fixed checklist depth. **Chunk:** `systems-performance-chapter-2-methodologies-chunk-0013`
- **Two utilizations:** **time busy** vs **capacity delivered**—mixing them causes **100%** busy systems that still **accept** work. **Chunks:** `systems-performance-chapter-2-methodologies-chunk-0014`, `systems-performance-chapter-2-methodologies-chunk-0015`

## Candidate concepts

- methodologies-and-durable-theory
- system-under-test-perturbation
- latency-as-common-currency
- tuning-proximity-to-work
- load-versus-architecture
- utilization-time-and-capacity
- scalability-knee-and-contention
- cache-hit-ratio-and-miss-rate

## Candidate insights

- Methodology is the missing layer between **metric definitions** and **constrained investigation** under time pressure.
- Expressing work as **time** (latency) often outranks raw **count** metrics when **contexts** differ.
- **Appropriate depth** follows **ROI** and **user experience**, not a single “correct” level of analysis.
- This promoted slice is **intra-section**: Chapter 2 continues after page 75 in later Phase 1 work.

## Contradictions / caveats

- **Running headers:** e.g. `Chapter 2}}Methodologies` in chunk `text` is **layout** noise from extraction, not a second title. **Chunks:** `systems-performance-chapter-2-methodologies-chunk-0010`–`systems-performance-chapter-2-methodologies-chunk-0016`
- **End state:** the book continues **§2.3.14** and beyond after **`systems-performance-chapter-2-methodologies-chunk-0016`**; do not treat p.75 as the end of **Methodologies** or of **§2.3**. **Chunk:** `systems-performance-chapter-2-methodologies-chunk-0016`

## Provenance

- **processed_id:** `systems-performance-processed-001` — `processed/systems-performance/manifest.json` (`slice_id` **chapter-2-methodologies-p60-75**)
- **raw_id:** `systems-performance-raw-001` — `raw/systems-performance/Systems.Performance.Enterprise.and.the.Cloud.pdf`
- **Chunk JSON (this page):** `systems-performance-chapter-2-methodologies-chunk-0010` through `…-chunk-0016` under `processed/systems-performance/chunks/`
- **Page range (this slice):** 60–75 — **section_range:** `chapter-2-methodologies`
