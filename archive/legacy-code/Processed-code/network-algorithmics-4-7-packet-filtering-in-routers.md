# Network Algorithmics — 4.7 Packet filtering in routers (slice)

- Source: raw/code/pdf/Network.Algorithmics.pdf
- Full-text extraction: processed/code/network-algorithmics-full-layout.txt
- Slice start: PDF page 114
- Slice: from `4.7 Packet filtering in routers` up to next detected section heading

---

4.7 Packet filtering in routers
Chapter 12 describes protocols that set up resources at routers for traffic, such as video, that needs
performance guarantees. Such protocols use the concept of packet filters, sometimes called classifiers.
Thus, in Fig. 4.12 each receiver attached to a router may specify a packet filter describing the packets
it wishes to receive. For example, in Fig. 4.12 Receiver 1 may be interested in receiving NBC, which is
specified by Filter 4. Each filter is some specification of the fields that describe the video packets that
NBC sends. For example, NBC may be specified by packets that use the source address of the NBC
transmitter in Germany and use a specified TCP destination and source port number.
    Similarly, in Fig. 4.12 Receiver m may be interested in receiving ABC Sports and CNN, which are
described by Filters 1 and 7, respectively. Packets arrive at the router at high speeds and must be sent

88        Chapter 4 Principles in action




FIGURE 4.12
Packet filtering in a router may require a slow linear scan of all filters followed by making a copy of the packet for
all filters that match.


to all receivers that request the packet. For example, Receivers 1 and 2 may both wish to receive NBC.
This leads to the following problem.
Problem
Each receiving packet must be matched against all filters and sent to all receivers that match. A simple
linear scan of all filters is expensive if the number of filters is large. Assume the number of filters is
over a thousand. How can this expensive process be sped up?
Hint: One might think of optimizing the expected case by caching (P11a). However, why is caching
difficult in this case? Consider adding a field (P10) to the packet header to make caching easier.
Ideally, which protocol layer should this be added to? Adding a fixed well-known field for each
possible video type is not a panacea because it requires global standardization, and filters can be
based on other fields, such as the source address. Assume the field you add does not require globally
standardized identifiers. What properties of this field must the source ensure?

Solution
Caching (P11a), the old workhorse of system designers, is not very straightforward in this problem. In
general, a cache stores a mapping between an input a and some output f (a). The cache then consists
of a set of pairs of the form (a, f (a)). This set of pairs is stored as a database keyed by values of
a. The database can be implemented as a hash table (in software) or a content-addressable memory
(in hardware). Given input a and the need to calculate f (a), the database is first checked to see if
a is already in the database. If so, the fast path exits with the existing value of f (a). If not, f (a) is
computed using some other (possibly expensive) computation and the pair (a, f (a)) is then inserted
into the cache database. Subsequent inputs with value a can then be calculated very fast.
    In the packet filtering problem, the goal is to calculate the set of receivers associated with a packet
P . The problem is that the output is a function of a (potentially) large number of packet header fields
of P . Thus to use caching, one has to store a large portion of the headers of P associated with the set of
receivers for P . Storing a mapping between 64 bytes of packet header and an output set of receivers is
an expensive proposition. It is expensive in time, since searching the cache can take longer because the

                                                                    4.7 Packet filtering in routers       89




FIGURE 4.13
Adding a flow identifier (which is unique only with respect to a source) can speed up packet filtering.



keys are wide. It is also clearly expensive in storage. The larger storage needs in turn imply that fewer
mappings can be cached for a given cache size, which leads to a poorer cache hit rate.
    The ideal is to cache a mapping between one or two packet fields and the output receiver set. This
would speed up cache search time and improve the cache hit rate. These fields should also preferably
be in the routing header, which routers examine anyway. The problem is that there may be no such field
that uniquely fingerprints packet P .
    However, suppose we are system designers designing the routing protocol. We can add a field to
the routing header. The problem might seem trivial if we could assign each possible stream of packets
a unique global identifier. For example, if we could assign NBC identifier 1, ABC identifier 2, and
CNN identifier 3, then we could cache using the identifier as the key. Such a solution would require
some form of global standards committee responsible for naming every application stream. Even if that
could be done, the receiver filter might ask for all NBC packets from a given source, and the filter could
depend on other packet fields. This leads to the following final idea.
    Change the routing header to add a flow identifier F (Fig. 4.13), whose meaning depends on the
source. In other words, different sources can use the same flow identifier because it is the combination
of the source and the flow identifier that is unique. Thus there is no need for global standardization (or
other global coordination) of flow identifiers. A flow identifier is only a local counter maintained by the
source. The idea is that a sending application at the sender can ask the routing layer for a flow identifier.
This identifier is added to the routing header of all the packets for this application.
    As usual, when the application packet first arrives, the router does a (slow) linear search to deter-
mine the set of receivers associated with the packet header. Because identifiers are not unique across
sources, the router caches the mapping using the concatenation of the packet source address and the
flow identifier as the key. Clearly, correctness depends on the sender application’s not changing fields
that could affect a filter without also changing the flow identifier in the packet.

90        Chapter 4 Principles in action




FIGURE 4.14
The LSP of router R1 (with even 500 endnode neighbors) may be too large to fit into a data link frame. Without a
clever idea, this would require inefficient fragmentation and reassembly of the LSP at every hop.



Exercises

• What can go wrong if the source crashes and comes up again without remembering which identifiers
  it has assigned to different applications? What can go wrong when a receiver adds a new filter? How
  can these problems be solved?
• In the current solution, the flow identifier is used as a tip (Chapter 3) and not as a hint. What addi-
  tional costs would be incurred if the flow identifier-source address pair is treated as a hint and not as
  a tip?
