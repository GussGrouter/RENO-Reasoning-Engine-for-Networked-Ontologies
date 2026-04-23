# network-algorithmics-9-2-1-cyclic-redundancy-checks (chunk 000003)

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
