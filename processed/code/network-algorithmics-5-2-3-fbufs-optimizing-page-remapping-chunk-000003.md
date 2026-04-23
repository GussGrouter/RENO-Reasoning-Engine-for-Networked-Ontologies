# network-algorithmics-5-2-3-fbufs-optimizing-page-remapping (chunk 000003)

To implement the fbuf idea the operating system could take some number of physical pages
P1 , . . . , Pk and premap them onto the page tables of the Ethernet driver, the TCP/IP code, and the
Web application. The same operation could be performed with a different set of physical pages for
Ethernet, OSI, and FTP. Thus we are using principle P2a to precompute mappings. Reserving physical
pages for each path could be wasteful because traffic is bursty; instead, a better idea is to lazily establish
(P2b) such mappings when a path becomes busy.
    Lazy establishment avoids the overheads of updating multiple levels of page tables, acquiring locks,
flushing TLBs, and allocating destination VM after the first few data packets arrive and are sent. Instead,
all this work is done once, when the transfer first starts. To make fbufs work, it is crucial that when a
packet arrives, the lowest-level driver (or even the adaptor itself) be able to quickly figure out what the
complete path the packet will be mapped to when receiving a packet from the network. This function,
called early demultiplexing, is described in detail in Chapter 8. Intuitively, in Fig. 5.5 this is done by
examining all the packet headers to determine (for instance) that a packet with an Ethernet, IP, and
HTTP header belongs to Path 1.
    The driver (or the adaptor) will then have a list of free buffers for that path, which will be used
by the adaptor to write the packet to; when the adaptor is done it will pass the buffer descriptor to the
next application in the path. Note that a buffer descriptor is only a pointer to a shared page, not the
page itself. When the last application in the path finishes with the page, it passes it back to the first
application in the path, where it again becomes a free buffer, and so on.
    At this point, the reader may wonder why paths are unidirectional. Paths are made unidirectional
because the first process on each path is assumed to be a writer and the remaining processes are as-
sumed to be readers. This can be enforced during the premapping by setting a write-allowed bit for
the first application in its page table entry, and a read-only bit in the page table entries of all the other
applications. Clearly, this is asymmetric in both directions and requires unidirectional paths. But this
does ensure some level of protection.
    This is shown in Fig. 5.6 with just two domains in a path. Note that the writer writes packets into
buffers described by a queue of free fbufs and then puts the written descriptor onto a queue of written
fbufs that are read by the next application (only one is shown in Fig. 5.6).

122        Chapter 5 Copying data

FIGURE 5.6
The single writer optimization.
