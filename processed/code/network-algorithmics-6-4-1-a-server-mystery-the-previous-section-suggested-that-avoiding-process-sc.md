# Network Algorithmics — 6.4.1 A server mystery The previous section suggested that avoiding process-scheduling overheads was important in a Web (slice)

- Source: raw/code/pdf/Network.Algorithmics.pdf
- Full-text extraction: processed/code/network-algorithmics-full-layout.txt
- Slice start: PDF page 186
- Slice: from `6.4.1 A server mystery The previous section suggested that avoiding process-scheduling overheads was important in a Web` up to next detected section heading

---

6.4.1 A server mystery
The previous section suggested that avoiding process-scheduling overheads was important in a Web
server. For example, an event-driven server completely reduces process scheduling overhead by using
a single thread for all clients and then using a FindActive() call such as select(). Now, the CERN
Web proxy used a process per client, and the Squid (formerly Harvest) Web server (Chankhunthod et
al., 1996) used an event-driven implementation. Measurements done in a LAN (local area network)
environment indeed showed (Chankhunthod et al., 1996) that the Squid Web proxy performed an order
of magnitude better than the CERN server.

160        Chapter 6 Transferring control



    A year later another group repeated these tests in a WAN (i.e., wide area network) environment
(Maltzahn et al., 1997) and found that in the WAN environment there was no difference in performance
between the CERN and Squid servers. The problem is to elucidate this mystery.
    The mystery was finally solved by Banga and Mogul (1998). A key observation is that given the
same throughput (in terms of connections per second), the higher round-trip delays in a WAN envi-
ronment lead to a larger number of concurrent connections in a WAN setting. For example, in a WAN
environment with mean connection times of 2 seconds (Banga et al., 1999) and a Web server throughput
of 3000 connections per second, Little’s law (from queuing theory) predicts that the average number of
concurrent connections is the product, or 6000.
    On the other hand, in a LAN environment with a round-trip delay of 2 milliseconds, the average
number of concurrent connections drops to six. Note that if the throughput stays the same, in the wide
area setting a large fraction of the connections must be idle (waiting for replies) at any given time.
    Given this, the two main causes of overhead were two system calls used by the event-driven server.
The standard UNIX implementation of both these calls scales poorly with a large number of connec-
tions. The two calls were:
• select(): Event-driven servers running on UNIX use the select() call for the FindActive() call. Ex-
  periments by Banga and Mogul (1998) show that more than half of the CPU is used for kernel and
  user-level select() functions with 500 connections.
• ufalloc(): The server also needs to allocate the lowest unallocated descriptor for new sockets or files.
  This seemingly simple call took around a third of the CPU time.
    ufalloc() performance can easily be explained and fixed. Normally, finding a free descriptor can
be efficiently implemented using a free list of descriptors. Unfortunately, UNIX requires choosing the
lowest unused descriptor. For example, if the currently allocated descriptor list has the elements (in an
unsorted order) 9, 1, 5, 4, 2, then one cannot determine that the lowest unallocated number is 3 without
traversing the entire unsorted list. Fortunately, a simple change to the kernel implementation (P15, use
efficient data structures) can reduce this overhead to nearly zero.6
