# network-algorithmics-2-3-2-router-architecture (chunk 000003)

These protocols are implemented in one or more route processors. For example, when a LSP is sent
to the router in Fig. 2.10, lookup will recognize that this is a packet destined for the router itself and
will cause the packet to be switched to the route processor. The route processor maintains the link-state
database and computes shortest paths; after computation, the route processor loads the new forwarding
databases in each of the forwarding processors through either the switch or a separate out-of-band path.
    In the early days, Cisco won its spurs by processing not just Internet packets but also other routing
protocols, such as DECNET, SNA, and AppleTalk. The need for such multiprotocol processing is less
clear now. A much more important trend is multi-protocol-label switching (MPLS), which appears to
be de rigeur for core routers. In MPLS, the IP header is augmented with a header containing simple
integer indices that can be looked up directly without a prefix lookup; Chapter 11 provides more details
about MPLS.

Protocol processing
All routers today have to implement the simple network management protocol (SNMP) and provide a
set of counters that can be inspected remotely. To allow remote communication with the router, most
routers also implement TCP and UDP. In addition, routers have to implement the Internet control mes-
sage protocol (ICMP), which is basically a protocol for sending error messages, such as “time-to-live
exceeded.”

Fragmentation, redirects, and ARPs
While it is clear that route and protocol processing is best relegated to a route processor on a so-called
“slow path,” there are a few router functions that are more ambiguous. For example, if a packet of 3000
bytes is to be sent over a link with a maximum packet size (MTU) of 1500 bytes, the packet has to
be fragmented into two pieces.12 While the prevailing trend is for sources, instead of routers, to do
fragmentation, some routers do fragmentation in the fast path. Another such function is the sending of
Redirects. If an endnode sends a message to the wrong router, the router is supposed to send a Redirect
back to the endnode. A third such function is the sending of address resolution protocol (ARP) requests,
whose operation is explored in the exercises.
    Finally, routers today have a number of other tasks they may be called on to perform. Many routers
within enterprises do content-based handling of packets, where the packet processing depends on
strings found in the packet data. For example, a router that fronts a Web farm of many servers may
wish to forward packets with the same Web URL to the same Web server. There are also the issues of
accounting and traffic measurement. Some of these new services are described in Chapter 16.
Example 7. Network Processors: Network processors are general-purpose programmable processors
optimized for network traffic. Their proponents say that they are needed because the unpredictable
nature of router tasks (such as content-based delivery) makes committing router forwarding to silicon a
risky proposition. For example, the Intel IXP1200 network processor evaluated in Spalink et al. (2000)
internally contains six processors, each running at 177 MHz with a 5.6-nsec clock cycle. Each processor
receives packets from an input queue; packets are stored in a large DRAM; after the processor has
looked up the packet destination, the packet is placed on the output queue with a tag describing the
output link it should be forwarded to.

12 Strictly speaking, since each fragment adds headers, there will be three pieces.

---

## PDF page 66
