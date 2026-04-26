<!-- pdftotext -f 321 -l 360 Systems.Performance.Enterprise.and.the.Cloud.pdf (Chapter 6 CPUs continued) -->

6.6.19 hardirqs
hardirqs(8)16 is a BCC tool that shows time spent servicing hard IRQs (hard interrupts). The
system-wide time in hard interrupts is readily available from different tools. For example,
mpstat(1) shows it as %irq. There is also /proc/interrupts to show counts of hard IRQ events. The
BCC hardirqs(8) tool differs in that it can show time per hard IRQ rather than an event count.
For example, from a 2-CPU database instance and a 10-second trace:
# hardirqs 10 1
Tracing hard irq event time... Hit Ctrl-C to end.
HARDIRQ

TOTAL_usecs

nvme0q2

35

ena-mgmnt@pci:0000:00:05.0

72

ens5-Tx-Rx-1

326

nvme0q1

878

ens5-Tx-Rx-0

5922

The output shows that 5.9 milliseconds were spent servicing the ens5-Tx-Rx-0 IRQ (networking)
while tracing. As with softirqs(8), this can show CPU consumers that are not typically included
in CPU profiling.
hardirqs(8) has similar options to softirqs(8).

6.6.20

bpftrace

bpftrace is a BPF-based tracer that provides a high-level programming language, allowing the
creation of powerful one-liners and short scripts. It is well suited for custom application analysis
based on clues from other tools. There are bpftrace versions of the earlier tools runqlat(8) and
runqlen(8) in the bpftrace repository [Iovisor 20a].
bpftrace is explained in Chapter 15. This section shows some example one-liners for CPU
analysis.
16

Origin: I developed the BCC version on 19-Oct-2015, inspired by my earlier inttimes.d tool, which itself was based
on another intr.d tool.

6.6 Observability Tools

One-liners
The following one-liners are useful and demonstrate different bpftrace capabilities.
Trace new processes with arguments:
bpftrace -e 'tracepoint:syscalls:sys_enter_execve { join(args->argv); }'

Count syscalls by process:
bpftrace -e 'tracepoint:raw_syscalls:sys_enter { @[pid, comm] = count(); }'

Count syscalls by syscall probe name:
bpftrace -e 'tracepoint:syscalls:sys_enter_* { @[probe] = count(); }'

Sample running process names at 99 Hertz:
bpftrace -e 'profile:hz:99 { @[comm] = count(); }'

Sample user and kernel stacks at 49 Hertz, system wide, with the process name:
bpftrace -e 'profile:hz:49 { @[kstack, ustack, comm] = count(); }'

Sample user-level stacks at 49 Hertz, for PID 189:
bpftrace -e 'profile:hz:49 /pid == 189/ { @[ustack] = count(); }'

Sample user-level stacks 5 frames deep at 49 Hertz, for PID 189:
bpftrace -e 'profile:hz:49 /pid == 189/ { @[ustack(5)] = count(); }'

Sample user-level stacks at 49 Hertz, for processes named “mysqld”:
bpftrace -e 'profile:hz:49 /comm == "mysqld"/ { @[ustack] = count(); }'

Count kernel CPU scheduler tracepoints:
bpftrace -e 'tracepont:sched:* { @[probe] = count(); }'

Count off-CPU kernel stacks for context switch events:
bpftrace -e 'tracepont:sched:sched_switch { @[kstack] = count(); }'

Count kernel function calls beginning with “vfs_”:
bpftrace -e 'kprobe:vfs_* { @[func] = count(); }'

Trace new threads via pthread_create():
bpftrace -e 'u:/lib/x86_64-linux-gnu/libpthread-2.27.so:pthread_create {
printf("%s by %s (%d)\n", probe, comm, pid); }'

283

284

Chapter 6 CPUs

Examples
The following shows bpftrace profiling the MySQL database server at 49 Hertz, and collecting
only the first three levels of the user stack:
# bpftrace -e 'profile:hz:49 /comm == "mysqld"/ { @[ustack(3)] = count(); }'
Attaching 1 probe...
^C
[...]
@[
my_lengthsp_8bit(CHARSET_INFO const*, char const*, unsigned long)+32
Field::send_to_protocol(Protocol*) const+194
THD::send_result_set_row(List<Item>*)+203
]: 8
@[
ppoll+166
vio_socket_io_wait(Vio*, enum_vio_io_event)+22
vio_read(Vio*, unsigned char*, unsigned long)+236
]: 10
[...]

The output was been truncated to only include two stacks, sampled 8 and 10 times. These both
appear to show CPU time spent in networking.

Scheduling Internals
If needed, you can develop custom tools that show the behavior of the CPU scheduler. Start by
trying the tracepoints. Listing them:
# bpftrace -l 'tracepoint:sched:*'
tracepoint:sched:sched_kthread_stop
tracepoint:sched:sched_kthread_stop_ret
tracepoint:sched:sched_waking
tracepoint:sched:sched_wakeup
tracepoint:sched:sched_wakeup_new
tracepoint:sched:sched_switch
tracepoint:sched:sched_migrate_task
tracepoint:sched:sched_process_free
[...]

Each of these has arguments that can be listed using -lv. If the tracepoints are insufficient, consider using dynamic instrumentation with kprobes. Listing kprobe targets for kernel functions
beginning with “sched”:

6.6 Observability Tools

# bpftrace -lv 'kprobe:sched*'
kprobe:sched_itmt_update_handler
kprobe:sched_set_itmt_support
kprobe:sched_clear_itmt_support
kprobe:sched_set_itmt_core_prio
kprobe:schedule_on_each_cpu
kprobe:sched_copy_attr
kprobe:sched_free_group
[...]

On this kernel version (5.3) there are 24 sched tracepoints and 104 possible kprobes beginning
with “sched.”
Because scheduler events can be frequent, instrumenting them can consume significant
overhead. Use caution and find ways to reduce this overhead: use maps to summarize statistics
instead of printing per-event details, and trace the fewest possible events.

6.6.21

Other Tools

CPU observability tools included in other chapters of this book, and in BPF Performance Tools
[Gregg 19], are listed in Table 6.11.

Table 6.11

Other CPU observability tools

Section

Tool

Description

5.5.3

offcputime

Off-CPU profiling using scheduler tracing

5.5.5

execsnoop

Lists new process execution

5.5.6

syscount

Counts system calls by type and process

[Gregg 19]

runqslower

Prints run queue waits slower than a threshold

[Gregg 19]

cpufreq

Samples CPU frequency by process

[Gregg 19]

smpcalls

Times SMP remote CPU calls

[Gregg 19]

llcstat

Summarizes LLC hit ratio by process

Other Linux CPU observability tools and sources include:
■

■

■

■

oprofile: The original CPU profiling tool by John Levon.
atop: Includes many more system-wide statistics and uses process accounting to catch the
presence of short-lived processes.
/proc/cpuinfo: This can be read to see processor details, including clock speed and feature flags.
lscpu: Shows CPU architecture information.

285

286

Chapter 6 CPUs

■

lstopo: Shows hardware topology (provided by the hwloc package).

■

cpupower: Shows processor power states.

■

■

getdelays.c: This is an example of delay accounting observability and includes CPU
scheduler latency per process. It is demonstrated in Chapter 4, Observability Tools.
valgrind: A memory debugging and profiling toolkit [Valgrind 20]. It contains callgrind,
a tool to trace function calls and gather a call graph, which can be visualized using
kcachegrind; and cachegrind for analysis of hardware cache usage by a given program.

An example lstopo(1) output as SVG is shown in Figure 6.18.

Figure 6.18 lstopo(1) SVG output
This lstopo(1) visualization shows which logical CPUs are mapped to which CPU cores (e.g.,
CPUs 0 and 4 are mapped to core 0).
Another tool worth showing is this output of cpupower(1):
# cpupower idle-info
CPUidle driver: intel_idle
CPUidle governor: menu
analyzing CPU 0:
Number of idle states: 9
Available idle states: POLL C1 C1E C3 C6 C7s C8 C9 C10

6.6 Observability Tools

POLL:
Flags/Description: CPUIDLE CORE POLL IDLE
Latency: 0
Usage: 80442
Duration: 36139954
C1:
Flags/Description: MWAIT 0x00
Latency: 2
Usage: 3832139
Duration: 542192027
C1E:
Flags/Description: MWAIT 0x01
Latency: 10
Usage: 10701293
Duration: 1912665723
[...]
C10:
Flags/Description: MWAIT 0x60
Latency: 890
Usage: 7179306
Duration: 48777395993

This not only lists the processor power states, but also provides some statistics: Usage shows the
number of times the state was entered, Duration is the time spent in the state in microseconds,
and Latency is the exit latency in microseconds. This is only showing CPU 0: you can see all
CPUs from their /sys files, for example, the durations can be read from /sys/devices/system/cpu/
cpu*/cpuidle/state0/time [Wysocki 19].
There are also sophisticated products for CPU performance analysis, in particular Intel vTune [22]
and AMD uprof [23].

GPUs
There is not yet a comprehensive set of standard tools for GPU analysis. GPU vendors typically
release specific tools that only work for their own products. Examples include:
■

nvidia-smi, nvperf, and Nvidia Visual Profiler: For Nvidia GPUs

■

intel_gpu_top and Intel vTune: For Intel GPUs

■

radeontop: For Radeon GPUs

These tools provide basic observability statistics such as instruction rates and GPU resource
utilization. Other possible observability sources are PMCs and tracepoints (try perf list |
grep gpu).
GPU profiling is different from CPU profiling, as GPUs do not have a stack trace showing code
path ancestry. Profilers instead can instrument API and memory transfer calls and their timing.

287

288

Chapter 6 CPUs

6.7 Visualizations
CPU usage has historically been visualized as line graphs of utilization or load average, including the original X11 load tool (xload(1)). Such line graphs are an effective way to show variation,
as magnitudes can be visually compared. They can also show patterns over time, as was shown
in Chapter 2, Methodologies, Section 2.9, Monitoring.
However, line graphs of per-CPU utilization don’t scale with the CPU counts we see today,
especially for cloud computing environments involving tens of thousands of CPUs—a graph of
10,000 lines can become paint.
Other statistics plotted as line graphs, including averages, standard deviations, maximums,
and percentiles, provide some value and do scale. However, CPU utilization is often bimodal—
composed of some CPUs that are idle or near-idle, and some at 100% utilization—which is not
effectively conveyed with these statistics. The full distribution often needs to be studied. A
utilization heat map makes this possible.
The following sections introduce CPU utilization heat maps, CPU subsecond-offset heat maps,
flame graphs, and FlameScope. I created these visualization types to solve problems in enterprise
and cloud performance analysis.

6.7.1 Utilization Heat Map
Utilization versus time can be presented as a heat map, with the saturation (darkness) of each
pixel showing the number of CPUs at that utilization and time range [Gregg 10a]. Heat maps
were introduced in Chapter 2, Methodologies.
Figure 6.19 shows CPU utilization for an entire data center, running a public cloud environment.
It includes over 300 physical servers and 5,312 CPUs.

Figure 6.19 CPU utilization heat map, 5,312 CPUs

6.7

Visualizations

The darker shading at the bottom of this heat map shows that most CPUs are running between
0% and 30% utilization. However, the solid line at the top shows that, over time, there are also
some CPUs at 100% utilization. The fact that the line is dark shows that multiple CPUs were at
100%, not just one.

6.7.2 Subsecond-Offset Heat Map
This heat map type allows activity within a second to be examined. CPU activity is typically
measured in microseconds or milliseconds; reporting this data as averages over an entire second
can wipe out useful information. The subsecond-offset heat map puts the subsecond offset on
the y-axis, with the number of non-idle CPUs at each offset shown by the saturation. This visualizes each second as a column, “painting” it from bottom to top.
Figure 6.20 shows a CPU subsecond-offset heat map for a cloud database (Riak).

Figure 6.20 CPU subsecond-offset heat map
What is interesting about this heat map isn’t the times that the CPUs were busy servicing the
database, but the times that they were not, indicated by the white columns. The duration of
these gaps was also interesting: hundreds of milliseconds during which none of the database
threads were on-CPU. This led to the discovery of a locking issue where the entire database was
blocked for hundreds of milliseconds at a time.
If we had examined this data using a line graph, a dip in per-second CPU utilization might have
been dismissed as variable load and not investigated further.

6.7.3 Flame Graphs
Profiling stack traces is an effective way to explain CPU usage, showing which kernel- or userlevel code paths are responsible. It can, however, produce thousands of pages of output. CPU
flame graphs visualize the profile stack frames, so that CPU usage can be understood more
quickly and more clearly [Gregg 16b]. The example in Figure 6.21 shows the Linux kernel profiled using perf(1) as a CPU flame graph.

289

290

Chapter 6 CPUs

Figure 6.21 Linux kernel flame graph
Flame graphs can be built from any CPU profile that include stack traces, including profiles from
perf(1), profile(8), bpftrace, and many more. Flame graphs can also visualize profiles other than
CPU profiles. This section describes CPU flame graphs generated by flamegraph.pl [Gregg 20g].
(There are many other implementations, including d3 flame graphs created by my colleague
Martin Spier [Spier 20a].)

Characteristics
A CPU flame graph has the following characteristics:
■

■

■

■

Each box represents a function in the stack (a “stack frame”).
The y-axis shows stack depth (number of frames on the stack). The top-most box shows
the function that was on-CPU. Everything beneath that is ancestry. The function beneath
a function is its parent, just as in the stack traces shown earlier.
The x-axis spans the sample population. It does not show the passing of time from
left to right, as most graphs do. The left-to-right ordering has no meaning (it’s sorted
alphabetically).
The width of the box shows the total time the function was on-CPU or part of an ancestry
that was on-CPU (based on sample count). Wider box functions may be slower than

6.7

Visualizations

narrow box functions, or they may simply be called more often. The call count is not
shown (nor is it known via sampling).
The sample count can exceed elapsed time if multiple threads were running and sampled in
parallel.

Colors
The frames can be colored based on different schemes. The default shown in Figure 6.21 uses
random warm colors for each frame, which helps visually distinguish adjacent towers. Over the
years I’ve added more color schemes. I’ve found the following to be most useful to flame graph
end users:
■

■

■

Hue: The hue indicates the code type.17 For example, red can indicate native user-level
code, orange for native kernel-level code, yellow for C++, green for interpreted functions,
aqua for inlined functions, and so on depending on the languages you use. Magenta is
used to highlight search matches. Some developers have customized flame graphs to
always highlight their own code in a certain hue so that it stands out.
Saturation: Saturation is hashed from the function name. It provides some color variance
that helps differentiate adjacent towers, while preserving the same colors for function
names to more easily compare multiple flame graphs.
Background color: The background color provides a visual reminder of the flame graph
type. For example, you might use yellow for CPU flame graphs, blue for off-CPU or I/O
flame graphs, and green for memory flame graphs.

Another useful color scheme is one used for IPC (instructions per cycle) flame graphs, where an
additional dimension, IPC, is visualized by coloring each frame using a gradient from blue to
white to red.

Interactivity
Flame graphs are interactive. My original flamegraph.pl generates an SVG with an embedded
JavaScript routine, that when opened in a browser allows you to mouse over elements to reveal
details at the bottom, and other interactive functions. In the Figure 6.21 example, start_xmit()
was highlighted, which shows that it was present in 72.55% of the sampled stacks.
You can also click to zoom18 and Ctrl-F to search19 for a term. When searching, a cumulative
percentage is also shown to indicate how often a stack trace containing that search term was
present. This makes it trivial to calculate how much of the profile was in particular code areas.
For example, you can search for “tcp_” to show how much was in the kernel TCP code.

Interpretation
To explain how to interpret a flame graph in detail, consider the simple synthetic CPU flame
graph shown in Figure 6.22.
17

This was suggested to me by my colleague Amer Ather. My first version was a five-minute regex hack.

18

Adrien Mahieux developed the horizontal zoom feature for flame graphs.

19

Thorsten Lorenz first added a search feature to his flame graph implementation.

291

292

Chapter 6 CPUs

Figure 6.22 Synthetic CPU flame graph
The top edge has been highlighted with a line: this shows the functions that are directly running on-CPU. func_c() was directly on-CPU for 70% of the time, func_b() was on-CPU for 20%
of the time, and func_e() was on-CPU for 10% of the time. The other functions, func_a() and
func_d(), were never sampled on-CPU directly.
To read a flame graph, look for the widest towers and understand them first. In Figure 6.22, it is
the code path func_a() -> func_b() -> func_c(). In the Figure 6.21 flame graph, it is the code path
that ends in the iowrite16() plateau.
For large profiles of thousands of samples, there may be code paths that were sampled only a
few times, and are printed in such a narrow tower that there is no room to include the function
name. This turns out to be a benefit: Your attention is naturally drawn to the wider towers that
have legible function names, and looking at them helps you understand the bulk of the profile
first.
Note that for recursive functions, each level is shown by a separate frame.
Section 6.5.4, Profiling, includes more tips for interpretation, and Section 6.6.13, perf, shows
how to create them using perf(1).

6.7.4 FlameScope
FlameScope is an open-source tool developed at Netflix that marries the previous two visualizations: subsecond-offset heat maps and flame graphs [Gregg 18b]. A subsecond-offset heat map
shows a CPU profile, and ranges including subsecond ranges can be selected to show a flame
graph just for that range. Figure 6.23 shows the FlameScope heat map with annotations and
instructions.
FlameScope is suited for studying issues or perturbations and variance. These can be too small
to see in a CPU profile, which shows the full profile at once: a 100 ms CPU perturbation during
a 30-second profile will only span 0.3% of the width of a flame graph. In FlameScope, a 100 ms
perturbation will show up as a vertical stripe 1/10th of the height of the heat map. Several
such perturbations are visible in the Figure 6.23 example. When selected, a CPU flame graph is
shown just for those time ranges, showing the code paths responsible.

6.8

Experimentation

Figure 6.23 FlameScope
FlameScope is open source [Netflix 19] and has been used to find numerous performance wins at
Netflix.
