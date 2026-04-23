# Network Algorithmics — 12.2 Packet-classification problem (slice)

- Source: raw/code/pdf/Network.Algorithmics.pdf
- Full-text extraction: processed/code/network-algorithmics-full-layout.txt
- Slice start: PDF page 325
- Slice: from `12.2 Packet-classification problem` up to next detected section heading

---

12.2 Packet-classification problem
Traditionally, the rules for classifying a message are called rules and the packet-classification problem
is to determine the lowest-cost matching rule for each incoming message at a router.
    Assume that the information relevant to a lookup is contained in K distinct header fields in each
message. These header fields are denoted H [1], H [2], . . . , H [K], where each field is a string of bits.

                                                                  12.2 Packet-classification problem                        299



For instance, the relevant fields for an IPv4 packet could be the destination address (32 bits), the source
address (32 bits), the protocol field (8 bits), the destination port (16 bits), the source port (16 bits),
and TCP flags (8 bits). The number of relevant TCP flags is limited, and so the protocol and TCP
flags are combined into one field—for example, TCP-ACK can be used to mean a TCP packet with the
ACK bit set.1 Other relevant TCP flags can be represented similarly; UDP packets are represented by
H [3] = U DP .
    Thus, the combination (D, S, TCP-ACK, 63, 125) denotes the header of an IP packet with destina-
tion D, source S, protocol TCP, destination port 63, source port 125, and the ACK bit set.
    The classifier, or rule database, router consists of a finite set of rules, R1 , R2 , . . . , RN . Each rule
is a combination of K values, one for each header field. Each field in a rule is allowed three kinds of
matches: exact match, prefix match, and range match. In an exact match, the header field of the packet
should exactly match the rule field—for instance, this is useful for protocol and flag fields. In a prefix
match, the rule field should be a prefix of the header field—this could be useful for blocking access
from a certain subnetwork. In a range match, the header values should lie in the range specified by the
rule—this can be useful for specifying port number ranges.
    Each rule Ri has an associated directive dispi , which specifies how to forward the packet matching
this rule. The directive specifies if the packet should be blocked. If the packet is to be forwarded, the
directive specifies the outgoing link to which the packet is sent and, perhaps, also a queue within that
link if the message belongs to a flow with bandwidth guarantees.
    A packet P is said to match a rule R if each field of P matches the corresponding field of
R—the match type is implicit in the specification of the field. For instance, if the destination field
is specified as 1010∗, then it requires a prefix match; if the protocol field is UDP, then it requires
an exact match; if the port field is a range, such as 1024–1100, then it requires a range match. For
instance, let R = (1010∗, ∗, T CP , 1024–1080, ∗) be a rule, with disp = block. Then, a packet with
header (10101 . . . 111, 11110 . . . 000, TCP, 1050, 3) matches R and is therefore blocked. The packet
(10110 . . . 000, 11110 . . . 000, TCP, 80, 3), on the other hand, doesn’t match R.
    Since a packet may match multiple rules in the database, each rule R in the database is associated
with a nonnegative number, cost(R). Ambiguity is avoided by returning the least-cost rule matching
the packet’s header. The cost function generalizes the implicit precedence rules that are used in practice
to choose between multiple matching rules. In firewall applications or Cisco ACLs, for instance, rules
are placed in the database in a specific linear order, where each rule takes precedence over a subsequent
rule. Thus, the goal there is to find the first matching rule. Of course, the same effect can be achieved
by making cost(R) equal to the position of rule R in the database.
    As an example of a rule database, consider the topology and firewall database (Cheswick and
Bellovin, 1995) shown in Fig. 12.2, where a screened subnet configuration interposes between a com-
pany subnetwork (shown on top left) and the rest of the Internet (including hackers). There is a so-called
bastion host M within the company that mediates all access to and from the external world. M serves
as the mail gateway and also provides external name server access. TI, TO are network time protocol
(NTP) sources, where TI is internal to the company and TO is external. S is the address of the secondary
name server, which is external to the company.


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
