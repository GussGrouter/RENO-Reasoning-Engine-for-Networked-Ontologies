# network-algorithmics-18-5-the-inner-life-of-a-networking-device (chunk 000004)

A.1.2 Routing protocols
Fig. A.2 shows a more detailed view of a plausible network topology between Web client S and Web
server D of Fig. A.1. The source is attached to a local area network such as an Ethernet, to which is
also connected a router, R1. Routers are the automated post offices of the Internet, which consult the
destination address in an Internet message (often called a packet) to decide on which output link to
forward the message.
    In the figure source S belongs to an administrative unit (say, a small company) called a domain. In
this simple example, the domain of S consists only of an Ethernet and a router, R1, that connects to an
Internet service provider (ISP) through router R2. Our Internet service provider is also a small outfit,
and it consists only of three routers, R2, R3, and R4, connected by fiber-optic communication links.
Finally, R4 is connected to router R5 in D’s domain, which leads to the destination, D.
    Internet routing is broken into two conceptual parts, called forwarding and routing. First consider
forwarding, which explains how packets move from S to D through intermediate routers.
    When S sends a TCP packet to D, it first places the IP address of D in the routing header of the
packet and sends it to the neighboring router, R1. Forwarding at endnodes such as S and D is kept
simple and consists of sending the packet to an adjoining router. R1 realizes it has no information
about D and so passes it to ISP router R2. When it gets to R2, R2 must choose to send the packet to
either R3 or R4. R2 makes its choice based on a forwarding table at R2 that specifies (say) that packets
to D should be sent to R4. Similarly, R4 will have a forwarding entry for traffic to D that points to R5.
A description of how forwarding entries are compressed using prefixes can be found in Section 2.3.2. In
summary, an Internet packet is forwarded to a destination by following forwarding information about
the destination at each router. Each router need not know the complete path to D, but only the next hop
to get to D.
    While forwarding must be done at extremely high speeds, the forwarding tables at each router must
be built by a routing protocol. For example, if the link from R2 to R4 fails, the routing protocol within
the ISP domain should change the forwarding table at R2 to forward packets to D to R3. Typically,
each domain uses its own routing protocol to calculate shortest-path routes within the domain. Two
main approaches to routing within a domain are distance vector and link state.
    In the distance vector approach exemplified by the protocol RIP (Perlman, 1992), the neighbors of
each router periodically exchange distance estimates for each destination network. Thus in Fig. A.2
R2 may get a distance estimate of 2 to D’s network from R3 and a distance estimate of 1 from R4.
Thus R2 picks the shorter-distance neighbor, R4, to reach D. If the link from R2 to R4 fails, R2 will

Detailed models        533
