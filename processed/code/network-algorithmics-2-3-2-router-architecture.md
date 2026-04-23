# Network Algorithmics — router architecture (2.3.2) (slice)

- Source: raw/code/pdf/Network.Algorithmics.pdf
- Extraction: pdftotext -f 62 -l 71 -layout
- Slice: from `2.3.2 Router architecture` up to (excluding) `2.4 Operating systems`

---

2.3.2 Router architecture
A router model that covers both high-end routers (such as Juniper’s M-series routers) and low-end
routers (such as the Cisco Catalyst) is shown in Fig. 2.10. Basically, a router is a box with a set of input
links, shown on the left, and a set of output links, shown on the right; the task of the router is to switch
a packet from an input link to the appropriate output link based on the destination address in the packet.
While the input and output links are shown separately, the two links in each direction between two
routers are often packaged together. We review three main bottlenecks in a router: lookup, switching,
and output queuing.

---

## PDF page 63

36        Chapter 2 Network implementation models




FIGURE 2.10
A model of a router labeled with the three main bottlenecks in the forwarding path: address lookup (B1), switching
(B2), and output scheduling (B3).


Lookup
A packet arrives on, say, the left link, input link i. Every packet carries a 32-bit Internet Protocol (IP)
address.10 Assume that the first six bits of the destination address of a sample packet are 100100. A
processor in the router inspects the destination address to determine where to forward the packet.
    The processor consults a forwarding table to determine the output link for the packet. The forward-
ing table is sometimes called a FIB, for forwarding information base. The FIB contains a set of prefixes
with corresponding output links. The reason for prefixes will be explained in Chapter 11; for now, think
of prefixes as variable-length “area codes” that greatly reduce the FIB size. A prefix like 01*, where the
* denotes the usual “don’t care” symbol, matches IP addresses that start with 01. Assume that prefix
100* has associated output link 6, while prefix 1* has output link 2. Thus our sample packet, whose
destination address starts with 100100, matches both prefixes 100* and 1*. The disambiguating rule
that IP routers use is to match an address to the longest matching prefix. Assuming no longer matching
prefixes, our sample packet should be forwarded to output link 6.
    The processor that does the lookup and basic packet processing can be either shared or dedicated
and can be either a general processor or a special-purpose chip. Early router designs used a shared
processor (or processors), but this proved to be a bottleneck. Later designs, including Cisco’s GSR
family, use a dedicated processor per input link interface. The earliest designs used a standard CPU
processor, but many of the fastest routers today, such as Juniper’s M-160, use a dedicated chip (ASIC)
with some degree of programmability. There has been a backlash to this trend toward ASICs, however,
with customers asking routers to perform new functions, such as Web load balancing. Thus some new
routers use network processors (see Example 7), which are general-purpose processors optimized for
networking.


10 Recall that while most users deal with domain names, these names are translated to an IP address by a directory service,
called DNS, before packets are sent.

---

## PDF page 64

                                                                     2.3 Network device architectures                         37



    Algorithms for prefix lookups are described in Chapter 11. Many routers today also offer a more
complex lookup called packet classification (Chapter 12), where the lookup takes as input the destina-
tion address as well as source address and TCP ports.

Switching
After address lookup in the example of Fig. 2.10, the processor instructs an internal switching system
to transfer the packet from link i to output link 6. In older processors, the switch was a simple bus,
such as shown in Fig. 2.8. This proved to be a major bottleneck because, if the switch has N input links
running at B bits per second, the bus would have to have a bandwidth of B · N . Unfortunately, as N
increases, electrical effects (such as the capacitive load of a bus) predominate, limiting the bus speed.
    Thus the fastest routers today internally use a parallel switch of the sort shown in Fig. 2.9. The
throughput of the switch is increased by using N parallel buses, one for each input and one for each
output. An input and an output are connected by turning on transistors connecting the corresponding
input bus and output bus. While it is easy to build the data path, it is harder to schedule the switch, be-
cause multiple inputs may wish to send to the same output link at the same time. The switch-scheduling
problem boils down to matching available inputs and outputs every packet arrival time. Algorithms for
this purpose are described in Chapter 13.

Queuing
Once the packet in Fig. 2.10 has been looked up and switched to output link 6, output link 6 may be
congested, and thus the packet may have to be placed in a queue for output link 6. Many older routers
simply place the packet in a first-in-first-out (FIFO) transmission queue. However, some routers employ
more sophisticated output scheduling to provide fair bandwidth allocation and delay guarantees. Output
scheduling is described in Chapter 14.
    Besides the major tasks of lookups, switching, and queuing, there are a number of other tasks that
are less time-critical.

Header validation and checksums
The version number of a packet is checked, and the header-length field is checked for options. Options
are additional processing directives that are rarely used; such packets are often shunted to a separate
route processor. The header also has a simple checksum that must be verified. Finally, a time-to-live
(TTL) field must be decremented and the header checksum recalculated. Chapter 9 shows how to
incrementally update the checksum. Header validation and checksum computation are often done in
hardware.

Route processing
Section A.1.2 describes briefly how routers build forwarding tables using routing protocols. Routers
within domains implement RIP and OSPF, while routers that link domains also must implement BGP.11


11 It is possible to buy versions of these protocols, but the software must be customized for each new hardware platform. A more
insidious problem, especially with BGP and OSPF, is that many of the first implementations of these protocols vary in subtle
ways from the actual specifications. Thus a new implementation that meets the specification may not interoperate with existing
routers. Thus ISPs are reluctant to buy new routers unless they can trust the “quality” of the BGP code, in terms of its ability to
interoperate with existing routers.

---

## PDF page 65

38         Chapter 2 Network implementation models



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
