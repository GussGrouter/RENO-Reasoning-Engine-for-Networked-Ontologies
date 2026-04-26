# network-algorithmics-10-1-challenge-1-ethernet-under-fire (chunk 000003)

transmission opportunity to send it on the upper Ethernet. This avoids the physical coupling between
the collision-resolution processes on the two Ethernets that would be caused by using a bit repeater.
Thus the distance span increases to 3 km, but the effective bandwidth is still that of one Ethernet
because every frame is sent on both Ethernets.
   Filtering Repeater: The frame repeater idea in Fig. 10.1 causes needless waste (P1) when A sends
a packet to B by sending the packet unnecessarily on the upper Ethernet. This waste can be avoided
if the bridge has a table that maps station addresses to Ethernets. For example, suppose the bridge in
Fig. 10.1 has a table that maps A and B to the lower Ethernet and C to the upper Ethernet. Then on
receipt of a packet from A to B on the lower Ethernet, the bridge need not forward the frame because
the table indicates that destination B is on the same Ethernet the packet was received on. If, say, a
fraction p of traffic on each Ethernet is to destinations on the same Ethernet (locality assumption), then
the overall bandwidth of the two Ethernet systems becomes (1 + p) times the bandwidth of a single
Ethernet. This follows because the fraction p can be simultaneously sent on both Ethernets, increasing
overall bandwidth by this fraction. Hence both bandwidth and distance increase. The only difficulty is
figuring out how the mapping table is built.
   Filtering Repeater With Learning: It is infeasible to have a manager build a mapping table for
a large bridged network. Can the table be built automatically? One aspect of Principle P13 (exploit
degrees of freedom) is Polya’s (Polya, 1957) problem-solving question: “Have you used all the data?”
So far, the bridge has looked only at destination addresses to forward the data. Why not also look at
source addresses? When receiving a frame from A to B, the bridge can look at the source address field
to realize that A is on the lower Ethernet. Over time, the bridge will learn the ports through which all
active stations can be reached.
   Perhaps Mark rushed out after his insight, shouting “Eureka!” But he still had to work out a few more
issues. First, because the table is initially empty, bridges must forward a packet, perhaps unnecessarily,
when the location of the destination has not been learned. Second, to handle station movement, table
entries must be timed out if the source address is not seen for some time period T . Third, the entire idea
generalizes to more than two Ethernets connected together without cycles, to bridges with more than
two Ethernet attachments, and to links other than Ethernets that carry destination and source addresses.
But there was a far more serious challenge that needed to be resolved.
