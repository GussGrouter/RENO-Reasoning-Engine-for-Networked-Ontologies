# Network Algorithmics — 6.2.1 Making user-level protocol implementations real (slice)

- Source: raw/code/pdf/Network.Algorithmics.pdf
- Full-text extraction: processed/code/network-algorithmics-full-layout.txt
- Slice start: PDF page 178
- Slice: from `6.2.1 Making user-level protocol implementations real` up to next detected section heading

---

6.2.1 Making user-level protocol implementations real
Most modern machines certainly do not implement each protocol layer in a separate process. Instead,
in UNIX or Linux, all the protocol code (transport, network, and data link) is handled as part of a single
kernel “process” or a more lightweight process called a “thread”. When a packet arrives via an interrupt,
the interrupt handler notes the arrival of the packet, possibly queues it to memory, and then schedules a
kernel thread (via what is sometimes called a software interrupt) to actually process the packet.
    The kernel thread does the data link, network, and transport-layer code (using upcalls); by looking at
the transport port numbers, the kernel process knows the application. It then wakes up the application.
Thus every packet is processed using at least two context switches: one from the interrupt context to
the kernel process doing protocol handling, and one from the kernel thread to the thread running the
application code (e.g., the Web, FTP).
    The idea behind user-level protocol implementation is to realize the aspect of Clark’s idea shown in
the receive process of Fig. 6.2, where the protocol handlers execute in the same process as the appli-
cation and can communicate using upcalls. User-level implementations have two possible advantages:
We can potentially bypass the kernel and go directly from the interrupt handler to the application, as in
the Clark model, saving a context switch. Also, the protocol code can be written and debugged in user
space, which is a far friendlier place to implement protocols (debugging tools work in user space and
do not work well at all in the kernel).
    One extreme way to do this was advocated in Mach, where all protocols were implemented in
user space. Also, protocols were allowed to be significantly more general than in Clark’s example of
Fig. 6.2. Thus when a receiving interrupt handler received a packet, it had no way of easily telling to
which process it should dispatch the packet (since the network-layer implementations done in the final
process contained the demultiplexing code). In particular, one can’t just call transport to examine the
port number (as in Clark’s example) since we can have lots of possible transport protocols and lots of
possible network protocols.
    A naive method was initially used, as shown in Fig. 6.3. This involved a separate demultiplexing
process that received all packets and examined them to determine the final destination process, which
they are then dispatched to. The naive method was quite inefficient years ago; it is less so now with
multicore machines as we will see in the structuring of Google’s Snap (Marty et al., 2019) system
described later in this chapter. The inefficiency arises because context switches were expensive, and the
new demultiplexing process actually adds back the missing context switch.
    The simple idea used to remedy this situation is to pass extra information (P9) across the
application–kernel interface so that each application can pass information about what kinds of packets
it wants to process. This is shown in Fig. 6.4. For example, a mail application may wish for all pack-
ets whose Ethernet-type field is IP, whose IP number specifies TCP and whose TCP destination port
number is 25.

152       Chapter 6 Transferring control




FIGURE 6.3
Demultiplexing a packet to the final destination process using an intermediate demultiplexing process is expensive.




FIGURE 6.4
The packet filter approach to demultiplexing.


     Recall that we are talking about the mail application implementing all of IP, TCP, and mail. To do so,
the kernel defines an interface, which is typically some form of programming language. For example,
the earliest one was the CSPF (CMU Stanford packet filter), which specifies the fields for packets
using a stack-based programming language. A more commonly used language is BPF (Berkeley packet
filter), which uses a stack-based language; a more efficient language is Pathfinder. These demultiplexing
algorithms are described in Chapter 8.
     Note that one has to be careful about passing information from an application to a kernel; any
such information should be checked so that malicious or wrong applications cannot destroy the kernel.
In particular, one has to prevent applications from providing arbitrary code to kernels, which then
causes havoc. Fortunately, there are software technologies that can “sandbox” foreign code so that it
can do damage only within its own allotted space of memory (its sandbox). For example, a stack-based
language can be made to work on a specified size of stack that can be bounds checked at every point.
This form of technology has culminated recently in execution of arbitrary Java applets received from
the network.
     Clearly, if packets are dispatched from the kernel interrupt handler (using the collection of packet
filters) to the receiving process, the receiving process should implement the protocol stack. However,
replicating the TCP/IP code in every application would cause a lot of code redundancy. Thus TCP/IP
is generally (in such systems) implemented as a shared library that is linked in (a single copy is used
to which the application has a pointer, but with the code written in a so-called reentrant way, to allow
reuse).
     This is not as easy as it looks because there is some TCP state that is common to all connections,
though most are TCP state connection specific. There are other problems because the last write done

                                     6.3 Avoiding context-switching overhead in applications                               153



by an application should be retransmitted by TCP, but the application may exit its process after its last
write. However, these problems can be fixed. User-level implementations have been written (Maeda and
Bershad, 1993; Thekkath et al., 1993) to provide excellent performance. Fundamentally, they exploit a
degree of freedom (P13) in observing that protocols do not have to be implemented in the kernel.
