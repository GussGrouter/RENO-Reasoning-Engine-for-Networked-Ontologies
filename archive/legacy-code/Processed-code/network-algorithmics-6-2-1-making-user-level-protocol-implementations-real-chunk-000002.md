# network-algorithmics-6-2-1-making-user-level-protocol-implementations-real (chunk 000002)

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
