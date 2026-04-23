<!-- pdftotext -f 231 -l 285 Systems.Performance.Enterprise.and.the.Cloud.pdf (Chapter 6 CPUs begins in this extract) -->
affinity. On NUMA systems, per-CPU run queues also improve memory locality. This improves
performance by keeping threads running on the same memory node (as described in Chapter 7,
Memory), and avoids the cost of thread synchronization (mutex locks) for queue operations,
which would hurt scalability if the run queue was global and shared among all CPUs.


6.3

Concepts

6.3 Concepts
The following are a selection of important concepts regarding CPU performance, beginning
with a summary of processor internals: the CPU clock rate and how instructions are executed. This is background for later performance analysis, particularly for understanding the
instructions-per-cycle (IPC) metric.

