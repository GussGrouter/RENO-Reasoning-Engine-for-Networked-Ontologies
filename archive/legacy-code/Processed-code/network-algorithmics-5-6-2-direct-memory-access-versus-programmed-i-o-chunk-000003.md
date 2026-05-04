# network-algorithmics-5-6-2-direct-memory-access-versus-programmed-i-o (chunk 000003)

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
