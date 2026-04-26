7.2.4

Overcommit

Linux supports the notion of overcommit, which allows more memory to be allocated than the
system can possibly store—more than physical memory and swap devices combined. It relies
on demand paging and the tendency of applications to not use much of the memory they have
allocated.
With overcommit, application requests for memory (e.g., malloc(3)) will succeed when they
would otherwise have failed. Instead of allocating memory conservatively to remain within
virtual memory limits, an application programmer can allocate memory generously and later
use it sparsely on demand.
On Linux, the behavior of overcommit can be configured with a tunable parameter. See
Section 7.6, Tuning, for details. The consequences of overcommit depend on how the kernel
manages memory pressure; see the discussion of the OOM killer in Section 7.3, Architecture.
