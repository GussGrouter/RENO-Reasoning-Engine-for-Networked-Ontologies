# Network Algorithmics — 6.5 Avoiding system calls or Kernel Bypass (slice)

- Source: raw/code/pdf/Network.Algorithmics.pdf
- Full-text extraction: processed/code/network-algorithmics-full-layout.txt
- Slice start: PDF page 193
- Slice: from `6.5 Avoiding system calls or Kernel Bypass` up to next detected section heading

---

6.5 Avoiding system calls or Kernel Bypass
For now, forget about the intervening discussion of select() and recall the discussion of user-level net-
working. We seem to have gotten the kernel out of the picture on the receipt or sending of a packet,
but sadly that is not quite the case. When an application wants to send data, it must somehow tell the
adaptor where the data is.
    When the application wants to receive data, it must specify buffers where the received packet data
should be written to. Today, in UNIX this is typically done using system calls, where the application
tells the kernel about data it wishes to send and buffers it wishes to receive to. Even if we implement
the protocol in user space, the kernel must service these system calls (which can be expensive; see
Chapter 2) for every packet sent and received.
    This appears to be required because there can be several applications sending and receiving data
from a common adaptor; since the adaptor is a shared resource, it seems unthinkable for an application
to write directly to the device registers of a network adaptor without kernel mediation to check for
malicious or erroneous use. Or is it?
    A simple analogy suggests that alternatives may be possible. In Fig. 6.7 we see that when an appli-
cation wants to set the value of a variable X equal to 10, it does not actually make a call to the kernel.
If this were the case, every read and write in a program would be slowed down very badly. Instead, the
hardware determines the virtual page of X, translates it to a physical page (say, 10) via the TLB, and
then allows direct access as long as the application has Page 10 mapped into its virtual memory.
    If Page 10 is not mapped into the application’s virtual memory, the hardware generates an exception
and causes the kernel to intervene to determine why there is a page access violation. Notice that the
kernel was involved in setting up the virtual memory for the application (only the kernel should be
allowed to do so, for reasons of security) and may be involved if the application violates its page
accesses that the kernel set up. However, the kernel is not involved in every access. Could we hope for
a similar approach for application access to adaptor memory to avoid wasted system calls (P1)?
    To see if this is possible, we need to examine more carefully what information an application sends
and receives from an adaptor. Clearly, we must prevent incorrect or malicious applications from dam-
aging other applications or the kernel itself. Fig. 6.8 shows an application that wishes to receive data
directly from the adaptor. Typically, an application that does so must queue a descriptor. A descriptor
is a small piece of information that describes the buffer in main memory where the data for the next

                                               6.5 Avoiding system calls or Kernel Bypass           167




FIGURE 6.7
Reading and writing to memory is not mediated by the kernel.




FIGURE 6.8
Application device channels.


packet (for this application) should be written to. Thus we should consider carefully and separately
both descriptor memory as well as the actual buffer memory.
    We can deal with descriptor memory quite easily by recalling that the adaptor memory is memory
mapped. Suppose that the adaptor has 10,000 bytes of memory that is considered memory on the bus
and that the physical page size of the system is 1000 bytes. This means that the adaptor has 10 physical
pages. Suppose we allocate two physical pages to each of five high-performance applications (e.g.,
Web, FTP) that want to use the adaptor to transfer data. Suppose the Web application gets two physical
pages, 9 and 10. Then the kernel maps the physical pages 9 and 10 into the Web application’s page
table and the physical pages 3 and 4 into the FTP application’s page table.
    Now the Web application can write directly to physical pages 9 and 10 without any danger; if it
tries to write into pages 3 and 4, the virtual memory hardware will generate an exception. Thus we are
exploiting existing hardware (P4c) in the form of the TLB to protect access to pages. So now let us
assume that Page 10 is a sequence of free buffer descriptors written by the Web application; each buffer
descriptor describes a page of main memory (assume this can be done using just 32 bits) that will be
used to receive the next packet described for the Web application.
    For example, Page 10 could contain the sequence 18, 12 (see Fig. 6.8). This means that the Web
application has currently queued physical pages 18 and 12 for the next incoming packet and its succes-
sor. We assume that pages 18 and 12 are in main memory and are physically locked pages that were
assigned to the Web application by the kernel when the Web application first started.
    When a new packet arrives for the Web application, the adaptor will demultiplex the packet to the
descriptor Page 10 using a packet filter, and then it will write the data of the packet (using DMA (direct

168        Chapter 6 Transferring control



memory access)) to Page 18. When it is done, the adaptor will write the descriptor 18 to a page of
written page descriptors (exactly as in fbufs), say, Page 9, that the Web application is authorized to
read. It is up to the Web application to finish processing written pages and periodically to queue new
free buffer descriptors to the adaptor.
    This sounds fine, but there is a serious security flaw. Suppose the Web application, through malice
or error, writes the sequence 155, 120 to its descriptor page (which it can do). Suppose further that Page
155 is in main memory and is where the kernel stores its data structures. When the adaptor gets the next
packet for the Web application it will write it to Page 155, overwriting the kernel data structures. This
causes a serious problem, at least causing the machine to crash.
    Why, you may ask, can’t virtual memory hardware detect this problem? The reason is that virtual
memory hardware (observe the position of the TLB in Fig. 6.7) only protects against unauthorized
access by processes running on the CPU. This is because the TLB intercepts every Read (or Write)
access done by the CPU and can do checks. However, devices like adaptors that do DMA bypass the
virtual memory system and access memory directly.
    This is not a problem in practice because applications cannot program the devices (such as disks,
adaptors) to read or write to specific places at the application’s command. Instead, access is always
mediated by the kernel. If we are getting rid of the kernel, then we have to ensure that everything the
application can instruct the adaptor to do is carefully scrutinized.
    The solution used in the application device channel (ADC) (Druschel et al., 1994) solution promoted
by Druschel, Davy, and Peterson is to have the kernel pass (P9, pass hints in interfaces) the adaptor a
list of valid physical pages that each application using the adaptor can access directly. This can be
done once when the application first starts and before data transfer begins. In other words, the time-
consuming computation involved in authorizing pages is shifted in time (P2) from the data transfer
phase to application initialization. For example, when the Web application first starts, it can ask the
kernel for two physical pages, say, 18 and 12, and then ask the kernel to authorize the use of these
pages to the adaptor.
    The kernel is then bypassed for normal data operation. However, if now the Web application queues
the descriptor 155 and a new packet arrives, the adaptor will first check the number 155 against its
authorized list for the application (i.e., 18, 12). Since 155 is not in the list, the adaptor will not overwrite
the kernel data structures (phew!).
    In summary, ADCs are based on shifting protection functions in space (P3c) from the kernel to the
adaptor, using some precomputed information (list of allowed physical pages, P2a) passed from the
kernel to the adaptor (P9), and augmented with the normal virtual memory hardware (P4c).
    The architecture community has, in recent years, been promoting the use of active messages (von
Eicken et al., 1992a), for similar reasons. An active message is a message that carries the address of the
user-level process that will handle the packet.9
    An active message (such as the ADC approach) avoids kernel intervention and temporary buffering
by using preallocated buffers or by using small messages that are responded to directly by the appli-
cation, thus providing low latency. Low latency, in turn, allows computation and communication to
overlap in parallel machines. The active messages implementation (von Eicken et al., 1992a) allowed


9 This is a way of avoiding packet filters completely by passing more information in packets, but it is a bit scary in a networking
environment because of the security risks; however, it is typically used only within clusters of machines that trust each other.

                                            6.5 Avoiding system calls or Kernel Bypass               169



only small messages or (large) block transfer. The fast messages implementation (Pakin et al., 1997)
goes further to combine user-level scatter–gather interfaces and flow control to enable uniform high
performance for a continuum from short to long messages.

What are kernels good for?
It is important to consider this question because the ADC and active message approaches bypass the
kernel. Kernels are good for protection (protecting the system and good users from malice or errors)
and for scheduling resources among different applications. Thus if we remove the kernel from the run-
time data path, it is up to the solution to provide these services in lieu of the kernel. For example, ADCs
do protection using the virtual memory hardware (to protect descriptors) and adaptor enforcement (to
protect buffer memory).
     It also must multiplex the physical communication link (especially on the sending side) among the
different ADCs and provide some sort of fairness. To do this in every device would require replicating
traditional kernel code in every device; however, it can be argued that some devices, such as the disk
and the network adaptor, are special in terms of their performance needs and are worth giving special
treatment. The first commercial deployment of the ADC idea and the UUNET solution (similar to
ADCs and proposed concurrently) advocated at Cornell (von Eicken et al., 1995) was known as the
Virtual Interface Architecture (VIA). We briefly describe VIA and then move on to the modern version
called DPDK (2018) that is widely deployed.
