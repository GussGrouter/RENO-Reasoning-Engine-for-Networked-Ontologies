# Network Algorithmics — 8.3 CMU/Stanford packet filter: pioneering packet filters (slice)

- Source: raw/code/pdf/Network.Algorithmics.pdf
- Full-text extraction: processed/code/network-algorithmics-full-layout.txt
- Slice start: PDF page 225
- Slice: from `8.3 CMU/Stanford packet filter: pioneering packet filters` up to next detected section heading

---

8.3 CMU/Stanford packet filter: pioneering packet filters
The CMU/CSPF (Mogul et al., 1987) was developed to allow user-level protocol implementations in
the Mach operating system. In the CSPF model application programs provide the kernel with a program
describing the packets they wish to receive. The program supplied by A operates on a packet header and
returns true if the packet should be routed to application A. Like the old Texas Instrument calculators,
the programming language is a stack-based implementation of an expression tree model.
    As shown in Fig. 8.2, the leaves of the tree represent simple test predicates on packet headers.
An example of a test predicate is equality comparison with a fixed value; for example, in Fig. 8.2,
ETHER.TYPE = ARP represents a check of whether the Ethernet type field in the received packet

                   8.4 Berkeley packet filter: enabling high-performance monitoring                            199




FIGURE 8.2
The CMU/CSPF allows applications to provide programs that specify an expression tree representing the packets
they wish to receive. The tree shown here effectively asks for all IP and ARP packets sent by IP source address X.



matches the constant value specified for ARP (address resolution protocol) packets. The other nodes in
the tree represent boolean operations such as AND and OR.
    Thus the left subtree of the expression tree in Fig. 8.2 represents any ARP packet sent from source
IP address X, while the right subtree represents any IP packet sent from source IP address X. Since
the root represents an OR operation, the overall tree asks for all IP or ARP packets sent by a source X.
Such an expression could be provided by a debugging tool to the kernel on behalf of a user who wished
to examine IP traffic coming from source X.
    While the expression tree model provides a declarative model of a filter, such filters actually use an
imperative stack-based language to describe expression trees. To provide safety, CSPF provides stack
instructions of limited power; to bound running times, there are no jumps or looping constructs. Safety
is also achieved by checking program loads and stores in real time to eliminate wild memory refer-
ences. Thus stack references are monitored to ensure compliance with the stack range, and references
to packets are vetted to ensure they stay within the length of the packet being demultiplexed.
