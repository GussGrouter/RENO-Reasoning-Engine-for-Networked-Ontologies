# network-algorithmics-2-2-7-final-hardware-lessons (chunk 000001)

# Network Algorithmics — 2.2.7 Final hardware lessons (slice)

- Source: raw/code/pdf/Network.Algorithmics.pdf
- Full-text extraction: processed/code/network-algorithmics-full-layout.txt
- Slice start: PDF page 59
- Slice: from `2.2.7 Final hardware lessons` up to next detected section heading

---

2.2.7 Final hardware lessons
If all else is forgotten in this hardware design section, it is helpful to remember the design techniques
of Section 2.2.5. Knowledge of the following parameter values is also useful to help system designers
quickly weed out infeasible designs without detailed knowledge of hardware design. Unfortunately,
these parameters are a moving target, and the following numbers were written based on technology
available in 2004.
• Chip Complexity Scaling: The number of components per chip appears to double every 2 years.
  While 0.13-micron processes are common, 90-nm technology is ramping up, and 65-nm technology
  is expected after that. As a result, current ASICs can pack several million gate equivalents (that’s
  a lot of combinatorial logic) plus up to 50 Mbits (at the time of writing, using half a 12-mm/side
  die) of on-chip SRAM on an ASIC.7 Embedded DRAM is also a common option to get more space
  on-chip at the cost of larger latency.
• Chip Speeds: As feature sizes go down, on-chip clock speeds of 1 GHz are becoming common, with
  some chips even pushing close to 3 GHz. To put this in perspective, the clock cycle to do a piece
  of computation on a 1-GHz chip is 1 nsec. By using parallelism via pipelining and wide memory
  words, multiple operations can be performed per clock cycle.
• Chip I/O: The number of pins per chip grows, but rather slowly. While there are some promising
  technologies, it is best to assume that designs are pin limited to around 1000 pins.
• Serial I/O: Chip-to-chip I/O has also come a long way, with 10-Gbit serial links available to connect
  chips.
• Memory Scaling: On-chip SRAM with access times of 1 nsec are available, with even smaller ac-
  cess times being worked on. Off-chip SRAM with access times of 2.5 nsec are commonly available.
  On-chip DRAM access times are around 30 nsec, while off-chip DRAM of around 60 nsec is com-
  mon. Of course, the use of interleaved DRAM, as discussed in the memory subsection, is a good
  way to increase memory subsystem throughput for certain applications. DRAM costs roughly 4–10
  times less than SRAM per bit.
• Power and Packaging: The large power consumption of high-speed routers requires careful de-
  sign of the cooling system. Finally, most ISPs have severe rack space limitations, and so there is
  considerable pressure to build routers that have small form factors.
    These parameter values have clear implications for high-speed networking designs. For instance,
at OC-768 speeds, a 40-byte packet arrives in 3.2 nsec. Thus it seems clear that all states required to
process the packet must be in on-chip SRAM. While the amount of on-chip SRAM is growing, this
memory is not growing as fast as the number of flows seen by a router. Similarly, with 1-nsec SRAMs,
at most, three memory accesses can be made to a single memory bank in a packet arrival time.
    Thus the design techniques of Section 2.2.5 must be used within a chip to gain parallelism using
multiple memory banks and wide words and to increase the usable memory by creative combinations

7 FPGAs are more programmable chips that can only offer smaller amounts of on-chip SRAM.

2.3 Network device architectures                         33

that involve off- and on-chip memory. However, given that chip densities and power constraints limit
parallelism to, say, a factor of at most 60, the bottom line is that all packet-processing functions at high
speeds must complete using at most 200 memory accesses and limited on-chip memory.8 Despite these
limitations, a rich variety of packet-processing functions have been implemented at high speeds.
