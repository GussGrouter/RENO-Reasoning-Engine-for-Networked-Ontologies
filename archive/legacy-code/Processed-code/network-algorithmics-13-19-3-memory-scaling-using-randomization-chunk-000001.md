# network-algorithmics-13-19-3-memory-scaling-using-randomization (chunk 000001)

# Network Algorithmics — 13.19.3 Memory scaling using randomization (slice)

- Source: raw/code/pdf/Network.Algorithmics.pdf
- Full-text extraction: processed/code/network-algorithmics-full-layout.txt
- Slice start: PDF page 404
- Slice: from `13.19.3 Memory scaling using randomization` up to next detected section heading

---

13.19.3 Memory scaling using randomization
In all the switches seen so far packets have to be stored in buffers during periods of congestion. The
standard rule of thumb is for routers to have one RTT (Roundtrip Time) worth of buffering to allow
congestion-control algorithms to slow down without causing packet loss. While it may be possible to
get around this limit using better higher-level congestion-control algorithms, it appears that the com-
bination of TCP and RED (random early detection) today requires this amount of buffering. Using
200 msec as a conservative estimate for round-trip delay, a two-terabit router must have 0.4 terabit’s
worth of packet buffers. Thus as link speeds increase and assuming no congestion-control innovations,
the memory needs will also increase.
    Consider an input-buffered switch and packets coming in at OC-768 speeds. Thus a minimum-size
packet arrives every 8 nanoseconds and will require at least two accesses to memory: the first to store
the packet and the second to read it out for transmission through the fabric. Given that the fastest DRAM
available at the time of writing has a cycle time of 50 nanoseconds, it is clear that the only way to meet
the memory bandwidth needs using DRAM would be to use a wider memory word.
    Unfortunately, one cannot use a wider memory word size than that of a minimum-size packet be-
cause it is not possible to guarantee that the next packet will be read out at the same time. One could

378       Chapter 13 Switching

use SRAMs (at 4 nanoseconds cycle times at the time of writing, this should be just adequate), but then
one would have to pay a cost premium of anywhere from a factor of four to a factor of 10.4
    One way out of this dilemma is to use parallel banks of DRAMs. It is possible to keep up with
link speeds using 12 DRAM banks working in parallel, each with a 40-byte access width. Intuitively,
this seems plausible. For any input stream of packets, send the first packet to DRAM 1, the second to
DRAM 2, etc. Unfortunately, because of QoS and scheduling algorithms, it is not clear in which order
packets will be read out. Thus it may be that during some period of time, all the packets are read out
from a few DRAMs only, causing memory bandwidth contention and eventual packet loss.
    Such memory contention problems are familiar to computer architects when using interleaved mem-
ory. For example, if an array is laid out sequentially across memory banks, it is possible that accesses
that are spaced a certain stride apart (e.g., column accesses) may all hit the same bank. One poten-
tially clever way out of the contention problem is to steal a leaf from the designers of the CYDRA-2
stride-insensitive memory (Rau, 1991). Their idea was to pseudorandomly interleave storage requests
to memory such that with high probability any access pattern (other than to the same word) would not
cause hot spots. Indeed, techniques of performing such stride-insensitive or even adversary-resistant
randomized memory interleaving have been proposed in several recent papers (Lin et al., 2009; Wang
et al., 2010; Zhao et al., 2009).
    In the router context instead of sending packet 1 to DRAM 1 and so on, one would send each packet
to a randomly selected DRAM. Of course, as with all randomized interleaving schemes (see the earlier
Clos and Benes sections), reassembly gets more complicated, with the states having to be kept (in
SRAM?) to resequence these packets.
