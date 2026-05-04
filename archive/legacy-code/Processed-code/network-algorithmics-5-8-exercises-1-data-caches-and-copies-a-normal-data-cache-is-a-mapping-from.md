# Network Algorithmics — 5.8 Exercises 1. Data caches and copies: A normal data cache is a mapping from a memory location address to a (slice)

- Source: raw/code/pdf/Network.Algorithmics.pdf
- Full-text extraction: processed/code/network-algorithmics-full-layout.txt
- Slice start: PDF page 170
- Slice: from `5.8 Exercises 1. Data caches and copies: A normal data cache is a mapping from a memory location address to a` up to next detected section heading

---

5.8 Exercises
1. Data caches and copies: A normal data cache is a mapping from a memory location address to a
   piece of content. If the content is frequently accessed, then the content can be accessed directly from
   the fast cache instead of making a memory access. Assuming the cache is a write-back cache, even
   writes can be written to the cache instead of memory and only written to memory when the cache is
   overwritten. A modern cache block is fairly large (128 bits), with a mapping from a 32-bit address
   to 128 bits of data starting at that address.
   We want to address the copying problem where various modules (including the network and file
   system) copy data via intermediate buffers that are soon overwritten (e.g., socket buffer, application
   buffer). The chapter did so with software changes. Here we consider whether changing the hardware
   architecture can help without software changes such as IO-Lite, fbufs, and mmap.
   • Even an ordinary data cache may help remove some of the overhead when copying data from
     location L to location M. Explain why. (Assume that location M is a temporary buffer that is
     soon overwritten, as in a socket buffer. Assume that if only a single word is written in a large
     cache block, the remaining words can be marked invalid.) Intuitively, this problem is asking
     whether there is an equivalent of COW (used to reduce copying between virtual address spaces)
     in the world of data caches.
   • Now assume a different data cache design, where a cache is a mapping from one or more
     addresses to the same content. Thus a cache has changed from a one-to-one mapping to a many-
     to-one mapping. For example, assume a cache where two locations can point to the same content.
     Thus a cache entry may be (L, M, C), where L and M are addresses and C is the common con-

144      Chapter 5 Copying data



     tents of L and M. A memory access to either L or M will return C. What is the advantage over
     the previous scheme in the previous item?
   • This is all very speculative and wild. Comment on the disadvantages of the idea in the previous
     item. In particular, many caches use a technique called set associativity, where a simple hash
     function (e.g., low-order bits) is used to select a small set of cache entries that the hardware
     searches in parallel. Why might the multiple address per cache entry interact poorly with the set
     associative search?
2. Application-level optimizations for Web servers: Operating systems such as the Exokernel (En-
   gler et al., 1995) take an even more extreme viewpoint and allow the application to customize kernel
   features for its benefit without compromising safety for other applications. One interesting optimiza-
   tion is to combine the final TCP FIN with the read of the last data segment (an optimization allowed
   by TCP).
   • Why does this optimization help small Web transfers (which are quite common)?
   • Why is this optimization hard to do in a regular Web server, and why is it easier if the application
     is integrated with the kernel, as in the Exokernel?
   • Explain how this optimization can be migrated to an ordinary Web server by passing information
     across the interface (P9) without compromising safety.
3. Reverse copyout: The emulated COW paper (Brustoloni and Steenkiste, 1996) describes an inter-
   esting degree of freedom (P13) for copying page-aligned data between two modules (say, system
   and application). Imagine that you wish to copy a partial page from an application page, X, to a
   system page, Y . If the page is full, assume that you can swap the two pages efficiently. Assume the
   partial page has useful data D and some remainder R.
   • If the amount of data D is small compared to R, it is simpler to copy D to the destination page in
     Y . On the other hand, if D is large (say, almost all of the page) compared to R, devise a simple
     strategy to minimize copying. Note that if the destination page, Y , has some other data in the
     remainder of the page, that data must remain after the copy.
   • What is a simple threshold you would use to choose between these two strategies?

                                                                                                                  CHAPTER


Transferring control
                                                                                                                      6
                                                                           Control thy passions, lest they take vengeance on thee.
                                                                                                                      —Epictetus


In a Scott Adams cartoon Dilbert complains to Dogbert that he is embarrassed to work at a company
where even paying a simple invoice takes 6 months. The invoice first comes into the mail room for
aging, spends some time at the secretary’s desk, goes to the desk of the main decision maker, and
finally ends up in accounts payable. When processing an invoice in Dilbert’s company, the flow of
control works its way through layers of command, each of which incurs significant overhead.
    A management consultant might suggest that Dilbert’s company streamline the processing of an
invoice by eliminating mediating layers wherever possible and by making each layer as responsive as
possible. However, each layer has some reason for existence. The mailroom aggregates mail delivery
service for all departments in the company. The secretary protects the busy boss from interrupts and
weeds out inappropriate requests. The boss must eventually decide whether the invoice is worth paying.
Finally, the mundane details of disbursing cash are best left to accounts payable.
    A modern CPU processing a network message also goes through similar layers of mediation. The
device, for example, an Ethernet adaptor, interrupts the CPU, asking somewhat stridently for attention.
Control is passed to the kernel. The kernel batches interrupt wherever possible, does the network layer
processing for the packet, and finally schedule the application process (say, a Web server) to run. As
always, the reception of a single packet provides too limited a picture of the overall processing context.
For instance, a Web server will parse the request (such as a GET) in the network packet, look for the
file, and institute proceedings to retrieve the file from disk. When the file gets read into memory, a
response containing the requested file is sent back, prepended with an HTTP header.
    While Chapter 5 concentrated on reducing the overhead of operations that touch the data in a packet
(e.g., copying, checksumming), this chapter concentrates on reducing the control overheads involved in
processing a packet. As in Chapter 5, we start by examining the control overheads involved in sending
or receiving a packet. We then broaden to our canonical network application, a Web server.
    As we said in the introduction to Chapter 5, there have been changes in the underlying technologies,
but not the principles, since the first edition. The most relevant for the purposes of reducing control
overheads are as follows. First, as described in Chapter 5 multicore CPUs are the norm. However, the
issue that concerns us more in this chapter is affinity. How do modern CPUs make sure that that network
processing occurs in the same CPU (or on CPUs that share the same L3 cache) that runs the application?
We describe packet steering mechanisms to affinitize packet processing.
    Second, hypervisors and virtual switches are standard in data centers to improve server utilization.
This adds another layer of control overhead. Thus, new solutions like SRIOV (2018) (Single Root I/O
Virtualization, see later for details) have emerged to bypass these overheads. Third, in the first edition,
Network Algorithmics. https://doi.org/10.1016/B978-0-12-809927-8.00012-9
Copyright © 2022 Elsevier Inc. All rights reserved.
                                                                                                                            145

146       Chapter 6 Transferring control



the major industry standard for kernel bypass to avoid system calls was called VIA (Buonadonna et al.,
2002). VIA has largely been subsumed by a new standard called DPDK (2018) (Data Plane Develop-
ment Kit) that we describe at the end of Section 6.5.
    Fourth, warehouse scale computing (Barroso et al., 2017) has become the de facto standard for pro-
cessing user requests in clouds like Amazon, Azure, and Google. In response to the slowing down of
Moore’s Law, such clouds often serve a request (e.g., a Search or Shopping request) by farming out a
query to thousands of servers and collecting the response. Since the response is gated by the response
of the slowest server, there is a new focus on the tail latency of requests, seeking to reduce this latency
to microseconds. Further, compared to High Performance Computing (Barroso et al., 2017), warehouse
scale computing is less interested in merely higher performance, but in the highest performance per dol-
lar. Thus, dedicating cores to a networking function may be unacceptable in the interests of maximizing
resource utilization (Marty et al., 2019).
    We are grateful to Amy Ousterhout, Jeff Mogul, and Sylvia Ratnasamy for pointers to recent work;
any errors or omissions, of course, are completely our responsibility.
    This chapter is organized as follows. Section 6.1 starts by describing the control flow costs involved
in a computer: interrupt overheads (involved when a device asks asynchronously for attention), sys-
tem calls (involved when a user asks the kernel for service, thus moving the flow of control across a
protection boundary), and process-context switching (allowing a new process to run when the current
process is stymied waiting for some resource or has run too long). Thus the rest of this chapter is orga-
nized around reducing these control overhead costs, from the largest (context switching) to the smallest
(interrupt overhead).
    Accordingly, Section 6.2 concentrates on reducing process-context switching by describing how to
structure networking code (e.g., TCP/IP) to avoid context switching. Section 6.3 then describes how to
structure application code (e.g., a Web server) to reduce context-switching costs. Sections 6.4 and 6.5
focus on reducing or eliminating system call overhead. Section 6.4 shows how to reduce overhead in
the implementation of a crucial system call used by event-driven Web servers to decide which of the
connections they are handling are ready to be serviced. Section 6.5 goes further and describes user-level
networking that bypasses the kernel in the common case of sending and receiving a packet. Section 6.6
describes more recent and forward looking research in fundamentally restructuring operating systems
to reduce network control overhead. Finally, Section 6.7 briefly describes simple ideas to avoid interrupt
overhead.
    The techniques described in this chapter (and the corresponding principles invoked) are summarized
in Table 6.1.


   Quick reference guide
   The most useful sections for an implementor today are as follows. Section 6.3 describes how to structure application code
   (e.g., a Web server) to reduce context-switching costs, presenting alternatives to event-driven Web servers. Section 6.4
   focuses on reducing the overhead of the select() system call (or similar calls in other operating systems) used by event-
   driven servers to decide which client to service next, and the use of the epoll() systems call in Linux. Section 6.5 shows
   how to eliminate system call overhead using techniques such as DPDK (Data Plane Development Kit) and SRIOV (Single
   Root I/O Virtualization). Section 6.6 describes radical restructuring of operating systems towards reducing network control
   overheads. Section 6.7 describes NAPI polling in Linux to prevent receive livelock.

                                                                      6.1 Why control overhead?          147



             Table 6.1 Techniques for reducing control overhead that are discussed in
             this chapter, together with the corresponding principles.
             Number                             Principle                              Used in
             P8         Go beyond downcalls used in specifications               Upcalls
             P8         Process per message, not per layer                       x-Kernel
             P13        Link protocol implementation with user code              Mach variants
             P13        Process per disk access                                  Flash
             P13        Modularize by task, not clients                          Haboob Web server
             P4         VM mapping to avoid copies in cache and application      Flash
             P15        Bitmap tree                                              Fast ufalloc()
             P12a       Incrementally compute interest vector                    Fast select()
             P9         Pass hints from protocol to select ()
             P12        Remember interest across calls
             P3c        Move protection from kernel to adaptor                   ADCs
             P2         Have kernel authorize adaptor on initialization
             P13        Batch process interrupts                                 Most OSs
             P2b        Execute protocol in the context of the receive process   LRP (lazy receiver
                                                                                 processing)
