# Network Algorithmics — 11.2.1 Threaded indices and tag switching (slice)

- Source: raw/code/pdf/Network.Algorithmics.pdf
- Full-text extraction: processed/code/network-algorithmics-full-layout.txt
- Slice start: PDF page 282
- Slice: from `11.2.1 Threaded indices and tag switching` up to next detected section heading

---

11.2.1 Threaded indices and tag switching
In threaded indices (Chandranmenon and Varghese, 1996), each router passes an index into the next
router’s forwarding table, thereby avoiding prefix lookups. The indexes are precomputed by the routing
protocol whenever the topology changes. Thus in Fig. 11.1 source S sends a packet to destination D
to the first router A as usual; however, the packet header also contains an index i into A’s forwarding
table. A’s entry for D says that the next hop is router B and that B stores its forwarding entry for D
at index j . Thus A sends the packet on to B, but first it writes j (Fig. 11.1) as the packet index. This
process is repeated, with each router in the path using the index in the packet to look up its forwarding
table.
     The two main differences between threaded indices and VCIs are as follows. First, threaded indexes
are per destination and not per active source–destination pair as in virtual circuit networks such as
ATM. Second, and more importantly, threaded indexes are precomputed by the routing protocol when-
ever the topology changes. As a simple example, consider Fig. 11.2, which shows a sample router
topology where the routers run the Bellman–Ford protocol to find their distances to destinations.
     In Bellman–Ford (used, for example, in the intradomain protocol Routing Information Protocol
[RIP] (Perlman, 1992)), a router R calculates its shortest path to D by taking the minimum of the cost
to D through each neighbor. The cost through a neighbor such as A is A’s cost to D (i.e., 5) plus the
cost from R to A (i.e., 3). In Fig. 11.2 the best-cost path from R to D is through router B, with cost 7.
R can compute this because each neighbor of R (e.g., A, B) passes its current cost to D to R, as shown
in the figure. To compute indices as well, we modify the basic protocol so that each neighbor reports
its index for a destination in addition to its cost to the destination. Thus in Fig. 11.2 A passes i and B
passes j ; thus when R chooses B, it also uses B’s index j in its routing table entry for D. In summary,
each router uses the index of the minimal-cost neighbor for each destination as the threaded index for
that destination.

256       Chapter 11 Prefix-match lookups




FIGURE 11.2
Setting up the threaded indexes or tags by modifying Bellman–Ford routing.


    Cisco later introduced tag switching (Meiners et al., 2008), which is similar in concept to threaded
indices, except tag switching also allows a router to pass a stack of tags (indices) for multiple routers
downstream. Both schemes, however, do not deal well with hierarchies. Consider a packet that arrives
from the backbone to the first router in the exit domain. The exit domain is the last autonomously
managed network the packet traverses—say, the enterprise network in which the destination of the
packet resides.
    The only way to avoid a lookup at the first router, R, in the exit domain is to have some earlier router
outside the exit domain pass an index (for the destination subnet) to R. But this is impossible because
the prior backbone routers should have only one aggregated routing entry for the entire destination
domain and can thus pass only one index for all subnets in that domain. The only solution is either to
add extra entries to routers outside a domain (infeasible) or to require ordinary IP lookup at domain
entry points (the chosen solution). Today tag switching is flourishing in a more general form called
multiprotocol label switching (MPLS) (Meiners et al., 2008). However, neither tag switching nor MPLS
completely avoids the need for ordinary IP lookups.


11.2.2 Flow switching
A second proposal to finesse lookups was called flow switching (Newman et al., 1997; Parulkar et al.,
1995). Flow switching also relies on a previous hop router to pass an index into the next hop router.
Unlike tag switching, however, these indexes are computed on demand when data arrives, and they are
then cached.
   Flow switching starts with routers that contain an internal ATM switch and (potentially slow) pro-
cessors capable of doing IP forwarding and routing. Two such routers R1 and R2 are shown in Fig. 11.3.
When R2 first sends an IP packet to destination D that arrives on the left input port of R1, the input
port sends the packet to its central processor. This is the slow path. The processor does the IP lookup
and switches the packet internally to output link L. So far nothing is out of the ordinary.

                                                                            11.2 Finessing lookups                257




FIGURE 11.3
In IP switching, if R1 wishes to switch packets sent to D that are destined for output link L, R1 picks an idle vir-
tual circuit I , places the mapping I, L in its input port, and then sends I back to R2. If R2 now sends packets to D
labeled with VCI I , the packet will get switched directly to the output link without going through the processor.


     Life gets more exciting if R1 decides to “switch” packets going to D. R1 may decide to do so if, for
instance, there is a lot of traffic going to D. In that case R1 first picks an idle virtual circuit identifier
I , places the mapping I → L in its input port hardware, and then sends I back to R2. If R2 now sends
packets to D labeled with VCI I to the input port of R1, the input port looks up the mapping from I to
L and switches the packet directly to the output link L without going through the processor.
     Of course, R2 can repeat this switching process with the preceding router in the path, and so on.
Eventually, IP forwarding can be completely dispensed with in the switched portion of a sequence of
flow-switching routers.
     Despite its elegance, flow switching seems likely to work poorly in the backbone. This is because
backbone flows are short lived and exhibit poor locality. A contrarian opinion is presented in Molinero-
Fernandez and McKeown (2002) where the authors argue for the resurrection of flow switching based
on TCP connections. They claim that the current use of circuit-switched optical switches to link core
routers, the underutilization of backbone links running at 10% of capacity, and increasing optical band-
widths all favor the simplicity of circuit switching at higher speeds.
     Both IP and tag switching are techniques to finesse the need for IP lookups by passing information
in protocol headers. Like ATM, both schemes rely on passing indices (P10). However, tag switching
precomputes the index (P2a) at an earlier time scale (topology change time) than ATM (just before data
transfer). On the other hand, in IP switching the indices are computed on demand (P2c, lazy evaluation)
after the data begins to flow. However, neither tag nor IP switching completely avoids prefix lookups,
and each adds a complex protocol. We now look afresh at the supposed complexity of IP lookups.
