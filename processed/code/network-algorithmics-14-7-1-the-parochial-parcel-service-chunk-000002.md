# network-algorithmics-14-7-1-the-parochial-parcel-service (chunk 000002)

14.7.2 Deficit round-robin
What was all this stuff about a parcel service about? Clearly, parcels correspond to packets, the par-
cel office to a router, and loading docks to outbound links. More importantly, the seemingly facetious
slice-by-slice round-robin corresponds to a seminal idea, called bit-by-bit round-robin or the DKS (De-
mers, Keshav, and Shenker) scheme (Demers et al., 1989). Simulated bit-by-bit round-robin provides
provably fair bandwidth distribution and some remarkably tight delay bounds; unfortunately, it is hard
to implement at gigabit speeds. A considerable improvement to bit-by-bit round-robin is proposed in
the paper by Stiliadis and Varma (1996b), which shows how to reduce the linear overhead of the DKS
scheme to the purely logarithmic overhead of sorting. Sorting can be done at high speeds with hardware
multiway heaps; however, it is still more complex than deficit round-robin for bandwidth guarantees.

396       Chapter 14 Scheduling packets

FIGURE 14.10
Brown’s entry causes the time stamp of Jones and Smith to change. In general, when a new flow becomes active, the
overhead is linear in the number of flows.
