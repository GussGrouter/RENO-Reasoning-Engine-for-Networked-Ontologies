# network-algorithmics-12-2-packet-classification-problem (chunk 000003)

1 TCP flags are important for packet classification because the first packet in a connection does not have the ACK bit set, while
the others do. This allows a simple rule to block TCP connections initiated from the outside while allowing responses to internally
initiated connections.

300       Chapter 12 Packet classification

FIGURE 12.2
The top half of the figure shows the topology of a small company; the bottom half shows a sample firewall database
for this company as described in the book by Cheswick and Bellovin (1995). The block flags are not shown in the
figure; the first seven rules have block = f alse (i.e., allow) and the last rule has block = true (i.e., block). We as-
sume that all the addresses within the company subnetwork (shown on top left) start with the prefix Net, including
M and T I .

Clearly, the site manager wishes to allow communication from within the network to TO and S and
yet wishes to block hackers. The database of rules shown at the bottom of Fig. 12.2 implements this
intention. Terse explanations of each rule are shown on the right of each rule. Assume that all addresses
of machines within the company’s network start with the CIDR prefix N et. Thus M and TI both match
the prefix N et. All packets matching any of the first seven rules are allowed; the remaining (last rule)
are dropped by the screening router. A more general firewall could arbitrarily interleave rules that allow
packets with rules that drop packets.
    As an example, consider a packet sent to M from S with UDP destination port equal to 53. This
packet matches Rules 2, 3, and 8 but must be allowed through because the first matching rule is Rule 2.
    Note that this description uses N for the number of rules and K for the number of packet fields.
K is sometimes called the number of dimensions, for reasons that will become clearer in Section 12.6.

12.4 Simple solutions          301
