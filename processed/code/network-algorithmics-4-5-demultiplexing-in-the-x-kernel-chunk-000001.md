# network-algorithmics-4-5-demultiplexing-in-the-x-kernel (chunk 000001)

# Network Algorithmics — 4.5 Demultiplexing in the x-kernel (slice)

- Source: raw/code/pdf/Network.Algorithmics.pdf
- Full-text extraction: processed/code/network-algorithmics-full-layout.txt
- Slice start: PDF page 111
- Slice: from `4.5 Demultiplexing in the x-kernel` up to next detected section heading

---

4.5 Demultiplexing in the x-kernel
The x-kernel (Hutchinson and Peterson, 1991) provides a software infrastructure for protocol imple-
mentation in hosts. The x-kernel system provides support for a number of required protocol functions.
One commonly required function is protocol demultiplexing. For example, when the Internet routing
layer IP receives a packet, it must use the protocol field to determine whether the packet should be
subsequently sent to TCP (transmission control protocol) or UDP (user datagram protocol).
    Most protocols do demultiplexing based on some identifier in the protocol header. These identifiers
can vary in length in different protocols. For example, Ethernet-type fields can be 5 bytes while TCP
port numbers are 2 bytes long. Thus the x-kernel allows demultiplexing based on variable-length pro-
tocol identifiers. When the system is initialized, the protocol routine can register the mapping between
the identifier and the destination protocol with the x-kernel. At run time, when a packet arrives the pro-
tocol routine can extract the protocol identifier from the packet and query the x-kernel demultiplexing
routine for the destination protocol. Since packets can arrive at high speeds, the demultiplexing routine
should be fast. This leads to the following problem.

Problem
On average, the fastest way to do a lookup is to use a hash table. As shown in Fig. 4.9, this requires
computing some hash function on the identifier K to generate a hash index, using this index to access
the hash table, and comparing the key L stored in the hash table entry with K. If there is a match, the
demultiplexing routine can retrieve the destination protocol associated with key L. Assume that the
hash function has been chosen to make collisions infrequent.
    However, since the identifier length is an arbitrary number of bytes, the comparison routine that
compares the two keys must, in general, do byte-by-byte comparisons. However, suppose the most
common case is 4-byte identifiers, which is the machine word size. In this case, it is much more efficient
to do a word comparison. Thus the goal is to exploit efficient word comparisons (P4c) to optimize the
expected case (P11). How can this be done while still handling arbitrary protocols?

Hint: Notice that if the x-kernel has to demultiplex a 3-byte identifier, it has to use a byte-by-
byte comparison routine; if the x-kernel has to demultiplex a 4-byte identifier and 4 bytes are the
machine word size, it can use a word compare. The first degree of freedom that can be exploited is
to have different comparison routines for the most common cases (e.g., word compares, long-word
compares) and a default comparison routine that uses byte comparisons. Doing so trades some extra

4.6 Tries with node compression            85

space for time (P4b). For correctness, however, it is important to know which comparison routine
to use for each protocol. Consider invoking principles P9 to pass hints in interfaces and P2a to do
some precomputation.

Solution
Each protocol has to declare its identifier and destination protocol to the x-kernel when the system
initializes. When this happens, each protocol can predeclare its identifier length, so the x-kernel can use
a specialized comparison routine for each protocol. Effectively, information is being passed between the
client protocol and the x-kernel (P9) at an earlier time (P2a). Assume that the x-kernel has a separate
hash table for each client protocol and that the x-kernel knows the context for each client in order to
use code specialized for thatclient.

Exercises
