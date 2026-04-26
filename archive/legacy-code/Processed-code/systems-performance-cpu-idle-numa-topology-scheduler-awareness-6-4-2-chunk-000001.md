<!-- pdftotext -f 231 -l 285 Systems.Performance.Enterprise.and.the.Cloud.pdf (Chapter 6 CPUs continues) -->

Idle Thread
Introduced in Chapter 3, the kernel “idle” thread (or idle task) runs on-CPU when there is no
other runnable thread and has the lowest possible priority. It is usually programmed to inform
the processor that CPU execution may either be halted (halt instruction) or throttled down to
conserve power. The CPU will wake up on the next hardware interrupt.

NUMA Grouping
Performance on NUMA systems can be significantly improved by making the kernel NUMA-aware,
so that it can make better scheduling and memory placement decisions. This can automatically
detect and create groups of localized CPU and memory resources and organize them in a topology to reflect the NUMA architecture. This topology allows the cost of any memory access to be
estimated.
On Linux systems, these are called scheduling domains, which are in a topology beginning with
the root domain.
A manual form of grouping can be performed by the system administrator, either by binding
processes to run on one or more CPUs only, or by creating an exclusive set of CPUs for processes
to run on. See Section 6.5.10, CPU Binding.

Processor Resource-Aware
The CPU resource topology can also be understood by the kernel so that it can make better
scheduling decisions for power management, hardware cache usage, and load balancing.

