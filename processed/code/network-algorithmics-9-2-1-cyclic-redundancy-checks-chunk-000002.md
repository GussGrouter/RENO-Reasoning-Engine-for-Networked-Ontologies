# network-algorithmics-9-2-1-cyclic-redundancy-checks (chunk 000002)

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
