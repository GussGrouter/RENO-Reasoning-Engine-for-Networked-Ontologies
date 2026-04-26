4.2.1 Fixed Counters
Kernels maintain various counters for providing system statistics. They are usually implemented
as unsigned integers that are incremented when events occur. For example, there are counters
for the number of network packets received, disk I/O issued, and interrupts that occurred. These
are exposed by monitoring software as metrics (see Section 4.2.4, Monitoring).
A common kernel approach is to maintain a pair of cumulative counters: one to count events
and the other to record the total time in the event. These provide the count of events directly

133

134

Chapter 4 Observability Tools

and the average time (or latency) in the event, by dividing the total time by the count. Since
they are cumulative, by reading the pair at a time interval (e.g., one second) the delta can be
calculated, and from that the per-second count and average latency. This is how many system
statistics are calculated.
Performance-wise, counters are considered “free” to use since they are enabled by default and
maintained continually by the kernel. The only additional cost when using them is the act of
reading their values from user-space (which should be negligible). The following example tools
read these system-wide or per process.

System-Wide
These tools examine system-wide activity in the context of system software or hardware
resources, using kernel counters. Linux tools include:
■

vmstat(8): Virtual and physical memory statistics, system-wide

■

mpstat(1): Per-CPU usage

■

iostat(1): Per-disk I/O usage, reported from the block device interface

■

nstat(8): TCP/IP stack statistics

■

sar(1): Various statistics; can also archive them for historical reporting

These tools are typically viewable by all users on the system (non-root). Their statistics are also
commonly graphed by monitoring software.
Many follow a usage convention where they accept an optional interval and count, for example,
vmstat(8) with an interval of one second and an output count of three:
$ vmstat 1 3
procs -----------memory---------- ---swap-- -----io---- -system-- ------cpu----r

b

4

0 1446428 662012 142100 5644676

swpd

free

buff

cache

si
1

so
4

bi
28

bo
152

in

cs us sy id wa st
1 29

8 63

0

0

4

0 1446428 665988 142116 5642272

0

0

0

284 4957 4969 51

0 48

0

0

4

0 1446428 685116 142116 5623676

0

0

0

0 4488 5507 52

0 48

0

0

33

The first line of output is the summary-since-boot, which shows averages for the entire time
the system has been up. The subsequent lines are the one-second interval summaries, showing
current activity. At least, this is the intent: this Linux version mixes summary-since-boot and
current values for the first line (the memory columns are current values; vmstat(8) is explained
in Chapter 7).

Per-Process
These tools are process-oriented and use counters that the kernel maintains for each process.
Linux tools include:
■

ps(1): Shows process status, shows various process statistics, including memory and
CPU usage.

4.2 Tool Types

■

top(1): Shows top processes, sorted by CPU usage or another statistic.

■

pmap(1): Lists process memory segments with usage statistics.

These tools typically read statistics from the /proc file system.
