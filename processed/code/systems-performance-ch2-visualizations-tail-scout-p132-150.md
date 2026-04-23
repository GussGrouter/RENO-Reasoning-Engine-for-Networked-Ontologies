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
98   Chapter 3 Operating Systems




     Figure 3.6 Interrupt processing

     How this is implemented depends on the kernel version. On Linux, device drivers can be mod-
     eled as two halves, with the top half handling the interrupt quickly, and scheduling work to a
     bottom half to be processed later [Corbet 05]. Handling the interrupt quickly is important as the
     top half runs in interrupt-disabled mode to postpone the delivery of new interrupts, which can
     cause latency problems for other threads if it runs for too long. The bottom half can be either
     tasklets or work queues; the latter are threads that can be scheduled by the kernel and can sleep
     when necessary.

     Linux network drivers, for example, have a top half to handle IRQs for inbound packets, which
     calls the bottom half to push the packet up the network stack. The bottom half is implemented
     as a softirq (software interrupt).

     The time from an interrupt’s arrival to when it is serviced is the interrupt latency, which is depen-
     dent on the hardware and implementation. This is a subject of study for real-time or low-latency
     systems.


     Interrupt Masking
     Some code paths in the kernel cannot be interrupted safely. An example is kernel code that
     acquires a spin lock during a system call, for a spin lock that might also be needed by an inter-
     rupt. Taking an interrupt with such a lock held could cause a deadlock. To prevent such a situ-
     ation, the kernel can temporarily mask interrupts by setting the CPU’s interrupt mask register.
     The interrupt disabled time should be as short as possible, as it can perturb the timely execution
     of applications that are woken up by other interrupts. This is an important factor for real-time
     systems—those that have strict response time requirements. Interrupt disabled time is also a
     target of performance analysis (such analysis is supported directly by the Ftrace irqsoff tracer,
     mentioned in Chapter 14, Ftrace).

     Some high-priority events should not be ignored, and so are implemented as non-maskable inter-
     rupts (NMIs). For example, Linux can use an Intelligent Platform Management Interface (IPMI)
                                                                                                3.2   Background   99


watchdog timer that checks if the kernel appears to have locked up based on a lack of interrupts
during a period of time. If so, the watchdog can issue an NMI interrupt to reboot the system.5


3.2.5           Clock and Idle
A core component of the original Unix kernel is the clock() routine, executed from a timer inter-
rupt. It has historically been executed at 60, 100, or 1,000 times per second6 (often expressed
in Hertz: cycles per second), and each execution is called a tick.7 Its functions have included
updating the system time, expiring timers and time slices for thread scheduling, maintaining
CPU statistics, and executing scheduled kernel routines.

There have been performance issues with the clock, improved in later kernels, including:

       ■   Tick latency: For 100 Hertz clocks, up to 10 ms of additional latency may be encountered
           for a timer as it waits to be processed on the next tick. This has been fixed using high-
           resolution real-time interrupts so that execution occurs immediately.
       ■   Tick overhead: Ticks consume CPU cycles and slightly perturb applications, and are one
           cause of what is known as operating system jitter. Modern processors also have dynamic
           power features, which can power down parts during idle periods. The clock routine inter-
           rupts this idle time, which can consume power needlessly.

Modern kernels have moved much functionality out of the clock routine to on-demand inter-
rupts, in an effort to create a tickless kernel. This reduces overhead and improves power efficiency
by allowing processors to remain in sleep states for longer.

The Linux clock routine is scheduler_tick(), and Linux has ways to omit calling the clock
while there isn’t any CPU load. The clock itself typically runs at 250 Hertz (configured by the
CONFIG_HZ Kconfig option and variants), and its calls are reduced by the NO_HZ functionality
(configured by CONFIG_NO_HZ and variants), which is now commonly enabled [Linux 20a].


Idle Thread
When there is no work for the CPUs to perform, the kernel schedules a placeholder thread that
waits for work, called the idle thread. A simple implementation would check for the availability
of new work in a loop. In modern Linux the idle task can call the hlt (halt) instruction to power
down the CPU until the next interrupt is received, saving power.


3.2.6           Processes
A process is an environment for executing a user-level program. It consists of a memory address
space, file descriptors, thread stacks, and registers. In some ways, a process is like a virtual early
computer, where only one program is executing with its own registers and stacks.




5
    Linux also has a software NMI watchdog for detecting lockups [Linux 20d].
6
    Other rates include 250 for Linux 2.6.13, 256 for Ultrix, and 1,024 for OSF/1 [Mills 94].
7
    Linux also tracks jiffies, a unit of time similar to ticks.
100   Chapter 3 Operating Systems


      Processes are multitasked by the kernel, which typically supports the execution of thousands of
      processes on a single system. They are individually identified by their process ID (PID), which is a
      unique numeric identifier.

      A process contains one or more threads, which operate in the process address space and share
      the same file descriptors. A thread is an executable context consisting of a stack, registers, and
      an instruction pointer (also called a program counter). Multiple threads allow a single process to
      execute in parallel across multiple CPUs. On Linux, threads and processes are both tasks.

      The first process launched by the kernel is called “init,” from /sbin/init (by default), with PID 1,
      which launches user space services. In Unix this involved running start scripts from /etc, a
      method now referred to as SysV (after Unix System V). Linux distributions now commonly use
      the systemd software to start services and track their dependencies.


      Process Creation
      Processes are normally created using the fork(2) system call on Unix systems. On Linux, C librar-
      ies typically implement the fork function by wrapping around the versatile clone(2) syscall.
      These syscalls create a duplicate of the process, with its own process ID. The exec(2) system call
      (or a variant, such as execve(2)) can then be called to begin execution of a different program.

      Figure 3.7 shows an example process creation for a bash shell (bash) executing the ls command.




      Figure 3.7 Process creation

      The fork(2) or clone(2) syscall may use a copy-on-write (COW) strategy to improve performance.
      This adds references to the previous address space rather than copying all of the contents. Once
      either process modifies the multiple-referenced memory, a separate copy is then made for the
      modifications. This strategy either defers or eliminates the need to copy memory, reducing
      memory and CPU usage.


      Process Life Cycle
      The life cycle of a process is shown in Figure 3.8. This is a simplified diagram; for modern mul-
      tithreaded operating systems it is the threads that are scheduled and run, and there are some
      additional implementation details regarding how these map to process states (see Figures 5.6
      and 5.7 in Chapter 5 for more detailed diagrams).
                                                                                3.2   Background      101




Figure 3.8 Process life cycle

The on-proc state is for running on a processor (CPU). The ready-to-run state is when the process
is runnable but is waiting on a CPU run queue for its turn on a CPU. Most I/O will block, putting
the process in the sleep state until the I/O completes and the process is woken up. The zombie
state occurs during process termination, when the process waits until its process status has been
reaped by the parent process or until it is removed by the kernel.


Process Environment
The process environment is shown in Figure 3.9; it consists of data in the address space of the
process and metadata (context) in the kernel.




Figure 3.9 Process environment

The kernel context consists of various process properties and statistics: its process ID (PID), the
owner’s user ID (UID), and various times. These are commonly examined via the ps(1) and top(1)
commands. It also has a set of file descriptors, which refer to open files and which are (usually)
shared between threads.
102   Chapter 3 Operating Systems


      This example pictures two threads, each containing some metadata, including a priority in
      kernel context8 and user stack in the user address space. The diagram is not drawn to scale; the
      kernel context is very small compared to the process address space.

      The user address space contains memory segments of the process: executable, libraries, and heap.
      For more details, see Chapter 7, Memory.

      On Linux, each thread has its own user stack and a kernel exception stack9 [Owens 20].


      3.2.7 Stacks
      A stack is a memory storage area for temporary data, organized as a last-in, first-out (LIFO) list.
      It is used to store less important data than that which fits in the CPU register set. When a func-
      tion is called, the return address is saved to the stack. Some registers may be saved to the stack as
      well if their values are needed after the call.10 When the called function has finished, it restores
      any required registers and, by fetching the return address from the stack, passes execution to the
      calling function. The stack can also be used for passing parameters to functions. The set of data
      on a stack related to a function’s execution is called a stack frame.

      The call path to the currently executing function can be seen by examining the saved return
      addresses across all the stack frames in the thread’s stack (a process called stack walking).11 This
      call path is referred to as a stack back trace or a stack trace. In performance engineering it is often
      called just a “stack” for short. These stacks can answer why something is executing, and are an
      invaluable tool for debugging and performance analysis.


      How to Read a Stack
      The following example kernel stack (from Linux) shows the path taken for TCP transmission, as
      printed by a tracing tool:

              tcp_sendmsg+1
              sock_sendmsg+62
              SYSC_sendto+319
              sys_sendto+14
              do_syscall_64+115
              entry_SYSCALL_64_after_hwframe+61



      8
        The kernel context may be its own full address space (as with SPARC processors) or a restricted range that does
      not overlap with user addresses (as with x86 processors).
      9
          There are also special-purpose kernel stacks per-CPU, including those used for interrupts.
      10
        The calling convention from the processor ABI specifies which registers should retain their values after a function
      call (they are non-volatile) and are saved to the stack by the called function (“callee-saves”). Other registers are
      volatile and may be clobbered by the called function; if the caller wishes to retain their values, it must save them to
      the stack (“caller-saves”).
      11
         For more detail on stack walking and the different possible techniques (which include: frame-pointer based,
      debuginfo, last branch record, and ORC) see Chapter 2, Tech, Section 2.4, Stack Trace Walking, of BPF Performance
      Tools [Gregg 19].
                                                                                   3.2   Background       103


Stacks are usually printed in leaf-to-root order, so the first line printed is the function currently
executing, and beneath it is its parent, then its grandparent, and so on. In this example, the tcp_
sendmsg() function was executing, called by sock_sendmsg(). In this stack example, to the right
of the function name is the instruction offset, showing the location within a function. The first
line shows tcp_sendmsg() offset 1 (which would be the second instruction), called by sock_
sendmsg() offset 62. This offset is only useful if you desire a low-level understanding of the code
path taken, down to the instruction level.

By reading down the stack, the full ancestry can be seen: function, parent, grandparent, and so
on. Or, by reading bottom-up, you can follow the path of execution to the current function: how
we got here.

Since stacks expose the internal path taken through source code, there is typically no documen-
tation for these functions other than the code itself. For this example stack, this is the Linux kernel
source code. An exception to this is where functions are part of an API and are documented.


User and Kernel Stacks
While executing a system call, a process thread has two stacks: a user-level stack and a kernel-
level stack. Their scope is pictured in Figure 3.10.




Figure 3.10 User and kernel stacks

The user-level stack of the blocked thread does not change for the duration of a system call, as
the thread is using a separate kernel-level stack while executing in kernel context. (An excep-
tion to this may be signal handlers, which may borrow a user-level stack depending on their
configuration.)

On Linux, there are multiple kernel stacks for different purposes. Syscalls use a kernel exception
stack associated with each thread, and there are also stacks associated with soft and hard inter-
rupts (IRQs) [Bovet 05].
104   Chapter 3 Operating Systems


      3.2.8 Virtual Memory
      Virtual memory is an abstraction of main memory, providing processes and the kernel with their
      own, almost infinite,12 private view of main memory. It supports multitasking, allowing processes
      and the kernel to operate on their own private address spaces without worrying about contention.
      It also supports oversubscription of main memory, allowing the operating system to transparently
      map virtual memory between main memory and secondary storage (disks) as needed.

      The role of virtual memory is shown in Figure 3.11. Primary memory is main memory (RAM),
      and secondary memory is the storage devices (disks).




      Figure 3.11 Virtual memory address spaces13

      Virtual memory is made possible by support in both the processor and operating system. It is not
      real memory, and most operating systems map virtual memory to real memory only on demand,
      when the memory is first populated (written).

      See Chapter 7, Memory, for more about virtual memory.


      Memory Management
      While virtual memory allows main memory to be extended using secondary storage, the kernel
      strives to keep the most active data in main memory. There are two kernel schemes for this:
          ■   Process swapping moves entire processes between main memory and secondary storage.
          ■   Paging moves small units of memory called pages (e.g., 4 Kbytes).

      12
         On 64-bit processors, anyway. For 32-bit processors, virtual memory is limited to 4 Gbytes due to the limits of a
      32-bit address (and the kernel may limit it to an even smaller amount).
      13
         Process virtual memory is shown as starting from 0 as a simplification. Kernels today commonly begin a process’s
      virtual address space at some offset such as 0x10000 or a random address. One benefit is that a common pro-
      gramming error of dereferencing a NULL (0) pointer will then cause the program to crash (SIGSEGV) as the 0 address
      is invalid. This is generally preferable to dereferencing data at address 0 by mistake, as the program would continue
      to run with corrupt data.
                                                                               3.2   Background     105


Process swapping is the original Unix method and can cause severe performance loss. Paging is
more efficient and was added to BSD with the introduction of paged virtual memory. In both
cases, least recently used (or not recently used) memory is moved to secondary storage and
moved back to main memory only when needed again.

In Linux, the term swapping is used to refer to paging. The Linux kernel does not support the
(older) Unix-style process swapping of entire threads and processes.

For more on paging and swapping, see Chapter 7, Memory.


3.2.9 Schedulers
Unix and its derivatives are time-sharing systems, allowing multiple processes to run at the same
time by dividing execution time among them. The scheduling of processes on processors and
individual CPUs is performed by the scheduler, a key component of the operating system kernel.
The role of the scheduler is pictured in Figure 3.12, which shows that the scheduler operates
on threads (in Linux, tasks), mapping them to CPUs.




Figure 3.12 Kernel scheduler

The basic intent is to divide CPU time among the active processes and threads, and to maintain
a notion of priority so that more important work can execute sooner. The scheduler keeps track
of all threads in the ready-to-run state, traditionally on per-priority queues called run queues
[Bach 86]. Modern kernels may implement these queues per CPU and may also use other data
structures, apart from queues, to track the threads. When more threads want to run than there
are available CPUs, the lower-priority threads wait their turn. Most kernel threads run with a
higher priority than user-level processes.

Process priority can be modified dynamically by the scheduler to improve the performance of
certain workloads. Workloads can be categorized as either:
106   Chapter 3 Operating Systems


          ■   CPU-bound: Applications that perform heavy compute, for example, scientific and math-
              ematical analysis, which are expected to have long runtimes (seconds, minutes, hours,
              days, or even longer). These become limited by CPU resources.
          ■   I/O-bound: Applications that perform I/O, with little compute, for example, web servers,
              file servers, and interactive shells, where low-latency responses are desirable. When their
              load increases, they are limited by I/O to storage or network resources.

      A commonly used scheduling policy dating back to UNIX identifies CPU-bound workloads and
      decreases their priority, allowing I/O-bound workloads—where low-latency responses are more
      desirable—to run sooner. This can be achieved by calculating the ratio of recent compute time
      (time executing on-CPU) to real time (elapsed time) and decreasing the priority of processes with
      a high (compute) ratio [Thompson 78]. This mechanism gives preference to shorter-running
      processes, which are usually those performing I/O, including human interactive processes.

      Modern kernels support multiple scheduling classes or scheduling policies (Linux) that apply different
      algorithms for managing priority and runnable threads. These may include real-time scheduling,
      which uses a priority higher than all noncritical work, including kernel threads. Along with
      preemption support (described later), real-time scheduling provides predictable and low-latency
      scheduling for systems that require it.

      See Chapter 6, CPUs, for more about the kernel scheduler and other scheduling algorithms.


      3.2.10       File Systems
      File systems are an organization of data as files and directories. They have a file-based interface
      for accessing them, usually based on the POSIX standard. Kernels support multiple file system
      types and instances. Providing a file system is one of the most important roles of the operating
      system, once described as the most important role [Ritchie 74].

      The operating system provides a global file namespace, organized as a top-down tree topology
      starting with the root level (“/”). File systems join the tree by mounting, attaching their own tree
      to a directory (the mount point). This allows the end user to navigate the file namespace transpar-
      ently, regardless of the underlying file system type.

      A typical operating system may be organized as shown in Figure 3.13.




      Figure 3.13 Operating system file hierarchy
                                                                                   3.2   Background      107


The top-level directories include etc for system configuration files, usr for system-supplied user-
level programs and libraries, dev for device nodes, var for varying files including system logs,
tmp for temporary files, and home for user home directories. In the example pictured, var and
home may reside on their own file system instances and separate storage devices; however, they
can be accessed like any other component of the tree.

Most file system types use storage devices (disks) to store their contents. Some file system types
are dynamically created by the kernel, such as /proc and /dev.

Kernels typically provide different ways to isolate processes to a portion of the file namespace,
including chroot(8), and, on Linux, mount namespaces, commonly used for containers (see
Chapter 11, Cloud Computing).


VFS
The virtual file system (VFS) is a kernel interface to abstract file system types, originally devel-
oped by Sun Microsystems so that the Unix file system (UFS) and the Network file system (NFS)
could more easily coexist. Its role is pictured in Figure 3.14.




Figure 3.14 Virtual file system

The VFS interface makes it easier to add new file system types to the kernel. It also supports
providing the global file namespace, pictured earlier, so that user programs and applications can
access various file system types transparently.


I/O Stack
For storage-device-based file systems, the path from user-level software to the storage device is
called the I/O stack. This is a subset of the entire software stack shown earlier. A generic I/O stack
is shown in Figure 3.15.

Figure 3.15 shows a direct path to block devices on the left, bypassing the file system. This path
is sometimes used by administrative tools and databases.

File systems and their performance are covered in detail in Chapter 8, File Systems, and the
storage devices they are built upon are covered in Chapter 9, Disks.
108   Chapter 3 Operating Systems




      Figure 3.15 Generic I/O stack

      3.2.11 Caching
      Since disk I/O has historically had high latency, many layers of the software stack attempt to
      avoid it by caching reads and buffering writes. Caches may include those shown in Table 3.2 (in
      the order in which they are checked).


      Table 3.2   Example cache layers for disk I/O
              Cache                                 Examples
      1       Client cache                          Web browser cache
      2       Application cache                     —
      3       Web server cache                      Apache cache
      4       Caching server                        memcached
      5       Database cache                        MySQL buffer cache
      6       Directory cache                       dcache
      7       File metadata cache                   inode cache
      8       Operating system buffer cache         Buffer cache
      9       File system primary cache             Page cache, ZFS ARC
      10      File system secondary cache           ZFS L2ARC
      11      Device cache                          ZFS vdev
                                                                                 3.2   Background   109



        Cache                                   Examples
12      Block cache                             Buffer cache
13      Disk controller cache                   RAID card cache
14      Storage array cache                     —
15      On-disk cache                           —



For example, the buffer cache is an area of main memory that stores recently used disk blocks.
Disk reads may be served immediately from the cache if the requested block is present, avoiding
the high latency of disk I/O.

The types of caches present will vary based on the system and environment.


3.2.12      Networking
Modern kernels provide a stack of built-in network protocols, allowing the system to communi-
cate via the network and take part in distributed system environments. This is referred to as the
networking stack or the TCP/IP stack, after the commonly used TCP and IP protocols. User-level
applications access the network through programmable endpoints called sockets.

The physical device that connects to the network is the network interface and is usually provided
on a network interface card (NIC). A historical duty of the system administrator was to associate
an IP address with a network interface, so that it can communicate with the network; these
mappings are now typically automated via the dynamic host configuration protocol (DHCP).

Network protocols do not change often, but there is a new transport protocol seeing growing
adoption: QUIC (summarized in Chapter 10, Network). Protocol enhancements and options
change more often, such as newer TCP options and TCP congestion control algorithms. Newer
protocols and enhancements typically require kernel support (with the exception of user-space
protocol implementations). Another change is support for different network interface cards,
which require new device drivers for the kernel.

For more on networking and network performance, see Chapter 10, Network.


3.2.13      Device Drivers
A kernel must communicate with a wide variety of physical devices. Such communication is
achieved using device drivers: kernel software for device management and I/O. Device drivers are
often provided by the vendors who develop the hardware devices. Some kernels support pluggable
device drivers, which can be loaded and unloaded without requiring a system restart.

Device drivers can provide character and/or block interfaces to their devices. Character devices,
also called raw devices, provide unbuffered sequential access of any I/O size down to a single
character, depending on the device. Such devices include keyboards and serial ports (and in
original Unix, paper tape and line printer devices).

Block devices perform I/O in units of blocks, which have historically been 512 bytes each. These
can be accessed randomly based on their block offset, which begins at 0 at the start of the block
110   Chapter 3 Operating Systems


      device. In original Unix, the block device interface also provided caching of block device buffers
      to improve performance, in an area of main memory called the buffer cache. In Linux, this buffer
      cache is now part of the page cache.


      3.2.14      Multiprocessor
      Multiprocessor support allows the operating system to use multiple CPU instances to execute
      work in parallel. It is usually implemented as symmetric multiprocessing (SMP) where all CPUs
      are treated equally. This was technically difficult to accomplish, posing problems for accessing
      and sharing memory and CPUs among threads running in parallel. On multiprocessor systems
      there may also be banks of main memory connected to different sockets (physical processors) in
      a non-uniform memory access (NUMA) architecture, which also pose performance challenges. See
      Chapter 6, CPUs, for details, including scheduling and thread synchronization, and Chapter 7,
      Memory, for details on memory access and architectures.


      IPIs
      For a multiprocessor system, there are times when CPUs need to coordinate, such as for cache
      coherency of memory translation entries (informing other CPUs that an entry, if cached, is now
      stale). A CPU can request other CPUs, or all CPUs, to immediately perform such work using an
      inter-processor interrupt (IPI) (also known as an SMP call or a CPU cross call). IPIs are processor
      interrupts designed to be executed quickly, to minimize interruption of other threads.

      IPIs can also be used by preemption.


      3.2.15      Preemption
      Kernel preemption support allows high-priority user-level threads to interrupt the kernel and
      execute. This enables real-time systems that can execute work within a given time constraint,
      including systems in use by aircraft and medical devices. A kernel that supports preemption is
      said to be fully preemptible, although practically it will still have some small critical code paths
      that cannot be interrupted.

      Another approach supported by Linux is voluntary kernel preemption, where logical stopping
      points in the kernel code can check and perform preemption. This avoids some of the complexity
      of supporting a fully preemptive kernel and provides low-latency preemption for common work-
      loads. Voluntary kernel preemption is commonly enabled in Linux via the CONFIG_PREEMPT_
      VOLUNTARY Kconfig option; there is also CONFIG_PREEMPT to allow all kernel code (except
      critical sections) to be preemptible, and CONFIG_PREEMPT_NONE to disable preemption,
      improving throughput at the cost of higher latencies.


      3.2.16      Resource Management
      The operating system may provide various configurable controls for fine-tuning access to system
      resources, such as CPUs, memory, disk, and the network. These are resource controls and can be
      used to manage performance on systems that run different applications or host multiple tenants
      (cloud computing). Such controls may impose fixed limits per process (or groups of processes) for
      resource usage, or a more flexible approach—allowing spare usage to be shared among them.
                                                                                    3.3   Kernels    111


Early versions of Unix and BSD had basic per-process resource controls, including CPU priorities
with nice(1), and some resource limits with ulimit(1).

For Linux, control groups (cgroups) have been developed and integrated in Linux 2.6.24 (2008),
and various additional controls have been added since then. These are documented in the kernel
source under Documentation/cgroups. There is also an improved unified hierarchical scheme
called cgroup v2, made available in Linux 4.5 (2016) and documented in Documentation/admin-
guide/cgroup-v2.rst.

Specific resource controls are mentioned in later chapters as appropriate. An example use case
is described in Chapter 11, Cloud Computing, for managing the performance of OS-virtualized
tenants.


3.2.17      Observability
The operating system consists of the kernel, libraries, and programs. These programs include tools
to observe system activity and analyze performance, typically installed in /usr/bin and /usr/
sbin. Third-party tools may also be installed on the system to provide additional observability.

Observability tools, and the operating system components upon which they are built, are
introduced in Chapter 4.



3.3 Kernels
The following sections discuss Unix-like kernel implementation details with a focus on perfor-
mance. As background, the performance features of earlier kernels are discussed: Unix, BSD, and
Solaris. The Linux kernel is discussed in more detail in Section 3.4, Linux.

Kernel differences can include the file systems they support (see Chapter 8, File Systems), the
system call (syscall) interfaces, network stack architecture, real-time support, and scheduling
algorithms for CPUs, disk I/O, and networking.

Table 3.3 shows Linux and other kernel versions for comparison, with syscall counts based on
the number of entries in section 2 of the OS man pages. This is a crude comparison, but enough
to see some differences.


Table 3.3   Kernel versions with documented syscall counts
Kernel Version                             Syscalls
UNIX Version 7                             48
SunOS (Solaris) 5.11                       142
FreeBSD 12.0                               222
Linux 2.6.32-21-server                     408
Linux 2.6.32-220.el6.x86_64                427
Linux 3.2.6-3.fc16.x86_64                  431
Linux 4.15.0-66-generic                    480
Linux 5.3.0-1010-aws                       493
