                                                                             2.10 Visualizations      81




Figure 2.28 Median, mean, standard deviation, percentiles

2.10.2      Scatter Plots
Figure 2.29 shows disk I/O events for the same time range as a scatter plot, which enables all data
to be seen. Each disk I/O is drawn as a point, with its completion time on the x-axis and latency
on the y-axis.




Figure 2.29 Scatter plot

Now the source of the higher-than-expected average latency can be understood fully: there are
many disk I/O with latencies of 10 ms, 20 ms, even over 50 ms. The scatter plot has shown all the
data, revealing the presence of these outliers.
82   Chapter 2 Methodologies


     Many of the I/O were submillisecond, shown close to the x-axis. This is where the resolution of
     scatter plots begins to become a problem, as the points overlap and become difficult to distin-
     guish. This gets worse with more data: imagine plotting events from an entire cloud, involving
     millions of data points, on one scatter plot: the dots can merge and become a “wall of paint.”
     Another problem is the volume of data that must be collected and processed: x and y coordinates
     for every I/O.


     2.10.3      Heat Maps
     Heat maps (more properly called a column quantization) can solve the scatter plot scalability prob-
     lems by quantizing x and y ranges into groups called buckets. These are displayed as large pixels,
     colored based on the number of events in that x and y range. This quantizing also solves the
     scatter plot visual density limit, allowing heat maps to show data from a single system or thou-
     sands of systems in the same way. Heat maps had previously been used for location such as disk
     offsets (e.g., TazTool [McDougall 06a]); I invented their use in computing for latency, utilization,
     and other metrics. Latency heat maps were first included in Analytics for the Sun Microsystems
     ZFS Storage appliance, released in 2008 [Gregg 10a][Gregg 10b], and are now commonplace in
     performance monitoring products such as Grafana [Grafana 20].

     The same dataset as plotted earlier is shown in Figure 2.30 as a heat map.




     Figure 2.30 Heat map

     High-latency outliers can be identified as blocks that are high in the heat map, usually of light
     colors as they span few I/O (often a single I/O). Patterns in the bulk of the data begin to emerge,
     which may be impossible to see with a scatter plot.

     The full range of seconds for this disk I/O trace (not shown earlier) is shown in the Figure 2.31
     heat map.
                                                                               2.10 Visualizations     83




Figure 2.31 Heat map: full range

Despite spanning nine times the range, the visualization is still very readable. A bimodal distri-
bution can be seen for much of the range, with some I/O returning with near-zero latency (likely
a disk cache hit), and others with a little less than 1 ms (likely a disk cache miss).

There are other examples of heat maps later in this book, including in Chapter 6, CPUs, Section 6.7,
Visualizations; Chapter 8, File Systems, Section 8.6.18, Visualizations; and Chapter 9, Disks,
Section 9.7.3, Latency Heat Maps. My website also has examples of latency, utilization, and
subsecond-offset heat maps [Gregg 15b].


2.10.4      Timeline Charts
A timeline chart shows a set of activities as bars on a timeline. These are commonly used for
front-end performance analysis (web browsers), where they are also called waterfall charts, and
show the timing of network requests. An example from the Firefox web browser is shown in
Figure 2.32.

In Figure 2.32, the first network request is highlighted: apart from showing its duration as a hor-
izontal bar, components of this duration are also shown as colored bars. These are also explained
in the right panel: the slowest component for the first request is “Waiting,” which is waiting
for the HTTP response from the server. Requests two to six begin after the first request begins
receiving data, and are likely dependent on that data. If explicit dependency arrows are included
in the chart, it becomes a type of Gantt chart.

For back-end performance analysis (servers), similar charts are used to show timelines for
threads or CPUs. Example software includes KernelShark [KernelShark 20] and Trace Compass
[Eclipse 20]. For an example KernelShark screenshot, see Chapter 14, Ftrace, Section 14.11.5,
KernelShark. Trace Compass also draws arrows showing dependencies, where one thread has
woken up another.
84   Chapter 2 Methodologies




     Figure 2.32 Firefox timeline chart

     2.10.5      Surface Plot
     This is a representation of three dimensions, rendered as a three-dimensional surface. It works
     best when the third-dimension value does not frequently change dramatically from one point
     to the next, producing a surface resembling rolling hills. A surface plot is often rendered as a
     wireframe model.

     Figure 2.33 shows a wireframe surface plot of per-CPU utilization. It contains 60 seconds of
     per-second values from many servers (this is cropped from an image that spanned a data center
     of over 300 physical servers and 5,312 CPUs) [Gregg 11b].

     Each server is represented by plotting its 16 CPUs as rows on the surface, the 60 per-second uti-
     lization measurements as columns, and then setting the height of the surface to the utilization
     value. Color is also set to reflect the utilization value. Both hue and saturation could be used, if
     desired, to add fourth and fifth dimensions of data to the visualization. (With sufficient resolu-
     tion, a pattern could be used to indicate a sixth dimension.)

     These 16 × 60 server rectangles are then mapped across the surface as a checkerboard. Even
     without markings, some server rectangles can be clearly seen in the image. One that appears as
     an elevated plateau on the right shows that its CPUs are almost always at 100%.

     The use of grid lines highlights subtle changes in elevation. Some faint lines are visible, which
     indicate a single CPU constantly running at low utilization (a few percent).
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
