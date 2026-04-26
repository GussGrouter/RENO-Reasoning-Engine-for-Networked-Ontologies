# network-algorithmics-6-5-avoiding-system-calls-or-kernel-bypass (chunk 000003)

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
