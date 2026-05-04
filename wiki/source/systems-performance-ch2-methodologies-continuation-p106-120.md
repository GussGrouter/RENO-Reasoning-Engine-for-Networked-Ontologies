---
id: systems-performance-ch2-methodologies-continuation-p106-120
type: source
status: active
phase: phase-2-source-built
parent: systems-performance-hub
prev: systems-performance-ch2-methodologies-continuation-p91-105
next: systems-performance-ch2-methodologies-tail-p121-126
source_id: systems-performance
raw_id: systems-performance-raw-001
processed_ids: ["systems-performance-processed-001"]
chunk_ids: ["systems-performance-chapter-2-methodologies-continuation-chunk-0029", "systems-performance-chapter-2-methodologies-continuation-chunk-0030", "systems-performance-chapter-2-methodologies-continuation-chunk-0031", "systems-performance-chapter-2-methodologies-continuation-chunk-0032", "systems-performance-chapter-2-methodologies-continuation-chunk-0033"]
title: "Systems Performance Chapter 2 — Methodologies continuation (pages 106-120)"
source_kind: book-section
section_range: chapter-2-methodologies-continuation
---

# Systems Performance Chapter 2 — Methodologies continuation (pages 106-120)

## Source scope

- **Source:** Systems Performance: Enterprise and the Cloud, Second Edition (Brendan Gregg); bounded slice **pages 106–120**, `section_range` **chapter-2-methodologies-continuation**, `source_kind` **book-section**.
- **Chunk span:** `systems-performance-chapter-2-methodologies-continuation-chunk-0029` … `systems-performance-chapter-2-methodologies-continuation-chunk-0033`; `slice_id` **chapter-2-methodologies-continuation-p106-120** in `manifest.json`.
- **Narrative role:** Finishes **§2.6** queueing (Kendall notation, M/D/1 “60%” latency story, R plotting), introduces **§2.7 capacity planning** (resource limits extrapolation, factor analysis, horizontal/vertical scaling, ASG/HPA/sharding), then **§2.8 statistics** (quantifying gains, means, geometric/harmonic means, averages-over-time and decayed averages, percentiles/SLA language), **§2.9 monitoring** (time-based patterns, products/agents, summary-since-boot), and opens **§2.10 visualizations** (line, scatter). **Chapter 3** (p128+) is **outside** this slice.

## Graph navigation

- **Hub:** [[systems-performance]]
- **Previous bounded page:** [[systems-performance-ch2-methodologies-continuation-p91-105]] (pages 91–105).
- **Next bounded page:** [[systems-performance-ch2-methodologies-tail-p121-126]] (pages 121–126).

## Section outline

1. **§2.6 queueing** — questions queues answer; Kendall A/S/m; M/M/1, M/M/c, M/G/1, M/D/1; disk M/D/1 curve vs utilization; R plot snippet. (`systems-performance-chapter-2-methodologies-continuation-chunk-0029`)
2. **§2.7 capacity planning** — resource limits four-step model; peak vs average traffic; factor analysis ten-test strategy; load balancers, sharding, ASG/HPA examples. (`systems-performance-chapter-2-methodologies-continuation-chunk-0030`)
3. **§2.8 statistics** — observation vs experiment quantification; arithmetic/geometric/harmonic means; 5-minute average masking 100% CPU spikes; decayed averages; percentiles and SLAs. (`systems-performance-chapter-2-methodologies-continuation-chunk-0031`)
4. **§2.8 continued; §2.9 monitoring** — CV and multimodal distributions; monitoring time patterns; monitoring products; summary-since-boot. (`systems-performance-chapter-2-methodologies-continuation-chunk-0032`)
5. **§2.10 visualizations start** — line charts with median/p99; scatter plots for disk latency outliers. (`systems-performance-chapter-2-methodologies-continuation-chunk-0033`)

## Extracted source memory

### Queueing models and the M/D/1 disk lesson

Queueing answers capacity questions (mean response if load doubles, effect of extra CPU, tail SLOs under doubled load). Simple models use arrival process, service distribution, and service-center count (**Kendall** A/S/m). Examples: **M/M/1**, **M/M/c**, **M/G/1** (often disks), **M/D/1** deterministic disk service. The **M/D/1** graph shows mean response time doubling past ~**60%** utilization and tripling by 80%—different from preemptible CPUs—so “disk not 100%” can still be the app limiter. **Chunk:** `systems-performance-chapter-2-methodologies-continuation-chunk-0029`

### Capacity planning: limits, factors, scaling patterns

**Resource limits** method: measure request rate, resource use, express requests per resource, extrapolate to first 100% bottleneck (worked numeric web-server example). **Factor analysis** avoids factorial explosion by starting at max config, dropping one factor at a time, attributing performance and cost deltas, then re-testing the chosen config. **Scaling solutions:** vertical vs horizontal; cloud finer increments; **ASG**-style auto-scale on metrics; **Kubernetes HPA**; **database sharding** with key choice for even spread. **Chunk:** `systems-performance-chapter-2-methodologies-continuation-chunk-0030`

### Statistics for quantifying gains and reading averages

**Quantifying** uses reliable metrics—latency composes across components for “what-if” estimates; async work must not be mixed into synchronous request latency. **Experimentation** compares before/after when safe. **Means:** arithmetic default; **geometric** for multiplicative stack layers; **harmonic** for rates over unequal segments. **Averages over time** need explicit interval—**5-minute CPU average** hid **100%** second-level saturation. **Decayed averages** damp short noise (load average cited). **Percentiles** tie to **SLAs** for tail-aware health. **Chunk:** `systems-performance-chapter-2-methodologies-continuation-chunk-0031`

### Coefficient of variation, multimodal data, monitoring practice

**CV** and **z-score** contextualize variance vs mean. **Multimodal** latency (cache hit vs miss) makes a single **mean** misleading—the “average depth six inches” joke. **Outliers** (disk >1s when bulk is <10ms) may not move mean but break UX—histograms recommended. **Monitoring** records time series for growth, peaks, and “normal” envelopes; patterns include hourly, daily, weekly, quarterly, yearly cycles plus irregular spikes (releases, outages, sports finals). **Products** use agents/exporters; centralized views for large fleets. **Summary-since-boot** is fallback when no history. **Chunk:** `systems-performance-chapter-2-methodologies-continuation-chunk-0032`

### Visualization opening: line and scatter plots

**Visualizations** beat raw text for correlation and pattern volume. **Line charts** plot latency over time; adding **median**, **σ**, **percentiles** widens y-axis and reveals why mean was high (p99 >20ms while median ~1ms). **Scatter plots** plot every I/O as latency vs completion time, exposing **outliers** the mean hid. **Chunk:** `systems-performance-chapter-2-methodologies-continuation-chunk-0033`

## Decision-relevant ideas

- Use **queueing vocabulary** when arguing disk vs CPU saturation—same utilization number means different queue discipline. **Chunk:** `systems-performance-chapter-2-methodologies-continuation-chunk-0029`
- Treat **60% disk utilization** as a planning conversation starter, not a universal constant—model family and variance matter. **Chunk:** `systems-performance-chapter-2-methodologies-continuation-chunk-0029`
- **Resource-limit extrapolation** turns one (throughput, utilization) observation into a first bottleneck forecast—then validate with multi-point monitoring. **Chunk:** `systems-performance-chapter-2-methodologies-continuation-chunk-0030`
- **Factor analysis** trades exhaustive combinatorics for disciplined single-factor drops when buying storage clusters. **Chunk:** `systems-performance-chapter-2-methodologies-continuation-chunk-0030`
- When **mean latency** looks acceptable, demand **distribution shape** (percentiles, multimodality) before signing off. **Chunks:** `systems-performance-chapter-2-methodologies-continuation-chunk-0031`, `systems-performance-chapter-2-methodologies-continuation-chunk-0032`
- Match **metric interval** to **symptom interval**—long averages are summaries, not proofs of absence of saturation. **Chunk:** `systems-performance-chapter-2-methodologies-continuation-chunk-0031`
- Prefer **layered charts** (mean + tail lines) before escalating hardware on dashboard “green.” **Chunk:** `systems-performance-chapter-2-methodologies-continuation-chunk-0033`

## Candidate concepts

- kendall-notation-queueing-models
- md1-disk-utilization-response-curve
- resource-limit-extrapolation
- factor-analysis-capacity-buying
- harmonic-mean-for-rate-averages
- multimodal-latency-and-misleading-means
- monitoring-time-series-patterns
- scatter-plot-for-latency-outliers

## Candidate insights

- A five-minute smooth CPU line can miss second-long 100% windows that dominate p99 latency.
- Multimodal latency turns the arithmetic mean into an anti-metric unless paired with percentiles.
- Queueing discipline explains why “disks at 70%” still owns your request tail.

## Contradictions / caveats

- **Chapter boundary:** text references **Chapter 5** applications, **Chapter 4** observability—forward pointers only; **no Chapter 3 OS body** appears in pages **106–120**. **Chunks:** `systems-performance-chapter-2-methodologies-continuation-chunk-0029`, `systems-performance-chapter-2-methodologies-continuation-chunk-0032`
- **Running headers** and page footers remain **parser noise**. **Chunks:** `systems-performance-chapter-2-methodologies-continuation-chunk-0029`–`systems-performance-chapter-2-methodologies-continuation-chunk-0033`
- **Named vendors** (Netflix Atlas scale, AWS ASG, Kubernetes) illustrate patterns—separate the **mechanism** from the **brand**. **Chunks:** `systems-performance-chapter-2-methodologies-continuation-chunk-0030`, `systems-performance-chapter-2-methodologies-continuation-chunk-0032`

## Provenance

- **processed_id:** `systems-performance-processed-001` — `processed/systems-performance/manifest.json` (`slice_id` **chapter-2-methodologies-continuation-p106-120**)
- **raw_id:** `systems-performance-raw-001` — `raw/systems-performance/Systems.Performance.Enterprise.and.the.Cloud.pdf`
- **Chunk JSON (this page):** `systems-performance-chapter-2-methodologies-continuation-chunk-0029` … `systems-performance-chapter-2-methodologies-continuation-chunk-0033` under `processed/systems-performance/chunks/`
- **Page range (this slice):** 106–120 — **section_range:** `chapter-2-methodologies-continuation`
