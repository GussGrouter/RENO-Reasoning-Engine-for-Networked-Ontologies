# network-algorithmics-16-4-1-motivation-and-design-objectives (chunk 000002)

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
