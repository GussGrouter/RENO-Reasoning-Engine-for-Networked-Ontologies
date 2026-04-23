# network-algorithmics-2-2-6-component-level-design (chunk 000001)

# Network Algorithmics — 2.2.6 Component-level design (slice)

- Source: raw/code/pdf/Network.Algorithmics.pdf
- Full-text extraction: processed/code/network-algorithmics-full-layout.txt
- Slice start: PDF page 58
- Slice: from `2.2.6 Component-level design` up to next detected section heading

---

2.2.6 Component-level design
The methods of the last two subsections can be used to implement a state machine that implements
arbitrary computation. A state machine has a current state stored in memory; the machine processes
inputs using combinatorial logic that reads the current state and possibly writes the state. An example
of a complex state machine is a Pentium processor, whose state is the combination of registers, caches,
and main memory. An example of a simpler state machine is the flow ID lookup chip of Fig. 2.7, whose
state is the registers used to track each of 16 concurrent lookups and the RDRAM storing the B-tree.
    While a few key chips may have to be designed to build a router or a network interface card, the
remainder of the design can be called component-level design: organizing and interconnecting chips
on a board and placing the board in a box while paying attention to form factor, power, and cooling. A
key aspect of the component-level design is understanding pin-count limitations, which often provide a
quick “parity check” on feasible designs.

Example 5. Pin-Count Implications for Router Buffers: Consider a router that has forty 10 Gb/sec
links. The overall buffering required is 200 msec * 400 Gb/sec, which is 80 gigabits. For cost and
power, we use DRAM for packet buffers. Since each packet must go in and out of the buffer, the overall
memory bandwidth needs to be twice the bandwidth into the box—i.e., 800 Gb/sec. Assuming 100%
overhead for internal packet headers, links between packets in queues, and wasted memory bandwidth,
it is reasonable to aim for 1600-Gb/sec memory bandwidth.
     Using a single direct 64-bit-wide RDRAM with 16 banks, specifications show peak memory band-
width of 1.28 GB/sec,6 or 10.24 Gb/sec. Accessing each RDRAM requires 64 interface pins for data
and 25 other pins for address and control, for a total of roughly 90 pins. A 1600-Gbps memory band-
width requires 160 RDRAMs, which require 14400 pins in total. A conservative upper bound on the
number of pins on a chip is around 1000. This implies that even if the router vendor were to build an

6 Assuming the DRAM takes 100 ns between reads, if the width is 64 bits (8 bytes), with a single bank we can read 8 bytes
every 100 ns (as mentioned on page 28), or 0.08 GB/sec.

32        Chapter 2 Network implementation models

extremely fast custom-designed packet-forwarding chip that could handle all packets at the maximum
box rate, one would still need at least one more chip to drive data in and out of the RAMBUS packet
buffers. Our message is that pin limitations are a key constraint in partitioning a design between chips.
