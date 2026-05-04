<!-- Extracted from systems-performance-ch4-scout-p171-220.txt (combined extract; Chapter 5 Applications §5.2.5–5.2.7) -->
each fiber represents a schedulable program. The application can use its own scheduling
logic to choose which fiber to run. These can be used, for example, to allocate a fiber to
handle each application request, with less overhead than doing the same with OS threads.
Microsoft Windows, for example, supports fibers.2
Co-routines: More lightweight than a fiber, a co-routine is a subroutine that can be scheduled by the user-mode application, providing a mechanism for concurrency.
Event-based concurrency: Programs are broken down into a series of event handlers, and
runnable events can be planned on and executed from a queue. These can be used, for
example, by allocating metadata for each application request, which is referenced by event
handlers. For example, the Node.js runtime uses event-based concurrency using a single
event worker thread (which can become a bottleneck, as it can only execute on one CPU).

With all of these mechanisms, I/O must still be handled by the kernel, so OS thread switching
is typically inevitable.3 Also, for parallelism, multiple OS threads must be used so they can be
scheduled across multiple CPUs.
Some runtimes use both co-routines for lightweight concurrency and multiple OS threads for
parallelism. An example is the Golang runtime, which uses goroutines (co-routines) on a pool
of OS threads. To improve performance, when a goroutine makes a blocking call, Golang’s
scheduler automatically moves other goroutines on the blocking thread to other threads to run
[Golang 20].
Three common models of multithreaded programming are:
■

■

■

