                                                                                2.11   Exercises   85




Figure 2.33 Wireframe surface plot: data center CPU utilization

2.10.6       Visualization Tools
Unix performance analysis has historically focused on the use of text-based tools, due in part
to limited graphical support. Such tools can be executed quickly over a login session and report
data in real time. Visualizations have been more time-consuming to access and often require a
trace-and-report cycle. When working urgent performance issues, the speed at which you can
access metrics can be critical.

Modern visualization tools provide real-time views of system performance, accessible from the
browser and mobile devices. There are numerous products that do this, including many that
can monitor your entire cloud. Chapter 1, Introduction, Section 1.7.1, Counters, Statistics, and
Metrics, includes an example screenshot from one such product, Grafana, and other monitoring
products are discussed in Chapter 4, Observability Tools, Section 4.2.4, Monitoring.



2.11         Exercises
1. Answer the following questions about key performance terminology:
   ■   What are IOPS?
   ■   What is utilization?
   ■   What is saturation?
   ■   What is latency?
   ■   What is micro-benchmarking?
86   Chapter 2 Methodologies


     2. Choose five methodologies to use for your (or a hypothetical) environment. Select the order
        in which they can be conducted, and explain the reason for choosing each.

     3. Summarize problems when using average latency as a sole performance metric. Can these
        problems be solved by including the 99th percentile?



     2.12        References
        [Amdahl 67] Amdahl, G., “Validity of the Single Processor Approach to Achieving Large
        Scale Computing Capabilities,” AFIPS, 1967.

        [Jain 91] Jain, R., The Art of Computer Systems Performance Analysis: Techniques for Experimental
        Design, Measurement, Simulation and Modeling, Wiley, 1991.

        [Cockcroft 95] Cockcroft, A., Sun Performance and Tuning, Prentice Hall, 1995.

        [Gunther 97] Gunther, N., The Practical Performance Analyst, McGraw-Hill, 1997.

        [Wong 97] Wong, B., Configuration and Capacity Planning for Solaris Servers, Prentice Hall, 1997.

        [Elling 00] Elling, R., “Static Performance Tuning,” Sun Blueprints, 2000.

        [Millsap 03] Millsap, C., and J. Holt., Optimizing Oracle Performance, O’Reilly, 2003.

        [McDougall 06a] McDougall, R., Mauro, J., and Gregg, B., Solaris Performance and Tools:
        DTrace and MDB Techniques for Solaris 10 and OpenSolaris, Prentice Hall, 2006.

        [Gunther 07] Gunther, N., Guerrilla Capacity Planning, Springer, 2007.

        [Allspaw 08] Allspaw, J., The Art of Capacity Planning, O’Reilly, 2008.

        [Gregg 10a] Gregg, B., “Visualizing System Latency,” Communications of the ACM, July 2010.

        [Gregg 10b] Gregg, B., “Visualizations for Performance Analysis (and More),” USENIX LISA,
        https://www.usenix.org/legacy/events/lisa10/tech/#gregg, 2010.

        [Gregg 11b] Gregg, B., “Utilization Heat Maps,” http://www.brendangregg.com/HeatMaps/
        utilization.html, published 2011.
        [Williams 11] Williams, C., “The $300m Cable That Will Save Traders Milliseconds,” The
        Telegraph, https://www.telegraph.co.uk/technology/news/8753784/The-300m-cable-that-will-
        save-traders-milliseconds.html, 2011.

        [Gregg 13b] Gregg, B., “Thinking Methodically about Performance,” Communications of the
        ACM, February 2013.

        [Gregg 14a] Gregg, B., “Performance Scalability Models,” https://github.com/brendangregg/
        PerfModels, 2014.

        [Harrington 14] Harrington, B., and Rapoport, R., “Introducing Atlas: Netflix’s Primary
        Telemetry Platform,” Netflix Technology Blog, https://medium.com/netflix-techblog/
        introducing-atlas-netflixs-primary-telemetry-platform-bd31f4d8ed9a, 2014.

        [Gregg 15b] Gregg, B., “Heatmaps,” http://www.brendangregg.com/heatmaps.html, 2015.
                                                                             2.12   References    87


[Wilkie 18] Wilkie, T., “The RED Method: Patterns for Instrumentation & Monitoring,”
Grafana Labs, https://www.slideshare.net/grafana/the-red-method-how-to-monitoring-your-
microservices, 2018.

[Eclipse 20] Eclipse Foundation, “Trace Compass,” https://www.eclipse.org/tracecompass,
accessed 2020.

[Wikipedia 20] Wikipedia, “Five Whys,” https://en.wikipedia.org/wiki/Five_whys, accessed
2020.

[Grafana 20] Grafana Labs, “Heatmap,” https://grafana.com/docs/grafana/latest/features/
panels/heatmap, accessed 2020.

[KernelShark 20] “KernelShark,” https://www.kernelshark.org, accessed 2020.

[Kubernetes 20a] Kubernetes, “Horizontal Pod Autoscaler,” https://kubernetes.io/docs/tasks/
run-application/horizontal-pod-autoscale, accessed 2020.

[R Project 20] R Project, “The R Project for Statistical Computing,” https://www.r-project.org,
accessed 2020.
This page intentionally left blank
                                                         Chapter 3
                                     Operating Systems


An understanding of the operating system and its kernel is essential for systems performance
analysis. You will frequently need to develop and then test hypotheses about system behavior,
such as how system calls are being performed, how the kernel schedules threads on CPUs, how
limited memory could be affecting performance, or how a file system processes I/O. These
activities will require you to apply your knowledge of the operating system and the kernel.

The learning objectives of this chapter are:
    ■   Learn kernel terminology: context switches, swapping, paging, preemption, etc.
    ■   Understand the role of the kernel and system calls.
    ■   Gain a working knowledge of kernel internals, including: interrupts, schedulers, virtual
        memory, and the I/O stack.
    ■   See how kernel performance features have been added from Unix to Linux.
    ■   Develop a basic understanding of extended BPF.

This chapter provides an overview of operating systems and kernels and is assumed knowl-
edge for the rest of the book. If you missed operating systems class, you can treat this as a crash
course. Keep an eye out for any gaps in your knowledge, as there will be an exam at the end (I’m
kidding; it’s just a quiz). For more on kernel internals, see the references at the end of
this chapter.

This chapter has three sections:

    ■   Terminology lists essential terms.
    ■   Background summarizes key operating system and kernel concepts.
    ■   Kernels summarizes implementation specifics of Linux and other kernels.

Areas related to performance, including CPU scheduling, memory, disks, file systems, network-
ing, and many specific performance tools, are covered in more detail in the chapters that
follow.
90   Chapter 3 Operating Systems



     3.1        Terminology
     For reference, here is the core operating system terminology used in this book. Many of these are
     also concepts that are explained in more detail in this and later chapters.
         ■   Operating system: This refers to the software and files that are installed on a system so
             that it can boot and execute programs. It includes the kernel, administration tools, and
             system libraries.
         ■   Kernel: The kernel is the program that manages the system, including (depending on the
             kernel model) hardware devices, memory, and CPU scheduling. It runs in a privileged
             CPU mode that allows direct access to hardware, called kernel mode.
         ■   Process: An OS abstraction and environment for executing a program. The program runs
             in user mode, with access to kernel mode (e.g., for performing device I/O) via system calls
             or traps into the kernel.
         ■   Thread: An executable context that can be scheduled to run on a CPU. The kernel has
             multiple threads, and a process contains one or more.
         ■   Task: A Linux runnable entity, which can refer to a process (with a single thread), a thread
             from a multithreaded process, or kernel threads.
         ■   BPF program: A kernel-mode program running in the BPF1 execution environment.
         ■   Main memory: The physical memory of the system (e.g., RAM).
         ■   Virtual memory: An abstraction of main memory that supports multitasking and over-
             subscription. It is, practically, an infinite resource.
         ■   Kernel space: The virtual memory address space for the kernel.
         ■   User space: The virtual memory address space for processes.
         ■   User land: User-level programs and libraries (/usr/bin, /usr/lib...).
         ■   Context switch: A switch from running one thread or process to another. This is a normal
             function of the kernel CPU scheduler, and involves switching the set of running CPU
             registers (the thread context) to a new set.
         ■   Mode switch: A switch between kernel and user modes.
         ■   System call (syscall): A well-defined protocol for user programs to request the kernel to
             perform privileged operations, including device I/O.
         ■   Processor: Not to be confused with process, a processor is a physical chip containing one
             or more CPUs.
         ■   Trap: A signal sent to the kernel to request a system routine (privileged action). Trap types
             include system calls, processor exceptions, and interrupts.




     1
       BPF originally stood for Berkeley Packet Filter, but the technology today has so little to do with Berkeley, packets, or
     filtering that BPF has become a name in itself rather than an acronym.
                                                                               3.2   Background     91


   ■   Hardware interrupt: A signal sent by physical devices to the kernel, usually to request
       servicing of I/O. An interrupt is a type of trap.

The Glossary includes more terminology for reference if needed for this chapter, including
address space, buffer, CPU, file descriptor, POSIX, and registers.



3.2 Background
The following sections describe generic operating system and kernel concepts, and will help you
understand any operating system. To aid your comprehension, this section includes some Linux
implementation details. The next sections, 3.3 Kernels, and 3.4 Linux, focus on Unix, BSD, and
Linux kernel implementation specifics.


3.2.1 Kernel
The kernel is the core software of the operating system. What it does depends on the kernel
model: Unix-like operating systems including Linux and BSD have a monolithic kernel that
manages CPU scheduling, memory, file systems, network protocols, and system devices (disks,
network interfaces, etc.). This kernel model is shown in Figure 3.1.




Figure 3.1 Role of a monolithic operating system kernel

Also shown are system libraries, which are often used to provide a richer and easier program-
ming interface than the system calls alone. Applications include all running user-level software,
including databases, web servers, administration tools, and operating system shells.
92   Chapter 3 Operating Systems


     System libraries are pictured here as a broken ring to show that applications can call system calls
     (syscalls) directly.2 For example, the Golang runtime has its own syscall layer that doesn’t require
     the system library, libc. Traditionally, this diagram is drawn with complete rings, which reflect
     decreasing levels of privilege starting with the kernel at the center (a model that originated in
     Multics [Graham 68], the predecessor of Unix).

     Other kernel models also exist: microkernels employ a small kernel with functionality moved to
     user-mode programs; and unikernels compile kernel and application code together as a single pro-
     gram. There are also hybrid kernels, such as the Windows NT kernel, which use approaches from
     both monolithic kernels and microkernels together. These are summarized in Section 3.5, Other
     Topics.

     Linux has recently changed its model by allowing a new software type: Extended BPF, which
     enables secure kernel-mode applications along with its own kernel API: BPF helpers. This allows
     some applications and system functions to be rewritten in BPF, providing higher levels of secu-
     rity and performance. This is pictured in Figure 3.2.




     Figure 3.2 BPF applications

     Extended BPF is summarized is Section 3.4.4, Extended BPF.


     Kernel Execution
     The kernel is a large program, typically millions of lines of code. It primarily executes on
     demand, when a user-level program makes a system call, or a device sends an interrupt. Some
     kernel threads operate asynchronously for housekeeping, which may include the kernel clock
     routine and memory management tasks, but these try to be lightweight and consume very little
     CPU resources.



     2
       There are some exceptions to this model. Kernel bypass technologies, sometimes used for networking, allow user-
     level to access hardware directly (see Chapter 10, Network, Section 10.4.3, Software, heading Kernel Bypass).
     I/O to hardware may also be submitted without the expense of the syscall interface (although syscalls are required
     for initialization), for example, with memory-mapped I/O, major faults (see Chapter 7, Memory, Section 7.2.3,
     Demand Paging), sendfile(2), and Linux io_uring (see Chapter 5, Applications, Section 5.2.6, Non-Blocking I/O).
                                                                                 3.2   Background     93


Workloads that perform frequent I/O, such as web servers, execute mostly in kernel context.
Workloads that are compute-intensive usually run in user mode, uninterrupted by the kernel.
It may be tempting to think that the kernel cannot affect the performance of these compute-
intensive workloads, but there are many cases where it does. The most obvious is CPU contention,
when other threads are competing for CPU resources and the kernel scheduler needs to decide
which will run and which will wait. The kernel also chooses which CPU a thread will run on
and can choose CPUs with warmer hardware caches or better memory locality for the process,
to significantly improve performance.


3.2.2 Kernel and User Modes
The kernel runs in a special CPU mode called kernel mode, allowing full access to devices and the
execution of privileged instructions. The kernel arbitrates device access to support multitasking,
preventing processes and users from accessing each other’s data unless explicitly allowed.

User programs (processes) run in user mode, where they request privileged operations from the
kernel via system calls, such as for I/O.

Kernel and user mode are implemented on processors using privilege rings (or protection rings) fol-
lowing the model in Figure 3.1. For example, x86 processors support four privilege rings, numbered
0 to 3. Typically only two or three are used: for user mode, kernel mode, and the hypervisor if
present. Privileged instructions for accessing devices are only allowed in kernel mode; executing
them in user mode causes exceptions, which are then handled by the kernel (e.g., to generate a
permission denied error).

In a traditional kernel, a system call is performed by switching to kernel mode and then execut-
ing the system call code. This is shown in Figure 3.3.




Figure 3.3 System call execution modes

Switching between user and kernel modes is a mode switch.

All system calls mode switch. Some system calls also context switch: those that are blocking, such
as for disk and network I/O, will context switch so that another thread can run while the first is
blocked.
94   Chapter 3 Operating Systems


     Since mode and context switches cost a small amount of overhead (CPU cycles),3 there are various
     optimizations to avoid them, including:
         ■   User-mode syscalls: It is possible to implement some syscalls in a user-mode library alone.
             The Linux kernel does this by exporting a virtual dynamic shared object (vDSO) that is
             mapped into the process address space, which contains syscalls such as gettimeofday(2)
             and getcpu(2) [Drysdale 14].
         ■   Memory mappings: Used for demand paging (see Chapter 7, Memory, Section 7.2.3,
             Demand Paging), it can also be used for data stores and other I/O, avoiding syscall
             overheads.
         ■   Kernel bypass: This allows user-mode programs to access devices directly, bypassing
             syscalls and the typical kernel code path. For example, DPDK for networking: the Data
             Plane Development Kit.
         ■   Kernel-mode applications: These include the TUX web server [Lever 00], implemented
             in-kernel, and more recently the extended BPF technology pictured in Figure 3.2.

     Kernel and user mode have their own software execution contexts, including a stack and regis-
     ters. Some processor architectures (e.g., SPARC) use a separate address space for the kernel, which
     means the mode switch must also change the virtual memory context.


     3.2.3       System Calls
     System calls request the kernel to perform privileged system routines. There are hundreds of system
     calls available, but some effort is made by kernel maintainers to keep that number as small
     as possible, to keep the kernel simple (Unix philosophy; [Thompson 78]). More sophisticated
     interfaces can be built upon them in user-land as system libraries, where they are easier to
     develop and maintain. Operating systems generally include a C standard library that provides
     easier-to-use interfaces for many common syscalls (e.g., the libc or glibc libraries).

     Key system calls to remember are listed in Table 3.1.


     Table 3.1     Key system calls
     System Call            Description
     read(2)                Read bytes
     write(2)               Write bytes
     open(2)                Open a file
     close(2)               Close a file
     fork(2)                Create a new process
     clone(2)               Create a new process or thread
     exec(2)                Execute a new program

     3
      With the current mitigation for the Meltdown vulnerability, context switches are now more expensive. See
     Section 3.4.3 KPTI (Meltdown).
                                                                                            3.2    Background      95



System Call                Description
connect(2)                 Connect to a network host
accept(2)                  Accept a network connection
stat(2)                    Fetch file statistics
ioctl(2)                   Set I/O properties, or other miscellaneous functions
mmap(2)                    Map a file to the memory address space
brk(2)                     Extend the heap pointer
futex(2)                   Fast user-space mutex



System calls are well documented, each having a man page that is usually shipped with the oper-
ating system. They also have a generally simple and consistent interface and use error codes to
describe errors when needed (e.g., ENOENT for “no such file or directory”).4

Many of these system calls have an obvious purpose. Here are a few whose common usage may
be less obvious:
       ■   ioctl(2): This is commonly used to request miscellaneous actions from the kernel, espe-
           cially for system administration tools, where another (more obvious) system call isn’t
           suitable. See the example that follows.
       ■   mmap(2): This is commonly used to map executables and libraries to the process address
           space, and for memory-mapped files. It is sometimes used to allocate the working memory
           of a process, instead of the brk(2)-based malloc(2), to reduce the syscall rate and improve
           performance (which doesn’t always work due to the trade-off involved: memory-mapping
           management).
       ■   brk(2): This is used to extend the heap pointer, which defines the size of the working
           memory of the process. It is typically performed by a system memory allocation library,
           when a malloc(3) (memory allocate) call cannot be satisfied from the existing space in the
           heap. See Chapter 7, Memory.
       ■   futex(2): This syscall is used to handle part of a user space lock: the part that is likely to block.

If a system call is unfamiliar, you can learn more in its man page (these are in section 2 of the
man pages: syscalls).

The ioctl(2) syscall may be the most difficult to learn, due to its ambiguous nature. As an
example of its usage, the Linux perf(1) tool (introduced in Chapter 6, CPUs) performs privileged
actions to coordinate performance instrumentation. Instead of system calls being added for each
action, a single system call is added: perf_event_open(2), which returns a file descriptor for use
with ioctl(2). This ioctl(2) can then be called using different arguments to perform the different
desired actions. For example, ioctl(fd, PERF_EVENT_IOC_ENABLE) enables instrumentation.
The arguments, in this example PERF_EVENT_IOC_ENABLE, can be more easily added and
changed by the developer.

4
    glibc provides these errors in an errno (error number) integer variable.
96   Chapter 3 Operating Systems


     3.2.4 Interrupts
     An interrupt is a signal to the processor that some event has occurred that needs processing, and
     interrupts the current execution of the processor to handle it. It typically causes the processor
     to enter kernel mode if it isn’t already, save the current thread state, and then run an interrupt
     service routine (ISR) to process the event.

     There are asynchronous interrupts generated by external hardware and synchronous interrupts
     generated by software instructions. These are pictured in Figure 3.4.




     Figure 3.4 Interrupt types

     For simplicity Figure 3.4 shows all interrupts sent to the kernel for processing; these are sent to
     the CPU first, which selects the ISR in the kernel to run the event.


     Asynchronous Interrupts
     Hardware devices can send interrupt service requests (IRQs) to the processor, which arrive asyn-
     chronously to the currently running software. Examples of hardware interrupts include:
         ■   Disk devices signaling the completion of disk I/O
         ■   Hardware indicating a failure condition
         ■   Network interfaces signaling the arrival of a packet
         ■   Input devices: keyboard and mouse input

     To explain the concept of asynchronous interrupts, an example scenario is pictured in Figure 3.5
     showing the passage of time as a database (MySQL) running on CPU 0 reads from a file system.
     The file system contents must be fetched from disk, so the scheduler context switches to another
     thread (a Java application) while the database is waiting. Sometime later, the disk I/O completes,
                                                                                   3.2   Background    97


but at this point the database is no longer running on CPU 0. The completion interrupt has
occurred asynchronously to the database, showed by a dotted line in Figure 3.5.




Figure 3.5 Asynchronous interrupt example

Synchronous Interrupts
Synchronous interrupts are generated by software instructions. The following describes differ-
ent types of software interrupts using the terms traps, exceptions, and faults; however, these terms
are often used interchangeably.
    ■   Traps: A deliberate call into the kernel, such as by the int (interrupt) instruction. One
        implementation of syscalls involves calling the int instruction with a vector for a syscall
        handler (e.g., int 0x80 on Linux x86). int raises a software interrupt.
    ■   Exceptions: A exceptional condition, such as by an instruction performing a divide by
        zero.
    ■   Faults: A term often used for memory events, such as page faults triggered by accessing a
        memory location without an MMU mapping. See Chapter 7, Memory.

For these interrupts, the responsible software and instruction are still on CPU.


Interrupt Threads
Interrupt service routines (ISRs) are designed to operate as quickly as possible, to reduce the
effects of interrupting active threads. If an interrupt needs to perform more than a little work,
especially if it may block on locks, it can be processed by an interrupt thread that can be sched-
uled by the kernel. This is pictured in Figure 3.6.
