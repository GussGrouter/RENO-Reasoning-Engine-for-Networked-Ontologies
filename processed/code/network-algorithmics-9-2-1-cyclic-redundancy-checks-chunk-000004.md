# network-algorithmics-9-2-1-cyclic-redundancy-checks (chunk 000004)

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
