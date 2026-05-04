---
id: systems-performance-ch3-operating-systems-continuation-p158-167
type: source
status: active
phase: phase-2-source-built
parent: systems-performance-hub
prev: systems-performance-ch3-operating-systems-continuation-p143-157
next: systems-performance-ch4-observability-tools-p168-182
source_id: systems-performance
raw_id: systems-performance-raw-001
processed_ids: ["systems-performance-processed-001"]
chunk_ids: ["systems-performance-chapter-3-operating-systems-continuation-chunk-0049", "systems-performance-chapter-3-operating-systems-continuation-chunk-0050", "systems-performance-chapter-3-operating-systems-continuation-chunk-0051", "systems-performance-chapter-3-operating-systems-continuation-chunk-0052"]
title: "Systems Performance Chapter 3 — Operating Systems continuation (pages 158-167)"
source_kind: book-section
section_range: chapter-3-operating-systems-continuation
---

# Systems Performance Chapter 3 — Operating Systems continuation (pages 158-167)

## Source scope

- **Source:** Systems Performance: Enterprise and the Cloud, Second Edition (Brendan Gregg); bounded slice **pages 158–167**, `section_range` **chapter-3-operating-systems-continuation**, `source_kind` **book-section**.
- **Chunk span:** `systems-performance-chapter-3-operating-systems-continuation-chunk-0049` … `systems-performance-chapter-3-operating-systems-continuation-chunk-0052` (linear chain; `slice_id` **chapter-3-operating-systems-continuation-p158-167** in `manifest.json`).
- **Boundary constraint:** This bounded page **must not** include Chapter 4 material; Chapter 3 ends at **PDF page 167** and Chapter 4 starts at **PDF page 168** (confirmed by Phase 1 slice repair; this slice stops at 167 by design). **Chunks:** `systems-performance-chapter-3-operating-systems-continuation-chunk-0051`, `systems-performance-chapter-3-operating-systems-continuation-chunk-0052`

## Graph navigation

- **Hub:** [[systems-performance]]
- **Previous bounded page:** [[systems-performance-ch3-operating-systems-continuation-p143-157]] (pages 143–157).
- **Next bounded page:** [[systems-performance-ch4-observability-tools-p168-182]] (pages 168–182).

## Section outline

1. **Linux developments (part 2)** — continues the Linux performance feature list (I/O schedulers, PCID, PSI, io_uring, etc.). (`systems-performance-chapter-3-operating-systems-continuation-chunk-0049`)
2. **Linux topics in detail: systemd + KPTI + extended BPF** — boot-time critical path analysis, syscall/TLB costs, BPF architecture and uses. (`systems-performance-chapter-3-operating-systems-continuation-chunk-0049`)
3. **Other kernel topics** — PGO/FDO, unikernels, micro/hybrid kernels, distributed OS. (`systems-performance-chapter-3-operating-systems-continuation-chunk-0050`)
4. **Kernel comparisons + exercises + references/reading** — benchmarking caveats, Linux vs others, chapter exercises and long reference list. (`systems-performance-chapter-3-operating-systems-continuation-chunk-0051`, `systems-performance-chapter-3-operating-systems-continuation-chunk-0052`)

## Extracted source memory

### Linux kernel developments list continues: performance is accumulation across subsystems

Continues listing kernel changes that affect performance work: multiqueue I/O schedulers (BFQ/Kyber), kernel TLS, zerocopy send, PCID (to reduce TLB flush costs under KPTI), PSI (stall metrics), EDT send scheduling, io_uring, various network improvements, and broader “many small improvements” framing. **Chunk:** `systems-performance-chapter-3-operating-systems-continuation-chunk-0049`

### systemd: boot-time performance as a dependency critical path

Uses `systemd-analyze` and `critical-chain` output as a methodology for diagnosing boot-time latency by identifying the critical path and slowest services. Frames boot tuning as a performance task where dependency-aware timing data gives a concrete “where to tune next.” **Chunk:** `systems-performance-chapter-3-operating-systems-continuation-chunk-0049`

### KPTI (Meltdown): security mitigations can change syscall/context-switch costs materially

Describes KPTI as a mitigation that increases overhead (extra cycles, TLB flushing) especially for syscall-heavy workloads; PCID support can reduce some TLB flushes. Mentions empirical impact range (workload-dependent) and mitigation/tuning ideas (huge pages; tracing syscalls to reduce rate), noting many tracing tools are implemented with extended BPF. **Chunk:** `systems-performance-chapter-3-operating-systems-continuation-chunk-0049`

### Extended BPF: programmable kernel event handling with verifier-enforced safety

Summarizes modern BPF: verifier safety checks, type info via BTF, output via perf ring buffer or maps, and attachment to kernel/user event sources (tracepoints, kprobes/uprobes, perf events, etc.). Positions BPF as key to modern performance tooling and includes examples like timing I/O and building histograms. **Chunk:** `systems-performance-chapter-3-operating-systems-continuation-chunk-0050`

### Other topics: PGO kernels, unikernels, micro/hybrid, distributed OS

Summarizes PGO/FDO as production-profile-driven kernel compilation to improve a workload’s performance; notes LTO and vendor experience claims. Covers unikernels as “small image” performance/security trade-offs with debugging/tooling constraints. Reviews microkernels/hybrid kernels trade-off (IPC overhead vs modularity/fault tolerance; hybrid moves critical services into kernel space). Mentions distributed OSes and notes limited adoption. **Chunk:** `systems-performance-chapter-3-operating-systems-continuation-chunk-0050`

### Kernel comparisons: microbenchmarks are error-prone; tuning and workload fit dominate

Discusses that “fastest kernel” depends on configuration and workload; expects Linux to often win due to community/performance work but with exceptions (e.g., FreeBSD for Netflix CDN). Warns microbenchmark comparisons can mislead if the tested syscall/path doesn’t match production usage/flags; accurate comparison can take weeks and should follow benchmarking methodology. Notes Linux’s earlier tracer gap has been addressed by BPF-based tools, but complexity makes tuning laborious and many deployments are untuned. **Chunk:** `systems-performance-chapter-3-operating-systems-continuation-chunk-0051`

### End matter: exercises + references + additional reading

Provides exercises that probe terminology and conceptual understanding (process vs thread vs task; mode vs context switches; paging vs swapping; VFS role; reasons a thread leaves a CPU), and then an extensive bibliography plus additional reading list. This slice ends with Chapter 3 supplemental reading entries at PDF page 167, with no Chapter 4 text included. **Chunk:** `systems-performance-chapter-3-operating-systems-continuation-chunk-0052`

## Decision-relevant ideas

- **Boot latency is a dependency critical path problem**; measure the critical chain before “optimizing randomly.” **Chunk:** `systems-performance-chapter-3-operating-systems-continuation-chunk-0049`
- **Security mitigations can shift performance fundamentals** (syscall/context-switch costs), so “regressions” may be policy changes; PCID/huge pages and syscall-rate reductions become levers. **Chunk:** `systems-performance-chapter-3-operating-systems-continuation-chunk-0049`
- **BPF is a tooling substrate**: it turns kernel events into programmable measurements (timers, histograms) with safety constraints (verifier). **Chunk:** `systems-performance-chapter-3-operating-systems-continuation-chunk-0050`
- **Kernel comparison needs workload realism and tuning parity**; microbenchmarks alone are unreliable. **Chunk:** `systems-performance-chapter-3-operating-systems-continuation-chunk-0051`

## Candidate concepts

- systemd-critical-chain-boot-latency
- kpti-syscall-overhead-tlb-flush
- pcid-reduces-tlb-flush
- bpf-verifier-and-attachment-points
- pgo-kernel-workload-specific
- unikernel-debuggability-tradeoff
- microkernel-ipc-overhead-vs-modularity
- kernel-microbenchmark-mismatch-risk

## Candidate insights

- When a “syscall-heavy workload” regresses after a kernel update, explicitly check for security mitigations (KPTI-like) and TLB behavior before blaming application code paths. **Chunk:** `systems-performance-chapter-3-operating-systems-continuation-chunk-0049`
- If you can’t add tools to the environment (unikernel-like constraints), you must push observability into the platform/host layer; otherwise you’ll be blind in production. **Chunk:** `systems-performance-chapter-3-operating-systems-continuation-chunk-0050`

## Contradictions / caveats

- **Chapter boundary enforcement:** This slice is constrained to **pages 158–167**; Chapter 4 starts at **page 168** and must not appear here. **Chunks:** `systems-performance-chapter-3-operating-systems-continuation-chunk-0051`, `systems-performance-chapter-3-operating-systems-continuation-chunk-0052`
- **Running headers / parser noise:** `Chapter 3}}Operating Systems` persists in-line. **Chunk:** `systems-performance-chapter-3-operating-systems-continuation-chunk-0051`

## Provenance

- **processed_id:** `systems-performance-processed-001` — `processed/systems-performance/manifest.json` (`slice_id` **chapter-3-operating-systems-continuation-p158-167**)
- **raw_id:** `systems-performance-raw-001` — `raw/systems-performance/Systems.Performance.Enterprise.and.the.Cloud.pdf`
- **Chunk JSON (this page):** `systems-performance-chapter-3-operating-systems-continuation-chunk-0049`, `systems-performance-chapter-3-operating-systems-continuation-chunk-0050`, `systems-performance-chapter-3-operating-systems-continuation-chunk-0051`, `systems-performance-chapter-3-operating-systems-continuation-chunk-0052` under `processed/systems-performance/chunks/`
- **Page range (this slice):** 158–167 — **section_range:** `chapter-3-operating-systems-continuation`
