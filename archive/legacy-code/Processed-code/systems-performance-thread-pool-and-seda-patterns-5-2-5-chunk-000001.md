at the same time. This is parallelism, which an application may accomplish by using multiple
processes (multiprocess) or multiple threads (multithreaded), each performing its own task. For
reasons explained in Chapter 6, CPUs, Section 6.3.13, Multiprocess, Multithreading, multiple
threads (or the equivalent tasks) are more efficient and are therefore the preferred approach.
Apart from increased throughput of CPU work, multiple threads (or processes) is one way to
allow I/O to be performed concurrently, as other threads can execute while a thread blocked on
I/O waits. (The other way is asynchronous I/O.)

177

178

Chapter 5 Applications

The use of multiprocess or multithreaded architectures means allowing the kernel to decide
who to run, via the CPU scheduler, and with the cost of context-switch overheads. A different
approach is for the user-mode application to implement its own scheduling mechanism and
program model so that it can service different application requests (or programs) in the same OS
thread. Mechanisms include:
■

