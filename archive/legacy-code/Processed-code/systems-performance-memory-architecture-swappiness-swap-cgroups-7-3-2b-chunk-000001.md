The Linux swappiness parameter controls whether to favor freeing memory by paging applications
or by reclaiming it from the page cache. It is a number between 0 and 100 (the default value
is 60), where higher values favor freeing memory by paging. Controlling the balance between
these memory freeing techniques allows system throughput to be improved by preserving warm
file system cache while paging out cold application memory [Corbet 04].
It is also interesting to ask what happens if no swap device or swap file is configured. This limits
virtual memory size, so if overcommit has been disabled, memory allocations will fail sooner.
On Linux, this may also mean that the OOM killer is used sooner.
Consider an application with an issue of endless memory growth. With swap, this is likely to
first become a performance issue due to paging, which is an opportunity to debug the issue live.
Without swap, there is no paging grace period, so either the application hits an “Out of memory”
error or the OOM killer terminates it. This may delay debugging the issue if it is seen only after
hours of usage.
In the Netflix cloud, instances typically do not use swap, so applications are OOM killed if they
exhaust memory. Applications are distributed across a large pool of instances, and having one

7.3

Architecture

OOM killed causes traffic to be immediately redirected to other healthy instances. This is considered preferable to allowing one instance to run slowly due to swapping.
When memory cgroups are used, similar memory freeing techniques can be used as those shown
in Figure 7.6 to manage cgroup memory. A system may have an abundance of free memory, but is
swapping or encountering the OOM killer because a container has exhausted its cgroup-controlled
limit [Evans 17]. For more on cgroups and containers, see Chapter 11, Cloud Computing.
The following sections describe free lists, reaping, and the page-out daemon.
