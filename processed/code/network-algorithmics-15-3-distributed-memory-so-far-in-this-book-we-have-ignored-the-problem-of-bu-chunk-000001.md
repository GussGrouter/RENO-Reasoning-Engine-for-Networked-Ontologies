# network-algorithmics-15-3-distributed-memory-so-far-in-this-book-we-have-ignored-the-problem-of-bu (chunk 000001)

# Network Algorithmics — 15.3 Distributed Memory So far in this book, we have ignored the problem of building packet buffers. The following section is (slice)

- Source: raw/code/pdf/Network.Algorithmics.pdf
- Full-text extraction: processed/code/network-algorithmics-full-layout.txt
- Slice start: PDF page 465
- Slice: from `15.3 Distributed Memory So far in this book, we have ignored the problem of building packet buffers. The following section is` up to next detected section heading

---

15.3 Distributed Memory
So far in this book, we have ignored the problem of building packet buffers. The following section is
based on Chapter 7 of Sundar Iyer’s PhD Thesis (Sundar, 2008). The reader should consult the thesis
for more details.
    Packet buffers are an important part of the hardware of a router for three reasons: size and ubiquity
and Quality of Service. First, the size of packet buffers has been increasing as speeds increase. The
classic rule of thumb is that a switch should buffer RT T × R bits to account for congestion (where
RT T is the average round-trip time for TCP flows passing through the router. Assuming a coast to
coast delay of around 250 msec, a 100 Gb/s interface requires 25 Gb of memory, within the capacity
of commodity DRAMs, but much larger than high-speed SRAMs. Iyer’s thesis (Sundar, 2008) claims
that at the time of writing, buffering was responsible for almost 40% of all memory consumed by high
speed routers/switches. There is reason to believe that the situation is only worse today.
    Second, packet buffers are ubiquitous in routers. Iyer’s thesis (Sundar, 2008) gives several examples
of where buffers are used. Two important examples are at the input to the VOQs in an input buffered
switch (because of contention for output ports), and at the output port (because of congestion on the
output link). There are, however, many other places in real routers including reordering buffers when
packets are striped across the fabric as seen in the previous section, and multicast replication buffers.
    Third, router buffering is complicated by Quality of Service (QoS) as we have seen earlier. Routers
used by service providers, such as the Cisco GSR 12000 router maintain about 2,000 queues per line
card, while edge routers such as the Juniper E-series provide as many as 64,000 queues for fine-grained
QoS (Sundar, 2008).
    The principal problem with router buffers today is that as soon as the link speed exceeds 10 Gb/s,
a miniumum size 40-byte packet arrives within 32 ns. This implies that every 16 ns a packet needs to
be written to or read from memory (recall a packet must be written and stored, and read out to be sent
out). If one uses a single standard DRAM with a 50-ns access time, this is impossible. Similarly, the
use of SRAMs of this capacity is much too expensive and power hungry.
    A possible approach is to design new DRAMs with smaller access times. The access time of a
DRAM depends on its geometry. One can theoretically make DRAMs faster by designing it internally
with smaller banks creating even DRAMs with (say) 20 nsec access times. Unfortunately, this approach

15.3 Distributed Memory             439

does not scale as speeds increase. Further, the extra bank overhead requires significantly larger chip
area, and leads to an unacceptable area versus cost tradeoff. This is true especially in a world where
router memory is a very small portion of the overall DRAM market, which is dominated today by the
stringent cost pressures of computer memory.
