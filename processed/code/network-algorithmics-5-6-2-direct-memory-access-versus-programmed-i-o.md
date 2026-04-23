# Network Algorithmics — 5.6.2 Direct memory access versus programmed I/O (slice)

- Source: raw/code/pdf/Network.Algorithmics.pdf
- Full-text extraction: processed/code/network-algorithmics-full-layout.txt
- Slice start: PDF page 169
- Slice: from `5.6.2 Direct memory access versus programmed I/O` up to next detected section heading

---

5.6.2 Direct memory access versus programmed I/O
Earlier sections stated that the Witless scheme uses programmed I/O, or PIO (i.e., the processor or
CPU is involved in every word transferred between memory and adaptor), while other schemes, such as
VAX Clusters, use DMA (where the adaptor copies data directly to memory). It may seem that DMA is
always better than PIO. However, comparisons between DMA and PIO are tricky because each method
has subtle implications for the overall memory bandwidth used.
    For instance, PIO has one advantage in that the data flows through the processor and thus ends up
in the processor cache. This can be useful to prevent loss of memory bandwidth for subsequent access.
Also, with PIO it is easy to integrate other functions, such as checksums, without requiring adaptor
hardware to do the same function.
    However, some studies have shown that if data arrives and is used much later (e.g., one scheduling
quantum later) by the application, then placing data in the D-cache too early is wasteful of the D-cache
and lowers rather than raises D-cache hit rate. On the other hand, DMA can steal cycles from the CPU
and also requires some careful cache invalidation when data is written into a memory location (that
could also be cached). So the jury is still out. The choice between the two is best decided on a case-by-
case basis, taking into account architectural considerations and the application at hand. A more detailed
study of the issues involved can be found in Mogul and Ramakrishnan (1997).



5.7 Conclusions
As networks get faster, links today, such as Gigabit Ethernet, are often faster than the buses and memo-
ries within desktop computers and servers. Thus memory and bus bandwidth are crucial resources. This
chapter describes techniques to optimize the use of memory and bus bandwidth for processing IP and
Web packets, the dominant traffic streams found today on the Internet.
    To this end, the chapter started by showing how to remove redundant copies involved in processing
an IP packet using adaptor memory or VM remapping. We then showed how to remove redundant
copies involved in processing Web requests at a server by generalizing VM remapping to include the
file system or by combining file system and network I/O in a single system call. We then showed how
to combine various data manipulations in one fell swoop. All of these techniques require changes to the
application and kernel, but the changes are fairly localized and mostly preserve modularity.
    It is important to state that all the performance problems involved in building a modern Web server
have not been eliminated. Complex Web sites, such as amazon.com, often use several tiers of processing
to respond to Web requests, including an application server, a Web server, and a database server. Such
database-driven Web servers introduce new bottlenecks that may require new techniques beyond those
described in this chapter. However, the underlying principles should hopefully remain the same.
    Table 5.1 presents a summary of the techniques used in this chapter, together with the major prin-
ciples involved. In terms of principles this chapter is about the repeated use of P1, avoiding obvious
waste, where the waste is unnecessary reads and writes that consume precious memory and bus band-
width. At first glance, principle P1 seems vacuous or at best a cliché. What makes this principle deeper
is that the waste is not apparent unless one broadens one’s vision to see as much of the system as
possible.
    Within each local subsystem (e.g., application to kernel, kernel to network, disk to file system) there
is no wasted memory bandwidth. It is only when one follows the adventures of a received packet that

                                                                               5.8 Exercises        143



one discovers the redundancy between application-to-kernel and kernel-to-network copies. It is only
when one broadens one’s view even further to see the contortions involved in responding to a Web
request that one notices the further redundancies involving the file system. Only when one broadens
one’s view further still does one see all the manipulations involved in processing a packet and the
wasted reads to memory. Finally, it is only when one examines the loading of instructions that one sees
the alarming possibility that the protocol code can be several times larger than the packet size.
    Thus the use of the first principle of network algorithmics requires a synoptic eye, one that sees
the whole system, from HTTP and its headers, to the file system, and down to the instruction caches.
While this seems daunting in complexity, Chapter 2 has already argued that simple models of hard-
ware, architecture, operating systems, and protocols can make such a holistic viewpoint possible. For
example, I-caches have a number of complex variants, but a simple model of a direct-mapped I-cache
with multiple instructions per block is not hard for an operating system designer to keep in mind.
    Finally, compared to the beauty and complexity of theoretical techniques such as the ellipsoid algo-
rithm for linear programming and the theory of rapidly mixing Markov chains, techniques in systems
such as copy avoidance seem drab and shallow. However, one can argue that the complexity of sys-
tems is not in depth (i.e., the complexity of each component by itself) but in breadth (i.e., the complex
relationships between components). Perhaps the breadth of understanding (HTTP, file system, network-
ing code, instruction cache implementation) required to optimize memory bandwidth in a Web server
provides some evidence for this thesis.
