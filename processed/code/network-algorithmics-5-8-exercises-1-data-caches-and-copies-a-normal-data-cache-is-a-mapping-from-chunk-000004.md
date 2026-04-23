# network-algorithmics-5-8-exercises-1-data-caches-and-copies-a-normal-data-cache-is-a-mapping-from (chunk 000004)

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
