7.4.1

Tools Method

The tools method is a process of iterating over available tools, examining key metrics they provide. This is a simple methodology that may overlook issues for which the tools you happen to
have available provide poor or no visibility, and can be time-consuming to perform.
For memory, the tools method can involve checking the following for Linux:
■

■

■

■

Page scanning: Look for continual page scanning (more than 10 seconds) as a sign of
memory pressure. This can be done using sar -B and checking the pgscan columns.
Pressure stall information (PSI): cat /proc/pressure/memory (Linux 4.20+) to check
memory pressure (saturation) statistics and how it is changing over time.
Swapping: If swap is configured, the swapping of memory pages (Linux definition of
swapping) is a further indication that the system is low on memory. You can use vmstat(8)
and check the si and so columns.
vmstat: Run vmstat 1 and check the free column for available memory.

323

324

Chapter 7 Memory

■

■

■

OOM killer: These events can be seen in the system log /var/log/messages, or from
dmesg(1). Search for “Out of memory.”
top: See which processes and users are the top physical memory consumers (resident) and
virtual memory consumers (see the man page for the names of the columns, which differ
depending on version). top(1) also summarizes free memory.
perf(1)/BCC/bpftrace: Trace memory allocations with stack traces, to identify the cause
of memory usage. Note that this can cost considerable overhead. A cheaper, though coarse,
solution is to perform CPU profiling (timed stack sampling) and search for allocation
code paths.

See Section 7.5, Observability Tools, for more about each tool.
