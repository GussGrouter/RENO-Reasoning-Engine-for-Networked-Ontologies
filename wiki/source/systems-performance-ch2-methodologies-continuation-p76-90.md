---
id: systems-performance-ch2-methodologies-continuation-p76-90
type: source
status: active
phase: phase-2-source-built
parent: systems-performance-hub
prev: systems-performance-ch2-methodologies-p60-75
next: systems-performance-ch2-methodologies-continuation-p91-105
source_id: systems-performance
raw_id: systems-performance-raw-001
processed_ids: ["systems-performance-processed-001"]
chunk_ids: ["systems-performance-chapter-2-methodologies-continuation-chunk-0017", "systems-performance-chapter-2-methodologies-continuation-chunk-0018", "systems-performance-chapter-2-methodologies-continuation-chunk-0019", "systems-performance-chapter-2-methodologies-continuation-chunk-0020", "systems-performance-chapter-2-methodologies-continuation-chunk-0021", "systems-performance-chapter-2-methodologies-continuation-chunk-0022"]
title: "Systems Performance Chapter 2 — Methodologies continuation (pages 76-90)"
source_kind: book-section
section_range: chapter-2-methodologies-continuation
---

# Systems Performance Chapter 2 — Methodologies continuation (pages 76-90)

## Source scope

- **Source:** Systems Performance: Enterprise and the Cloud, Second Edition (Brendan Gregg); **pages 76–90**, `section_range` **chapter-2-methodologies-continuation**, `source_kind` **book-section**.
- **Chunk span:** `systems-performance-chapter-2-methodologies-continuation-chunk-0017` … `systems-performance-chapter-2-methodologies-continuation-chunk-0022`; `slice_id` **chapter-2-methodologies-continuation-p76-90** in `manifest.json`.
- **Narrative role:** Continues immediately after [[systems-performance-ch2-methodologies-p60-75]], whose last promoted chunk ended mid-**§2.3.14** (caching): here **warm/hot/warmth** cache states, **§2.3.15 known-unknowns**, **§2.4** resource vs workload perspectives, then the **§2.5** methodology catalog, anti-methods, **problem statement**, **scientific method** / **diagnosis cycle**, **tools method**, **USE method** (through metric tables **2.6** / **2.7** on page 90)—still **inside Chapter 2**, not Chapter 3.

## Graph navigation

- **Hub:** [[systems-performance]]
- **Previous bounded page:** [[systems-performance-ch2-methodologies-p60-75]] (pages 60–75).
- **Next bounded page:** [[systems-performance-ch2-methodologies-continuation-p91-105]] (pages 91–105).

## Section outline

1. **Cache warmth; §2.3.15; §2.4** perspectives, resource vs workload stacks, metrics emphasis. (`systems-performance-chapter-2-methodologies-continuation-chunk-0017`)
2. **§2.5** opens: methodology **Table 2.4** / **2.5**; **streetlight**, **random change** anti-methods. (`systems-performance-chapter-2-methodologies-continuation-chunk-0018`)
3. **Blame-else**, **ad hoc checklist**, **problem statement** questions, **scientific method** start. (`systems-performance-chapter-2-methodologies-continuation-chunk-0019`)
4. **Scientific** examples (obs/exp), **diagnosis cycle**, **tools method** limits vs streetlight. (`systems-performance-chapter-2-methodologies-continuation-chunk-0020`)
5. **USE method** definition, **errors first**, burst utilization vs averages, **resource list**, block diagram. (`systems-performance-chapter-2-methodologies-continuation-chunk-0021`)
6. **USE metrics** tables **2.6**–**2.7**, **known-unknowns** in the checklist, pointer to **Appendix A** Linux checklist. (`systems-performance-chapter-2-methodologies-continuation-chunk-0022`)

## Extracted source memory

### Cache warmth and epistemic framing (§2.3.15, §2.4)

**Warm/hot/warmth** completes the cache-state vocabulary; large or slow backing tiers mean **long warm-up** (worked example: **DRAM + flash + disk**, **random read** throughput math yielding **multi-hour** warm paths). **§2.3.15** maps **known-knowns / known-unknowns / unknown-unknowns** to performance work—the field grows **known-unknowns** as you learn. **§2.4** splits **resource** vs **workload** analysis (Figures **2.10–2.11**): admins vs app owners; resource side stresses **IOPS, throughput, utilization, saturation**; workload side stresses **requests, latency, completion/errors**, with **latency** as the headline app metric and drill-down through app → libs → kernel. **Chunk:** `systems-performance-chapter-2-methodologies-continuation-chunk-0017`

### §2.5 catalog and weak methodologies

**§2.5** frames methodology as **where to start** in complex stacks; **Table 2.4** enumerates sections (**USE**, **RED**, **workload characterization**, **drill-down**, **Method R**, **tracing**, **static tuning**, etc.) and **Table 2.5** points to **later-chapter** variants. Narrative recommends **problem statement first** after comparing weak patterns: **streetlight** (familiar tools only), **random change** (tune/measure loop without theory), **blame-someone-else** (hypothesis without data—countered by asking for **screenshots** and second opinions). **Chunks:** `systems-performance-chapter-2-methodologies-continuation-chunk-0018`, `systems-performance-chapter-2-methodologies-continuation-chunk-0019`

### Structured methods: checklist, questions, science, tools

**Ad hoc checklist** gives fast **iostat**-style checks but is **point-in-time** and needs **refresh**. **Problem statement** lists **six** discovery questions (symptom, regression, change, latency framing, blast radius, environment)—sometimes enough **without** logging in. **Scientific method** and **diagnosis cycle** tie **hypothesis ↔ data**; examples rule out **file system** for slow DB, confirm **datacenter move** for HTTP latency, and use a **negative test** (shrinking record size) before **drill-down** on cache paths. **Tools method** inverts to **tool-first** checklists and risks **unknown unknowns** (no custom tracing). **Chunk:** `systems-performance-chapter-2-methodologies-continuation-chunk-0020`

### USE method: resources, order, expressiveness, checklist

**USE** = per-resource **utilization, saturation, errors**; **capacity-type** memory vs **time-busy** CPUs cross-referenced to **§2.3.11**; **errors** matter for **retry** paths. Iteration is **resource-first** (not tool-first), surfacing **known-unknowns** when metrics missing. Procedure: **errors → saturation → utilization**; first hit may not be **the** bottleneck—iterate. **Burst** **100%** can hide inside **five-minute** averages (**tollbooth** analogy). **Resource list** spans **CPU, memory, NIC, storage, accelerators, controllers, interconnects**; some parts are **multi-role** (disk as **I/O + capacity**). **Caches** may be skipped for USE vs bottleneck focus. **Functional block diagram** (Figure **2.13**) guides flow hunting. **Chunks:** `systems-performance-chapter-2-methodologies-continuation-chunk-0021`, `systems-performance-chapter-2-methodologies-continuation-chunk-0022`

## Decision-relevant ideas

- **Perspective choice:** resource metrics vs workload **latency** answer different questions; doc that over-rotates on **vmstat/iostat** alone is one **lens**, not the whole system. **Chunk:** `systems-performance-chapter-2-methodologies-continuation-chunk-0017`
- **Method hygiene:** **problem statement** and **hypothesis-led** steps reduce **streetlight** and **blame-else** waste; **tools method** needs explicit **coverage** gaps for dynamic tracing. **Chunks:** `systems-performance-chapter-2-methodologies-continuation-chunk-0018`, `systems-performance-chapter-2-methodologies-continuation-chunk-0019`, `systems-performance-chapter-2-methodologies-continuation-chunk-0020`
- **USE as triage:** **errors first**, then **saturation**, then **utilization**; treat **~30-metric** checklists as **known-unknown** inventories—start with **easy** high-signal rows. **Chunks:** `systems-performance-chapter-2-methodologies-continuation-chunk-0021`, `systems-performance-chapter-2-methodologies-continuation-chunk-0022`

## Candidate concepts

- cache-warmth-and-warm-up-time
- known-knowns-unknowns-performance
- resource-analysis-vs-workload-analysis
- streetlight-random-change-anti-methods
- problem-statement-first-response
- scientific-method-and-diagnosis-cycle
- use-method-triage-order
- use-metric-checklist-known-unknowns

## Candidate insights

- Warm-up is a **capacity × rate** problem: big caches plus slow fills make “empty cache” a long-lived incident state.
- The USE checklist is deliberately **resource-complete** before **tool shopping**, converting silent blind spots into explicit **known-unknowns**.
- Short **utilization spikes** can saturate while long-window averages look healthy—SLO design must match **sensor interval** to **symptom interval**.
- This bounded page ends mid-**§2.5** methodology material (tables **2.7** onward still in-flight in the book).

## Contradictions / caveats

- **Running headers:** `Chapter 2}}Methodologies` remains **parser/layout noise** alongside real section headers. **Chunks:** `systems-performance-chapter-2-methodologies-continuation-chunk-0017`–`systems-performance-chapter-2-methodologies-continuation-chunk-0022`
- **Slice boundary:** Page **90** stops during **USE** metric enumeration and **advanced Table 2.7**; the next Phase 1 slice should continue **§2.5** / later **§2.6+** as promoted. **Chunk:** `systems-performance-chapter-2-methodologies-continuation-chunk-0022`

## Provenance

- **processed_id:** `systems-performance-processed-001` — `processed/systems-performance/manifest.json` (`slice_id` **chapter-2-methodologies-continuation-p76-90**)
- **raw_id:** `systems-performance-raw-001` — `raw/systems-performance/Systems.Performance.Enterprise.and.the.Cloud.pdf`
- **Chunk JSON (this page):** `systems-performance-chapter-2-methodologies-continuation-chunk-0017` … `systems-performance-chapter-2-methodologies-continuation-chunk-0022` under `processed/systems-performance/chunks/`
- **Page range (this slice):** 76–90 — **section_range:** `chapter-2-methodologies-continuation`
