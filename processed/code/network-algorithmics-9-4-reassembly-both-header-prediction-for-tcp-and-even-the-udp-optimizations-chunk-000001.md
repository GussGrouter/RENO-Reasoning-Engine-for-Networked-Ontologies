# network-algorithmics-9-4-reassembly-both-header-prediction-for-tcp-and-even-the-udp-optimizations (chunk 000001)

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
