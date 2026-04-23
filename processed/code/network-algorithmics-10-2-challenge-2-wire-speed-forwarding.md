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



    The data flow through the bridge was as follows. Imagine a packet P sent on Ethernet 1. Both Eth-
ernet chips were set in “promiscuous mode,” whereby they received all packets. Thus the bits of P are
captured by the upper Ethernet chip and stored in the shared memory in a receive queue. The processor
eventually reads the header of P , extracts the destination address D, and gives it to the lookup engine.
    The lookup engine looks up D in a database also stored in the shared memory and returns the port
(upper or lower Ethernet) in around 1.3 microsecond. If the destination is on the upper Ethernet, then
the packet buffer pointer is moved to a free queue, effectively discarding the packet; otherwise, the
buffer pointer is moved to the transmit queue of the lower Ethernet chip. The processor also provides
the source address S in packet P to the lookup engine for learning.
    His design paid careful attention to algorithmics in at least three areas to achieve wire speed for-
warding at a surprisingly small manufacturing cost of around $1000.
• Architectural Design: To minimize the cost, the memory was cheap DRAM with a cycle time of
  100 nanosecond that was used for packet buffers, scratch memory, and the lookup database. The
  four-port memory (including the separate connection from the lookup engine to the memory) and
  the buses were carefully designed to maximize parallelism and minimize interference. For example,
  while the lookup engine worked on doing lookups to memory, the processor continued to do useful
  work. Note that the processor has to examine the receive queues of both Ethernet chips in dove-
  tailed fashion to check for packets to be forwarded from either the top or bottom Ethernets. Careful
  attention was paid to memory bandwidth, including the use of page mode (Chapter 2).
• Data Copying: The Lance chips used DMA (Chapter 5) to place packets in the memory without
  processor control. When a packet was to be forwarded between the two Ethernets, the processor
  only flipped a pointer from the receive queue of one Ethernet chip to the transmit queue of the other
  processor.
• Control Overhead: As with most processors, the interrupt overhead of the 68000 was substantial.
  To minimize this overhead, the processor used polling, staying in a loop after a packet interrupt and
  servicing as many packets that arrive, in order to reduce context-switching overhead (Chapter 6).
  When the receive queues are empty, the processor moves on to doing other chores, such as pro-
  cessing control traffic. The first data packet arrival after such an idle period interrupts the processor,
  but this interrupt overhead is spread over the entire batch of packets that arrive before another idle
  period begins.
• Lookups: Very likely, Mark went through the eight cautionary questions found in Chapter 3. First,
  to avoid any complaints, he decided to use binary search (P15, efficient data structures) for lookup
  because of its determinism. Second, having a great deal of software experience before he began
  designing hardware, he wrote some sample 68000 code and determined that software binary search
  lookup was the bottleneck (Q2 in Chapter 3) and would exceed his packet processing budget of 25.6
  microsecond. Eliminating the destination and source lookup would allow him to achieve wire speed
  forwarding (Q3). Recall that each iteration of binary search reads an address from the database in
  memory, compares it with the address that must be looked up, and uses this comparison to determine
  the next address to be read. With added hardware (P5), the comparison can be implemented using
  combinatorial logic (Chapter 2), and so a first-order approximation of lookup time is the number

                                                          10.2 Challenge 2: wire speed forwarding                            241



    of DRAM memory accesses. As the first product aimed for a table size of 8000,4 this required
    log2 8000 memory accesses of 100-nanosecond each, yielding a lookup time of 1.3 microsecond.
    Given that the processor does useful work during the lookup, two lookups for source and destination
    easily fit within a 25.6 microsecond budget (Q4).
    To answer Q5 in Chapter 3 as to whether custom hardware is worthwhile, Mark found that the
lookup chip could be cheaply and quickly implemented using a PAL (programmable array logic; see
Chapter 2). To answer Q7, his initial prototype met wire speed tests constructed using logic analyzers.
Finally, Q8, which asks about the sensitivity to environment changes, was not relevant to a strictly
worst-case design like this.
    The 68000 software, written by Bob Shelley, also had to be carefully constructed to maximize
parallelism. After the prototype was built, Tony Lauck, then head of DECNET, was worried that bridges
would not work correctly if they were placed in cyclic topologies. For example, if two bridges are placed
between the same pair of Ethernets, messages sent on one Ethernet will be forwarded at wire speed in
the loop between bridges. In response, Radia Perlman, then the DEC routing architect, invented her
celebrated spanning tree algorithm. The algorithm ensures that bridges compute a loop-free topology
by having redundant bridges turn off appropriate bridge ports.
    While you can read up on the design of the spanning tree algorithm in Perlman’s book (Perlman,
1992), it is interesting to note that there was initial resistance to implementing her algorithm, which ap-
peared to be “complex” when compared to simple, fast bridge data forwarding. However, the spanning
tree algorithm used control messages, called Hellos, that are not processed in real time.
    A simple back-of-the-envelope calculation by Tony Lauck related the number of instructions used to
process a hello (at most 1000), the rate of hello generation (specified at that time to be once every sec-
ond), and the number of instructions per second of the Motorola 68000 (around 1 million). Lauck’s vi-
sion and analysis carried the day, and the spanning tree algorithm was implemented in the final product.
    Manufactured at a cost of $1000, the first bridge was initially sold at a markup of around eight,
ensuring a handsome profit for DEC when sales initially climbed. In 1986 Mark Kempf was awarded
US Patent 4,597,078, titled “Bridge circuit for interconnecting networks.” DEC made no money from
patent licensing, choosing instead to promote the IEEE 802.1 bridge interconnection standards process.
    Together with the idea of self-learning bridges, the spanning tree algorithm has passed into history.
Ironically, one of the first customers complained that the bridge did not work correctly; field service
later determined that the customer had connected two bridge ports to the same Ethernet, and the span-
ning tree had (rightly) turned the bridge off! While features like autoconfigurability and provable fault
tolerance have only recently been added to Internet protocols, they were part of the bridge protocols in
the 1980s.
    The success of Ethernet bridges led to proposals for several other types of bridges connecting other
local area networks and even wide area bridges. The author even remembers working with John Hart
(who went on to become CTO of 3Com) and Fred Baker (who went on to become a Cisco Fellow)
on building satellite bridges that could link geographically distributed sites. While some of the initital
enthusiasm to extend bridges to supplant routers was somewhat extreme, bridges found their most
successful niche in cheaply interconnecting similar local area networks at wire speeds.


4 This allows a bridged Ethernet to have only 8000 stations. While this is probably sufficient for most customer sites, later bridge
implementations raised this figure to 16K and even 64K.

242      Chapter 10 Exact-match lookups



    However, after the initial success of 10-Mbps Ethernet bridges, engineers at DEC began to worry
about bridging higher-speed LANs. In particular, DEC decided, perhaps unwisely, to concentrate their
high-speed interconnect strategy around 100-Mbps FDDI token rings (UNH Inter Operability Lab,
2001). Thus in the early 1990s engineers at DEC and other companies began to worry about building a
bridge to interconnect two 100-Mpbs FDDI rings. Could wire speed forwarding, and especially exact-
match lookups, be made 10 times faster?
