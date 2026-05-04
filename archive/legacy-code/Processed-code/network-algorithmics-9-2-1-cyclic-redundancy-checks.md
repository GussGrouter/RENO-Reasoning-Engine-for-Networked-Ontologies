# Network Algorithmics — 9.2.1 Cyclic redundancy checks (slice)

- Source: raw/code/pdf/Network.Algorithmics.pdf
- Full-text extraction: processed/code/network-algorithmics-full-layout.txt
- Slice start: PDF page 245
- Slice: from `9.2.1 Cyclic redundancy checks` up to next detected section heading

---

9.2.1 Cyclic redundancy checks
The CRC “hash” function is calculated by dividing the packet data, treated as a number, with a
fixed generator G. G is just a binary string of predefined length. For example, CRC-16 is the string
11000000000000101, of length 17; it is called CRC-16 because the remainder added to the packet
turns out to be 16 bits long.
    Generators are easier to remember when written in polynomial form. For example, the same CRC-
16 in polynomial form becomes x 16 + x 15 + x 2 + 1. Notice that whenever x i is present in the generator
polynomial, position i is equal to 1 in the generator string. Whatever CRC polynomial is picked (and
CRC-32 is very common), the polynomial is published in the data link implementation specification
and is known in advance to both receiver and sender.
    A formal description of CRC calculation is as follows. Let r be the number of bits in the generator
string G. Let M be the message whose CRC is to be calculated. The CRC is simply the remainder c of
2r−1 M (i.e., M left-shifted by r − 1 bits) when divided by G. The only catch is the division is mod-2
division, which is illustrated next.
    Working out the mathematics slightly, 2r−1 M = k.G + c. Thus 2r−1 M + c = k.G because addition
is the same as subtraction in mod-2 arithmetic, a fact strange but true. Thus, even ignoring the preceding
math, the bottom line is that if we append the calculated CRC c to the end of the message, the resulting
number divides the generator G.
    Any bit errors that cause the sent packet to change to some other packet will be caught as long as the
resulting packet is not divisible by G. CRCs, like good hash functions, are effective because common
errors based on flipping a few bits (random errors) or changing any bit in a group of contiguous bits
(burst errors) are likely to create a packet that does not divide G. Simple analytical properties of CRCs
are derived in Tanenbaum (1981).
    For the implementor, however, what matters is not why CRC works but how to implement it. The
main thing to learn is how to compute remainders using mod-2 division. The algorithm uses a simple
iteration in which the generator G is progressively “subtracted” from the message M until the remainder
is “smaller” than the generator G. This is exactly like ordinary division except that “subtraction” is
now exclusive-OR, and the definition of whether a number is “smaller” depends on whether its most
significant bit (MSB) is 0.
    More precisely, a register R is loaded with the first r bits of the message. At each stage of the
iteration, the MSB of R is checked. If it is 1, R is “too large” and the CRC string G is “subtracted”
from R. Subtraction is done by exclusive-OR (EX-OR) in mod-2 arithmetic. Assuming that the MSB
of the generator is always 1, this zeroes out the MSB of R. Finally, if the MSB of R is already 0, R is
“small enough” and there is no need to EX-OR.
    A single iteration completes by left-shifting R so that the MSB of R is lost, and the next message
bit gets shifted in. The iterations continue until all message bits are shifted in, and the MSB of register
R is 0. At this point, register R contains the required checksum.

                                            9.2 Cyclic redundancy checks and checksums                            219




FIGURE 9.3
CRC is calculated by dividing the shifted message with the generator. The intent is to shift in all the message bits
and to zero out any most significant bits that are set. Horizontal lines indicate EX-OR operations. Vertical lines
denote shifting in the next message bit. Dashed lines show where the generator is brought down. The generator is
used for the EX-OR when the MSB of the current result is 1; if not, zero is used.




FIGURE 9.4
Naive hardware implementation requires three clock cycles per bit.


    For example, let M = 110 and G = 111. Then 2r−1 M = 11000. Then the checksum c is calculated
as shown in Fig. 9.3. In the first step of Fig. 9.3 the algorithm places the first 3 bits (110) of the shifted
message in R. Since the MSB of 110 is 1, the algorithm hammers away at R by EX-ORing R with
the generator G = 111 to get 001. The first iteration completes by shifting out the MSB and (Fig. 9.3
topmost vertical arrow) shifting in the fourth message bit, to get R = 010.
    In the second iteration the MSB of R is 0 and so the algorithm desists. This is represented in
Fig. 9.3 by computing the EX-OR of R with 000 instead of the generator. As usual, the MSB of the
result is shifted in, and the last message bit, also a zero, is shifted in to get R = 100. Finally, in the
third iteration because the MSB of R is 1, the algorithm once again EX-ORs R with the generator. The
algorithm terminates at this point because the MSB of R is 0. The resulting checksum is R without the
MSB, or 11.

Naive implementation
Cyclic redundancy checks have to be implemented at a range of speeds from 1 Gbit/second to slower
rates. Higher-speed implementations are typically done in hardware. The simplest hardware implemen-
tation would mimic the foregoing description and use a shift register that shifts in bits one at time. Each
iteration requires three basic steps: checking the MSB, computing the EX-OR, and then shifting.
    The naive hardware implementation shown in Fig. 9.4 would require three clock cycles to shift in a
bit; doing a comparison for the MSB in one cycle and the actual EX-OR in another cycle and the shift

220       Chapter 9 Protocol processing




FIGURE 9.5
Linear feedback shift register implementation of a CRC remainder calculation. The EX-ORs are combined with a
shift by placing EX-OR gates (the circles) to the right of some registers. Specifically, an EX-OR gate is placed to
the right of register i if bit i in the generator string (see dashed lines) is set. The only exception is (what would have
been) register R5. Such a register need not be stored because it corresponds to the MSB, which is always shifted out.



in the third cycle. However, a cleverer implementation can be used to shift in one bit every clock cycle
by combining the test for MSB, the EX-OR, and the shift into a single operation.

Implementation using linear feedback shift registers
In Fig. 9.5 the remainder R is stored as five separate 1-bit registers, R4 through R0, instead of a single
5-bit register, assuming a 6-bit generator string. The idea makes use of the observation that the EX-OR
needs to be done only if the MSB is 1; thus in the process of shifting left the MSB, we can feed back
the MSB to the appropriate bits of the remainder register. The remaining bits are EX-ORed during their
shift to the left.
    Notice that in Fig. 9.5 an EX-OR gate is placed to the right of register i if bit i in the generator
string (see dashed lines) is set. The reason for this rule is as follows. Compared to the simple iterative
algorithm, the hardware of Fig. 9.5 effectively combines the left shift of iteration J together with the
MSB check and EX-OR of iteration J + 1. Thus the bit that will be in position i in iteration J + 1 is in
position i − 1 in iteration J .
    If this is grasped (and this requires shifting one’s mental pictures of iterations), the test for the MSB
(i.e., bit 5) in iteration J + 1 amounts to checking MSB − 1 (i.e., bit 4 in R4) in iteration J . If bit 4 is
1, then an EX-OR must be performed with the generator. For example, the generator string has a 1 in
bit 2, so R2 must be EX-ORed with a 1 in iteration J + 1. But bit 2 in iteration J + 1 corresponds to
bit 1 in iteration J . Thus the EX-OR corresponding to R2 in iteration J + 1 can be achieved by placing
an EX-OR gate to the right of R2: the bit that will be placed in R2 is EX-ORed during its transit from
R1.
    Notice that the check for MSB has been finessed in Fig. 9.5 by using the output of R4 as an input
to all the EX-OR gates. The effect of this is that if the MSB of iteration J + 1 is 1 (recall that this is in
R4 during iteration J ), then all the EX-ORs are performed. If not, and if the MSB is 0, no EX-ORs are
done, as desired; this is the same as EX-ORing with zero in Fig. 9.3.
    The implementation of Fig. 9.5 is called a linear feedback shift register (LFSR), for obvious reasons.
This is a classical hardware building block, which is also useful for the generation of random numbers

                                               9.2 Cyclic redundancy checks and checksums                221



for, say, QoS (Chapter 14). For example, random numbers using, say, the Tausworth implementation
can be generated using three LFSRs and an EX-OR.

Faster implementations
The bottleneck in the implementation of Fig. 9.5 is the shifting, which is done one bit at a time. Even
at one bit every clock cycle, this is very slow for fast links. Most logic on packets occurs after the bit
stream arriving from the link has been deserialized3 into wider words of, say, size W . Thus the packet-
processing logic is able to operate on W bits in a single clock cycle, which allows the hardware clock
to run W times slower than the interarrival time between bits.
    Thus to gain speed, CRC implementations have to shift W bits at a time, for W > 1. Suppose the
current remainder is r and we shift in W more message bits whose value as a number is, say, n. Then
in essence the implementation needs to find the remainder of (2W · r + n) in one clock cycle.
    If the number of bits in the current remainder register is small, the remainder of 2W · r can be
precomputed (P2a) for all r by table lookup. This is the basis of a number of software CRC implemen-
tations that shift in, say, 8 bits at a time. In hardware it is faster and more space efficient to use a matrix
of XOR gates to do the same computation. The details of the parallel implementation can be found in
Albertengo and Riccardo (1990), based on the original idea described by Sarwate (1988).
