<!-- pdftotext -f 231 -l 285 Systems.Performance.Enterprise.and.the.Cloud.pdf -->

5.4 Methodology

Once you’ve established in which states the threads are spending their time, you can investigate
them further:
■

■

■

■

■

■

■

User or Kernel: Profiling can determine which code paths are consuming CPU, including
time spent spinning on locks. See Section 5.4.1, CPU Profiling.
Runnable: Time in this state means the application wants more CPU resources. Examine
CPU load for the entire system, and any CPU limits present for the application (e.g.,
resource controls).
Swapping (anonymous paging): A lack of available main memory for the application can
cause swapping delays. Examine memory usage for the entire system and any memory
limits present. See Chapter 7, Memory, for details.
Disk: This state includes direct disk I/O and page faults. To analyze, see Section 5.4.3,
Syscall Analysis, Chapter 8, File Systems, and Chapter 9, Disks. Workload characterization
can help solve many disk I/O problems; examine file names, I/O sizes, and I/O types.
Network: This state is for time blocked during network I/O (send/receive), but not listening for new connections (that’s idle time). To analyze, see Section 5.4.3, Syscall Analysis;
Section 5.5.7, bpftrace and the I/O Profiling heading; and Chapter 10, Network. Workload
characterization can also be useful for network I/O problems; examine hostnames, protocols, and throughput.
Sleeping: Analyze the reason (code path) and duration of the sleeps.
Lock: Identify the lock, the thread holding it, and the reason why the holder held it for
so long. The reason may be that the holder was blocked on another lock, which requires
further unwinding. This is an advanced activity, usually performed by the software
developer who has intimate knowledge of the application and its locking hierarchy. I
have developed a BCC tool to aid this type of analysis: offwaketime(8) (included in BCC),
which shows the blocking stack trace along with the waker.

Because of how applications typically wait for work, you will often find that time in the network
I/O and lock states is actually idle time. An application worker thread may implement idle by
waiting on network I/O for the next request (e.g., HTTP keep-alive) or by waiting on a conditional variable (lock state) to be woken up to process work.
The following summarizes how these thread states may be measured on Linux.

Linux
Figure 5.7 shows a Linux thread state model based on kernel thread state.
The kernel thread state is based on the kernel task_struct state member: Runnable is TASK_
RUNNING, Disk is TASK_UNINTERRUPTIBLE, and Sleep is TASK_INTERRUPTIBLE. These states
are shown by tools including ps(1) and top(1) using single-letter codes: R, D, and S, respectively.
(There are more states, such as stopped by a debugger, that I did not include here.)
While this provides some clues for further analysis, it is far from dividing time into the nine
states described earlier. More information is required: for example, Runnable can be split into
user and kernel time using /proc or getrusage(2) statistics.

195


196

Chapter 5 Applications

Figure 5.7 Linux thread states
Other kernels typically provide more states, making this methodology easier to apply. I originally developed and used this methodology on the Solaris kernel, inspired by its microstate
accounting feature, which recorded thread time in eight different states: user, system, trap, text
fault, data fault, lock, sleep, and run queue (scheduler latency). These don’t match my ideal
states, but are a better starting point.
I’ll discuss three approaches that I use on Linux: clue-based, off-CPU analysis, and direct
measurement.

Clue-Based
You can start by using common OS tools, such as pidstat(1) and vmstat(8), to suggest where
thread state time may be spent. The tools and column of interest are:
■

User: pidstat(1) “%usr” (this state is measured directly)

■

Kernel: pidstat(1) “%system” (this state is measured directly)

■

Runnable: vmstat(8) “r” (system-wide)

■

Swapping: vmstat(8) “si” and “so” (system-wide)

■

Disk I/O: pidstat(1) -d “iodelay” (includes the swapping state)

■

Network I/O: sar(1) -n DEV “rxkB/s” and “txkB/s” (system-wide)

■

Sleeping: Not easily available

■

Lock: perf(1) top (may identify spin lock time directly)

■

Idle: Not easily available

Some of these statistics are system-wide. If you find via vmstat(8) that there is a system-wide rate
of swapping, you could investigate that state using deeper tools to confirm that the application
is affected. These tools are covered in the following sections and chapters.


5.4 Methodology

Off-CPU Analysis
As many of the states are off-CPU (everything except User and Kernel), you can apply off-CPU
analysis to determine the thread state. See Section 5.4.2, Off-CPU Analysis.

Direct Measurement
Measure thread time accurately by thread state as follows:
User: User-mode CPU is available from a number of tools and in /proc/PID/stat and getrusage(2).
pidstat(1) reports this as %usr.
Kernel: Kernel-mode CPU is also in /proc/PID/stat and getrusage(2). pidstat(1) reports this as
%system.
Runnable: This is tracked by the kernel schedstats feature in nanoseconds and is exposed via
/proc/PID/schedstat. It can also be measured, at the cost of some overhead, using tracing tools
including the perf(1) sched subcommand and BCC runqlat(8), both covered in Chapter 6, CPUs.
Swapping: Time swapping (anonymous paging) in nanoseconds can be measured by delay
accounting, introduced in Chapter 4, Observability Tools, Section 4.3.3, Delay Accounting,
which included an example tool: getdelays.c. Tracing tools can also be used to instrument swapping latency.
Disk: pidstat(1) -d shows “iodelay” as the number of clock ticks during which a process was
delayed by block I/O and swapping; if there was no system-wide swapping (as reported by
vmstat(8)), you could conclude that any iodelay was the I/O state. Delay accounting and other
accounting features, if enabled, also provide block I/O time, as used by iotop(8). You can also use
tracing tools such as biotop(8) from BCC.
Network: Network I/O can be investigated using tracing tools such as BCC and bpftrace, including the tcptop(8) tool for TCP network I/O. The application may also have instrumentation to
track time in I/O (network and disk).
Sleeping: Time entering voluntary sleep can be examined using tracers and events including the
syscalls:sys_enter_nanosleep tracepoint. My naptime.bt tool traces these sleeps and prints the
PID and duration [Gregg 19][Gregg 20b].
Lock: Lock time can be investigated using tracing tools, including klockstat(8) from BCC and,
from the bpf-perf-tools-book repository, pmlock.bt and pmheld.bt for pthread mutex locks, and
mlock.bt and mheld.bt for kernel mutexes.
Idle: Tracing tools can be used to instrument the application code paths that handle waiting for
work.
