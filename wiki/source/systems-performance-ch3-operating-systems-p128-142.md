---
id: systems-performance-ch3-operating-systems-p128-142
type: source
status: active
phase: phase-2-source-built
parent: systems-performance-hub
prev: systems-performance-ch2-methodologies-tail-p121-126
next: systems-performance-ch3-operating-systems-continuation-p143-157
source_id: systems-performance
raw_id: systems-performance-raw-001
processed_ids: ["systems-performance-processed-001"]
chunk_ids: ["systems-performance-chapter-3-operating-systems-chunk-0036", "systems-performance-chapter-3-operating-systems-chunk-0037", "systems-performance-chapter-3-operating-systems-chunk-0038", "systems-performance-chapter-3-operating-systems-chunk-0039", "systems-performance-chapter-3-operating-systems-chunk-0040", "systems-performance-chapter-3-operating-systems-chunk-0041"]
title: "Systems Performance Chapter 3 — Operating Systems (pages 128-142)"
source_kind: book-section
section_range: chapter-3-operating-systems
---

# Systems Performance Chapter 3 — Operating Systems (pages 128-142)

## Source scope

- **Source:** Systems Performance: Enterprise and the Cloud, Second Edition (Brendan Gregg); bounded slice **pages 128–142**, `section_range` **chapter-3-operating-systems**, `source_kind` **book-section**.
- **Chunk span:** `systems-performance-chapter-3-operating-systems-chunk-0036` … `systems-performance-chapter-3-operating-systems-chunk-0041` (linear chain; `slice_id` **chapter-3-operating-systems-p128-142** in `manifest.json`).
- **Narrative role:** Chapter 3 opener plus early **§3.1 Terminology** and **§3.2 Background** through system calls, interrupts, clock/idle, processes, and stacks—foundation for later performance chapters.

## Graph navigation

- **Hub:** [[systems-performance]]
- **Previous bounded page:** [[systems-performance-ch2-methodologies-tail-p121-126]] (pages 121–126).
- **Next bounded page:** [[systems-performance-ch3-operating-systems-continuation-p143-157]] (pages 143–157).

## Section outline

1. **Chapter 3 opener + §3.1 terminology** — kernel/user space, mode/context switch, syscall/trap, process/thread/task, virtual memory. (`systems-performance-chapter-3-operating-systems-chunk-0036`)
2. **Kernel model + execution** — kernel models (monolithic/micro/hybrid/unikernel), BPF as kernel-mode apps, kernel executes on syscalls/interrupts. (`systems-performance-chapter-3-operating-systems-chunk-0037`)
3. **Kernel/user modes + syscalls** — mode vs context switches; syscall list; overhead-avoidance patterns (vDSO, mmap, bypass, kernel-mode apps). (`systems-performance-chapter-3-operating-systems-chunk-0037`, `systems-performance-chapter-3-operating-systems-chunk-0038`)
4. **Interrupts + clock/idle** — async vs sync interrupts, ISR top/bottom halves, interrupt masking/latency, tickless kernels, idle thread. (`systems-performance-chapter-3-operating-systems-chunk-0038`, `systems-performance-chapter-3-operating-systems-chunk-0039`)
5. **Processes + stacks** — fork/exec/COW, process life cycle, process environment, stack traces, user+kernel stacks during syscalls. (`systems-performance-chapter-3-operating-systems-chunk-0040`, `systems-performance-chapter-3-operating-systems-chunk-0041`)

## Extracted source memory

### Why OS internals matter for performance work

The chapter frames OS/kernel knowledge as required to form and test performance hypotheses: syscall paths, scheduler behavior, memory pressure, and how file systems process I/O. **Chunk:** `systems-performance-chapter-3-operating-systems-chunk-0036`

### Terminology: name the boundary and the switches correctly

Defines key terms used throughout the book: operating system vs kernel, process/thread/task, kernel space vs user space (and “user land”), context switch vs mode switch, syscall/trap, plus related primitives like interrupts and (extended) BPF programs. **Chunk:** `systems-performance-chapter-3-operating-systems-chunk-0036`

### Kernel models and where the kernel actually runs

Explains kernel models (monolithic, microkernel, unikernel, hybrid) and that the kernel runs mostly on demand (syscalls and device interrupts), with lightweight asynchronous housekeeping threads. Extended BPF is introduced as a way to run secure kernel-mode programs with helper APIs, effectively adding a kernel-mode application model. **Chunks:** `systems-performance-chapter-3-operating-systems-chunk-0037`, `systems-performance-chapter-3-operating-systems-chunk-0036`

### Syscalls, modes, and overhead: why interfaces stay minimal and how systems avoid switching costs

User programs run in user mode and invoke privileged operations through syscalls, switching to kernel mode; blocking syscalls may also lead to context switches. Overhead motivates avoidance mechanisms: vDSO user-mode syscalls, memory mappings, kernel bypass, and in-kernel apps (with extended BPF positioned as a modern example). The text emphasizes that syscalls are simple, documented interfaces; richer APIs are built in user-land libraries. **Chunks:** `systems-performance-chapter-3-operating-systems-chunk-0037`, `systems-performance-chapter-3-operating-systems-chunk-0038`

### System calls as a practical toolkit: what some “misc” calls are for

Highlights syscalls whose usage is less obvious: `ioctl(2)` as a multiplexed control mechanism; `mmap(2)` for mapping libraries/executables and sometimes allocation strategies; `brk(2)` heap growth via allocators; `futex(2)` as the blocking part of user-space locks. Uses perf as a concrete example: privileged actions exposed via `perf_event_open(2)` + `ioctl` control. **Chunk:** `systems-performance-chapter-3-operating-systems-chunk-0038`

### Interrupts and time: latency sources that happen “around” your workload

Interrupts are described as asynchronous (hardware IRQs) and synchronous (software traps/exceptions/faults). Linux driver handling is modeled as fast top halves that may schedule deferred work in bottom halves (tasklets/workqueues), and long interrupt-disabled regions are linked to latency risk. The clock/tick model is framed as historically periodic (ticks) with latency/overhead trade-offs; modern kernels push toward tickless behavior for efficiency and less jitter, and idle threads may halt CPUs until interrupts arrive. **Chunks:** `systems-performance-chapter-3-operating-systems-chunk-0038`, `systems-performance-chapter-3-operating-systems-chunk-0039`

### Processes and stacks: the “who is running” and “why is it running” evidence

Processes are environments with address spaces, file descriptors, and threads; Linux uses `fork/clone` + `exec` and may use copy-on-write to defer copying. Process states (on-proc, runnable, sleep, zombie) explain where time can be spent. Stack traces are introduced as a core evidence tool: they expose the call path through source code, and syscalls involve both user and kernel stacks (kernel stacks may differ by purpose, including IRQ stacks). **Chunks:** `systems-performance-chapter-3-operating-systems-chunk-0040`, `systems-performance-chapter-3-operating-systems-chunk-0041`

## Decision-relevant ideas

- **If performance depends on kernel activity, reason in terms of triggers**: syscalls and interrupts are “why the kernel is running now.” **Chunk:** `systems-performance-chapter-3-operating-systems-chunk-0037`
- **Separate mode switches from context switches** when you reason about overhead; blocking syscalls can induce both. **Chunk:** `systems-performance-chapter-3-operating-systems-chunk-0037`
- **Interrupt-disabled time is a latency lever**; long top halves and masked interrupts can delay wakeups and service. **Chunk:** `systems-performance-chapter-3-operating-systems-chunk-0039`
- **Tick/timer configuration can manifest as jitter and timer latency**; “tickless” aims to reduce overhead and perturbations. **Chunk:** `systems-performance-chapter-3-operating-systems-chunk-0039`
- **Stacks are performance evidence**: they answer “why is this executing?” across kernel/user code paths. **Chunk:** `systems-performance-chapter-3-operating-systems-chunk-0040`

## Candidate concepts

- kernel-mode-vs-user-mode
- mode-switch-vs-context-switch
- syscall-interface-minimalism
- interrupt-latency-and-masking
- tickless-kernel-and-jitter
- stack-trace-as-execution-cause

## Candidate insights

- A “compute-bound” workload can still be kernel-limited when contention and placement decisions dominate; don’t assume “user-mode” means “kernel irrelevant.” (grounded in scheduler discussion around contention/placement) **Chunk:** `systems-performance-chapter-3-operating-systems-chunk-0037`
- When you see latency spikes, ask whether they can be explained by interrupt disabled time or tick behavior before blaming the application. **Chunk:** `systems-performance-chapter-3-operating-systems-chunk-0039`

## Contradictions / caveats

- **Running headers / parser noise:** `Chapter 3}}Operating Systems` appears in-line and should not be treated as content. **Chunks:** `systems-performance-chapter-3-operating-systems-chunk-0036`, `systems-performance-chapter-3-operating-systems-chunk-0037`
- **Cross-chapter pointers:** Mentions of later chapters/tools (e.g., Ftrace, Memory, CPUs) are navigation, not evidence those sections are ingested here. **Chunks:** `systems-performance-chapter-3-operating-systems-chunk-0038`, `systems-performance-chapter-3-operating-systems-chunk-0039`, `systems-performance-chapter-3-operating-systems-chunk-0040`

## Provenance

- **processed_id:** `systems-performance-processed-001` — `processed/systems-performance/manifest.json` (`slice_id` **chapter-3-operating-systems-p128-142**)
- **raw_id:** `systems-performance-raw-001` — `raw/systems-performance/Systems.Performance.Enterprise.and.the.Cloud.pdf`
- **Chunk JSON (this page):** `systems-performance-chapter-3-operating-systems-chunk-0036`, `systems-performance-chapter-3-operating-systems-chunk-0037`, `systems-performance-chapter-3-operating-systems-chunk-0038`, `systems-performance-chapter-3-operating-systems-chunk-0039`, `systems-performance-chapter-3-operating-systems-chunk-0040`, `systems-performance-chapter-3-operating-systems-chunk-0041` under `processed/systems-performance/chunks/`
- **Page range (this slice):** 128–142 — **section_range:** `chapter-3-operating-systems`
