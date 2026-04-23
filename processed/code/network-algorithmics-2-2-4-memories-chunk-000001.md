# Chunk 000001

- Source: raw/code/pdf/Network.Algorithmics.pdf
- Slice: 2.2.4 Memories (registers/SRAM/DRAM intro)
- From: processed/code/network-algorithmics-2-2-4-memories-registers-sram-dram.md

---
2.2.4 Memories
In endnodes and routers, packet forwarding is performed using combinational logic, but packets and
forwarding state are stored in memories. Since memory access times are significantly slower than logic
delays, memories form major bottlenecks in routers and endnodes.


4 This can be done by ANDing the input with P encoded as a mask; such a mask is commonly known in the hardware community
as a thermometer encoding of P .

2.2 Hardware               27



    Further, different subsystems require different memory characteristics. For example, router vendors
feel it is important to buffer 200 msec—an upper bound on a round-trip delay—worth of packets to
avoid dropping packets during periods of congestion. At, say, 40 Gbit/sec per link, such packet buffer-
ing requires an enormous amount of memory. On the other hand, router lookups require a smaller
amount of memory, which is accessed randomly. Thus it helps to have simple models for different
memory technologies. Next, we describe registers, SRAMs, DRAMs, and interleaved memory tech-
nology. Simple implementation models of these memory components can be found in Section A.2.4 in
Appendix.

Registers
A flip-flop is a way of connecting two or more transistors in a feedback loop so that (in the absence of
Writes and power failures) the bit stays indefinitely without “leaking” away. A register is an ordered
collection of flip-flops. For example, most modern processors have a collection of 32- or 64-bit on-chip
registers. A 32-bit register contains 32 flip-flops, each storing a bit. Access from logic to a register on
the same chip is extremely fast, around 0.5–1 nsec.

SRAM
A static random access memory (SRAM) contains N registers addressed by log N address bits A.
SRAM is so named because the underlying flip-flops refresh themselves and so are “static.” Besides
flip-flops, an SRAM also needs a decoder that decodes A into a unary value used to select the right
register. Accessing an SRAM on-chip is only slightly slower than accessing a register because of the
added decode delay. At the time of writing, it was possible to obtain on-chip SRAMs with 0.5-nsec
access times. Access times of 1–2 nsec for on-chip SRAM and 5–10 nsec for off-chip SRAM are
common.

Dynamic RAM
An SRAM bit cell requires at least five transistors. Thus SRAM is always less dense or more expensive
than memory technology based on dynamic RAM (DRAM). The key idea is to replace the feedback
loop (and extra transistors) used to store a bit in a flip-flop with an output capacitance that can store
the bit; thus the charge leaks, but it leaks slowly. Loss due to leakage is fixed by refreshing the DRAM
cell externally within a few milliseconds. Of course, the complexity comes in manufacturing a high
capacitance using a tiny amount of silicon.
    DRAM chips appear to quadruple in capacity every 3 years (Fromm et al., 1997) and are heading
towards 1 gigabit on a single chip. Addressing these bits, even if they are packed together as 4- or even
32-bit “registers,” is tricky. Recall that the address must be decoded from (say) 20 bits to (say) one of
220 values. The complexity of such decode logic suggests divide-and-conquer. Why not decode in two
stages?
    Fig. 2.5 shows that most memories are internally organized two-dimensionally into rows and
columns. The upper address bits are decoded to select the row, and then the lower address bits are
used to decode the column. More precisely, the user first supplies the row address bits and enables a
signal called RAS (row address strobe); later, the user supplies the column address bits,5 and enables

5 Many DRAM chips take advantage of the fact that row and column addresses are not required at the same time to multiplex
row and column addresses on the same set of pins, reducing the pin count of the chip.

28        Chapter 2 Network implementation models
