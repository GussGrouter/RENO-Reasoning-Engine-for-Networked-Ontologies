---
id: stack-trace-as-execution-cause
type: concept
status: draft
phase: phase-3-reasoned
parent: null
prev: null
next: null
title: "Stack trace as execution cause"
---

# Stack trace as execution cause

## Definition

A **stack trace** is the saved chain of return addresses across the active call frames of a thread, ordered leaf-to-root. Read top-down it answers *what is currently executing*; read bottom-up it answers *why this code is running right now*. The second reading is the decision-relevant one: a stack trace converts an opaque "the system is busy" symptom into a falsifiable hypothesis about which call path produced the work.

A stack is **evidence**, not just a debugging artefact. Profilers (sampling), tracers (per-event), and snapshots (off-CPU, lock contention, page-fault handlers) all emit stacks; aggregating them is the basis of flame graphs and similar reductions. During a system call a thread typically has *both* a user-level and a kernel-level stack, and high-quality observability tools can capture both halves so the cause chain crosses the kernel/user boundary cleanly.

The reusable property is that **for any "why is this CPU busy / blocked / waiting" question, the stack at that moment is the most direct answer the system can give you**, subject to whether stack walking is reliable on the platform (frame pointers, ORC, DWARF, last-branch records).

## Use when

- A profile shows hot CPU in an unfamiliar function — the stack tells you which application call path is responsible, not just the leaf.
- An off-CPU profile shows blocked time — the stack at the block point names the operation that paid the latency (file read, lock wait, blocking syscall).
- An incident dashboard shows a symptom (high latency, error spike) but not a cause — a stack-aware tracer scoped to the symptom interval converts "the box is hot" into "this code path is hot".
- Reviewing a performance fix — the proposed change should be reachable from the stacks that produced the symptom; if it is not, the fix and the symptom are unrelated.
- Cross-kernel-boundary investigations — a kernel stack alone or a user stack alone is half a story; combine them via tools that walk both.

## Do not use when

- The runtime cannot produce honest stacks (JIT without frame pointers, deeply inlined code without DWARF, certain managed runtimes) — invest in the unwinder before drawing conclusions; otherwise the leaf is right but the parent is fiction.
- The bottleneck is *between* CPU events — network round trips, queue waits, IPC latency — where a single stack does not span the cause; pair with timeline / waterfall reasoning.
- For purely statistical cardinality questions (request rate, error rate, distribution shape) — stacks add cost without changing the answer.
- When the stack is captured at the wrong moment — a stack sampled outside the symptom interval is just any-stack, not symptom-stack.

## Related concepts

- [[use-method]] — when USE flags a saturated resource, the stacks of threads waiting on that resource name the call paths consuming it.
- [[mode-switch-vs-context-switch]] — kernel stacks distinguish syscall-serviced work from interrupt-serviced work; both are kernel time but their stacks tell different stories.
- [[latency-as-common-currency]] — aggregating stack samples in time (flame graph height ≈ time on CPU) is the bridge between code paths and time budgets.
- [[performance-anti-methods]] — a stack captured without a problem statement is the streetlight pattern in disguise; the symptom defines which stack to capture.
- [[problem-statement-first-response]] — the symptom interval and scope come from the problem statement; stack capture without that scope drifts.

## Source support

- [[systems-performance-ch3-operating-systems-p128-142]] — § 3.2.7 introduces stacks as performance evidence: leaf-to-root order, kernel + user stacks during syscalls, "why is this executing" framing.
- [[systems-performance-ch1-introduction-p40-55]] — § 1.7 frames profiling and tracing as the primary observability primitives; stacks are the underlying form their summaries are built on.
- [[systems-performance-ch2-methodologies-continuation-p91-105]] — § 2.5.12 drill-down ends in stage-3 stack-aware tools (`perf`, BCC, `bpftrace`, Ftrace) — the methodological home of stack analysis.
