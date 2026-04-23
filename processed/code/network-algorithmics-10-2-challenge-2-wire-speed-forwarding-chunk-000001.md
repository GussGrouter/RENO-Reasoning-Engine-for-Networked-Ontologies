# network-algorithmics-10-2-challenge-2-wire-speed-forwarding (chunk 000001)

# Network Algorithmics — 10.2 Challenge 2: wire speed forwarding (slice)

- Source: raw/code/pdf/Network.Algorithmics.pdf
- Full-text extraction: processed/code/network-algorithmics-full-layout.txt
- Slice start: PDF page 265
- Slice: from `10.2 Challenge 2: wire speed forwarding` up to next detected section heading

---

10.2 Challenge 2: wire speed forwarding
When the idea was first proposed, some doubting Thomas at DEC noticed a potential flaw. Suppose in
Fig. 10.1 that A sends 1000 packets to B and that A then follows this burst by sending, say, 10 packets
to C. The bridge receives the 1000 packets, buffers them, and begins to work on forwarding (actually
discarding) them. Suppose the time that the bridge takes to look up its forwarding table is twice as long
as the time it takes to receive a packet. Then after a burst of 1000 back-to-back packets arrive, a queue
of 500 packets from A to B will remain as a backlog of packets that the bridge has not even examined.
    Since the bridge has a finite amount of buffer storage for, say, 500 packets, when the burst from A
to C arrives they may be dropped without examination because the bridge has no more buffer storage.
This is ironic because the packets from A to B that are in the buffer will be dropped after examination,
but the bridge has dropped packets from A to C that need to be forwarded. One can change the numbers
used in this example but the bottom line is unchanged: If the bridge takes more time to forward a packet

10.2 Challenge 2: wire speed forwarding                    239

FIGURE 10.2
Implementation of the first Ethernet-to-Ethernet bridge.

than the minimum packet arrival time, there are always scenarios in which packets to be forwarded will
be dropped because the buffers are filled with packets that will be discarded.
    The critics were quick to point out that routers did not have this problem3 because routers dealt only
with packets addressed to the router. Thus if a router were used, the router–Ethernet interface would
not even pick up packets destined for B, avoiding this scenario.
    To finesse this issue and avoid interminable arguments, Mark proposed an implementation that
would do wire speed forwarding between two Ethernets. In other words, the bridge would look up the
destination address in the table (for forwarding) and the source address (for learning) in the time it took
a minimum-size packet to arrive on an Ethernet. Given a 64-byte minimum packet, this left 51.2 mi-
crosecond to forward a packet. Since a two-port bridge could receive a minimum-size packet on each of
its Ethernets every 51.2 microsecond, this actually translated into doing two lookups (destination and
source) every 25.6 microsecond.
    It is hard to appreciate today, when wire speed forwarding has become commonplace, how aston-
ishing this goal was in the early 1980s. This is because in those days one would be fortunate to find an
interconnect device (e.g., router, gateway) that worked at kilobit rates, let alone at 10 Mbit/sec. Impossi-
ble, many thoughts. To prove them wrong, Mark built a prototype as part of the Advanced Development
Group in DEC. A schematic of his prototype, which became the basis for the first bridge, is shown in
Fig. 10.2.
    The design in Fig. 10.2 consists of a processor (the first bridge used a Motorola 68000), two Ethernet
chips (the first bridge used AMD Lance chips), a lookup chip (which is described in more detail later),
and a four-ported shared memory. The memory could be read and written by the processor, the Ethernet
chips, and the lookup engine.

3 Oddly enough, even routers have the same problem of distinguishing important packets from less important ones in times of
congestion, but this was not taken seriously in the 1980s.

240      Chapter 10 Exact-match lookups
