5.5.1 perf
perf(1) is the standard Linux profiler, a multi-tool with many uses. It is explained in Chapter
13, perf. As CPU profiling is critical for application analysis, a summary of CPU profiling using
perf(1) is included here. Chapter 6, CPUs, covers CPU profiling and flame graphs in more detail.

CPU Profiling
The following uses perf(1) to sample stack traces (-g) across all CPUs (-a) at 49 Hertz (-F 49: samples per second) for 30 seconds, and then to list the samples:
# perf record -F 49 -a -g -- sleep 30
[ perf record: Woken up 1 times to write data ]
[ perf record: Captured and wrote 0.560 MB perf.data (2940 samples) ]
# perf script
mysqld 10441 [000] 64918.205722:

10101010 cpu-clock:pppH:

5587b59bf2f0 row_mysql_store_col_in_innobase_format+0x270 (/usr/sbin/mysqld)
5587b59c3951 [unknown] (/usr/sbin/mysqld)
5587b58803b3 ha_innobase::write_row+0x1d3 (/usr/sbin/mysqld)
5587b47e10c8 handler::ha_write_row+0x1a8 (/usr/sbin/mysqld)
5587b49ec13d write_record+0x64d (/usr/sbin/mysqld)


5.5 Observability Tools

5587b49ed219 Sql_cmd_insert_values::execute_inner+0x7f9 (/usr/sbin/mysqld)
5587b45dfd06 Sql_cmd_dml::execute+0x426 (/usr/sbin/mysqld)
5587b458c3ed mysql_execute_command+0xb0d (/usr/sbin/mysqld)
5587b4591067 mysql_parse+0x377 (/usr/sbin/mysqld)
5587b459388d dispatch_command+0x22cd (/usr/sbin/mysqld)
5587b45943b4 do_command+0x1a4 (/usr/sbin/mysqld)
5587b46b22c0 [unknown] (/usr/sbin/mysqld)
5587b5cfff0a [unknown] (/usr/sbin/mysqld)
7fbdf66a9669 start_thread+0xd9 (/usr/lib/x86_64-linux-gnu/libpthread-2.30.so)
[...]

There are 2,940 stack samples in this profile; only one stack has been included here. The perf(1)
script subcommand prints each stack sample in a previously recorded profile (the perf.data file).
perf(1) also has a report subcommand for summarizing the profile as a code-path hierarchy. The
profile can also be visualized as a CPU flame graph.

CPU Flame Graphs
CPU flame graphs have been automated at Netflix so that operators and developers can request
them from a browser-based UI. They can be built entirely using open-source software, including
from the GitHub repository in the following commands. For the Figure 5.3 CPU flame graph
shown earlier, the commands were:
# perf record -F 49 -a -g -- sleep 10; perf script --header > out.stacks
# git clone https://github.com/brendangregg/FlameGraph; cd FlameGraph
# ./stackcollapse-perf.pl < ../out.stacks | ./flamegraph.pl --hash > out.svg

The out.svg file can then be loaded in a web browser.
flamegraph.pl provides custom color palettes for different languages: for example, for Java applications, try --color=java. Run flamegraph.pl -h for all options.

Syscall Tracing
The perf(1) trace subcommand traces system calls by default, and is perf(1)’s version of strace(1)
(Section 5.5.4, strace). For example, tracing a MySQL server process:
# perf trace -p $(pgrep mysqld)
? (
): mysqld/10120 ... [continued]: futex())
= -1 ETIMEDOUT (Connection timed out)
0.014 ( 0.002 ms): mysqld/10120 futex(uaddr: 0x7fbddc37ed48, op: WAKE|
PRIVATE_FLAG, val: 1)
= 0
0.023 (10.103 ms): mysqld/10120 futex(uaddr: 0x7fbddc37ed98, op: WAIT_BITSET|
PRIVATE_FLAG, utime: 0x7fbdc9cfcbc0, val3: MATCH_ANY) = -1 ETIMEDOUT (Connection
timed out)
[...]

201


202

Chapter 5 Applications

Only a few output lines are included, showing futex(2) calls as various MySQL threads wait for
work (these dominated the off-CPU time flame graph in Figure 5.5).
The advantage of perf(1) is that it uses per-CPU buffers to reduce the overhead, making it much
safer to use than the current implementation of strace(1). It can also trace system-wide, whereas
strace(1) is limited to a set of processes (typically a single process), and it can trace events other
than syscalls. perf(1), however, does not have as many syscall argument translations as strace(1);
here is a single line from strace(1) for comparison:
[pid 10120] futex(0x7fbddc37ed98, FUTEX_WAIT_BITSET_PRIVATE, 0, {tv_sec=445110,
tv_nsec=427289364}, FUTEX_BITSET_MATCH_ANY) = -1 ETIMEDOUT (Connection timed out)

The strace(1) version has expanded the utime struct. There is work underway for perf(1) trace to
use BPF for improved argument “beautification.” As an end goal, perf(1) trace could ultimately
be a swap-in replacement for strace(1). (For more on strace(1), see Section 5.5.4, strace.)

Kernel Time Analysis
As perf(1) trace shows time in syscalls, it helps explain the system CPU time commonly shown
by monitoring tools, although it is easier to start with a summary than the event-by-event output. perf(1) trace summarizes syscalls with -s:
# perf trace -s -p $(pgrep mysqld)
mysqld (14169), 225186 events, 99.1%
syscall

calls

total

min

avg

max

(msec)

(msec)

(msec)

stddev

(msec)

(%)

--------------- -------- --------- --------- --------- ---------

------

sendto

27239

267.904

0.002

0.010

0.109

0.28%

recvfrom

69861

212.213

0.001

0.003

0.069

0.23%

ppoll

15478

201.183

0.002

0.013

0.412

0.75%

[...]

The output shows syscall counts and timing for each thread.
The earlier output showing futex(2) calls is not very interesting in isolation, and running perf(1)
trace on any busy application will produce an avalanche of output. It helps to start with this
summary first, and then to use perf(1) trace with a filter to inspect only the syscall types of
interest.

I/O Profiling
I/O syscalls are particularly interesting, and some were seen in the previous output. Tracing the
sendto(2) calls using a filter (-e):


5.5 Observability Tools

# perf trace -e sendto -p $(pgrep mysqld)
0.000 ( 0.015 ms): mysqld/14097 sendto(fd: 37<socket:[833323]>, buff:
0x7fbdac072040, len: 12664, flags: DONTWAIT) = 12664
0.451 ( 0.019 ms): mysqld/14097 sendto(fd: 37<socket:[833323]>, buff:
0x7fbdac072040, len: 12664, flags: DONTWAIT) = 12664
0.624 ( 0.011 ms): mysqld/14097 sendto(fd: 37<socket:[833323]>, buff:
