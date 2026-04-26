# network-algorithmics-2-3-2-router-architecture (chunk 000002)

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
