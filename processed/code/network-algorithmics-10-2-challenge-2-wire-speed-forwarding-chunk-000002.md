# network-algorithmics-10-2-challenge-2-wire-speed-forwarding (chunk 000002)

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
