# network-algorithmics-16-4-1-motivation-and-design-objectives (chunk 000003)

16.4.3 Detailed design
Fig. 16.4 depicts the ideas of randomization and bucketization. In particular, as depicted in Fig. 16.4(A),
to access the yth counter, a pseudorandom permutation function π : {1. . .N } → {1. . .N } is first applied
to the index y to obtain a permuted index i. This pseudorandom permutation function in practice can be
as simple as reversing the bits of y. The corresponding counter Ci can then be found in the th bucket
B , where  = i/k and k is the number of counters per bucket. The bucket structure is depicted
in Fig. 16.4(B). Unless otherwise noted, when we refer to the ith counter Ci , we will assume i is
already the result of a random permutation.

Partition into subcounters
As we explained before, the baseline bucketing scheme does not allow for efficient read and incre-
ment (by 1) accesses. In BRICK, a multi-level partitioning scheme is designed to address this problem
as follows. The worst-case counter width L is divided into p parts, which we refer to as “subcoun-

460       Chapter 16 Measuring network traffic

FIGURE 16.5
(A) Within a bucket, segmentation of variable-width counters into subcounter arrays. (B) Compact representation of
variable-width counters. (C) Updated data structure after incrementing C2 .
