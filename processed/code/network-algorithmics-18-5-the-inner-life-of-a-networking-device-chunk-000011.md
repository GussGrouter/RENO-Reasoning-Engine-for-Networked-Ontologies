# network-algorithmics-18-5-the-inner-life-of-a-networking-device (chunk 000011)

A.4 The interconnection network Zoo
There is a dazzling variety of (log N )-depth interconnection networks, all based on the same idea of
using bits in the output address to steer to the appropriate portion, starting with the most significant
bit. For example, one can construct the famous Butterfly network in a very similar way to the recursive
construction of the Delta network of Fig. 13.13. In the Delta network all the inputs to the top (N/2)-size
Delta network come from the 0 outputs of the first stage in order. Thus the 0 output of the first first-stage
switch is the first input, the 0 output of the second switch is the second input, etc.
     By contrast, in a Butterfly the second input of the upper N/2 switch is the 0 output of the middle
switch of the first stage (rather than the second switch of the first stage). The 0 output of the second
switch is then the third input, while the 0 output of the switch following the middle switch gets the
fourth input, etc. Thus the two halves are interleaved in the Butterfly but not in the Delta, forming a
classic bowtie or butterfly pattern. However, even with this change, it is still easy to see that the same
principle is operative: outputs with MSB 0 go to the top half, while outputs with MSB 1 go to the
bottom.
     Because the Butterfly can be created from the Delta by renumbering inputs and outputs, the two
networks are said to be isomorphic. Butterflies were extremely popular in parallel computing (Culler et
al., 1999), gaining fame in the BBN Butterfly, though they seem to have lost ground to low-dimensional
meshes (see Section 13.19) in recent machines.
     There is also a small variant of the Butterfly, called the Banyan, that involves pairing the inputs
even in the first stage in a more shuffled fashion (the first input pairs with the middle input, etc.) before
following Butterfly connections to the second stage. Banyans enjoyed a brief resurgence in the network
community when it was noticed that if the outputs for each input are in sorted order, then the Banyan
can route without internal blocking. An important such switch was the Sunshine switch (Giacopelli
et al., 1991). Since sorting can be achieved using Batcher sorting networks (Cormen et al., 1990),
these were called Batcher-Banyan networks. Perhaps because much the same effect can be obtained
by randomization in a Benes or Clos network without the complexity of sorting, this approach has not
found a niche commercially.
     Finally, there is another popular network called the hypercube. The networks described so far use
d-by-d building block switches, where d is a constant such as 2, independent of the size of N . By
contrast, hypercubes use switches with log N links per switch. Each switch is assigned a binary address
from 1 to N and is connected to all other switches that differ from it in exactly one bit. Thus in a very
similar fashion to traversing a Delta or a Butterfly one can travel from an input switch to an output
switch by successively correcting the bits that are different between output and input addresses, in any
order. Unfortunately, the log N link requirement is onerous for large N and can lead to an “impractical
number of links per line card” (Semeria, 2002).

References
