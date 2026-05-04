# network-algorithmics-16-2-reducing-sram-width-using-dram-backing-store (chunk 000003)

This leaf structure can be augmented with a simple tree that maintains the position of the first 1 (see
the end-of-chapter exercises). The tree can be easily pipelined for speed, and only roughly 2 bits per
counter are required for this additional data structure; thus c is increased from its optimal value, say, x
to x + 2, a reasonable cost.
    Thus, the final LR algorithm is a better algorithm (P15) and one that is easier to implement, provides
a new data structure to efficiently find the first bit set in a bitmap (P15), and adds pipelining hardware
(P5) to gain speed.
    The overall approach could be considered superficially similar to the usual use of the memory hier-
archy, in which a faster memory acts as a cache for a slower memory. However, unlike a conventional
cache, this design ensures worst-case performance and not expected case performance. The goals of the
two algorithms are also different: Counter management stores an entry for all items but seeks to reduce
the width of cache entries, while standard caching stores full widths for only some frequent items.
