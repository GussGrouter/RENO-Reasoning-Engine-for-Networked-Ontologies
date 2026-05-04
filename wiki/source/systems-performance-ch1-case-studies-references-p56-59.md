---
id: systems-performance-ch1-case-studies-references-p56-59
type: source
status: active
phase: phase-2-source-built
parent: systems-performance-hub
prev: systems-performance-ch1-introduction-p40-55
next: systems-performance-ch2-methodologies-p60-75
source_id: systems-performance
raw_id: systems-performance-raw-001
processed_ids: ["systems-performance-processed-001"]
chunk_ids: ["systems-performance-chapter-1-case-studies-and-references-chunk-0008", "systems-performance-chapter-1-case-studies-and-references-chunk-0009"]
title: "Systems Performance Chapter 1 — Case studies and references (pages 56-59)"
source_kind: book-section
section_range: chapter-1-case-studies-and-references
---

# Systems Performance Chapter 1 — Case studies and references (pages 56-59)

## Source scope

- **Source:** Systems Performance: Enterprise and the Cloud, Second Edition (Brendan Gregg); bounded slice **pages 56–59**, `section_range` **chapter-1-case-studies-and-references**, `source_kind` **book-section**.
- **Chunk span:** `systems-performance-chapter-1-case-studies-and-references-chunk-0008` (56–57) and `systems-performance-chapter-1-case-studies-and-references-chunk-0009` (58–59); `slice_id` in manifest: **chapter-1-case-studies-and-references-p56-59**.
- **Content:** Concludes **§1.11** (Slow Disks, Software Change) and **§1.12** references, plus a short **More Reading** forward pointer—still Chapter 1, not the Chapter 2 body.

## Graph navigation

- **Hub:** [[systems-performance]]
- **Previous bounded page:** [[systems-performance-ch1-introduction-p40-55]] (pages 40–55).
- **Next bounded page:** [[systems-performance-ch2-methodologies-p60-75]] (Chapter 2 Methodologies, pages 60–75).

## Section outline

1. **1.11 (cont.) — Slow Disks (Sumit):** iostat, off-CPU / BPF, workload characterization, `cachestat`, memory vs file-system cache, resolution. (`systems-performance-chapter-1-case-studies-and-references-chunk-0008`)
2. **1.11.2 — Software Change (Pamela):** non-regression / stress path, 700 r/s ceiling, then fixed-rate resource characterization and CPU regression; limiter is single-threaded client. (`systems-performance-chapter-1-case-studies-and-references-chunk-0008`, `systems-performance-chapter-1-case-studies-and-references-chunk-0009`)
3. **1.11.3 More Reading, 1.12 References:** points to Ch.16 case study; bibliography entries. (`systems-performance-chapter-1-case-studies-and-references-chunk-0009`)

## Extracted source memory

### Slow Disks: evidence and root cause (Sumit)

He refines one-minute **AcmeMon** with one-second `iostat`, sees saturation and high latency, and uses `offcputime` to show the DB blocks on file-system read during queries—enough to treat disk I/O as on the request path. Workload stats support high **load**, not “bad disks.” A colleague’s fragmentation theory fails at 30% full; the memorable finding is a **file-system cache** hit ratio that looks good in isolation (91%) but is worse than **peer servers** (~98%+) and tied to a **prototype app** **growing** memory, shrinking room for the **page cache** and turning more reads into disk—resolved when the app is **moved off** the server. Footnotes point ahead to **drill-down** in Ch.2 and `cachestat` in Ch.8. **Chunk:** `systems-performance-chapter-1-case-studies-and-references-chunk-0008`

### Software Change: non-regression, scaling ceiling, and limiter (Pamela)

She stress-tests by ramping request rate, hits an **~700/s** **throughput** plateau with **idle** server, repeats on new build—same ceiling—then **fixed 700/s** and compares **CPU%** to show a real **regression** (higher CPU at same load). Pushing from multiple clients **saturates** the server; throughput splits **3500** vs **2300** r/s, consistent with CPU. **Thread-state analysis** shows the **client workload generator** is **single-threaded** and 100% on-CPU: the **bottleneck** of the *test* setup. She **profiles** the new build (CPU flame graph) and files a bug on the **single-threaded** generator. A footnote is content-only: *“covered in Chapter 2, Methodologies…”* (cross-reference, not the start of Ch.2 in this PDF). **Chunks:** `systems-performance-chapter-1-case-studies-and-references-chunk-0008`, `systems-performance-chapter-1-case-studies-and-references-chunk-0009`

### Closing and references

**§1.11.3** defers a deep case study to **Chapter 16** and points to the **methodologies** chapter next. **§1.12** is a **reference list** (papers, blog, books). **Chunk:** `systems-performance-chapter-1-case-studies-and-references-chunk-0009`

## Decision-relevant ideas

- **When “disk is slow” is a proxy:** one-second metrics and off-CPU analysis can reframe a ticket from hardware blame to **cache pressure** and **memory** competition on the same host. **Chunk:** `systems-performance-chapter-1-case-studies-and-references-chunk-0008`
- **Non-regression vs the real limiter:** same ceiling under stress can miss a **regression** until you fix **load** and **compare resource** at a controlled rate; the **workload driver** can dominate before the server does. **Chunks:** `systems-performance-chapter-1-case-studies-and-references-chunk-0008`, `systems-performance-chapter-1-case-studies-and-references-chunk-0009`
- **Peer baselines for cache health:** a “high” **hit ratio** without **historical** or **peer** context can hide a regression in **cacheable working set** vs **available** cache. **Chunk:** `systems-performance-chapter-1-case-studies-and-references-chunk-0008`

## Candidate concepts

- file-system-cache-versus-workload-memory
- off-cpu-bpf-triage
- non-regression-and-stress-ceilings
- client-generator-as-bottleneck
- fixed-rate-resource-regression-compare
- reference-list-provenance

## Candidate insights

- A minute-granular dashboard can mis-time diagnosis; sub-minute tooling exists for a reason when saturation fluctuates.
- The component under test includes the *load* path: a single-threaded client can cap scalability before the server’s logic does.
- Cross-chapter footnotes in case studies are navigation, not a substitute for reading the promoted slice’s own `text` field.

## Contradictions / caveats

- **Cross-reference, not Ch.2 body:** the phrase “Chapter 2, Methodologies” appears in a **footnote** about drill-down; this slice still ends before the PDF’s Chapter 2 opening page. **Chunk:** `systems-performance-chapter-1-case-studies-and-references-chunk-0008`
- **Parser artifact:** `Chapter 1}}Introduction` in running headers in chunk `text` is layout noise. **Chunk:** `systems-performance-chapter-1-case-studies-and-references-chunk-0008` (and same pattern in `…-0009`).

## Provenance

- **processed_id:** `systems-performance-processed-001` — `processed/systems-performance/manifest.json` (`slice_id` **chapter-1-case-studies-and-references-p56-59**)
- **raw_id:** `systems-performance-raw-001` — `raw/systems-performance/Systems.Performance.Enterprise.and.the.Cloud.pdf`
- **Chunk JSON (this page):** `systems-performance-chapter-1-case-studies-and-references-chunk-0008`, `…-chunk-0009` under `processed/systems-performance/chunks/`
- **Page range (this slice):** 56–59 — **section_range:** `chapter-1-case-studies-and-references`
