---
id: systems-performance-ch3-operating-systems-continuation-p143-157
type: source
status: active
phase: phase-2-source-built
parent: systems-performance-hub
prev: systems-performance-ch3-operating-systems-p128-142
next: systems-performance-ch3-operating-systems-continuation-p158-167
source_id: systems-performance
raw_id: systems-performance-raw-001
processed_ids: ["systems-performance-processed-001"]
chunk_ids: ["systems-performance-chapter-3-operating-systems-continuation-chunk-0042", "systems-performance-chapter-3-operating-systems-continuation-chunk-0043", "systems-performance-chapter-3-operating-systems-continuation-chunk-0044", "systems-performance-chapter-3-operating-systems-continuation-chunk-0045", "systems-performance-chapter-3-operating-systems-continuation-chunk-0046", "systems-performance-chapter-3-operating-systems-continuation-chunk-0047", "systems-performance-chapter-3-operating-systems-continuation-chunk-0048"]
title: "Systems Performance Chapter 3 — Operating Systems continuation (pages 143-157)"
source_kind: book-section
section_range: chapter-3-operating-systems-continuation
---

# Systems Performance Chapter 3 — Operating Systems continuation (pages 143-157)

## Source scope

- **Source:** Systems Performance: Enterprise and the Cloud, Second Edition (Brendan Gregg); bounded slice **pages 143–157**, `section_range` **chapter-3-operating-systems-continuation**, `source_kind` **book-section**.
- **Chunk span:** `systems-performance-chapter-3-operating-systems-continuation-chunk-0042` … `systems-performance-chapter-3-operating-systems-continuation-chunk-0048` (linear chain; `slice_id` **chapter-3-operating-systems-continuation-p143-157** in `manifest.json`).
- **Narrative role:** Finishes late **§3.2 Background** (VM, schedulers, FS, caching, networking, drivers, preemption/resource controls) and begins **§3.3 Kernels** through early Linux history and a long list of Linux performance-relevant developments.

## Graph navigation

- **Hub:** [[systems-performance]]
- **Previous bounded page:** [[systems-performance-ch3-operating-systems-p128-142]] (pages 128–142).
- **Next bounded page:** [[systems-performance-ch3-operating-systems-continuation-p158-167]] (pages 158–167; Chapter 3 ends at PDF page 167).

## Section outline

1. **Virtual memory + scheduler + file systems** — oversubscription, paging vs swapping; CPU- vs I/O-bound; POSIX namespace, mounting. (`systems-performance-chapter-3-operating-systems-continuation-chunk-0042`)
2. **VFS, I/O stack, caching, networking, drivers** — VFS abstraction, cache layers, TCP/IP stack, device driver models. (`systems-performance-chapter-3-operating-systems-continuation-chunk-0043`)
3. **Multiprocessor + preemption + resource controls + observability bridge** — SMP/NUMA, IPIs, preemption modes, cgroups; observability positioned as Chapter 4 topic. (`systems-performance-chapter-3-operating-systems-continuation-chunk-0044`)
4. **Kernels background: Unix → BSD** — Unix philosophy (minimal decisions), kernel growth; BSD’s paged VM, demand paging, FFS, sockets, etc. (`systems-performance-chapter-3-operating-systems-continuation-chunk-0045`)
5. **Solaris + Linux origins + Linux kernel developments list (part 1)** — Solaris features (VFS, slab, DTrace, ZFS, zones); Linux ancestry; developments through kernel 5.8 era; extended BPF called out. (`systems-performance-chapter-3-operating-systems-continuation-chunk-0046`, `systems-performance-chapter-3-operating-systems-continuation-chunk-0047`, `systems-performance-chapter-3-operating-systems-continuation-chunk-0048`)

## Extracted source memory

### Virtual memory: oversubscription plus “what moves” matters (paging vs swapping terminology)

Virtual memory is a per-process/private address-space abstraction that supports multitasking and (practically) “infinite” memory by mapping between RAM and secondary storage. Two schemes are contrasted: process swapping (move whole processes) vs paging (move fixed-size pages). The text notes Linux uses “swapping” to mean paging and does not implement the older whole-process swapping model. **Chunk:** `systems-performance-chapter-3-operating-systems-continuation-chunk-0042`

### Schedulers: decide who runs, where they run, and why “interactive” tends to win

Schedulers map runnable entities (threads/tasks) to CPUs, tracking ready-to-run work and priorities. The text contrasts CPU-bound vs I/O-bound workloads and describes the classic policy of de-prioritizing CPU-bound work to favor I/O-bound/interactive latency, using recent CPU time vs elapsed time as an input (shorter jobs/interactive work run sooner). Mentions multiple scheduling classes/policies (including real-time scheduling plus preemption for low-latency/predictable systems). **Chunk:** `systems-performance-chapter-3-operating-systems-continuation-chunk-0042`

### File systems and namespace: why mounting is a performance-relevant boundary

File systems provide a POSIX file/dir interface and are joined into a global namespace via mounting; different instances may live on different devices but appear uniform. Kernel mechanisms for isolation (chroot, mount namespaces for containers) are called out as ways to constrain the namespace view. **Chunk:** `systems-performance-chapter-3-operating-systems-continuation-chunk-0042`

### VFS and the I/O stack: an abstraction boundary that enables multiple FS types

VFS is described as a kernel interface that abstracts file-system types and makes it easier to add new FS implementations while presenting a consistent global namespace. The “I/O stack” is positioned as the user→kernel→device path; direct block-device access bypassing the file system is noted as sometimes used by admin tools and databases. **Chunk:** `systems-performance-chapter-3-operating-systems-continuation-chunk-0043`

### Caching layers: “disk is slow” drives a whole hierarchy of caches

Caching spans many layers (client/app/db/OS/FS/device), so “disk I/O” symptoms may be hits/misses and buffering effects at multiple points, not just the physical device. **Chunk:** `systems-performance-chapter-3-operating-systems-continuation-chunk-0043`

### Networking + drivers: kernel protocol stacks and device drivers evolve with hardware/protocol change

Kernels provide a TCP/IP stack with sockets as endpoints; new options/hardware often require kernel/driver support. Drivers may be loadable; devices expose character vs block interfaces (with Linux caching folded into the page cache). **Chunks:** `systems-performance-chapter-3-operating-systems-continuation-chunk-0043`, `systems-performance-chapter-3-operating-systems-continuation-chunk-0044`

### Multiprocessor + preemption + resource controls: performance is coordination + isolation

Multiprocessor systems add SMP/NUMA complexity; CPUs coordinate via IPIs (e.g., for coherence/translation changes). Preemption options are described (fully preemptible vs voluntary), with Linux config modes called out. Resource controls evolve from basics (nice/ulimit) to Linux cgroups and cgroup v2, positioning these as mechanisms to manage multi-tenant performance. **Chunk:** `systems-performance-chapter-3-operating-systems-continuation-chunk-0044`

### Kernel evolution: “small kernel” philosophy vs feature growth (Unix → BSD → Solaris → Linux)

Unix’s philosophy is framed as “kernel makes few decisions,” but kernels grew for paging, networking, multiple file systems, and performance competition. BSD and Solaris are summarized as major sources of VM/FS/networking and observability primitives; Linux is presented as a 1991-era synthesis that now dominates servers/cloud. **Chunks:** `systems-performance-chapter-3-operating-systems-continuation-chunk-0045`, `systems-performance-chapter-3-operating-systems-continuation-chunk-0046`

### Linux kernel developments (partial list): performance is a long sequence of primitives

Provides a long, versioned list of Linux performance-relevant primitives across scheduling, I/O, tracing/profiling, networking, synchronization, and isolation (notably including perf/tracepoints and extended BPF). **Chunks:** `systems-performance-chapter-3-operating-systems-continuation-chunk-0046`, `systems-performance-chapter-3-operating-systems-continuation-chunk-0047`, `systems-performance-chapter-3-operating-systems-continuation-chunk-0048`

## Decision-relevant ideas

- **Paging vs swapping vocabulary is kernel-specific**; don’t assume “swap” implies whole-process swapping on Linux. **Chunk:** `systems-performance-chapter-3-operating-systems-continuation-chunk-0042`
- **Scheduling preference is an intentional policy choice**: prioritizing interactive/I/O-bound latency can reshape observed tail latency under load. **Chunk:** `systems-performance-chapter-3-operating-systems-continuation-chunk-0042`
- **VFS is a diagnostic boundary**: it’s where “POSIX file operations” meet “this specific FS implementation.” **Chunk:** `systems-performance-chapter-3-operating-systems-continuation-chunk-0043`
- **Cache layers imply ambiguous “where time went”**; misses/hits can happen at many layers, not just the disk. **Chunk:** `systems-performance-chapter-3-operating-systems-continuation-chunk-0043`
- **Preemption and cgroups are configuration choices** that can trade throughput for latency predictability and isolation. **Chunk:** `systems-performance-chapter-3-operating-systems-continuation-chunk-0044`

## Candidate concepts

- paging-vs-swapping-linux-terminology
- scheduler-policy-cpu-bound-vs-io-bound
- vfs-as-filesystem-abstraction
- io-stack-direct-block-bypass
- caching-layer-hierarchy
- preemption-modes-and-latency

## Candidate insights

- If a workload’s latency profile changes with “small OS config knobs,” check whether you altered scheduler policy, preemption mode, or cgroup constraints before searching for application regressions. **Chunk:** `systems-performance-chapter-3-operating-systems-continuation-chunk-0044`

## Contradictions / caveats

- **Running headers / parser noise:** `Chapter 3}}Operating Systems` appears in-line. **Chunks:** `systems-performance-chapter-3-operating-systems-continuation-chunk-0042`, `systems-performance-chapter-3-operating-systems-continuation-chunk-0043`
- **Forward references:** Mentions of later chapters (FS, Disks, Network, Cloud, Observability) are navigation; they don’t imply those chapters are ingested here. **Chunks:** `systems-performance-chapter-3-operating-systems-continuation-chunk-0042`, `systems-performance-chapter-3-operating-systems-continuation-chunk-0043`, `systems-performance-chapter-3-operating-systems-continuation-chunk-0044`

## Provenance

- **processed_id:** `systems-performance-processed-001` — `processed/systems-performance/manifest.json` (`slice_id` **chapter-3-operating-systems-continuation-p143-157**)
- **raw_id:** `systems-performance-raw-001` — `raw/systems-performance/Systems.Performance.Enterprise.and.the.Cloud.pdf`
- **Chunk JSON (this page):** `systems-performance-chapter-3-operating-systems-continuation-chunk-0042`, `systems-performance-chapter-3-operating-systems-continuation-chunk-0043`, `systems-performance-chapter-3-operating-systems-continuation-chunk-0044`, `systems-performance-chapter-3-operating-systems-continuation-chunk-0045`, `systems-performance-chapter-3-operating-systems-continuation-chunk-0046`, `systems-performance-chapter-3-operating-systems-continuation-chunk-0047`, `systems-performance-chapter-3-operating-systems-continuation-chunk-0048` under `processed/systems-performance/chunks/`
- **Page range (this slice):** 143–157 — **section_range:** `chapter-3-operating-systems-continuation`
