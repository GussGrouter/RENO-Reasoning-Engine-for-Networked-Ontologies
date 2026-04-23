<!-- pdftotext -f 286 -l 320 Systems.Performance.Enterprise.and.the.Cloud.pdf (Chapter 6 CPUs) -->

6.6.14

profile

profile(8) is a BCC tool that samples stack traces at timed intervals and reports a frequency
count. This is the most useful tool in BCC for understanding CPU consumption as it summarizes almost all code paths that are consuming CPU resources. (See the hardirqs(8) tool in
Section 6.6.19 for more CPU consumers.) profile(8) has lower overhead than perf(1) as only the
stack trace summary is passed to user space. This overhead difference is pictured in Figure 6.15.
profile(8) is also summarized in Chapter 5, Applications, Section 5.5.2, profile, for its use as an
application profiler.
By default, profile(8) samples both user and kernel stack traces at 49 Hertz across all CPUs. This can
be customized using options, and the settings are printed at the start of the output. For example:
# profile
Sampling at 49 Hertz of all threads by user + kernel stack... Hit Ctrl-C to end.
^C
[...]
finish_task_switch
__sched_text_start
schedule
schedule_hrtimeout_range_clock
schedule_hrtimeout_range
poll_schedule_timeout.constprop.0
do_sys_poll
__x64_sys_ppoll
do_syscall_64
entry_SYSCALL_64_after_hwframe
ppoll
vio_socket_io_wait(Vio*, enum_vio_io_event)
vio_read(Vio*, unsigned char*, unsigned long)
my_net_read(NET*)
Protocol_classic::read_packet()
Protocol_classic::get_command(COM_DATA*, enum_server_command*)
do_command(THD*)
start_thread
-

mysqld (5187)
151

The output shows the stack traces as a list of functions, followed by a dash (“-”) and the process name and PID in parentheses, and finally a count for that stack trace. The stack traces are
printed in frequency count order, from least to most frequent.
The full output in this example was 8,261 lines long and has been truncated here to show only
the last, most frequent, stack trace. It shows that scheduler functions were on-CPU, called from a
poll(2) code path. This particular stack trace was sampled 151 times while tracing.

277

278

Chapter 6 CPUs

profile(8) supports various options, including:
■

-U: Includes user-level stacks only

■

-K: Includes kernel-level stacks only

■

-a: Includes frame annotations (e.g., “_[k]” for kernel frames)

■

-d: Includes delimiters between kernel/user stacks

■

-f: Provides output in folded format

■

-p PID: Profiles this process only

■

--stack-storage-size SIZE: Number of unique stack traces (default 16,384)

If profile(8) prints this type of warning:
WARNING: 5 stack traces could not be displayed.

It means that the stack storage was exceeded. You can increase it using the --stack-storage-size
option.

profile CPU Flame Graphs
The -f option provides output suitable for importing by my flame graph software. Example
instructions:
# profile -af 10 > out.stacks
# git clone https://github.com/brendangregg/FlameGraph; cd FlameGraph
# ./flamegraph.pl --hash < out.stacks > out.svg

The out.svg file can then be loaded in a web browser.
profile(8) and the following tools (runqlat(8), runqlen(8), softirqs(8), hardirqs(8)) are BPF-based
tools from the BCC repository, which is covered in Chapter 15.

6.6.15 cpudist
cpudist(8)12 is a BCC tool for showing the distribution of on-CPU time for each thread wakeup.
This can be used to help characterize CPU workloads, providing details for later tuning and
design decisions. For example, from a 2-CPU database instance:
# cpudist 10 1
Tracing on-CPU time... Hit Ctrl-C to end.
usecs

: count

distribution

0 -> 1

: 0

|

|

2 -> 3

: 135

|

|

12
Origin: Sasha Goldshtein developed the BCC cpudist(8) on 29-Jun-2016. I developed a cpudists histogram tool for
Solaris in 2005.

6.6 Observability Tools

4 -> 7

: 26961

|********

|

8 -> 15

: 123341

|****************************************|

16 -> 31

: 55939

|******************

|

32 -> 63

: 70860

|**********************

|

64 -> 127

: 12622

|****

|

128 -> 255

: 13044

|****

|

256 -> 511

: 3090

|*

|

512 -> 1023

: 2

|

|

1024 -> 2047

: 6

|

|

2048 -> 4095

: 1

|

|

4096 -> 8191

: 2

|

|

The output shows that the database usually spent between 4 and 63 microseconds on-CPU.
That’s pretty short.
Options include:
■

-m: Prints output in milliseconds

■

-O: Shows off-CPU time instead of on-CPU time

■

-P: Prints a histogram per process

■

-p PID: Traces this process ID only

This can be used in conjunction with profile(8) to summarize how long an application ran
on-CPU, and what it was doing.

6.6.16

runqlat
13

runqlat(8) is a BCC and bpftrace tool for measuring CPU scheduler latency, often called run
queue latency (even when no longer implemented using run queues). It is useful for identifying
and quantifying issues of CPU saturation, where there is more demand for CPU resources than
they can service. The metric measured by runqlat(8) is the time each thread (task) spends waiting for its turn on CPU.
The following shows BCC runqlat(8) running on a 2-CPU MySQL database cloud instance operating at about 15% CPU utilization system-wide. The arguments to runqlat(8) are “10 1” to set a
10-second interval and output only once:
# runqlat 10 1
Tracing run queue latency... Hit Ctrl-C to end.
usecs

: count

distribution

0 -> 1

: 9017

|*****

|

2 -> 3

: 7188

|****

|

4 -> 7

: 5250

|***

|

13
Origin: I developed the BCC runqlat version on 7-Feb-2016, and bpftrace on 17-Sep-2018, inspired by my earlier
Solaris dispqlat.d tool (dispatcher queue latency: Solaris terminology for run queue latency).

279

280

Chapter 6 CPUs

8 -> 15

: 67668

|****************************************|

16 -> 31

: 3529

|**

|

32 -> 63

: 315

|

|

64 -> 127

: 98

|

|

128 -> 255

: 99

|

|

256 -> 511

: 9

|

|

512 -> 1023

: 15

|

|

1024 -> 2047

: 6

|

|

2048 -> 4095

: 2

|

|

4096 -> 8191

: 3

|

|

8192 -> 16383

: 1

|

|

16384 -> 32767

: 1

|

|

32768 -> 65535

: 2

|

|

65536 -> 131071

: 88

|

|

The output may be surprising for such a lightly-loaded system: there appears to be a high scheduler latency with 88 events in the 65 to 131 millisecond range. It turns out this instance was
CPU throttled by the hypervisor, injecting scheduler latency.
Options include:
■

-m: Prints output in milliseconds

■

-P: Prints a histogram per process ID

■

--pidnss: Prints a histogram per PID namespace

■

-p PID: Traces this process ID only

■

-T: Includes timestamps on output

runqlat(8) works by instrumenting scheduler wakeup and context switch events to determine
the time from wakeup to running. These events can be very frequent on busy production
systems, exceeding one million events per second. Even though BPF is optimized, at these rates
even adding one microsecond per event can cause noticeable overhead. Use with caution, and
consider using runqlen(8) instead.

6.6.17

runqlen
14

runqlen(8) is a BCC and bpftrace tool for sampling the length of the CPU run queues, counting
how many tasks are waiting their turn, and presenting this as a linear histogram. This can be
used to further characterize issues of run queue latency, or as a cheaper approximation. Since it
uses sampling at 99 Hertz across all CPUs, the overhead is typically negligible. runqlat(8), on the
other hand, samples every context switch, which can become millions of events per second.

14

Origin: I developed the BCC version on 12-Dec-2016 and the bpftrace version on 7-Oct-2018, inspired by my
earlier dispqlen.d tool.

6.6 Observability Tools

The following shows runqlen(8) from BCC running on a 2-CPU MySQL database instance that
is at about 15% CPU utilization system-wide (the same instance shown earlier with runqlat(8)).
The arguments to runqlen(8) are “10 1” to set a 10-second interval and output only once:
# runqlen 10 1
Sampling run queue length... Hit Ctrl-C to end.
runqlen

: count

distribution

0

: 1824

|****************************************|

1

: 158

|***

|

This output shows that for much of the time the run queue length was zero, and about 8% of the
time the run queue length was one, meaning that threads needed to wait their turn.
Options include:
■

-C: Prints a histogram per CPU

■

-O: Prints run queue occupancy

■

-T: Includes timestamps on output

Run queue occupancy is a separate metric that shows the percentage of time that there were
threads waiting. This is sometimes useful when a single metric is needed for monitoring, alerting, and graphing.

6.6.18

softirqs
15

softirqs(8) is a BCC tool that shows the time spent servicing soft IRQs (soft interrupts). The
system-wide time in soft interrupts is readily available from different tools. For example,
mpstat(1) shows it as %soft. There is also /proc/softirqs to show counts of soft IRQ events. The
BCC softirqs(8) tool differs in that it can show time per soft IRQ rather than an event count.
For example, from a 2-CPU database instance and a 10-second trace:
# softirqs 10 1
Tracing soft irq event time... Hit Ctrl-C to end.
SOFTIRQ
net_tx

TOTAL_usecs
9

rcu

751

sched

3431

timer

5542

tasklet

11368

net_rx

12225

15

Origin: I developed the BCC version on 20-Oct-2015.

281

