Chapter 3
Operating Systems

An understanding of the operating system and its kernel is essential for systems performance
analysis. You will frequently need to develop and then test hypotheses about system behavior,
such as how system calls are being performed, how the kernel schedules threads on CPUs, how
limited memory could be affecting performance, or how a file system processes I/O. These
activities will require you to apply your knowledge of the operating system and the kernel.
The learning objectives of this chapter are:
■

Learn kernel terminology: context switches, swapping, paging, preemption, etc.

■

Understand the role of the kernel and system calls.

■

Gain a working knowledge of kernel internals, including: interrupts, schedulers, virtual
memory, and the I/O stack.

■

See how kernel performance features have been added from Unix to Linux.

■

Develop a basic understanding of extended BPF.

This chapter provides an overview of operating systems and kernels and is assumed knowledge for the rest of the book. If you missed operating systems class, you can treat this as a crash
course. Keep an eye out for any gaps in your knowledge, as there will be an exam at the end (I’m
kidding; it’s just a quiz). For more on kernel internals, see the references at the end of
this chapter.
This chapter has three sections:
■

Terminology lists essential terms.

■

Background summarizes key operating system and kernel concepts.

■

Kernels summarizes implementation specifics of Linux and other kernels.

Areas related to performance, including CPU scheduling, memory, disks, file systems, networking, and many specific performance tools, are covered in more detail in the chapters that
follow.

90

Chapter 3 Operating Systems

3.1

Terminology

For reference, here is the core operating system terminology used in this book. Many of these are
also concepts that are explained in more detail in this and later chapters.
■

■

■

■

■

Operating system: This refers to the software and files that are installed on a system so
that it can boot and execute programs. It includes the kernel, administration tools, and
system libraries.
Kernel: The kernel is the program that manages the system, including (depending on the
kernel model) hardware devices, memory, and CPU scheduling. It runs in a privileged
CPU mode that allows direct access to hardware, called kernel mode.
Process: An OS abstraction and environment for executing a program. The program runs
in user mode, with access to kernel mode (e.g., for performing device I/O) via system calls
or traps into the kernel.
Thread: An executable context that can be scheduled to run on a CPU. The kernel has
multiple threads, and a process contains one or more.
Task: A Linux runnable entity, which can refer to a process (with a single thread), a thread
from a multithreaded process, or kernel threads.

■

BPF program: A kernel-mode program running in the BPF1 execution environment.

■

Main memory: The physical memory of the system (e.g., RAM).

■

Virtual memory: An abstraction of main memory that supports multitasking and oversubscription. It is, practically, an infinite resource.

■

Kernel space: The virtual memory address space for the kernel.

■

User space: The virtual memory address space for processes.

■

User land: User-level programs and libraries (/usr/bin, /usr/lib...).

■

■

■

■

■

Context switch: A switch from running one thread or process to another. This is a normal
function of the kernel CPU scheduler, and involves switching the set of running CPU
registers (the thread context) to a new set.
Mode switch: A switch between kernel and user modes.
System call (syscall): A well-defined protocol for user programs to request the kernel to
perform privileged operations, including device I/O.
Processor: Not to be confused with process, a processor is a physical chip containing one
or more CPUs.
Trap: A signal sent to the kernel to request a system routine (privileged action). Trap types
include system calls, processor exceptions, and interrupts.

1
BPF originally stood for Berkeley Packet Filter, but the technology today has so little to do with Berkeley, packets, or
filtering that BPF has become a name in itself rather than an acronym.

3.2

■

Background

Hardware interrupt: A signal sent by physical devices to the kernel, usually to request
servicing of I/O. An interrupt is a type of trap.

The Glossary includes more terminology for reference if needed for this chapter, including
address space, buffer, CPU, file descriptor, POSIX, and registers.
