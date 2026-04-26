# network-algorithmics-4-8-avoiding-fragmentation-of-lsps (chunk 000001)

# Network Algorithmics — 4.8 Avoiding fragmentation of LSPs (slice)

- Source: raw/code/pdf/Network.Algorithmics.pdf
- Full-text extraction: processed/code/network-algorithmics-full-layout.txt
- Slice start: PDF page 117
- Slice: from `4.8 Avoiding fragmentation of LSPs` up to next detected section heading

---

4.8 Avoiding fragmentation of LSPs
The following problem actually arose during the design of the OSI and OSPF (Perlman, 1992) link
state routing protocols. This problem is about protocol design, as opposed to protocol implementation
once the design is fixed. Despite this, it illustrates how design choices can greatly affect implementation
performance.
    Chapter 2 and Section 4.3 described link state routing. Recall that in link state routing, a router must
send an LSP listing all its neighbors. The link state protocol consists of two separate processes. The
first is the update process that sends LSPs reliably from router to router using a flooding protocol that
relies on a unique sequence number per LSP. The sequence number is used to reject duplicate copies
of an LSP. Whenever a router receives a new LSP numbered x from source S, the router will remember
number x and will reject any subsequent LSPs received from S with sequence number x. After the
update process does its work, the decision process at every router applies Dijkstra’s algorithm to the
network map formed by the LSPs.
    While a router may have a small number of router neighbors, a router may have a large number of
host computers (endnodes) that are connected directly to the router on the same LAN. For example,
in Fig. 4.14 router R1 has 500 endnode neighbors E1 . . . E500. Large LANs may even have a larger
number of endnodes. This leads to the following problem.

4.8 Avoiding fragmentation of LSPs               91

Problem
At 8 bytes per endnode (6 bytes to identify the endnode and 2 bytes of cost information), the LSP
can be very large (40,000 bytes for 5000 endnodes). This is much too huge for the LSP to fit into a
maximum-size frame on many commonly used data links. For example, Ethernet has a maximum size
of 1500 bytes and FDDI specifies a maximum of 4500 bytes. This implies that the large LSP must be
fragmented into many data link frames on each hop and reassembled at each router before it can be sent
onward. This requires an expensive reassembly process at each hop to determine whether all the pieces
of a LSP have been received.
    It also increases the latency of link state propagation. Suppose that each LSP can fit in M data link
frames, that the diameter of the network is D, and that the time to send a data link frame over a link is 1
time unit. Then with hop-by-hop reassembly, the propagation time of an LSP can be D · M. If a router
did not have to wait to reassemble each LSP at each hop, the propagation delay would be only M + D.
When the link state protocol was being designed, these problems were discovered by implementors
reviewing the initial specification.
    On the other hand, it seems impossible to propagate the fragments independently because the LSP
carries a single sequence number that is crucial to the update process. Simply copying the sequence
number into each fragment will not help because that will cause the later fragments to be rejected,
since they have the same sequence number as the first fragment. The problem is to make the impossible
possible by shifting computation around in space to avoid the need for hop-by-hop fragmentation.
Changes to the LSP routing protocol are allowed.
Hint: Does the information about all 5000 endnodes have to be in the same LSP? Consider invoking
P3c to shift computation in space.
