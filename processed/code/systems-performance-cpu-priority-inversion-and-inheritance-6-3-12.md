<!-- pdftotext -f 231 -l 285 Systems.Performance.Enterprise.and.the.Cloud.pdf (Chapter 6 CPUs continues) -->

6.3.12 Priority Inversion
Priority inversion occurs when a lower-priority thread holds a resource and blocks a higherpriority thread from running. This reduces the performance of the higher-priority work, as it
is blocked waiting.
This can be solved using a priority inheritance scheme. Here is an example of how this can work
(based on a real-world case):
1. Thread A performs monitoring and has a low priority. It acquires an address space lock for
a production database, to check memory usage.
2. Thread B, a routine task to perform compression of system logs, begins running.
3. There is insufficient CPU to run both. Thread B preempts A and runs.
4. Thread C is from the production database, has a high priority, and has been sleeping waiting for I/O. This I/O now completes, putting thread C back into the runnable state.
5. Thread C preempts B, runs, but then blocks on the address space lock held by thread A.
Thread C leaves CPU.
6. The scheduler picks the next-highest-priority thread to run: B.
7. With thread B running, a high-priority thread, C, is effectively blocked on a lower-priority
thread, B. This is priority inversion.
8. Priority inheritance gives thread A thread C’s high priority, preempting B, until it releases
the lock. Thread C can now run.
Linux since 2.6.18 has provided a user-level mutex that supports priority inheritance, intended
for real-time workloads [Corbet 06a].

