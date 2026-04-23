<!-- pdftotext -f 286 -l 320 Systems.Performance.Enterprise.and.the.Cloud.pdf (Chapter 6 CPUs) -->

6.6.13

perf

perf(1) is the official Linux profiler, a multi-tool with many capabilities. Chapter 13 provides a
summary of perf(1). This section covers its usage for CPU analysis.

One-Liners
The following one-liners are both useful and demonstrate different perf(1) capabilities for CPU
analysis. Some are explained in more detail in the following sections.
Sample on-CPU functions for the specified command, at 99 Hertz:
perf record -F 99 command

Sample CPU stack traces (via frame pointers) system-wide for 10 seconds:
perf record -F 99 -a -g -- sleep 10

Sample CPU stack traces for the PID, using dwarf (dbg info) to unwind stacks:
perf record -F 99 -p PID --call-graph dwarf -- sleep 10

Record new process events via exec:
perf record -e sched:sched_process_exec -a

Record context switch events for 10 seconds with stack traces:
perf record -e sched:sched_switch -a -g -- sleep 10

Sample CPU migrations for 10 seconds:
perf record -e migrations -a -- sleep 10

Record all CPU migrations for 10 seconds:
perf record -e migrations -a -c 1 -- sleep 10

267

268

Chapter 6 CPUs

Show perf.data as a text report, with data coalesced and counts and percentages:
perf report -n --stdio

List all perf.data events, with data header (recommended):
perf script --header

Show PMC statistics for the entire system, for 5 seconds:
perf stat -a -- sleep 5

Show CPU last level cache (LLC) statistics for the command:
perf stat -e LLC-loads,LLC-load-misses,LLC-stores,LLC-prefetches command

Show memory bus throughput system-wide every second:
perf stat -e uncore_imc/data_reads/,uncore_imc/data_writes/ -a -I 1000

Show the rate of context switches per-second:
perf stat -e sched:sched_switch -a -I 1000

Show the rate of involuntary context switches per-second (previous state was TASK_RUNNING):
perf stat -e sched:sched_switch --filter 'prev_state == 0' -a -I 1000

Show the rate of mode switches and context switches per second:
perf stat -e cpu_clk_unhalted.ring0_trans,cs -a -I 1000

Record a scheduler profile for 10 seconds:
perf sched record -- sleep 10

Show per-process scheduler latency from a scheduler profile:
perf sched latency

List per-event scheduler latency from a scheduler profile:
perf sched timehist

For more perf(1) one-liners see Chapter 13, perf, Section 13.2, One-Liners.

System-Wide CPU Profiling
perf(1) can be used to profile CPU call paths, summarizing where CPU time is spent in both
kernel- and user-space. This is performed by the record command, which captures sample to a
perf.data file. A report command can then be used to view the contents of the file. It works by
using the most accurate timer available: CPU-cycle-based if available, otherwise software based
(the cpu-clock event).

6.6 Observability Tools

In the following example, all CPUs (-a10) are sampled with call stacks (-g) at 99 Hz (-F 99) for
10 seconds (sleep 10). The --stdio option for report is used to print all the output, instead of
operating in interactive mode.
# perf record -a -g -F 99 -- sleep 10
[ perf record: Woken up 20 times to write data ]
[ perf record: Captured and wrote 5.155 MB perf.data (1980 samples) ]
# perf report --stdio
[...]
# Children

Self

Command

Shared Object

Symbol

# ........ ........ ............... ......................... ...................
...................................................................
#
29.49%

0.00%

mysqld

libpthread-2.30.so

[.] start_thread

|
---start_thread
0x55dadd7b473a
0x55dadc140fe0
|
--29.44%--do_command
|
|--26.82%--dispatch_command
|

|

|

--25.51%--mysqld_stmt_execute

|
|
Prepared_statement::execute_loop
|

|
--25.05%-|

|
Prepared_statement::execute

--24.90%--

|

|

|

--24.34%--

|

|

mysql_execute_command
[...]

The full output is many pages long, in descending sample count order. These sample counts are
given as percentages, which show where the CPU time was spent. In this example, 29.44% of
time was spent in the do_command() and its children, including mysql_execute_command().
These kernel and process symbols are available only if their debuginfo files are available; otherwise, hex addresses are shown.

10

The -a option became the default in Linux 4.11.

269

270

Chapter 6 CPUs

The stack ordering changed in Linux 4.4 from callee (beginning with the on-CPU function and
listing ancestry) to caller (beginning with the parent function and listing children). You can
switch back to callee using -g:
# perf report -g callee --stdio
[...]
19.75%
0.00% mysqld
Sql_cmd_dml::execute_inner

mysqld

[.]

|
---Sql_cmd_dml::execute_inner
Sql_cmd_dml::execute
mysql_execute_command
Prepared_statement::execute
Prepared_statement::execute_loop
mysqld_stmt_execute
dispatch_command
do_command
0x55dadc140fe0
0x55dadd7b473a
start_thread
[...]

To understand a profile, you can try both orderings. If you are unable to make sense of it quickly
at the command line, try a visualization such as flame graphs.

CPU Flame Graphs
CPU flame graphs can be generated from the same perf.data profile by using the flamegraph
report added in Linux 5.8.11 For example:
# perf record -F 99 -a -g -- sleep 10
# perf script report flamegraph

This creates a flamegraph using a d3-flame-graph template file in /usr/share/d3-flame-graph/
d3-flamegraph-base.html (if you do not have this file, it can be built by the d3-flame-graph software [Spier 20b]). These can also be combined as one command:
# perf script flamegraph -a -F 99 sleep 10

For older versions of Linux, you can use my original flamegraph software to visualize the samples reported by perf script. The steps (also included in Chapter 5) are:
# perf record -F 99 -a -g -- sleep 10
# perf script --header > out.stacks
11

Thanks to Andreas Gerstmayr for adding this option.

6.6 Observability Tools

$ git clone https://github.com/brendangregg/FlameGraph; cd FlameGraph
$ ./stackcollapse-perf.pl < ../out.stacks | ./flamegraph.pl --hash > out.svg

The out.svg file is the CPU flame graph, which can be loaded in a web browser. It includes
JavaScript for interactivity: click to zoom, and Ctrl-F to search. See Section 6.5.4, Profiling,
which illustrates these steps in Figure 6.15.
You can modify these steps to pipe perf script directly to stackcollapse-perf.pl, avoiding the
out.stacks file. However, I’ve found these files useful to archive for later reference and use with
other tools (e.g., FlameScope).

Options
flamegraph.pl supports various options, including:
■

--title TEXT: Set the title.

■

--subtitle TEXT: Set a subtitle.

■

--width NUM: Set the image width (default 1200 pixels).

■

--countname TEXT: Change the count label (default “samples”).

■

■

--colors PALETTE: Set a palette for the frame colors. Some of these use search terms or
annotations to use different color hues for different code paths. Options include hot (the
default), mem, io, java, js, perl, red, green, blue, yellow.
--bgcolors COLOR: Set the background color. Gradient choices are yellow (the default),
blue, green, grey; for flat (non-gradient) colors use “#rrggbb”.

■

--hash: Colors are keyed by a function name hash for consistency.

■

--reverse: Generate a stack-reversed flame graph, merging from leaf to root.

■

--inverted: Flip the y-axis to generate an icicle graph.

■

--flamechart: Generate a flame chart (time on the x-axis).

For example, this is the set of options I use for Java CPU flame graphs:
$ ./flamegraph.pl --colors=java --hash
--title="CPU Flame Graph, $(hostname), $(date)" < ...

This includes the hostname and date in the flame graph.
See Section 6.7.3, Flame Graphs, for interpreting flame graphs.

Process CPU Profiling
Apart from profiling across all CPUs, individual processes can be targeted using -p PID, and
perf(1) can execute a command directly and profile it:
# perf record -F 99 -g command

271

272

Chapter 6 CPUs

A “--” is often inserted before the command to stop perf(1) processing command line options
from the command.

Scheduler Latency
The sched command records and reports scheduler statistics. For example:
# perf sched record -- sleep 10
[ perf record: Woken up 63 times to write data ]
[ perf record: Captured and wrote 125.873 MB perf.data (1117146 samples) ]
# perf sched latency
------------------------------------------------------------------------------------Task

| Runtime ms

| Switches | Average delay ms | Maximum delay ms |

------------------------------------------------------------------------------------jbd2/nvme0n1p1-:175

|

0.209 ms |

3 | avg:

0.549 ms | max:

1.630 ms |

kauditd:22

|

0.180 ms |

6 | avg:

0.463 ms | max:

2.300 ms |

oltp_read_only.:(4)

| 3969.929 ms |

184629 | avg:

0.007 ms | max:

5.484 ms |

mysqld:(27)

| 8759.265 ms |

96025 | avg:

0.007 ms | max:

4.133 ms |

bash:21391

|

1 | avg:

0.007 ms | max:

0.007 ms |

0.275 ms |

[...]
------------------------------------------------------------------------------------TOTAL:

|

12916.132 ms |

281395 |

-------------------------------------------------

This latency report summarizes average and maximum scheduler latency (aka run queue
latency) per process. While there were many context switches for the oltp_read_only and mysqld
processes, their average and maximum scheduler latencies were still low. (To fit the output width
here, I elided a final “Maximum delay at” column.)
Scheduler events are frequent, so this type of tracing incurs significant CPU and storage overhead. The perf.data file in this case was 125 Mbytes from only ten seconds of tracing. The rate
of scheduler events may inundate perf(1)’s per-CPU ring buffers, causing events to be lost: the
report will state this at the end if it happened. Be careful with this overhead, as it may perturb
production applications.
perf(1) sched also has map and timehist reports for displaying the scheduler profile in different
ways. The timehist report shows per-event details:
# perf sched timehist
Samples do not have callchains.
time

cpu

task name

wait time

sch delay

[tid/pid]

(msec)

(msec)

run time
(msec)

---------

---------

---------

-------------- ------

----------------------------

437752.840756 [0000]

mysqld[11995/5187]

0.000

0.000

0.000

437752.840810 [0000]

oltp_read_only.[21483/21482]

0.000

0.000

0.054

6.6 Observability Tools

437752.840845 [0000]

mysqld[11995/5187]

0.054

0.000

0.034

437752.840847 [0000]

oltp_read_only.[21483/21482]

0.034

0.002

0.002

10000.080

0.004

0.127

[...]
437762.842139 [0001]

sleep[21487]

This report shows each context switch event with the time sleeping (wait time), scheduler
latency (sch delay), and time spent on CPU (runtime), all in milliseconds. The final line shows
the dummy sleep(1) command used to set the duration of perf record, which slept for 10
seconds.

PMCs (Hardware Events)
The stat subcommand counts events and produces a summary, rather than recording events
to perf.data. By default, perf stat counts several PMCs to show a high-level summary of CPU
cycles. For example, summarizing a gzip(1) command:
$ perf stat gzip ubuntu-19.10-live-server-amd64.iso
Performance counter stats for 'gzip ubuntu-19.10-live-server-amd64.iso':
25235.652299

task-clock (msec)

#

0.997 CPUs utilized

142

context-switches

#

0.006 K/sec

25

cpu-migrations

#

0.001 K/sec

128

page-faults

#

0.005 K/sec

94,817,146,941

cycles

#

3.757 GHz

152,114,038,783

instructions

#

1.60

28,974,755,679

branches

# 1148.167 M/sec

1,020,287,443

branch-misses

#

insn per cycle

3.52% of all branches

25.312054797 seconds time elapsed

The statistics include the cycle and instruction count, and the IPC. As described earlier, this is
an extremely useful high-level metric for determining the types of cycles occurring and how
many of them are stall cycles. In this case, the IPC of 1.6 is “good.”
Here is a system-wide example of measuring IPC, this time from a Shopify benchmark to investigate NUMA tuning, which ultimately improved application throughput by 20–30%. These
commands measure on all CPUs for 30 seconds.
Before:
# perf stat -a -- sleep 30
[...]
404,155,631,577
[100.00%]
[...]

instructions

#

0.72

insns per cycle

273

274

Chapter 6 CPUs

After NUMA tuning:
# perf stat -a -- sleep 30
[...]
490,026,784,002
[100.00%]

instructions

#

0.89

insns per cycle

[...]

IPC improved from 0.72 to 0.89: 24%, matching the final win. (See Chapter 16, Case Study, for
another production example of measuring IPC.)

Hardware Event Selection
There are many more hardware events that can be counted. You can list them using perf list:
# perf list
[...]
branch-instructions OR branches

[Hardware event]

branch-misses

[Hardware event]

bus-cycles

[Hardware event]

cache-misses

[Hardware event]

cache-references

[Hardware event]

cpu-cycles OR cycles

[Hardware event]

instructions

[Hardware event]

ref-cycles

[Hardware event]

[...]
LLC-load-misses

[Hardware cache event]

LLC-loads

[Hardware cache event]

LLC-store-misses

[Hardware cache event]

LLC-stores

[Hardware cache event]

[...]

Look for both “Hardware event” and “Hardware cache event.” For some processors you will find
additional groups of PMCs; a longer example is provided in Chapter 13, perf, Section 13.3, perf
Events. Those available depend on the processor architecture and are documented in the processor manuals (e.g., the Intel Software Developer’s Manual).
These events can be specified using –e. For example (this is from an Intel Xeon):
$ perf stat -e instructions,cycles,L1-dcache-load-misses,LLC-load-misses,dTLB-loadmisses gzip ubuntu-19.10-live-server-amd64.iso
Performance counter stats for 'gzip ubuntu-19.10-live-server-amd64.iso':
152,226,453,131

instructions

94,697,951,648

cycles

#

1.61

insn per cycle

6.6 Observability Tools

2,790,554,850

L1-dcache-load-misses

9,612,234

LLC-load-misses

357,906

dTLB-load-misses

25.275276704 seconds time elapsed

Apart from instructions and cycles, this example also measured the following:
■

■

■

L1-dcache-load-misses: Level 1 data cache load misses. This gives you a measure of the
memory load caused by the application, after some loads have been returned from the
Level 1 cache. It can be compared with other L1 event counters to determine cache hit ratio.
LLC-load-misses: Last level cache load misses. After the last level, this accesses main
memory, and so this is a measure of main memory load. The difference between this and
L1-dcache-load-misses gives an idea of the effectiveness of the CPU caches beyond Level 1,
but other counters are needed for completeness.
dTLB-load-misses: Data translation lookaside buffer misses. This shows the effectiveness
of the MMU to cache page mappings for the workload, and can measure the size of the
memory workload (working set).

Many other counters can be inspected. perf(1) supports both descriptive names (like those used
for this example) and hexadecimal values. The latter may be necessary for esoteric counters you
find in processor manuals, for which a descriptive name isn’t provided.

Software Tracing
perf can also record and count software events. Listing some CPU-related events:
# perf list
[...]
context-switches OR cs

[Software event]

cpu-migrations OR migrations

[Software event]

[...]
sched:sched_kthread_stop

[Tracepoint event]

sched:sched_kthread_stop_ret

[Tracepoint event]

sched:sched_wakeup

[Tracepoint event]

sched:sched_wakeup_new

[Tracepoint event]

sched:sched_switch

[Tracepoint event]

[...]

The following example uses the context switch software event to trace when applications leave
the CPU, and collects call stacks for one second:
# perf record -e sched:sched_switch -a -g -- sleep 1
[ perf record: Woken up 46 times to write data ]
[ perf record: Captured and wrote 11.717 MB perf.data (50649 samples) ]

275

276

Chapter 6 CPUs

# perf report --stdio
[...]
16.18%
16.18% prev_comm=mysqld prev_pid=11995 prev_prio=120 prev_state=S ==>
next_comm=swapper/1 next_pid=0 next_prio=120
|
---__sched_text_start
schedule
schedule_hrtimeout_range_clock
schedule_hrtimeout_range
poll_schedule_timeout.constprop.0
do_sys_poll
__x64_sys_ppoll
do_syscall_64
entry_SYSCALL_64_after_hwframe
ppoll
vio_socket_io_wait
vio_read
my_net_read
Protocol_classic::read_packet
Protocol_classic::get_command
do_command
start_thread
[...]

This truncated output shows mysql context switching to block on a socket via poll(2). To investigate further, see the Off-CPU analysis methodology in Chapter 5, Applications, Section 5.4.2,
Off-CPU Analysis, and supporting tools in Section 5.5.3, offcputime.
Chapter 9, Disks, includes another example of static tracing with perf(1): block I/O tracepoints.
Chapter 10, Network, includes an example of dynamic instrumentation with perf(1) for the
tcp_sendmsg() kernel function.

Hardware Tracing
perf(1) is also able to use hardware tracing for per-instruction analysis, if supported by the processor. This is a low-level advanced activity not covered here, but is mentioned again in Chapter 13,
perf, Section 13.13, Other Commands.

Documentation
For more on perf(1), see Chapter 13, perf. Also see its man pages, documentation in the Linux
kernel source under tools/perf/Documentation, my “perf Examples” page [Gregg 20f], the “Perf
Tutorial” [Perf 15], and “The Unofficial Linux Perf Events Web-Page” [Weaver 11].

6.6 Observability Tools

