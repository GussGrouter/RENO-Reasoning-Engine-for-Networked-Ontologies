# network-algorithmics-9-2-1-cyclic-redundancy-checks (chunk 000001)

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
