AMD: Section 2.1.1, “Performance Monitor Counters,” of Open-Source Register Reference For
AMD Family 17h Processors Models 00h-2Fh [AMD 18]
ARM: Section D7.10, “PMU Events and Event Numbers,” of Arm® Architecture Reference
Manual Armv8, for Armv8-A architecture profile [ARM 19]

There has been work to develop a standard naming scheme for PMCs that could be supported
across all processors, called the performance application programming interface (PAPI) [UTK 20].
Operating system support for PAPI has been mixed: it requires frequent updates to map PAPI
names to vendor PMC codes.
Chapter 6, CPUs, Section 6.4.1, Hardware, subsection Hardware Counters (PMCs), describes their
implementation in more detail and provides additional PMC examples.
9

Some of Intel’s documentation expands PEBS differently, as: processor event-based sampling.

10

I wrote the Xen code that allows different PMC modes: “ipc” for instructions-per-cycle PMCs only, and “arch” for
the Intel architectural set. My code was just a firewall on the existing vpmu support in Xen.

11

Currently only for larger Nitro instances where the VM owns a full processor socket (or more).

4.3 Observability Sources

4.3.10

Other Observability Sources

Other observability sources include:
■

■

■

■

■

■

■

■

MSRs: PMCs are implemented using model-specific registers (MSRs). There are other MSRs
for showing the configuration and health of the system, including the CPU clock rate,
usage, temperatures, and power consumption. The available MSRs are dependent on the
processor type (model-specific), BIOS version and settings, and hypervisor settings. One
use is an accurate cycle-based measurement of CPU utilization.
ptrace(2): This syscall controls process tracing, which is used by gdb(1) for process debugging and strace(1) for tracing syscalls. It is breakpoint-based and can slow the target over
one hundred-fold. Linux also has tracepoints, introduced in Section 4.3.5, Tracepoints, for
more efficient syscall tracing.
Function profiling: Profiling function calls (mcount() or __fentry__()) are added to the
start of all non-inlined kernel functions on x86 for efficient Ftrace function tracing. They
are converted to nop instructions until needed. See Chapter 14, Ftrace.
Network sniffing (libpcap): These interfaces provide a way to capture packets from network devices for detailed investigations into packet and protocol performance. On Linux,
sniffing is provided via the libpcap library and /proc/net/dev and is consumed by the
tcpdump(8) tool. There are overheads, both CPU and storage, for capturing and examining all packets. See Chapter 10 for more about network sniffing.
netfilter conntrack: The Linux netfilter technology allows custom handlers to be executed on events, not just for firewall, but also for connection tracking (conntrack). This
allows logs to be created of network flows [Ayuso 12].
Process accounting: This dates back to mainframes and the need to bill departments and
users for their computer usage, based on the execution and runtime of processes. It exists
in some form for Linux and other systems and can sometimes be helpful for performance
analysis at the process level. For example, the Linux atop(1) tool uses process accounting
to catch and display information from short-lived processes that would otherwise be
missed when taking snapshots of /proc [Atoptool 20].
Software events: These are related to hardware events but are instrumented in software.
Page faults are an example. Software events are made available via the perf_event_open(2)
interface and are used by perf(1) and bpftrace. They are pictured in Figure 4.5.
System calls: Some system or library calls may be available to provide some performance
metrics. These include getrusage(2), a system call for processes to get their own resource
usage statistics, including user- and system-time, faults, messages, and context switches.

If you are interested in how each of these works, you will find that documentation is usually
available, intended for the developer who is building tools upon these interfaces.

And More
Depending on your kernel version and enabled options, even more observability sources may
be available. Some are mentioned in later chapters of this book. For Linux these include I/O
accounting, blktrace, timer_stats, lockstat, and debugfs.

159

160

Chapter 4 Observability Tools

One way to find such sources is to read the kernel code you are interested in observing and see
what statistics or tracepoints have been placed there.
In some cases there may be no kernel statistics for what you are after. Beyond dynamic instrumentation (Linux kprobes and uprobes), you may find that debuggers such as gdb(1) and lldb(1)
can fetch kernel and application variables to shed some light on an investigation.

Solaris Kstat
As an example of a different way to provide system statistics, Solaris-based systems use a kernel
statistics (Kstat) framework that provides a consistent hierarchical structure of kernel statistics,
each named using the following four-tuple:
module:instance:name:statistic

These are
■
