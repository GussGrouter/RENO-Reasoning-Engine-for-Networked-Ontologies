# network-algorithmics-11-16-conclusions-it-is-important-to-gain-some-perspective-after-the-large-num (chunk 000002)

like Mashup Rios and Varghese (2022) can remedy that). Thus many core router vendors such as
Arista (Arista Corporation, 2010) still use and design algorithmic schemes for lookups based on RAM.
   For hardware schemes without CAM at Terabit speeds in the core, Tree Bitmap still seems appropri-
ate even after so many years. However, there may be patents that restrict the use of Tree bitmap. This
may make other bitmap schemes such as Poptrie (Asai and Ohara, 2015) attractive. Tree bitmap was
used in Cisco’s CRS-1 Router. On the other hand, ideas based on simplified SAIL (Yang et al., 2014)
(as described earlier) may be appropriate for hardware settings that use cheap and plentiful off-chip
DRAM.
   For data centers and enterprise networks, there seems to be adequate CAM in chips like the Tofino-3,
especially when leveraged (as in schemes like Mashup (Rios and Varghese, 2022)) to reduce power and
TCAM bits.
   For software implementations, the DXR scheme (Zec et al., 2012) seems to be the best approach
today especially in the context of Network Function Virtualization (NFV). The underlying binary-
search-on-ranges scheme allows efficient multithreading whose throughput scales with the number of
cores and fits into the L1 cache. It is also unencumbered by patents.
   Finally, binary search on prefix lengths is attractive because of its scaling properties to large address
lengths. Unfortunately, its use of hashing makes it hard to guarantee lookup times. It is, however, used
by a few vendors in software implementations. It may be a contender in the future as IPv6 becomes
more dominant.
   The bottom line is that algorithmic solutions together with pipelining can scale with link speeds as
long as SRAM speeds scale to match packet arrival times. All the schemes studied in this chapter can be
pipelined to provide one lookup per memory access time. The choice between CAMs and algorithmic
schemes will continue to be hard to quantify and will probably be made on an ad hoc basis for each
product.
   Fundamentally, if compressed trie schemes can use less than 32 bits per prefix, compressed tries
can use fewer transistors and less power than CAMs. This is because in a CAM the lookup logic is
distributed in each of N memory cells, whereas in an algorithmic solution the lookup logic, albeit more
complicated, is distributed among a small, constant number of stages. A careful VLSI scaling analysis
of these two approaches would be very useful.
   Underlying Principles: Although this is a chapter about lookups and thinking about lookups requires
paying attention to current market trends, it is important not to forget that this is a book about underlying
principles. It is plausible that routers in the misty future may use all-optical switches and all-optical
processing, even for lookups. In that case, the specific algorithms described in this chapter may be
discarded; but perhaps the underlying design principles will remain.
   All of the schemes described in this chapter start with the algorithmic principle of divide and conquer
(divide by bits in the address, address ranges, or prefix lengths) but gain efficiency by other principles.
First, most schemes use precomputation, which trades slower insert/delete times for fast search times.
The schemes also exploit hardware features such as wide memories, leverage fast and slow memories,
trade memory for time, and optimize the degrees of freedom in a given design. Table 11.1 summarizes
some of the schemes and the principles used in them. Many of them also use what we could call
information-preserving transformations. For example, replacing a sequence of one-way branches with
a text string, or representing a prefix as a start and end of range.
   Finally, this chapter cannot hope to do justice to all the interesting IP lookup schemes that have been
published in the academic and patent literature. You can look it up.

11.17 Exercises          291
