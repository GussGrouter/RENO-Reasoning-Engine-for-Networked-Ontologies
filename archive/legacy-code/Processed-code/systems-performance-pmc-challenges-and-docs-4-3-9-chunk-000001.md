performance metric: instructions per cycle (insn per cycle). This shows how efficiently the CPUs
are executing instructions—the higher, the better. This metric is explained in the Chapter 6,
CPUs, Section 6.3.7, IPC, CPI.

PMC Interface
On Linux PMCs are accessed via the perf_event_open(2) syscall and are consumed by tools
including perf(1).
While there are hundreds of PMCs available, there is only a fixed number of registers available
in the CPUs to measure them at the same time, perhaps as few as six. You need to choose which
PMCs you’d like to measure on those six registers, or cycle through different PMC sets as a way
of sampling them (Linux perf(1) supports this automatically). Other software counters do not
suffer from these constraints.
PMCs can be used in different modes: counting, where they count events with practically zero
overhead; and overflow sampling, where an interrupt is raised for one in every configurable
number of events, so that state can be captured. Counting can be used to quantify problems;
overflow sampling can be used to show the code path responsible.

157

158

Chapter 4 Observability Tools

perf(1) can perform counting using the stat subcommand, and sampling using the record subcommand; see Chapter 13, perf.

PMC Challenges
Two common challenges when using PMCs are their accuracy for overflow sampling and their
availability in cloud environments.
Overflow sampling may not record the correct instruction pointer that triggered the event, due
to interrupt latency (often called “skid”) or out-of-order instruction execution. For CPU cycle
profiling, such skid may not be a problem, and some profilers deliberately introduce jitter to
avoid lockstep sampling (or use an offset sampling rate such as 99 Hertz). But for measuring
other events, such as LLC misses, the sampled instruction pointer needs to be accurate.
The solution is processor support for what are known as precise events. On Intel, precise events
use a technology called precise event-based sampling (PEBS),9 which uses hardware buffers to
record a more accurate (“precise”) instruction pointer at the time of the PMC event. On AMD,
precise events use instruction-based sampling (IBS) [Drongowski 07]. The Linux perf(1) command supports precise events (see Chapter 13, perf, Section 13.9.2, CPU Profiling).
Another challenge is cloud computing, as many cloud environments disable PMC access for
their guests. It is technically possible to enable it: for example, the Xen hypervisor has the vpmu
command line option, which allows different sets of PMCs to be exposed to guests10 [Xenbits 20].
Amazon have enabled many PMCs for their Nitro hypervisor guests.11 Also, some cloud providers
offer “bare-metal instances” where the guest has full processor access, and therefore full PMC access.

PMCs Documentation
PMCs are processor-specific and documented in the appropriate processor software developer’s
manual. Examples by processor manufacturer:
■

■

■

Intel: Chapter 19, “Performance Monitoring Events,” of Intel® 64 and IA-32 Architectures
Software Developer’s Manual Volume 3 [Intel 16].
