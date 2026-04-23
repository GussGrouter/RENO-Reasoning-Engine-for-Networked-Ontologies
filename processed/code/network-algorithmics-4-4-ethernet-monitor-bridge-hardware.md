# Network Algorithmics — Ethernet monitor using bridge hardware (4.4) (slice)

- Source: raw/code/pdf/Network.Algorithmics.pdf
- Extraction: pdftotext -f 108 -l 136 -layout
- Slice: from `4.4 Ethernet monitor using bridge hardware` up to (excluding) `4.5`

---

4.4 Ethernet monitor using bridge hardware
Alyssa P. Hacker is working for Acme Networks and knows of the Ethernet bridge invented at Acme.
A bridge (see Chapter 10) is a device that can connect Ethernets together. To forward packets from one
Ethernet to another, the bridge must look up the 48-bit destination address in an Ethernet packet at high
speeds.
    Alyssa decides to convert the bridge into an Ethernet traffic monitor that will passively listen to
an Ethernet and produce statistics about traffic patterns. The marketing person tells her that she needs
to monitor traffic between arbitrary source–destination pairs. Thus for every active source–destination
pair, such as A, B, Alyssa must keep a variable PA,B that measures the number of packets sent from A
to B since the monitor was started. When a packet is sent from A to B, the monitor (which is listening
to all packets sent on the cable) will pick up a copy of the packet. If the source is A and the destination is
B, the monitor should increment PA,B . The problem is to do this in 64 µsec, the minimum interpacket
time on the Ethernet. The bottleneck is the lookup of the state PA,B associated with a pair of 48-bit
addresses A, B.
    Fortunately, the bridge hardware has a spiffy lookup hardware engine that can look up the state
associated with a single 48-bit address in 1.4 µsec. A call to the hardware can be expressed as Lookup(X,
D), where X is the 48-bit key and D is the database to be searched. The call returns the state associated
with X in 1.4 µsec for databases of less than 64,000 keys. What Alyssa must solve is the following
problem.

Problem
The monitor needs to update state for AB when a packet from A to B arrives. The monitor has a lookup
engine that can look up only single addresses and not address pairs. How can Alyssa use the existing
engine to look up address pairs? The problem is illustrated in Fig. 4.7.

Hint: The problem requires using P4c to exploit the existing bridge hardware. Since 1.4 µsec is
much smaller than 64 µsec, the design can afford to use more than one hardware lookup. How can
a 96-bit lookup be reduced to a 48-bit lookup using three lookups?
    A naive solution is to use two lookups to convert source A and destination B into smaller
(<24-bit) indices IA and IB . The indices IA and IB can then be used to look up a two-dimensional
array that stores the state for AB. This requires only two hardware lookups plus one more mem-
ory access, but it can require large amounts of memory. If there are 1000 possible sources and
1000 possible destinations, the array must contain a million entries. In practice, there may be
only 20,000 active source–destination pairs. How could you make the required amount of memory
proportional to the number of actual source–destination pairs?

---

## PDF page 110

                                                4.4 Ethernet monitor using bridge hardware                        83




FIGURE 4.7
Adapting an engine that does destination lookups to doing source-destination lookups.




FIGURE 4.8
Converting a 96-bit lookup into a 48-bit lookup by first converting each 48-bit address into a 24-bit index and
concatenating the indices.




Solution
As before, first use one lookup each to convert source A and destination B into smaller (<24-bit)
indices IA and IB . Then use a third lookup to map from IA IB to AB state. The solution is illustrated in
Fig. 4.8. The third lookup effectively compresses the two-dimensional array of the naive solution. This
solution is due to Mark Kempf and Mike Soha.

Exercises

• Can this problem be solved using only two bridge hardware lookups without requiring extra mem-
  ory?
• The set of active source–destination pairs may change with time because some pairs of addresses
  stop communicating for long periods. How can this be handled without keeping the state for every
  possible address pair that has communicated since the monitor was powered on?

---

## PDF page 111

84        Chapter 4 Principles in action




FIGURE 4.9
Demultiplexing in the x-kernel is done by hashing the protocol identifier K and (potentially) using a byte-by-byte
comparison with the key L stored at the hash table entry.
