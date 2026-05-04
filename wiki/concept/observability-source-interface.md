---
id: observability-source-interface
type: concept
status: draft
phase: phase-3-reasoned
parent: null
prev: null
next: null
title: "Observability source interface"
---

# Observability source interface

## Definition

Every observability tool reads from a kernel, library, or hardware **source interface**. The tool is a thin layer over that interface; the interface is the thing with the actual properties:

- **Coverage** — which events, states, or resources the interface can expose at all (e.g. `/proc` per-process state, tracepoints for selected kernel events, PMCs for microarchitectural events).
- **Stability** — whether the API and argument layout are part of a stable contract (tracepoints, USDT, `getrusage(2)`) or raw kernel/user internals that can drift across versions (kprobes, uprobes, MSRs).
- **Overhead and observer effect** — per-event CPU cost, storage cost, and measurement skew (e.g. text parsing on `/proc`, return-probe trampolines, `ptrace(2)` 100×+ slowdown, PMC overflow "skid").
- **Permissions** — what privilege is needed to read or attach (root vs unprivileged, capabilities, container restrictions, hypervisor-disabled PMCs).
- **Data model** — text vs binary, counter vs event, point-in-time vs interval, with or without notifications (`/proc` text, netlink binary structs, perf_event_open ring buffers).

The reusable property is that **two tools backed by the same interface share its limits**, and **two tools backed by different interfaces are independent enough to cross-check each other**. The tool name is not the unit of analysis; the source interface is.

## Use when

- Two tools disagree on the same metric — reconcile by their source interfaces (probably the same interface presented differently, or two interfaces with different definitions), not by tool brand.
- Choosing how to answer a new diagnostic question — pick the interface that *can* see the answer at acceptable risk first, then choose a tool.
- Auditing whether two metrics are genuinely independent — independence requires different interfaces, not just different consumers of the same interface.
- Reading an unfamiliar tool — read its source interface (e.g. via `strace` to see `/proc`, netlink, perf_event_open, tracefs) to predict what it can and cannot show.
- Building observability for a new platform, runtime, or container/VM environment — the interface inventory *is* the design.

## Do not use when

- The tool is already known good for this question and the interface adds no decision; over-deriving is overhead.
- The choice is purely UX/dashboard styling on top of fixed source data.
- Only one interface is reachable (locked-down PaaS, black-box endpoint); the lens is interface-bound, accept that explicitly rather than pretending to choose.

## Related concepts

- [[use-method]] — the resource-first checklist is implicitly an interface inventory; known-unknowns are interfaces you do not yet read.
- [[stack-trace-as-execution-cause]] — stack walking is itself an interface property (frame pointers, ORC, DWARF, LBR), not a tool feature.
- [[mode-switch-vs-context-switch]] — interface cost is partly switching cost (`/proc` text round-trips vs netlink binary; uprobe traps vs USDT).
- [[performance-anti-methods]] — the streetlight pattern is an interface-coverage failure dressed up as tool choice; tools-method picks the union of *interfaces*, not resources.
- [[scheduler-policy-shapes-latency]] — many policy effects only show up through specific interfaces (cgroup throttle counters, schedstats); missing those interfaces silently misframes the diagnosis.

## Source support

- [[systems-performance-ch4-observability-tools-p168-182]] — § 4.1 / § 4.2 tool quadrants and Table 4.2's observability-source list (`/proc`, `/sys`, `/sys/fs/cgroup`, `ptrace`, `perf_event`, `netlink`, `libpcap`, delay accounting, tracing sources).
- [[systems-performance-ch4-observability-tools-continuation-p183-197]] — sysfs vs netlink (taskstats / delay accounting); tracepoints vs kprobes vs uprobes vs USDT as distinct interfaces with their own stability/coverage/overhead profiles; PMCs as a hardware interface with register-count and cloud-availability constraints.
- [[systems-performance-ch4-observability-tools-tail-p198-209]] — § 4.3.10 "other sources" enumerates more interfaces (MSRs, `ptrace(2)`, function-profiling hooks, libpcap, conntrack, process accounting, software events, syscall-self-stat, `blktrace`/`debugfs`/etc.); Solaris Kstat as a contrasting structured interface; § 4.6 "observing observability" warns that interfaces — not just tools — are fallible.
