# network-algorithmics-11-2-1-threaded-indices-and-tag-switching (chunk 000002)

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
