# systems-performance-observability-1-7 (chunk 000002)

An effective visualization of CPU profiles is flame graphs. CPU flame graphs can help you find
     more performance wins than any other tool, after metrics. They reveal not only CPU issues,
     but other types of issues as well, found by the CPU footprints they leave behind. Issues of lock
     contention can be found by looking for CPU time in spin paths; memory issues can be analyzed
     by finding excessive CPU time in memory allocation functions (malloc()), along with the code
     paths that led to them; performance issues involving misconfigured networking may be discov-
     ered by seeing CPU time in slow or legacy codepaths; and so on.

Figure 1.6 is an example CPU flame graph showing the CPU cycles spent by the iperf(1) network
     micro-benchmark tool.

Figure 1.6 CPU profiling using flame graphs
                                                                                 1.7   Observability   11

This flame graph shows how much CPU time is spent copying bytes (the path that ends in
copy_user_enhanced_fast_string()) versus TCP transmission (the tower on the left that includes
tcp_write_xmit()). The widths are proportional to the CPU time spent, and the vertical axis
shows the code path.

Profilers are explained in Chapters 4, 5, and 6, and the flame graph visualization is explained in
Chapter 6, CPUs, Section 6.7.3, Flame Graphs.

1.7.3 Tracing
Tracing is event-based recording, where event data is captured and saved for later analysis or
consumed on-the-fly for custom summaries and other actions. There are special-purpose tracing
tools for system calls (e.g., Linux strace(1)) and network packets (e.g., Linux tcpdump(8)); and
general-purpose tracing tools that can analyze the execution of all software and hardware events
(e.g., Linux Ftrace, BCC, and bpftrace). These all-seeing tracers use a variety of event sources, in
particular, static and dynamic instrumentation, and BPF for programmability.

Static Instrumentation
Static instrumentation describes hard-coded software instrumentation points added to the
source code. There are hundreds of these points in the Linux kernel that instrument disk I/O,
scheduler events, system calls, and more. The Linux technology for kernel static instrumen-
tation is called tracepoints. There is also a static instrumentation technology for user-space
software called user statically defined tracing (USDT). USDT is used by libraries (e.g., libc) for
instrumenting library calls and by many applications for instrumenting service requests.

As an example tool that uses static instrumentation, execsnoop(8) prints new processes created
while it is tracing (running) by instrumenting a tracepoint for the execve(2) system call. The
following shows execsnoop(8) tracing an SSH login:

# execsnoop
PCOMM               PID     PPID    RET ARGS
ssh                 30656   20063      0 /usr/bin/ssh 0
sshd                30657   1401       0 /usr/sbin/sshd -D -R
sh                  30660   30657      0
env                 30661   30660      0 /usr/bin/env -i PATH=/usr/local/sbin:/usr/local...
run-parts           30661   30660      0 /bin/run-parts --lsbsysinit /etc/update-motd.d
00-header           30662   30661      0 /etc/update-motd.d/00-header
uname               30663   30662      0 /bin/uname -o
uname               30664   30662      0 /bin/uname -r
uname               30665   30662      0 /bin/uname -m
10-help-text        30666   30661      0 /etc/update-motd.d/10-help-text
50-motd-news        30667   30661      0 /etc/update-motd.d/50-motd-news
cat                 30668   30667      0 /bin/cat /var/cache/motd-news
cut                 30671   30667      0 /usr/bin/cut -c -80
tr                  30670   30667      0 /usr/bin/tr -d \000-\011\013\014\016-\037
head                30669   30667      0 /usr/bin/head -n 10
12   Chapter 1 Introduction

80-esm                    30672     30661        0 /etc/update-motd.d/80-esm
     lsb_release               30673     30672        0 /usr/bin/lsb_release -cs
     [...]

This is especially useful for revealing short-lived processes that may be missed by other observ-
     ability tools such as top(1). These short-lived processes can be a source of performance issues.

See Chapter 4 for more information about tracepoints and USDT probes.

Dynamic Instrumentation
     Dynamic instrumentation creates instrumentation points after the software is running, by
     modifying in-memory instructions to insert instrumentation routines. This is similar to
     how debuggers can insert a breakpoint on any function in running software. Debuggers pass
     execution flow to an interactive debugger when the breakpoint is hit, whereas dynamic instru-
     mentation runs a routine and then continues the target software. This capability allows custom
     performance statistics to be created from any running software. Issues that were previously
     impossible or prohibitively difficult to solve due to a lack of observability can now be fixed.

Dynamic instrumentation is so different from traditional observation that it can be difficult,
     at first, to grasp its role. Consider an operating system kernel: analyzing kernel internals can be
     like venturing into a dark room, with candles (system counters) placed where the kernel engi-
     neers thought they were needed. Dynamic instrumentation is like having a flashlight that you
     can point anywhere.

Dynamic instrumentation was first created in the 1990s [Hollingsworth 94], along with tools
     that use it called dynamic tracers (e.g., kerninst [Tamches 99]). For Linux, dynamic instrumen-
     tation was first developed in 2000 [Kleen 08] and began merging into the kernel in 2004
     (kprobes). However, these technologies were not well known and were difficult to use. This
     changed when Sun Microsystems launched their own version in 2005, DTrace, which was easy
     to use and production-safe. I developed many DTrace-based tools that showed how important
     it was for systems performance, tools that saw widespread use and helped make DTrace and
     dynamic instrumentation well-known.

BPF
     BPF, which originally stood for Berkeley Packet Filter, is powering the latest dynamic tracing
     tools for Linux. BPF originated as a mini in-kernel virtual machine for speeding up the execu-
     tion of tcpdump(8) expressions. Since 2013 it has been extended (hence is sometimes called
     eBPF3) to become a generic in-kernel execution environment, one that provides safety and fast
     access to resources. Among its many new uses are tracing tools, where it provides programmabil-
     ity for the BPF Compiler Collection (BCC) and bpftrace front ends. execsnoop(8), shown earlier,
     is a BCC tool.4

3
         eBPF was initially used to describe this extended BPF; however, the technology is now referred to as just BPF.
     4
         I first developed it for DTrace, and I have since developed it for other tracers including BCC and bpftrace.
                                                                            1.8   Experimentation   13

Chapter 3 explains BPF, and Chapter 15 introduces the BPF tracing front ends: BCC and bpf-
trace. Other chapters introduce many BPF-based tracing tools in their observability sections; for
example, CPU tracing tools are included in Chapter 6, CPUs, Section 6.6, Observability Tools. I
have also published prior books on tracing tools (for DTrace [Gregg 11a] and BPF [Gregg 19]).

Both perf(1) and Ftrace are also tracers with some similar capabilities to the BPF front ends.
perf(1) and Ftrace are covered in Chapters 13 and 14.

1.8 Experimentation
Apart from observability tools there are also experimentation tools, most of which are bench-
marking tools. These perform an experiment by applying a synthetic workload to the system
and measuring its performance. This must be done carefully, because experimental tools can
perturb the performance of systems under test.

There are macro-benchmark tools that simulate a real-world workload such as clients making
application requests; and there are micro-benchmark tools that test a specific component, such
as CPUs, disks, or networks. As an analogy: a car’s lap time at Laguna Seca Raceway could be
considered a macro-benchmark, whereas its top speed and 0 to 60mph time could be considered
micro-benchmarks. Both benchmark types are important, although micro-benchmarks are
typically easier to debug, repeat, and understand, and are more stable.

The following example uses iperf(1) on an idle server to perform a TCP network throughput
micro-benchmark with a remote idle server. This benchmark ran for ten seconds (-t 10) and
produces per-second averages (-i 1):
