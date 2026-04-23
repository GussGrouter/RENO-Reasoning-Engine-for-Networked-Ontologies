<!-- pdftotext -f 231 -l 285 Systems.Performance.Enterprise.and.the.Cloud.pdf (Chapter 6 CPUs continues) -->

6.4.2 Software
Kernel software to support CPUs includes the scheduler, scheduling classes, and the idle thread.

Scheduler
Key functions of the kernel CPU scheduler are shown in Figure 6.12.

Figure 6.12 Kernel CPU scheduler functions
These functions are:
■

■

■

Time sharing: Multitasking between runnable threads, executing those with the highest
priority first.
Preemption: For threads that have become runnable at a high priority, the scheduler can
preempt the currently running thread, so that execution of the higher-priority thread can
begin immediately.
Load balancing: Moving runnable threads to the run queues of idle or less-busy CPUs.

Figure 6.12 shows run queues, which is how scheduling was originally implemented. The term
and mental model are still used to describe waiting tasks. However, the Linux CFS scheduler
actually uses a red/black tree of future task execution.

241

242

Chapter 6 CPUs
In Linux, time sharing is driven by the system timer interrupt by calling scheduler_tick(), which
calls scheduler class functions to manage priorities and the expiration of units of CPU time called
time slices. Preemption is triggered when threads become runnable and the scheduler class
check_preempt_curr() function is called. Thread switching is managed by __schedule(), which
selects the highest-priority thread via pick_next_task() for running. Load balancing is performed
by the load_balance() function.
The Linux scheduler also uses logic to avoid migrations when the cost is expected to exceed the
benefit, preferring to leave busy threads running on the same CPU where the CPU caches should
still be warm (CPU affinity). In the Linux source, see the idle_balance() and task_hot() functions.
Note that all these function names may change; refer to the Linux source code, including documentation in the Documentation directory, for more detail.
