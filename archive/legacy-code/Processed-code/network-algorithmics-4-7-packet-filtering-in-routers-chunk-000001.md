# network-algorithmics-4-7-packet-filtering-in-routers (chunk 000001)

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
