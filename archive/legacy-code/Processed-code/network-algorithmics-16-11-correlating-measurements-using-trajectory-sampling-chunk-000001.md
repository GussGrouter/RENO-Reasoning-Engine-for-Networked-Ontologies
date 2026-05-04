# network-algorithmics-16-11-correlating-measurements-using-trajectory-sampling (chunk 000001)

# Network Algorithmics — 16.11 Correlating measurements using trajectory sampling (slice)

- Source: raw/code/pdf/Network.Algorithmics.pdf
- Full-text extraction: processed/code/network-algorithmics-full-layout.txt
- Slice start: PDF page 497
- Slice: from `16.11 Correlating measurements using trajectory sampling` up to next detected section heading

---

16.11 Correlating measurements using trajectory sampling
A final technique for router measurement is called trajectory sampling (Duffield and Grossglauser,
2000). It is orthogonal to the last two techniques and can be combined with them. Recall that in sampled
NetFlow and sampled charging, each router independently samples a packet. Thus, the set of packets
sampled at each router is different even when a set of routers sees the same stream of packets.
    The main idea in trajectory sampling is to have routers in a path make correlated packet-sampling
decisions using a common hash function. Fig. 16.122 shows packets entering a router line card. The
stream is “tapped” before it goes to the switch fabric. For every packet, a hash function h is used to
decide whether the packet will be sampled by comparing the hashed value of the packet to a specified
range. If the packet is sampled, a second hash function, g, on the packet is used to store a packet label
in a log.
    Trajectory sampling enables managers to correlate packets on different links. To ensure this, two
more things are necessary. First, all routers must use the same values of g and h. Second, since packets
can change header fields from router to router (e.g., TTL is decremented, data link header fields change),
the hash functions are applied only to portions of the network packet that are invariant. This is achieved
by computing the hash on header fields that do not change from hop to hop together with a few bytes
of the packet payload.
    A packet that is sampled at one router will be sampled at all routers in the packet’s trajectory or
path. Thus a manager can use trajectory sampling to see path effects, such as packet looping, packet
drops, and multiple shortest paths, that may not be possible to discern using ordinary sampled NetFlow.
    In summary, the two differences between trajectory sampling and sampled NetFlow are: (1) the use
of a hash function instead of a random number to decide when to sample a packet; and (2) the use of a
second hash function on invariant packet content to represent a packet header more compactly.
