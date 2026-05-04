<!-- pdftotext -f 321 -l 360 Systems.Performance.Enterprise.and.the.Cloud.pdf (Chapter 6 CPUs continued) -->

6.9 Tuning
For CPUs, the biggest performance wins are typically those that eliminate unnecessary work,
which is an effective form of tuning. Section 6.5, Methodology, and Section 6.6, Observability
Tools, introduced many ways to analyze and identify the work performed, helping you find any

6.9

Tuning

unnecessary work. Other methodologies for tuning were also introduced: priority tuning and
CPU binding. This section includes these and other tuning examples.
The specifics of tuning—the options available and what to set them to—depend on the processor type, the operating system version, and the intended workload. The following, organized by
type, provide examples of what options may be available and how they are tuned. The earlier
methodology sections provide guidance on when and why these tunables would be tuned.

6.9.1 Compiler Options
Compilers, and the options they provide for code optimization, can have a dramatic effect on
CPU performance. Common options include compiling for 64-bit instead of 32-bit, and selecting a level of optimizations. Compiler optimization is discussed in Chapter 5, Applications.

6.9.2

Scheduling Priority and Class

The nice(1) command can be used to adjust process priority. Positive nice values decrease priority,
and negative nice values (which only the superuser can set) increase priority. The range is from
-20 to +19. For example:
$ nice -n 19 command

runs the command with a nice value of 19—the lowest priority that nice can set. To change the
priority of an already running process, use renice(1).
On Linux, the chrt(1) command can show and set the scheduling priority directly, and the
scheduling policy. For example:
$ chrt -b command

will run the command in SCHED_BATCH (see Scheduling Classes in Section 6.4.2, Software).
Both nice(1) and chrt(1) can also be directed at a PID instead of launching a command (see their
man pages).
Scheduling priority can also be set directly using the setpriority(2) syscall, and the priority
and scheduling policy can be set using the sched_setscheduler(2) syscall.

6.9.3 Scheduler Options
Your kernel may provide tunable parameters to control scheduler behavior, although it is
unlikely that these will need to be tuned.
On Linux systems, various CONFIG options control scheduler behavior at a high level, and can
be set during kernel compilation. Table 6.12 shows examples from Ubuntu 19.10 and a Linux 5.3
kernel.

295

296

Chapter 6 CPUs

Table 6.12

Example Linux scheduler CONFIG options

Option

Default

Description

CONFIG_CGROUP_SCHED

y

Allows tasks to be grouped, allocating CPU time
on a group basis

CONFIG_FAIR_GROUP_SCHED

y

Allows CFS tasks to be grouped

CONFIG_RT_GROUP_SCHED

n

Allows real-time tasks to be grouped

CONFIG_SCHED_AUTOGROUP

y

Automatically identifies and creates task groups
(e.g., build jobs)

CONFIG_SCHED_SMT

y

Hyperthreading support

CONFIG_SCHED_MC

y

Multicore support

CONFIG_HZ

250

Sets kernel clock rate (timer interrupt)

CONFIG_NO_HZ

y

Tickless kernel behavior

CONFIG_SCHED_HRTICK

y

Use high-resolution timers

CONFIG_PREEMPT

n

Full kernel preemption (except spin lock regions
and interrupts)

CONFIG_PREEMPT_NONE

n

No preemption

CONFIG_PREEMPT_VOLUNTARY

y

Preemption at voluntary kernel code points

There are also scheduler sysctl(8) tunables can be set live on a running system, including those
listed in Table 6.13, with defaults from the same Ubuntu system.

Table 6.13

Example Linux scheduler sysctl(8) tunables

sysctl

Default

Description

kernel.sched_cfs_bandwidth_slice_us

5000

CPU time quanta used for CFS bandwidth
calculations.

kernel.sched_latency_ns

12000000

Targeted preemption latency. Increasing
this can increase a task’s time on-CPU,
at the cost of preemption latency.

kernel.sched_migration_cost_ns

500000

Task migration latency cost, used for
affinity calculations. Tasks that have
run more recently than this value are
considered cache hot.

kernel.sched_nr_migrate

32

Sets how many tasks can be migrated at
a time for load balancing.

kernel.sched_schedstats

0

Enables additional scheduler statistics,
including sched:sched_stat* tracepoints.

These sysctl(8) tunables can also be set from /proc/sys/sched.
