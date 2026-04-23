# network-algorithmics-11-2-1-threaded-indices-and-tag-switching (chunk 000001)

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
