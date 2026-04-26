7.2.7

Utilization and Saturation

Main memory utilization can be calculated as used memory versus total memory. Memory used
by the file system cache can be treated as unused, as it is available for reuse by applications.
If demands for memory exceed the amount of main memory, main memory becomes saturated.
The operating system may then free memory by employing paging, process swapping (if supported), and, on Linux, the OOM killer (described later). Any of these activities is an indicator of
main memory saturation.
Virtual memory can also be studied in terms of capacity utilization, if the system imposes a limit
on the amount of virtual memory it is willing to allocate (Linux overcommit does not). If so,
once virtual memory is exhausted, the kernel will fail allocations; for example, malloc(3) fails
with errno set to ENOMEM.
Note that the currently available virtual memory on a system is sometimes (confusingly) called
available swap.
