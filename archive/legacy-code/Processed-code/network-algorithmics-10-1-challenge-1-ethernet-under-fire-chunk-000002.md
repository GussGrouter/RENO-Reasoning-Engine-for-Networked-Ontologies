# network-algorithmics-10-1-challenge-1-ethernet-under-fire (chunk 000002)

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
