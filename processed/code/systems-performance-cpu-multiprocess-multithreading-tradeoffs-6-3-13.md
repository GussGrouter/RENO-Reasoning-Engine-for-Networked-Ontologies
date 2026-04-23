<!-- pdftotext -f 231 -l 285 Systems.Performance.Enterprise.and.the.Cloud.pdf (Chapter 6 CPUs continues) -->

6.3.13 Multiprocess, Multithreading
Most processors provide multiple CPUs of some form. For an application to make use of them,
it needs separate threads of execution so that it can run in parallel. For a 64-CPU system, for
example, this may mean that an application can execute up to 64 times faster if it can make use
of all CPUs in parallel, or handle 64 times the load. The degree to which the application can
effectively scale with an increase in CPU count is a measure of scalability.
The two techniques to scale applications across CPUs are multiprocess and multithreading, which
are pictured in Figure 6.4. (Note that this is software multithreading, and not the hardwarebased SMT mentioned earlier.)

227

228

Chapter 6 CPUs

Figure 6.4 Software CPU scalability techniques
On Linux both the multiprocess and multithread models may be used, and both are implemented
by tasks.
Differences between multiprocess and multithreading are shown in Table 6.1.

Table 6.1

Multiprocess and multithreading attributes

Attribute

Multiprocess

Multithreading

Development

Can be easier. Use of fork(2) or
clone(2).

Use of threads API (pthreads).

Memory overhead

Separate address space per process
consumes some memory resources
(reduced to some degree by pagelevel copy-on-write).

Small. Requires only extra
stack and register space, and
space for thread-local data.

CPU overhead

Cost of fork(2)/clone(2)/exit(2), which
includes MMU work to manage
address spaces.

Small. API calls.

Communication

Via IPC. This incurs CPU cost including
context switching for moving data
between address spaces, unless
shared memory regions are used.

Fastest. Direct access to
shared memory. Integrity via
synchronization primitives
(e.g., mutex locks).

Crash resilience

High, processes are independent.

Low, any bug can crash the
entire application.

Memory Usage

While some memory may be duplicated, Via system allocator. This may
separate processes can exit(2) and
incur some CPU contention
return all memory back to the system. from multiple threads, and
fragmentation before memory
is reused.

With all the advantages shown in the table, multithreading is generally considered superior,
although more complicated for the developer to implement. Multithreaded programming is
covered in [Stevens 13].
