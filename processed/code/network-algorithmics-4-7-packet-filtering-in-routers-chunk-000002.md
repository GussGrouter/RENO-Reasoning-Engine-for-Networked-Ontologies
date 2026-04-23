# network-algorithmics-4-7-packet-filtering-in-routers (chunk 000002)

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
