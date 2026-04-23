# Network Algorithmics — 16.4.1 Motivation and design objectives (slice)

- Source: raw/code/pdf/Network.Algorithmics.pdf
- Full-text extraction: processed/code/network-algorithmics-full-layout.txt
- Slice start: PDF page 484
- Slice: from `16.4.1 Motivation and design objectives` up to next detected section heading

---

16.4.1 Motivation and design objectives
While passive counters are good enough for many network monitoring applications, a number of other
applications require the maintenance of active counters, in which the values of counters need to be
read out as frequently as they are incremented, typically on a per packet basis. In many network data-
streaming algorithms (Cormode and Muthukrishnan, 2005; Estan and Varghese, 2002; Krishnamurthy
et al., 2003; Kumar et al., 2004b; Zhang et al., 2004; Zhao et al., 2005), upon the arrival of each packet,
values need to be read out from some counters to decide on actions that need to be taken; we will
provide a brief introduction to network data streaming and sketching in Section 16.15.
    A paper on approximate active counters (Stanojevic, 2007) identifies several other data-streaming
algorithms that need to maintain active counters, including multistage filters for elephant detection (Es-
tan and Varghese, 2002) and online hierarchical heavy hitter identification (Zhang et al., 2004). All these
data-streaming algorithms that use exact active counters implement them as full-size SRAM counters.
An efficient solution for exact active counters can significantly reduce SRAM cost for all such applica-
tions, as we will show next.
    BRICK (Bucketized Rank Index Counter) (Hua et al., 2008b) is an early solution to the problem
of efficiently maintaining exact active counters. BRICK allows extremely fast read and increment (by
1) accesses at on-chip SRAM speeds, yet is much more SRAM-efficient than the naive solution of
maintaining full-size SRAM counters, in the following sense.
    Suppose at the end of a measurement interval, the sum of the values of all N counters in the array,
which is equal to the total number of increments during the interval, is M. When the naive solution
is used, every SRAM counter has to be at least log2 M bits long since, in the worst case, all the
M increments can hit this counter. When BRICK is used, however, the average size of each SRAM
counter only needs to be slightly larger than log2 (M/N ) bits, the minimum length needed to encode

458      Chapter 16 Measuring network traffic




FIGURE 16.3
BRICK wall (conceptual baseline scheme) (Hua et al., 2008b).


the average counter value M/N. Hence, roughly speaking, BRICK pays the average cost (P11), not the
worst-case cost.
    We emphasize that the average cost log2 (M/N ) can be much smaller than the worst-case cost
log2 M. For example, let the total counts be M = 15 million and the number of counters be N =
1 million. In this case, the average cost log2 (M/N ) is only 4 bits, but the worst-case cost log2 M
is 24 bits, which is six times larger.


16.4.2 Overview of BRICK
The base idea of BRICK is intuitive and is based on a very familiar networking concept: statistical mul-
tiplexing. The idea is to first bundle groups of a fixed number (say 64) of counters, which is randomly
selected from the array, into buckets; then just enough bits are allocated to each counter in the sense
that, if its current value is Ci , log2 Ci  + 1 bits are allocated for storing the value. Therefore, counters
inside a bucket have variable widths.
     Suppose the mean width of a counter averaged over the entire array is γ . By the law of large
numbers, the total widths of counters in most of the buckets will be fairly close to γ multiplied by the
number of counters per bucket. Depicting each counter as a “brick,” as shown in Fig. 16.3, a section of
the “brick wall” illustrates the effect of statistical multiplexing, where each horizontal layer of bricks
(consisting of 64 of them) corresponds to a bucket and the length of bricks corresponds to the real
counter widths encoding flow sizes in a real-world Internet packet trace (the USC trace used in Hua et
al. (2008b)).
     As can be seen in this figure, when the bucket size is set to be slightly longer than 64γ (the vertical
dashed line), the probability of the total widths of the bricks overflowing over this line is quite small;
among the 20 buckets shown, only 1 of them has an overflow. Although overflowed buckets need to be
handled separately and will cost more memory, this probability can be made small so that the overall
overflow cost is small and bounded. Therefore, the memory consumption of BRICK only needs to be
slightly larger than 64γ per bucket, which is the optimal size (per bucket).
     This baseline approach is hard to implement in hardware in practice for two primary reasons. First,
the application (employing the active counter array) has to be able to randomly access (i.e., jump to)
any counter with ease. Since counters are of variable sizes, we have to store, for each counter, its
index within the bucket. Note that being able to randomly access is different from being able to delimit
all these counters. The latter can be solved with much less overhead using prefix-free coding (e.g.,

                                           16.4 Maintain active counters using BRICK                 459




FIGURE 16.4
Randomly bundling counters into buckets.


Huffman coding) of the counter values. But, in this case, to access the ith counter in a bucket, one has
to scan through the first i − 1 counters (and, hence, very slowly). Second, when the ith counter (brick)
in a bucket grows, counters i + 1, i + 2,..., 64 will have to be shifted.
    BRICK addresses these two difficulties with slightly more SRAM. It allows for very efficient read
and expansion (for increments that increase the width of a counter such as from 15 to 16). The op-
erations involved in reading and updating this data structure (based on the idea of rank indexing) not
only are simple for ASIC implementations but also are supported in modern processors through built-in
instructions (P4c) such as shift and popcount (Intel 64 and IA-32, 2007; AMD, 2007) so that soft-
ware implementation is efficient. For example, current generations of 64-bit ×86 processors have the
popcount instruction built-in (Intel 64 and IA-32, 2007; AMD, 2007), which is named “__builtin_pop-
count” and recognized by the GCC compiler on Linux.


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


ters”. The j th subcounter, j ∈ [1, p]
                                     (from     the least significant bits to the most significant bits) has
                                         p
wj bits, such that 0 < wj ≤ L and j =1 wj = L. To save space, for each counter, BRICK maintains
just enough of its subcounters to hold its current value. In other words, counters with values no more
than 2w1 +w2 +···+wi will not have its (i + 1)th, . . . , pth subcounters stored in BRICK. For example, if
w1 = 5, any counter with a value less than 25 = 32 will only be allocated a memory entry for its first
subcounter. Consider the example shown in Fig. 16.5(A) with k = 8 counters in a bucket. Only C1 and
C5 require more than their first subcounters. Such an on-demand allocation requires us to link together
all subcounters of a counter, which we achieve using a simple and memory-efficient bitmap indexing
scheme called rank indexing. Rank indexing enables efficient lookup and efficient expansion (when
counter values exceed certain thresholds after increments), which will be discussed in detail next.
    Each bucket contains p subcounter arrays A1 , A2 , . . ., Ap to store the 1st, 2nd, . . ., pth sub-counters
(as needed) of all k counters in the bucket. How many entries should be allocated for each array Ai ,
denoted as ki , turns out to be a nontrivial statistical optimization problem. On the one hand, to save
memory, we would like to make k2 , k3 , . . ., kp (k1 is fixed as k) as small as possible. On the other hand,
when we encounter the unlucky situation that we need to exceed any of these limits (say for a certain d,
we have more than kd counters in a bucket that have values larger than or equal to 2w1 +w2 +···+wi−1 ), then
we will have a “bucket overflow” that would require that all counters inside the bucket be relocated to
an additional array of full-size buckets with fixed worst-case width L for each counter. Given the high
cost of storing a duplicate bucket in the full-size array, we would like to choose larger k2 , . . . , kp to
make this probability as small as possible. For the example shown in Fig. 16.5(B), the allocation for
A1 , A2 , and A3 are k1 = k = 8, k2 = 3, and k3 = 1, respectively. Observe that the number of entries
is decreasing exponentially as we go to the higher subcounter arrays. In Hua et al. (2008b) extremely
tight tail bounds were developed on the overflow probability that can be used to guide the choosing of
parameters {ki }2≤i≤p and {wi }1≤i≤p−1 to achieve near-optimal tradeoffs between these two conflicting
issues and minimize the overall memory consumption.

Indexing for efficiently locating a counter
A key innovation in the BRICK data structure is an indexing scheme that allows for the efficient iden-
tification of the locations of the subcounters across the different subcounter arrays for some counter
Ci . In particular, for Ci , its d subcounters Ci,1 , . . . , Ci,d are spread across A1 , . . . , Ad at locations

                              16.5 Extending BRICK for maintaining associated states                       461



ai,1 , . . . , ai,d , respectively (i.e., Ci,j = Aj [ai,j ]). For example, as shown in Fig. 16.5(B), C5 is spread
across A3 [1] = 10, A2 [2] = 11, and A1 [5] = 11011.
     An index bitmap I is maintained for each bucket. I is divided into p − 1 parts, I1 , . . . , Ip−1 , with
a one-to-one correspondence to the subcounter arrays A1 , . . . , Ap−1 , respectively. Each part Ij is a
bitmap with kj bits, Ij [1], . . . , Ij [kj ], one bit Ij [a] for each entry Aj [a] in Aj . Each Ij [a] is used
to determine if the counter stored in Aj [a] has expanded beyond the j th subcounter array. Ij is also
used to compute the index location of Ci in the next subcounter array Aj +1 . Because a counter cannot
expand beyond the last sub-counter array, there is no need for an index bitmap component for the
most significant subcounter array Ap . For example, consider the entries A1 [1] and A1 [5] where the
corresponding counter has expanded beyond A1 . This is indicated by having the corresponding bit
positions I1 [1] and I1 [5] set to 1, as shown in shaded boxes in Fig. 16.5(B). All remaining bit positions
in I1 are set to 0, as shown in clear boxes.
     For each counter that has expanded beyond A1 , an arrow is shown in Fig. 16.5(B) that links a
subcounter in A1 with the corresponding subcounter entry in A2 . For example, for C5 , its subcounter
entry A1 [5] in A1 is linked to the subcounter entry A2 [2] in A2 . Rather than expending memory to store
these links explicitly, which could vanish savings gained by reduced counter widths, we dynamically
compute the location of a subcounter in the next subcounter array Aj +1 based on the current bitmap
Ij . In this way no memory space is needed to store link pointers. This dynamic computation can be
readily determined using an operation called rank(s, j ), which returns the number of ones only in the
range s[1] . . . s[j ] in the bit-string s (similar to the rank operator defined in Jacobson (1989)). The
rank operator in turn can be efficiently computed in software using the aforementioned popcount(s)
instruction, which returns the number of ones in the bit-string s.

Handling increments
The increment operation is also based on the traversal of subcounters using rank indexing. We will
first describe the basic idea by means of an example. Consider the counter C2 in Fig. 16.5(B). Its
count is 31, which can be encoded in just the subcounter array A1 with C2,1 = 11111. Suppose we
want to increment C2 . We first increment its first subcounter component C2,1 = 11111, which results
in C2,1 = 00000 with a carry propagation to the next level. This is depicted in Fig. 16.5(C).
    This carry propagation triggers the increment of the next subcounter component C2,2 . The location
of C2,2 can be determined using rank indexing (i.e. rank(I1 , 2) = 2). However, the location of A2 [2] was
previously occupied by counter C5 . To maintain rank ordering, we have to shift the entries in A2 down
by one to free up the location A2 [2]. This is achieved by applying an operation called varshift(s, j, c),
which performs a right shift on the substring starting at bit-position j by c bits (with vacant bits filled
by zeros). The varshift operator can be readily implemented in most processors by means of shift and
bitwise logical instructions.
