# Network Algorithmics — 9.4 Reassembly Both header prediction for TCP and even the UDP optimizations of Partridge and Pink (1993) assume (slice)

- Source: raw/code/pdf/Network.Algorithmics.pdf
- Full-text extraction: processed/code/network-algorithmics-full-layout.txt
- Slice start: PDF page 254
- Slice: from `9.4 Reassembly Both header prediction for TCP and even the UDP optimizations of Partridge and Pink (1993) assume` up to next detected section heading

---

9.4 Reassembly
Both header prediction for TCP and even the UDP optimizations of Partridge and Pink (1993) assume
that the received data stream has no unusual need for computation. For example, TCP segments are
assumed not to contain window size changes or to have flags set that need attention. Besides these, an
unstated assumption so far is that the IP packets do not need to be reassembled.
    Briefly, the original IP routing protocol dealt with diverse links with different maximum packet sizes
or maximum transmission units (MTUs) by allowing routers to slice up IP packets into fragments. Each
fragment is identified by a packet ID, a start byte offset into the original packet, and a fragment length.
The last fragment has a bit set to indicate it is the last. Note that an intermediate router can cause a
fragment to be itself fragmented into multiple smaller fragments. IP routing can also cause duplicates,
loss, and out-of-order receipt of fragments.
    At the receiver, Humpty Dumpty (i.e., the original packet) can be put together as follows. The first
fragment to arrive at the receiver sets up the state that is indexed by the corresponding packet ID. Sub-
sequent fragments are steered to the same piece of state (e.g., a linked list of fragments based on the
packet ID). The receiver can tell when the packet is complete if the last fragment has been received and
if the remaining fragments cover all the bytes in the original packets length, as indicated by each frag-
ment’s offset. If the packet is not reassembled after a specified time has elapsed, the state is timed out.
    While fragmentation allows IP to deal with links of different MTU sizes, it has the following dis-
advantages (Kent and Mogul, 1987). First, it is expensive for a router to fragment a packet because it
involves adding a new IP header for fragment, which increases the processing and memory bandwidth
needs. Second, reassembly at endnodes is considered expensive because determining when a complete
packet has been assembled potentially requires sorting the received fragments. Third, the loss of a frag-
ment leads to the loss of a packet; thus when a fragment is lost, transmission of the remaining fragments
is a waste of resources.

228        Chapter 9 Protocol processing




FIGURE 9.8
One data structure for reassembly is a linked list of fragments that is indexed by packet ID and sorted by the start
byte offset (first field). The second field is the end offset. Thus the fragment that starts at offset 25 is inserted after
the second list element.


     The current Internet strategy (Kent and Mogul, 1987) is to shift the fragmentation computation in
space (P3c) from the router and the receiver to the sender. The idea behind the so-called path MTU
scheme is that the onus falls on the sender to compute a packet size that is small enough to pass through
all links in the path from sender to receiver. Routers can now refuse to fragment a packet, sending back
a control message to the receiver. The sender uses a list of common packet sizes (P11, optimizing the
expected case) and works its way down this list when it receives a refusal.
     The path MTU scheme nicely illustrates algorithmics in action by removing a problem by moving
to another part of the system. However, a misconception has arisen that path MTU has completely
removed fragmentation in the Internet. This is not so. Almost all core routers support fragmentation in
hardware, and a significant amount of fragmented traffic has been observed (Shannon et al., 2001) on
Internet backbone links many years after the path MTU protocol was deployed.
     Note that the path MTU protocol requires the sender to keep state, typically in PCB, as to the best
current packet size to use. This works well if the sender uses TCP, but not if the sender uses UDP, which
is stateless. In the case of UDP path MTU can be implemented only if the application above UDP keeps
the necessary state and implements path MTU (unless the path MTU is stored as a routing table entry
like in an IBM AIX system). This is harder to deploy because it is harder to change many applications,
unlike changing just TCP. Thus at the time of writing, shared file system protocols such as NFS, IP
within IP encapsulation protocols, and many media player and game protocols run over UDP and do
not support path MTU. Finally, many attackers compromise security by splitting an attack payload
across multiple fragments. Thus intrusion detection devices must often reassemble IP fragments to
check for suspicious strings within the reassembled data.
     Thus it is worth investigating fast reassembly algorithms because common programs such as NFS
do not support the path MTU protocol and because real-time intrusion detection systems must reassem-
ble packets at line speeds to detect attacks hidden across fragments. The next section describes fast
reassembly implementations at receivers.
