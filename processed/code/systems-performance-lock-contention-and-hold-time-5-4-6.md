<!-- pdftotext -f 231 -l 285 Systems.Performance.Enterprise.and.the.Cloud.pdf -->
5.4.6 Lock Analysis
For multithreaded applications, locks can become a bottleneck, inhibiting parallelism and
scalability. Single-threaded applications can be inhibited by kernel locks (e.g., file system locks).
Locks can be analyzed by:
■

Checking for contention

■

Checking for excessive hold times

The first identifies whether there is a problem now. Excessive hold times are not necessarily an
immediate problem, but they may become so in the future with more parallel load. For each, try
to identify the name of the lock (if it exists) and the code path that led to using it.
While there are special-purpose tools for lock analysis, you can sometimes solve issues from CPU
profiling alone. For spin locks, contention shows up as CPU usage and can easily be identified
using CPU profiling of stack traces. For adaptive mutex locks, contention often involves some
spinning, which can also be identified by CPU profiling of stack traces. In that case, be aware
that the CPU profile gives only a part of the story, as threads may have blocked and slept while
waiting for the locks. See Section 5.4.1, CPU Profiling.
