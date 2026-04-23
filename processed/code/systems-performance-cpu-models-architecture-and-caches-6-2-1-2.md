<!-- pdftotext -f 231 -l 285 Systems.Performance.Enterprise.and.the.Cloud.pdf (Chapter 6 CPUs begins in this extract) -->

Processor: The physical chip that plugs into a socket on the system or processor board and
contains one or more CPUs implemented as cores or hardware threads.
Core: An independent CPU instance on a multicore processor. The use of cores is a way to
scale processors, called chip-level multiprocessing (CMP).
Hardware thread: A CPU architecture that supports executing multiple threads in parallel on a single core (including Intel’s Hyper-Threading Technology), where each thread is
an independent CPU instance. This scaling approach is called simultaneous multithreading
(SMT).
CPU instruction: A single CPU operation, from its instruction set. There are instructions
for arithmetic operations, memory I/O, and control logic.
Logical CPU: Also called a virtual processor,1 an operating system CPU instance (a schedulable CPU entity). This may be implemented by the processor as a hardware thread (in
which case it may also be called a virtual core), a core, or a single-core processor.
Scheduler: The kernel subsystem that assigns threads to run on CPUs.
Run queue: A queue of runnable threads that are waiting to be serviced by CPUs. Modern
kernels may use some other data structure (e.g., a red-black tree) to store runnable threads,
but we still often use the term run queue.

Other terms are introduced throughout this chapter. The Glossary includes basic terminology for
reference, including CPU, CPU cycle, and stack. Also see the terminology sections in Chapters 2
and 3.

1

It is also sometimes called a virtual CPU; however, that term is more commonly used to refer to virtual CPU
instances provided by a virtualization technology. See Chapter 11, Cloud Computing.


6.2 Models

6.2 Models
The following simple models illustrate some basic principles of CPUs and CPU performance.
Section 6.4, Architecture, digs much deeper and includes implementation-specific details.

6.2.1

CPU Architecture

Figure 6.1 shows an example CPU architecture, for a single processor with four cores and eight
hardware threads in total. The physical architecture is pictured, along with how it is seen by the
