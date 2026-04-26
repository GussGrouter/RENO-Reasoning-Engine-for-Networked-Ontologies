<!-- pdftotext -f 286 -l 320 Systems.Performance.Enterprise.and.the.Cloud.pdf (Chapter 6 CPUs) -->

This is a selection of tools and capabilities to support Section 6.5, Methodology. We begin with
traditional tools for CPU statistics, then proceed to tools for deeper analysis using code-path
profiling, CPU cycle analysis, and tracing tools. Some of the traditional tools are likely available
on (and sometimes originated on) other Unix-like operating systems, including: uptime(1),
vmstat(8), mpstat(1), sar(1), ps(1), top(1), and time(1). The tracing tools are based on BPF and the
BCC and bpftrace frontends (Chapter 15), and are: profile(8), cpudist(8), runqlat(8), runqlen(8),
softirqs(8), and hardirqs(8).
See the documentation for each tool, including its man pages, for full references for its features.

6.6.1 uptime
uptime(1) is one of several commands that print the system load averages:
$ uptime
9:04pm

up 268 day(s), 10:16,

2 users,

load average: 7.76, 8.32, 8.60

The last three numbers are the 1-, 5-, and 15-minute load averages. By comparing the three numbers, you can determine if the load is increasing, decreasing, or steady during the last 15 minutes
(or so). This can be useful to know: if you are responding to a production performance issue and
find that the load is decreasing, you may have missed the issue; if the load is increasing, the issue
may be getting worse!
The following sections explain load averages in more detail, but they are only a starting point,
so you shouldn’t spend more than five minutes considering them before moving on to other
metrics.

Load Averages
The load averages indicate the demand for system resources: higher means more demand. On
some operating systems (e.g., Solaris) the load averages show CPU demand, as did early versions of
Linux. But in 1993, Linux changed load averages to show system-wide demand: CPUs, disks, and

255

256

Chapter 6 CPUs

other resources.9 This was implemented by including threads in the TASK_UNINTERRUPTIBLE
thread state, shown by some tools as state “D” (this state was mentioned in Chapter 5,
Applications, Section 5.4.5, Thread State Analysis).
The load is measured as the current resource usage (utilization) plus queued requests (saturation).
Imagine a car toll plaza: you could measure the load at various points during the day by counting
how many cars were being serviced (utilization) plus how many cars were queued (saturation).
The average is an exponentially damped moving average, which reflects load beyond the 1-, 5-,
and 15-minute times (the times are actually constants used in the exponential moving sum
[Myer 73]). Figure 6.17 shows the results of a simple experiment where a single CPU-bound
thread was launched and the load averages plotted.

Figure 6.17 Exponentially damped load averages
By the 1-, 5-, and 15-minute marks, the load averages had reached about 61% of the known load
of 1.0.
Load averages were introduced to Unix in early BSD and were based on scheduler average queue
length and load averages commonly used by earlier operating systems (CTSS, Multics [Saltzer 70],
TENEX [Bobrow 72]). They were described in RFC 546 [Thomas 73]:
[1] The TENEX load average is a measure of CPU demand. The load average is an
average of the number of runable processes over a given time period. For example, an
hourly load average of 10 would mean that (for a single CPU system) at any time during
that hour one could expect to see 1 process running and 9 others ready to run (i.e., not
blocked for I/O) waiting for the CPU.
9

The change happened so long ago that the reason for it had been forgotten and was undocumented, predating the
Linux history in git and other resources; I eventually found the original patch in an online tarball from an old mail
system archive. Matthias Urlichs made that change, pointing out that if demand moved from CPUs to disks, then the
load averages should stay the same because the demand hadn’t changed [Gregg 17c]. I emailed him (for the first
time ever) about his 24-year old change, and got a reply in one hour!

6.6 Observability Tools

As a modern example, consider a 64-CPU system with a load average of 128. If the load was CPU
only, it would mean that on average there is always one thread running on each CPU, and one
thread waiting for each CPU. The same system with a CPU load average of 20 would indicate
significant headroom, as it could run another 44 CPU-bound threads before all CPUs are busy.
(Some companies monitor a normalized load average metric, where it is automatically divided by
the CPU count, allowing it to be interpreted without knowing the CPU count.)

Pressure Stall Information (PSI)
In the first edition of this book, I described how load averages could be provided for each resource
type to aid interpretation. An interface has now been added in Linux 4.20 that provides such
a breakdown: pressure stall information (PSI), which gives averages for CPU, memory, and I/O.
The average shows the percent of time something was stalled on a resource (saturation only).
This is compared with load averages in Table 6.9.

Table 6.9

Linux load averages versus pressure stall information

Attribute

Load Averages

Pressure Stall Information

Resources

System-wide

cpu, memory, io (each individually)

Metric

Number of busy and queued tasks

Percent of time stalled (waiting)

Times

1 min, 5 min, 15 min

10 s, 60 s, 300 s

Average

Exponentially damped moving sum

Exponentially damped moving sum

Table 6.10 shows what the metric shows for different scenarios:

Table 6.10

Linux load average examples versus pressure stall information

Example Scenario

Load Averages

Pressure Stall Information

2 CPUs, 1 busy thread

1.0

0.0

2 CPUs, 2 busy threads

2.0

0.0

2 CPUs, 3 busy threads

3.0

50.0

2 CPUs, 4 busy threads

4.0

100.0

2 CPUs, 5 busy threads

5.0

100.0

For example, showing the 2 CPU with 3 busy threads scenario:
$ uptime
07:51:13 up 4 days,

9:56,

2 users,

load average: 3.00, 3.00, 2.55

$ cat /proc/pressure/cpu
some avg10=50.00 avg60=50.00 avg300=49.70 total=1031438206

257

258

Chapter 6 CPUs

This 50.0 value means a thread (“some”) has stalled 50% of the time. The io and memory metrics
include a second line for when all non-idle threads have stalled (“full”). PSI best answers the
question: how likely is it that a task will have to wait on the resources?
Whether you use load averages or PSI, you should quickly move to more detailed metrics to
understand load, such as those provided by vmstat(1) and mpstat(1).

6.6.2 vmstat
The virtual memory statistics command, vmstat(8), prints system-wide CPU averages in the last
few columns, and a count of runnable threads in the first column. Here is example output from
the Linux version:
$ vmstat 1
procs -----------memory---------- ---swap-- -----io---- -system-- ------cpu----r

b

cache

si

so

bi

bo

in

cs us sy id wa st

15

0

swpd

0 451732

free

70588 866628

buff

0

0

1

10

43

38

15

0

0 450968

70588 866628

0

0

0

612 1064 2969 72 28

15

0

0 450660

70588 866632

0

0

0

0

15

0

0 450952

70588 866632

0

0

0

2

1 97

0

0

0

0

0

961 2932 72 28

0

0

0

0 1015 3238 74 26

0

0

0

[...]

The first line of output is supposed to be the summary-since-boot. However, on Linux the procs
and memory columns begin by showing the current state. (Perhaps one day they will be fixed.)
CPU-related columns are:
■

r: Run-queue length—the total number of runnable threads

■

us: User-time percent

■

sy: System-time (kernel) percent

■

id: Idle percent

■

wa: Wait I/O percent, which measures CPU idle when threads are blocked on disk I/O

■

st: Stolen percent, which for virtualized environments shows CPU time spent servicing
other tenants

All of these values are system-wide averages across all CPUs, with the exception of r, which is the
total.
On Linux, the r column is the total number of tasks waiting plus those running. For other
operating systems (e.g., Solaris) the r column only shows tasks waiting, not those running. The
original vmstat(1) by Bill Joy and Ozalp Babaoglu for 3BSD in 1979 begins with an RQ column
for the number of runnable and running processes, as the Linux vmstat(8) currently does.

6.6 Observability Tools

6.6.3 mpstat
The multiprocessor statistics tool, mpstat(1), can report statistics per CPU. Here is example output from the Linux version:
$ mpstat -P ALL 1
Linux 5.3.0-1009-aws (ip-10-0-239-218)

02/01/20

_x86_64_

(2 CPU)

18:00:32

CPU

%usr

%nice

%sys %iowait

%irq

%soft %steal %guest %gnice

%idle

18:00:33

all

32.16

0.00

61.81

0.00

0.00

0.00

0.00

0.00

0.00

6.03

18:00:33

0

32.00

0.00

64.00

0.00

0.00

0.00

0.00

0.00

0.00

4.00

18:00:33

1

32.32

0.00

59.60

0.00

0.00

0.00

0.00

0.00

0.00

8.08

18:00:33

CPU

%usr

%nice

%sys %iowait

%irq

%soft %steal %guest %gnice

%idle

18:00:34

all

33.83

0.00

61.19

0.00

0.00

0.00

0.00

0.00

0.00

4.98

18:00:34

0

34.00

0.00

62.00

0.00

0.00

0.00

0.00

0.00

0.00

4.00

18:00:34

1

33.66

0.00

60.40

0.00

0.00

0.00

0.00

0.00

0.00

5.94

[...]

The -P ALL option was used to print the per-CPU report. By default, mpstat(1) prints only the
system-wide summary line (all). The columns are:
■

CPU: Logical CPU ID, or all for summary

■

%usr: User-time, excluding %nice

■

%nice: User-time for processes with a nice’d priority

■

%sys: System-time (kernel)

■

%iowait: I/O wait

■

%irq: Hardware interrupt CPU usage

■

%soft: Software interrupt CPU usage

■

%steal: Time spent servicing other tenants

■

%guest: CPU time spent in guest virtual machines

■

%gnice: CPU time to run a niced guest

■

%idle: Idle

Key columns are %usr, %sys, and %idle. These identify CPU usage per CPU and show the usertime/kernel-time ratio (see Section 6.3.9, User-Time/Kernel-Time). This can also identify “hot”
CPUs—those running at 100% utilization (%usr + %sys) while others are not—which can be
caused by single-threaded application workloads or device interrupt mapping.
Note that the CPU times reported by this and other tools that source the same kernel statistics
(/proc/stat etc.), and the accuracy of these statistics depends on the kernel configuration. See the
CPU Statistic Accuracy heading in Chapter 4, Observability Tools, Section 4.3.1, /proc.

259

260

Chapter 6 CPUs

6.6.4 sar
The system activity reporter, sar(1), can be used to observe current activity and can be configured
to archive and report historical statistics. It was introduced in Chapter 4, Observability Tools,
Section 4.4, sar, and is mentioned in other chapters as appropriate.
The Linux version provides the following options for CPU analysis:
■

-P ALL: Same as mpstat -P ALL

■

-u: Same as mpstat(1)’s default output: system-wide average only

■

-q: Includes run-queue size as runq-sz (waiting plus running, the same as vmstat(1)’s r)
and load averages

sar(1) data collection may be enabled so that these metrics can be observed from the past. See
Section 4.4, sar, for more detail.

