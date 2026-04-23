# network-algorithmics-2-2-hardware-as-links-approach-40-gigabit-sec-oc-768-speeds-a-40-byte-packet (chunk 000001)

# Network Algorithmics — 2.2 Hardware As links approach 40-gigabit/sec OC-768 speeds, a 40-byte packet must be forwarded in 8 nsec. At such (slice)

- Source: raw/code/pdf/Network.Algorithmics.pdf
- Full-text extraction: processed/code/network-algorithmics-full-layout.txt
- Slice start: PDF page 49
- Slice: from `2.2 Hardware As links approach 40-gigabit/sec OC-768 speeds, a 40-byte packet must be forwarded in 8 nsec. At such` up to next detected section heading

---

2.2 Hardware
As links approach 40-gigabit/sec OC-768 speeds, a 40-byte packet must be forwarded in 8 nsec. At such
speeds, packet forwarding is typically directly implemented in hardware instead of on a programmable
processor. You cannot participate in the design process of such hardware-intensive designs without
understanding the tools and constraints of hardware designers. And yet, a few simple models can allow
you to understand and even play with hardware designs. Even if you have no familiarity with and
have a positive distaste for hardware, you are invited to take a quick tour of hardware design, full of
networking examples to keep you awake.
   Internet lookups are often implemented using combinational logic, Internet packets are stored in
router memories, and an Internet router is put together with components such as switches and lookup
chips. Thus our tour begins with logic implementation, continues with memory internals, and ends
with component-based design. For more details, we refer the reader to the classic VLSI text (Mead
and Conway, 1980), which still wears well despite its age, and the classic computer architecture text
(Hennessey and Patterson, 1996).

2.2.1 Combinatorial logic
Section A.2.1 in Appendix describes very simple models of basic hardware gates, such as NOT, NAND,
and NOR, that can be understood by even a software designer who is willing to read a few pages.
However, even knowing how basic gates are implemented is not required to have some insight into
hardware design.
    The first key to understanding logic design is the following observation. Given NOT, NAND, and
NOR gates, Boolean algebra shows that any Boolean function f (I1 , . . . , In ) of n inputs can be imple-
mented. Each bit of a multibit output can be considered a function of the input bits. Logic minimization
is often used to eliminate redundant gates and sometimes to increase speed. For example, if + denotes
OR and · denotes AND, then the function O = I1 · I2 + I1 · I2 can be simplified to O = I1 .

Example 1. Quality of Service and Priority Encoders: Suppose we have a network router that maintains
n output packet queues for a link, where queue i has higher priority than queue j if i < j . This problem
comes under the category of providing quality of service (QoS), which is covered in Chapter 14. The
transmit scheduler in the router must pick a packet from the first nonempty packet queue in priority
order. Assume the scheduler maintains an N -bit vector (bitmap) I such that I [ j ] = 1 if and only if
queue j is nonempty. Then the scheduler can find the highest-priority nonempty queue by finding the
smallest position in I in which a bit is set. Hardware designers know this function intimately as a
priority encoder. However, even a software designer should realize that this function is feasible for
hardware implementation for reasonable n. This function is examined more closely in Example 2.

2.2 Hardware     23
