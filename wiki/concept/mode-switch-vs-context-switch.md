---
id: mode-switch-vs-context-switch
type: concept
status: draft
phase: phase-3-reasoned
parent: null
prev: null
next: null
title: "Mode switch vs context switch"
---

# Mode switch vs context switch

## Definition

Two distinct kinds of CPU transition that are routinely conflated and have different costs:

- **Mode switch** — the CPU changes privilege level (user → kernel or back), usually triggered by a system call, trap, or interrupt. The currently running thread keeps its register state and CPU; only the privilege level (and on some processor architectures the address-space context) changes. Cost: small, but non-zero — and meaningfully larger when kernel page-table isolation forces extra TLB work.
- **Context switch** — the CPU swaps one runnable thread for another. The previous thread's registers and stack pointer are saved, scheduler bookkeeping runs, and a different thread is loaded. Cost: larger — cache-warmth and TLB locality are routinely lost in addition to the bookkeeping itself.

A blocking system call typically does **both** in sequence: a mode switch into the kernel, then a context switch to a different runnable thread while the original blocks. Treating the two as one indivisible "syscall cost" obscures where the time actually went.

## Use when

- Reasoning about syscall-heavy workloads — batch I/O, lots of small `read`/`write`, polling loops — where the unit cost matters and avoidance patterns (vDSO, `mmap`, kernel bypass, batching, ring-buffered async I/O) are on the table.
- Interpreting microbenchmark numbers — "syscall is 200 ns" usually means a non-blocking mode-switch path; blocking calls add scheduling cost on top and are not comparable.
- Diagnosing regressions after a kernel upgrade or security mitigation: KPTI-class fixes raise mode-switch cost noticeably; context-switch cost is comparatively stable.
- Designing async / event-driven architectures where the goal is to amortize switching cost across many requests rather than pay it once per request.
- Reading flame graphs or `perf` output that mixes user-mode time, kernel-mode time, and off-CPU wait — the three correspond, roughly, to no switch, one mode switch, and a full context switch respectively.

## Do not use when

- The bottleneck is clearly *inside* the kernel or *inside* user code; the switching distinction is irrelevant when the work itself dominates.
- The system has very low syscall and context-switch rates — at low rates, switching cost is negligible against per-request work, and chasing it is a streetlight move.
- For correctness-driven choices (e.g., choosing blocking vs non-blocking I/O for semantic reasons rather than performance); use the right primitive first, optimise switching cost second.
- Comparing across kernels or hardware where switching costs are not directly comparable; report the workload, mitigation status, and CPU model alongside any number.

## Related concepts

- [[latency-as-common-currency]] — both switches are paid in time; expressing them in nanoseconds makes them comparable and budgetable.
- [[use-method]] — context-switch *saturation* (long run-queues, high `csw`) is a USE-side signal; mode-switch *rate* shows up in syscall counters per CPU.
- [[load-versus-architecture]] — workloads that pay one mode switch per byte are architecture-bound by API design; batching is a structural change, not a tuning knob.
- [[scheduler-policy-shapes-latency]] — context-switch cadence is a scheduler-policy outcome; mode switches are mostly policy-independent.
- [[stack-trace-as-execution-cause]] — kernel stacks distinguish syscall-serviced kernel time from interrupt-serviced kernel time; both pay mode-switch cost but they tell different stories.

## Source support

- [[systems-performance-ch3-operating-systems-p128-142]] — § 3.1 defines mode switch and context switch as separate terms; § 3.2.2 states explicitly that all syscalls mode-switch but only blocking ones context-switch, and lists overhead-avoidance patterns (vDSO, `mmap`, kernel bypass, in-kernel apps).
- [[systems-performance-ch3-operating-systems-continuation-p158-167]] — § 3.4.3 KPTI: security mitigations raise mode-switch cost (extra cycles, TLB flushes); PCID can offset some of it.
