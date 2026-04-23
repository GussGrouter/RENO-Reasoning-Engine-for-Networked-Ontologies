# Network Algorithmics — 10.1 Challenge 1: Ethernet under fire (slice)

- Source: raw/code/pdf/Network.Algorithmics.pdf
- Full-text extraction: processed/code/network-algorithmics-full-layout.txt
- Slice start: PDF page 263
- Slice: from `10.1 Challenge 1: Ethernet under fire` up to next detected section heading

---

10.1 Challenge 1: Ethernet under fire
The first challenge arose in the late 1980s. Ethernet, invented in the 1970s as a low-cost, high-bandwidth
interconnect for personal computers, was attacked as behaving poorly at large loads and being incapable
of spanning large distances. Recall that if two or more nodes on an Ethernet send data at the same time,
a collision occurs on the shared wire. All senders then compute a random retransmission time and retry,
where the randomization is chosen to minimize the probability of further collisions.
    Theoretical analyses (e.g., Bux and Grillo, 1985) claimed that as the utilization of an Ethernet grew,
the effective throughput of the Ethernet dropped to zero because the entire bandwidth was wasted on
retransmissions. A second charge against Ethernet was its small distance limit of 1.5 km, much smaller
than the limits imposed by, say, the IBM token ring.
    While the limited-bandwidth charge turned out to be false in practice (Boggs et al., 1988), it re-
mained a potent marketing bullet for a long time. The limited-distance charge was, and remains, a true
limitation of a single Ethernet. In this embattled position network marketing people at Digital Equip-
ment Corporation (DEC) around 1980 pleaded with their technical experts for a technical riposte to

                                                              10.1 Challenge 1: Ethernet under fire   237




FIGURE 10.1
Toward designing a bridge connecting two Ethernets.


these attacks. Could not their bright engineers find a clever way to “extend” a single Ethernet such that
it could become a longer Ethernet with a larger effective bandwidth?
    First, it was necessary to discard some unworkable alternatives. Physical layer bit repeaters were un-
workable because they did not avoid the distance and bandwidth limits of ordinary Ethernets. Extending
an Ethernet using a router did, in theory, solve both problems but introduced two other problems. First,
in those days routers were extremely slow and could hardly keep up with the speed of the Ethernet.
    Second, there were at least six different routing protocols in use at that time, including IBM’s SNA,
Xerox’s SNS, DECNET, and AppleTalk. Hard as it may be to believe now, the Internet protocols were
then only a small player in the marketplace. Thus a router would have to be a complex beast capable
of routing multiple protocols (as Cisco would do a few years later), or one would have to incur the
extra cost of placing multiple routers, one for each protocol. Thus the router solution was considered a
nonstarter.
    Routers interconnect links using information in the routing header, while repeaters interconnect
links based on physical-layer information, such as bits. However, in classical network layering there is
an intermediate layer called the data link layer. For an Ethernet, the data link layer is quite simple and
contains a 48-bit unique Ethernet destination address.2 Why is it not possible, the DEC group argued,
to consider a new form of interconnection based only on the data link layer? They christened this new
beast a data link layer relay, or a bridge.
    Let us take an imaginary journey into the mind of Mark Kempf, an engineer in the Advanced
Development Group at DEC, who invented bridges in Tewksbury, MA, around 1980. Undoubtedly, he
drew something like Fig. 10.1, which shows two Ethernets connected by a bridge; the lower Ethernet
line contains stations A and B, while the upper Ethernet contains station C.
    The bridge should make the two Ethernets look like one big Ethernet so that when A sends an
Ethernet packet to C it magically gets to C without A’s having to even know there is a bridge in the
middle. Perhaps Mark reasoned as follows in his path to a final solution.
 Packet Repeater: Suppose A sends a packet to C (on the lower Ethernet) with destination address
C and source address A. Assume the bridge picks up the entire packet, buffers it, and waits for a


2 Note that Ethernet 48-bit addresses have no relation to 32-bit Internet addresses.

238      Chapter 10 Exact-match lookups



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
