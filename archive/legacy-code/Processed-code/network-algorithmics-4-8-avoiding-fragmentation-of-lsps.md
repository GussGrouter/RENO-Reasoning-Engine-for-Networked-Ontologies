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

Solution
If the individual fragments of the original LSP of R1 are to be propagated independently without hop-
by-hop reassembly, then each fragment must be a separate LSP by itself, with a separate sequence
number. This crucial observation leads to the following elegant idea.
    Modify the link state routing protocol to allow any router R1 to be multiple pseudorouters R1a ,
R1b , R1c (see Fig. 4.15). The original set of endnodes are divided among these pseudorouters, so the
LSP of each pseudorouter can fit into most data link frames without the need for fragmentation. For
example, if most data link sizes are at least 576 bytes, roughly 72 endnodes can fit within a data link
frame.
    How is this concept of a pseudorouter actually realized? In the original LSP propagation, each
router had a 6-byte ID that is placed in all LSPs sent by the router. To allow for pseudorouters, we
change the protocol to have LSPs carry a 7-byte ID (6-byte router ID + 1-byte pseudorouter ID). The
pseudorouter ID can be assigned by the actual router that houses all the pseudorouters. By allowing 256
pseudorouters per router, roughly 18,000 endnodes can be supported per router.
    While the LSP propagation treats pseudorouters separately, it is crucial that route computation treat
the separate pseudorouters as one router. After all, the endnodes are all directly connected to R1 in our
example. But this is easily done because all the LSPs with the same first 6 bytes can be recognized as
being from the same router.
    In summary, the main idea is to shift computation in space (P3c) by having the source fragment the
original LSP into independent LSPs instead of having each data link do the fragmentation. This is a

92        Chapter 4 Principles in action




FIGURE 4.15
Avoiding hop-by-hop fragmentation by dividing a large router into pseudorouters.



good example of systems thinking. Needless to say, the implementors liked this solution (invented by
Radia Perlman) much better than the original approach.

Exercises

• How can a router assign endnodes to pseudorouters? What happens if a router initially has a lot of
  endnodes (and hence a lot of pseudorouters) and then most of the endnodes die? This can leave a lot
  of pseudorouters, each of which has only a few endnodes. Why is this bad, and how can it be fixed?
• As in the relaxed-consistency examples described in Chapter 3, this solution can lead to some un-
  expected (but not very serious) temporary inconsistencies. Assuming a solution to the previous
  exercise, describe a scenario in which a given router, say, R2, can find (at some instant) that its
  LSP database shows the same endnode (say, E1) belonging to two pseudorouters, R1a and R1c .
  Why is this no worse than ordinary LSP routing?
