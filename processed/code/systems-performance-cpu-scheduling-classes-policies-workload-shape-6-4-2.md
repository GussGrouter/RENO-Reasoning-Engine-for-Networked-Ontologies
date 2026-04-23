<!-- pdftotext -f 231 -l 285 Systems.Performance.Enterprise.and.the.Cloud.pdf (Chapter 6 CPUs continues) -->

Scheduling Classes
Scheduling classes manage the behavior of runnable threads, specifically their priorities,
whether their on-CPU time is time-sliced, and the duration of those time slices (also known as
time quanta). There are also additional controls via scheduling policies, which may be selected
within a scheduling class and can control scheduling between threads of the same priority.
Figure 6.13 depicts them for Linux along with the thread priority range.

Figure 6.13 Linux thread scheduler priorities
The priority of user-level threads is affected by a user-defined nice value, which can be set to
lower the priority of unimportant work (so as to be nice to other system users). In Linux, the nice
value sets the static priority of the thread, which is separate from the dynamic priority that the
scheduler calculates.
For Linux kernels, the scheduling classes are:
■

RT: Provides fixed and high priorities for real-time workloads. The kernel supports both
user- and kernel-level preemption, allowing RT tasks to be dispatched with low latency.
The priority range is 0–99 (MAX_RT_PRIO-1).

6.4

■

■

■

■

Architecture

O(1): The O(1) scheduler was introduced in Linux 2.6 as the default time-sharing scheduler
for user processes. The name comes from the algorithm complexity of O(1) (see Chapter 5,
Applications, for a summary of big O notation). The prior scheduler contained routines
that iterated over all tasks, making it O(n), which became a scalability issue. The O(1)
scheduler dynamically improved the priority of I/O-bound over CPU-bound workloads, to
reduce the latency of interactive and I/O workloads.
CFS: Completely fair scheduling was added to the Linux 2.6.23 kernel as the default
time-sharing scheduler for user processes. The scheduler manages tasks on a red-black tree
keyed from the task CPU time, instead of traditional run queues. This allows low CPU consumers to be easily found and executed in preference to CPU-bound workloads, improving
the performance of interactive and I/O-bound workloads.
Idle: Runs threads with the lowest possible priority.
Deadline: Added to Linux 3.14, applies earliest deadline first (EDF) scheduling using three
parameters: runtime, period, and deadline. A task should receive runtime microseconds of
CPU time every period microseconds, and do so within the deadline.

To select a scheduling class, user-level processes select a scheduling policy that maps to a class,
using either the sched_setscheduler(2) syscall or the chrt(1) tool.
Scheduler policies are:
■

■

■

■

RR: SCHED_RR is round-robin scheduling. Once a thread has used its time quantum, it
is moved to the end of the run queue for that priority level, allowing others of the same
priority to run. Uses the RT scheduling class.
FIFO: SCHED_FIFO is first-in, first-out scheduling, which continues running the thread
at the head of the run queue until it voluntarily leaves, or until a higher-priority thread
arrives. The thread continues to run, even if other threads of the same priority are on the
run queue. Uses the RT class.
NORMAL: SCHED_NORMAL (previously known as SCHED_OTHER) is time-sharing
scheduling and is the default for user processes. The scheduler dynamically adjusts priority based on the scheduling class. For O(1), the time slice duration is set based on the static
priority: longer durations for higher-priority work. For CFS, the time slice is dynamic. Uses
the CFS scheduling class.
BATCH: SCHED_BATCH is similar to SCHED_NORMAL, but with the expectation that
the thread will be CPU-bound and should not be scheduled to interrupt other I/O-bound
interactive work. Uses the CFS scheduling class.

■

IDLE: SCHED_IDLE uses the Idle scheduling class.

■

DEADLINE: SCHED_DEADLINE uses the Deadline scheduling class.

Other classes and policies may be added over time. Scheduling algorithms have been researched
that are hyperthreading-aware [Bulpin 05] and temperature-aware [Otto 06], which optimize performance by accounting for additional processor factors.
When there is no thread to run, a special idle task (also called idle thread) is executed as a placeholder until another thread is runnable.
