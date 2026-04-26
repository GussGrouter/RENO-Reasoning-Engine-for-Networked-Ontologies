# network-algorithmics-2-4-1-processes (chunk 000001)

# Network Algorithmics — operating systems: processes (2.4.1) (slice)

- Source: raw/code/pdf/Network.Algorithmics.pdf
- Extraction: pdftotext -f 64 -l 71 -layout
- Slice: from `2.4.1 Uninterrupted computation via processes` up to (excluding) `2.4.2 Infinite memory via virtual memory`

---

2.4.1 Uninterrupted computation via processes
A program may not run very long on the processor before being interrupted by the network adaptor.
If application programmers had to deal with interrupts, a working 100-line program would be a mir-
acle. Thus operating systems provide programmers with the abstraction of uninterrupted, sequential
computation under the name of a process.
    The process abstraction is realized by three mechanisms: context switching, scheduling, and protec-
tion, the first two of which are depicted in Fig. 2.11. In Fig. 2.11, Process P1 has the illusion that it runs
on the processor by itself. In reality, as shown on the timeline below, Process P1 may be interrupted by a
timer interrupt, which causes the OS scheduler program to run on the processor. Displacing P1 requires
the operating system to save the state of P1 in memory. The scheduler may run briefly and decide to give
Process P2 a turn. Restoring P2 to run on the processor requires restoring the state of P2 from memory.
Thus the actual time line of a processor may involve frequent context switches between processes, as
orchestrated by the scheduler. Finally, protection ensures that incorrect or malicious behavior of one
process cannot affect other processes.
    As agents of computation, “processes” come in three flavors—interrupt handlers, threads, and user
processes—ranked in order of increasing generality and cost. Interrupt handlers are small pieces of

---

## PDF page 68

2.4 Operating systems                  41

FIGURE 2.12
The processing of a received Internet packet in BSD is divided between the network adaptor, the kernel, and the
destined process.

computation used to service urgent requests, such as the arrival of a message to the network adaptor;
interrupt handlers use only a small amount of state, typically a few registers. User processes use the
complete state of the machine, such as memory as well as registers; thus, it is expensive to switch
between user processes as directed by the scheduler. Within the context of a single process, threads offer
a cheaper alternative to processes. A thread is a lightweight process that requires less state, because
threads within the same process share the same memory (i.e., same variables). Thus context switching
between two threads in the same process is cheaper than switching processes, because memory does
not have to be remapped. The following example shows the relevance of these concepts to endnode
networking.
Example 8. Receiver Livelock in BSD Unix: In BSD UNIX, as shown in Fig. 2.12, the arrival of a
packet generates an interrupt. The interrupt is a hardware signal that causes the processor to save the
state of the currently running process, say, a Java program. The processor then jumps to the interrupt
handler code, bypassing the scheduler for speed. The interrupt handler copies the packet to a kernel
queue of IP packets waiting to be consumed, makes a request for an operating system thread (called a
software interrupt), and exits. Assuming no further interrupts, the interrupt exit passes control to the
scheduler, which is likely to cede the processor to the software interrupt, which has higher priority than
user processes.
    The kernel thread does TCP and IP processing and queues the packet to the appropriate application
queue, called a socket queue (Fig. 2.12). Assume that the application is a browser such as Netscape.
Netscape runs as a process that may have been asleep waiting for data and is now considered for being
run on the processor by the scheduler. After the software interrupt exits and control passes back to the
scheduler, the scheduler may decide to run Netscape in place of the original Java program.

---

## PDF page 69

42        Chapter 2 Network implementation models
