<!-- pdftotext -f 286 -l 320 Systems.Performance.Enterprise.and.the.Cloud.pdf (Chapter 6 CPUs §6.5 continued) -->

6.5.8 Priority Tuning
Unix has always provided a nice(2) system call for adjusting process priority, which sets a niceness value. Positive nice values result in lower process priority (nicer), and negative values—
which can be set only by the superuser (root)7—result in higher priority. A nice(1) command
became available to launch programs with nice values, and a renice(1M) command was later
added (in BSD) to adjust the nice value of already running processes. The man page from Unix
4th edition provides this example [TUHS 73]:
The value of 16 is recommended to users who wish to execute long-running programs
without flak from the administration.
The nice value is still useful today for adjusting process priority. This is most effective when
there is contention for CPUs, causing scheduler latency for high-priority work. Your task is to
identify low-priority work, which may include monitoring agents and scheduled backups, that
can be modified to start with a nice value. Analysis may also be performed to check that the
tuning is effective, and that the scheduler latency remains low for high-priority work.
7
Since Linux 2.6.12, a “nice ceiling” can be modified per process, allowing non-root processes to have lower nice
values. E.g., using: prlimit --nice=-19 -p PID.

6.5 Methodology

Beyond nice, the operating system may provide more advanced controls for process priority such
as changing the scheduler class and scheduler policy, and tunable parameters. Linux includes
a real-time scheduling class, which can allow processes to preempt all other work. While this can
eliminate scheduler latency (other than for other real-time processes and interrupts), make sure
that you understand the consequences. If the real-time application encounters a bug where
multiple threads enter an infinite loop, it can cause all CPUs to become unavailable for all other
work—including the administrative shell required to manually fix the problem.8

6.5.9 Resource Controls
The operating system may provide fine-grained controls for allocating CPU cycles to processes
or groups of processes. These may include fixed limits for CPU utilization and shares for a more
flexible approach—allowing idle CPU cycles to be consumed based on a share value. How these
work is implementation-specific and discussed in Section 6.9, Tuning.

6.5.10

CPU Binding

Another way to tune CPU performance involves binding processes and threads to individual
CPUs, or collections of CPUs. This can increase CPU cache warmth for the process, improving its
memory I/O performance. For NUMA systems it also improves memory locality, further improving performance.
There are generally two ways this is performed:
■

■

CPU binding: Configuring a process to run only on a single CPU, or only on one CPU
from a defined set.
Exclusive CPU sets: Partitioning a set of CPUs that can be used only by the process(es)
assigned to them. This can further improve CPU cache warmth, as when the process is idle
other processes cannot use those CPUs.

On Linux-based systems, the exclusive CPU sets approach can be implemented using cpusets.
Configuration examples are provided in Section 6.9, Tuning.
