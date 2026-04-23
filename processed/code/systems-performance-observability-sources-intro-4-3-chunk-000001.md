4.3

Observability Sources

The sections that follow describe various interfaces that provide the data for observability tools
on Linux. They are summarized in Table 4.2.

4.3 Observability Sources

Table 4.2

Linux observability sources

Type

Source

Per-process counters

/proc

System-wide counters

/proc, /sys

Device configuration and counters

/sys

Cgroup statistics

/sys/fs/cgroup

Per-process tracing

ptrace

Hardware counters (PMCs)

perf_event

Network statistics

netlink

Network packet capture

libpcap

Per-thread latency metrics

Delay accounting

System-wide tracing

Function profiling (Ftrace), tracepoints, software events,
kprobes, uprobes, perf_event

The main sources of systems performance statistics are covered next: /proc and /sys. Then other
Linux sources are covered: delay accounting, netlink, tracepoints, kprobes, USDT, uprobes,
PMCs, and more.
The tracers covered in Chapter 13 perf, Chapter 14 Ftrace, and Chapter 15 BPF utilize many of
these sources, especially system-wide tracing. The scope of these tracing sources is pictured in
Figure 4.5, along with event and group names: for example, block: is for all the block I/O tracepoints, including block:block_rq_issue.

Figure 4.5 Linux tracing sources

139

140

Chapter 4 Observability Tools

Only a few example USDT sources are pictured in Figure 4.5, for the PostgreSQL database
( postgres:), the JVM hotspot compiler (hotspot:), and libc (libc:). You may have many more
depending on your user-level software.
For more information on how tracepoints, kprobes, and uprobes work, their internals are
documented in Chapter 2 of BPF Performance Tools [Gregg 19].

