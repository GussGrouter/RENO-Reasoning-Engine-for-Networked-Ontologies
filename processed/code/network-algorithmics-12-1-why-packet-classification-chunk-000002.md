# network-algorithmics-12-1-why-packet-classification (chunk 000002)

Unfortunately, the Internet is becoming more complex because of its use for mission-critical func-
tions executed by organizations. Organizations desire that their critical activities not be subverted either
by high traffic sent by other organizations (they require QoS guarantees) or by malicious intruders (they
require security guarantees). Both QoS and security guarantees require a finer discrimination of packets,
based on fields other than the destination. This is called packet classification. To quote John McQuillan
(1997):
   Routing has traditionally been based solely on destination host numbers. In the future it will also be
   based on source host or even source users, as well as destination URLs (universal resource locators)
   and specific business policies. . . . Thus, in the future, you may be sent on one path when you casually
   browse the Web for CNN headlines. And you may be routed an entirely different way when you go to
   your corporate Web site to enter monthly sales figures, even though the two sites might be hosted by
   the same facility at the same location. . .. An order entry form may get very low latency, while other
   sections get normal service. And then there are Web sites comprised of different servers in different
   locations. Future routers and switches will have to use class of service and QoS to determine the
   paths to particular Web pages for particular end users. All this requires the use of layers 4, 5, and
   above.
    This (now standard) vision of forwarding is called packet classification. It is also sometimes called
layer 4 switching, because routing decisions can be based on headers available at layer 4 or higher
in the OSI architecture. Examples of other fields a router may need to examine include source ad-
dresses (to forbid or provide different service to some source networks), port fields (to discriminate
between traffic types, such as Napster and E-mail), and even TCP flags (to distinguish between ex-
ternally and internally initiated connections). Besides security and QoS, other functions that require
classification include network address translation (NAT), metering, traffic shaping, policing, and mon-
itoring.
    Several variants of packet classification have already established themselves on the Internet. First,
many routers implement firewalls (Cheswick and Bellovin, 1995) at trust boundaries, such as the entry
and exit points of a corporate network. A firewall database consists of a series of packet rules that
implement security policies. A typical policy may be to allow remote login from within the corporation
but to disallow it from outside the corporation.
    Second, the need for predictable and guaranteed service has led to proposals for reservation proto-
cols, such as DiffServ (Blake et al., 1998), that reserve bandwidth between a source and a destination.
Third, the cries for routing based on traffic type have become more strident recently—for instance, the
need to route Web traffic between Site 1 and Site 2 on, say, Route A and other traffic on, say, Route B.
Fig. 12.1 illustrates some of these examples.
    Classifiers historically evolved from firewalls, which were placed at the edges of networks to filter
out unwanted packets. Such databases are generally small, containing 10–500 rules, and can be handled
by ad hoc methods. However, with the DiffServ movement, there is potential for classifiers that could
support 100,000 rules for DiffServ and policing applications at edge routers.
    While large classifiers are anticipated for edge routers to enforce QoS via DiffServ, it is perhaps
surprising that even within the core, fairly large (e.g., 2000-rule) classifiers are commonly used for
security. While these core router classifiers are nowhere near the anticipated size of edge router clas-
sifiers, there seems no reason why they should not continue to grow beyond the sizes reported in this
book. For example, many of the rules appear to be denying traffic from a specified subnetwork outside

298       Chapter 12 Packet classification
