---
id: systems-performance-ch4-observability-tools-continuation-p183-197
type: source
status: active
phase: phase-2-source-built
parent: systems-performance-hub
prev: systems-performance-ch4-observability-tools-p168-182
next: systems-performance-ch4-observability-tools-tail-p198-209
source_id: systems-performance
raw_id: systems-performance-raw-001
processed_ids: ["systems-performance-processed-001"]
chunk_ids: ["systems-performance-chapter-4-observability-tools-continuation-chunk-0058", "systems-performance-chapter-4-observability-tools-continuation-chunk-0059", "systems-performance-chapter-4-observability-tools-continuation-chunk-0060", "systems-performance-chapter-4-observability-tools-continuation-chunk-0061", "systems-performance-chapter-4-observability-tools-continuation-chunk-0062"]
title: "Systems Performance Chapter 4 — Observability Tools continuation (pages 183-197)"
source_kind: book-section
section_range: chapter-4-observability-tools-continuation
---

# Systems Performance Chapter 4 — Observability Tools continuation (pages 183-197)

## Source scope

- **Source:** Systems Performance: Enterprise and the Cloud, Second Edition (Brendan Gregg); bounded slice **pages 183–197**, `section_range` **chapter-4-observability-tools-continuation**, `source_kind` **book-section**.
- **Chunk span:** `systems-performance-chapter-4-observability-tools-continuation-chunk-0058` … `systems-performance-chapter-4-observability-tools-continuation-chunk-0062` (linear chain; `slice_id` **chapter-4-observability-tools-continuation-p183-197** in `manifest.json`).
- **Narrative role:** continues Chapter 4’s observability source interfaces and event types, moving from `/sys` examples into delay accounting + netlink, then tracepoints/kprobes/uprobes/USDT, and ends with hardware counters (PMCs) and their constraints/caveats.

## Graph navigation

- **Hub:** [[systems-performance]]
- **Previous bounded page:** [[systems-performance-ch4-observability-tools-p168-182]] (pages 168–182).
- **Next bounded page:** [[systems-performance-ch4-observability-tools-tail-p198-209]] (pages 198–209).

## Source compression

This slice deepens the “observability sources” layer of Chapter 4 by treating interfaces as *APIs with tradeoffs*: file-backed stats (`/sys`) that expose large device/system inventories and state knobs; per-task delay accounting exposed via taskstats/netlink; and event sources for tracing with different stability/overhead properties (tracepoints vs kprobes vs uprobes vs USDT). It also adds “hardware observability” (PMCs) as a separate source family: powerful for microarchitectural efficiency but constrained by register scarcity, sampling accuracy issues (“skid”), and cloud availability.

Chunks: `systems-performance-chapter-4-observability-tools-continuation-chunk-0058`, `systems-performance-chapter-4-observability-tools-continuation-chunk-0059`, `systems-performance-chapter-4-observability-tools-continuation-chunk-0060`, `systems-performance-chapter-4-observability-tools-continuation-chunk-0061`, `systems-performance-chapter-4-observability-tools-continuation-chunk-0062`

## Key technical points

### `/sys`: structured kernel statistics and state

- `/sys/devices/...` exposes detailed per-device and per-topology attributes; the example enumerates CPU0 files and shows cache topology via `.../cache/index*/level` and `.../cache/index*/size`. **Chunk:** `systems-performance-chapter-4-observability-tools-continuation-chunk-0058`
- sysfs is both **read-only statistics** and **writeable state knobs** (example: CPU online/offline via writing `1`/`0` to `online`), reinforcing that “observability sources” also include control surfaces. **Chunk:** `systems-performance-chapter-4-observability-tools-continuation-chunk-0058`

### Delay accounting: time-in-state for tasks, sourced via taskstats/netlink

- With `CONFIG_TASK_DELAY_ACCT`, Linux tracks per-task time in scheduler latency (wait-on-CPU), block I/O wait, swapping, and memory reclaim; scheduler-latency delay accounting is sourced from `schedstats` but exposed alongside other states. **Chunk:** `systems-performance-chapter-4-observability-tools-continuation-chunk-0058`
- Retrieval is via **taskstats** (netlink). The slice points to kernel docs and a reference consumer (`tools/accounting/getdelays.c`) and shows example output with time units (ns unless stated) and interpretation (example taken from a CPU-loaded system suffering scheduler latency). **Chunk:** `systems-performance-chapter-4-observability-tools-continuation-chunk-0058`

### netlink: binary kernel interfaces for info + notifications

- netlink is described as an AF_NETLINK socket family using `send(2)` / `recv(2)` to exchange binary structs; more complex than `/proc` but more efficient and can provide notifications. **Chunk:** `systems-performance-chapter-4-observability-tools-continuation-chunk-0058`
- The `strace ss` example ties a tool (`ss(8)`) to `NETLINK_SOCK_DIAG`; several netlink groups are enumerated (route, socket diag, SELinux, audit, SCSI transport, crypto), and common consumers (`ip`, `ss`, etc.) are named. **Chunk:** `systems-performance-chapter-4-observability-tools-continuation-chunk-0058`

### Tracepoints: stable kernel event API, with format strings and two user interfaces

- Tracepoints are framed as static instrumentation points (stable API, limited in number) with coverage across syscall boundaries, scheduler, file systems, and disk I/O; availability can depend on kernel config. **Chunk:** `systems-performance-chapter-4-observability-tools-continuation-chunk-0058`
- The slice clarifies terminology: “tracepoints” in kernel source vs “trace events” generated via `TRACE_EVENT`, and notes inconsistent naming in tooling. **Chunk:** `systems-performance-chapter-4-observability-tools-continuation-chunk-0059`
- Each trace event has a **format string** under `.../tracing/events/.../format`, which defines arguments and print format; tools can filter (`perf trace --filter 'bytes > 65536'`) or print specific arguments (bpftrace `args->bytes`) from those definitions. **Chunk:** `systems-performance-chapter-4-observability-tools-continuation-chunk-0059`
- Two major interfaces are highlighted:
  - **tracefs** files (often under `/sys/kernel/debug/tracing`), shown by an `strace` example opening `events/.../enable`; includes an example of an external lock (`.ftrace-lock`) added by the tool due to tracefs concurrency limitations.
  - **perf_event_open(2)**, used by newer tooling and preferred where possible; shown by an `strace` example opening PERF_TYPE_TRACEPOINT events. **Chunk:** `systems-performance-chapter-4-observability-tools-continuation-chunk-0059`

## Tool/source taxonomy

- **Static state/statistics:** sysfs (`/sys`) for structured kernel statistics and state. **Chunk:** `systems-performance-chapter-4-observability-tools-continuation-chunk-0058`
- **Kernel-to-user binary interfaces:** netlink (AF_NETLINK) including taskstats. **Chunk:** `systems-performance-chapter-4-observability-tools-continuation-chunk-0058`
- **Tracing event sources (increasing “reach”, decreasing stability):**
  - **Tracepoints:** stable API with defined format/arguments. **Chunks:** `systems-performance-chapter-4-observability-tools-continuation-chunk-0058`, `systems-performance-chapter-4-observability-tools-continuation-chunk-0059`
  - **kprobes:** dynamic kernel instrumentation for “anything”, unstable API (raw kernel functions/args can change). **Chunk:** `systems-performance-chapter-4-observability-tools-continuation-chunk-0060`
  - **uprobes:** dynamic user-space instrumentation, unstable API with higher overhead. **Chunk:** `systems-performance-chapter-4-observability-tools-continuation-chunk-0061`
  - **USDT:** user-space static probes (stable/documented when present), implemented using uprobes; may require rebuild flags in packaged software; dynamic USDT exists for JIT/interpreted languages. **Chunk:** `systems-performance-chapter-4-observability-tools-continuation-chunk-0061`
- **Hardware observability:** performance monitoring counters (PMCs) accessed via perf_events. **Chunk:** `systems-performance-chapter-4-observability-tools-continuation-chunk-0062`

## Operational caveats

- **Event volume + overhead:** tracepoints add enabled overhead per event, plus tool post-processing and storage overhead; practical impact depends on event rate and CPU count (disk events often lower-rate than scheduler events). The slice gives order-of-magnitude guidance (negligible under ~10k/s; measurable over ~100k/s) and cites a measured minimum per-tracepoint CPU cost; raw tracepoints reduce argument-creation costs. **Chunk:** `systems-performance-chapter-4-observability-tools-continuation-chunk-0059`
- **Disabled overhead exists too:** even disabled tracepoints add small instruction/metadata footprint (e.g., NOPs and handlers increasing text size slightly), which matters when adding tracepoints to the kernel. **Chunk:** `systems-performance-chapter-4-observability-tools-continuation-chunk-0059`
- **Stability tradeoff:** kprobes/uprobes expose raw function boundaries and argument layouts that can change across versions; use as last-resort visibility when stable probes are absent. **Chunks:** `systems-performance-chapter-4-observability-tools-continuation-chunk-0060`, `systems-performance-chapter-4-observability-tools-continuation-chunk-0061`
- **Measurement skew:** duration measurement via return probes (kretprobes/uretprobes) can skew fast-function timing due to the probe/trampoline overhead; uretprobe overhead is called out as potentially significant. **Chunks:** `systems-performance-chapter-4-observability-tools-continuation-chunk-0060`, `systems-performance-chapter-4-observability-tools-continuation-chunk-0061`
- **PMC constraints:** few hardware counter registers force event selection or multiplexing; overflow sampling can misattribute instruction pointers due to interrupt latency (“skid”) and out-of-order execution; “precise events” (PEBS/IBS) address this for some events. **Chunk:** `systems-performance-chapter-4-observability-tools-continuation-chunk-0062`
- **Cloud availability:** PMCs may be disabled for guests; availability depends on hypervisor/provider (examples include Xen options and Nitro/bare-metal instances). **Chunk:** `systems-performance-chapter-4-observability-tools-continuation-chunk-0062`

## Chunk provenance

- **processed_id:** `systems-performance-processed-001` — `processed/systems-performance/manifest.json` (`slice_id` **chapter-4-observability-tools-continuation-p183-197**)
- **raw_id:** `systems-performance-raw-001` — `raw/systems-performance/Systems.Performance.Enterprise.and.the.Cloud.pdf`
- **Chunk JSON (this page):** `systems-performance-chapter-4-observability-tools-continuation-chunk-0058`, `systems-performance-chapter-4-observability-tools-continuation-chunk-0059`, `systems-performance-chapter-4-observability-tools-continuation-chunk-0060`, `systems-performance-chapter-4-observability-tools-continuation-chunk-0061`, `systems-performance-chapter-4-observability-tools-continuation-chunk-0062` under `processed/systems-performance/chunks/`
- **Page range (this slice):** 183–197 — **section_range:** `chapter-4-observability-tools-continuation`
