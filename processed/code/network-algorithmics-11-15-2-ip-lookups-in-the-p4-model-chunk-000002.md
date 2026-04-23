# network-algorithmics-11-15-2-ip-lookups-in-the-p4-model (chunk 000002)

Mashup is based on a technique called “tiling trees”. In other words, Mashup takes into account the
internal grain sizes of TCAMs when building a lookup tree. Note that TCAMs come in units, with a
grain size of W (width) by D (depth) like memory pages. The Tofino-3, for example, has W = 44 and
D = 512. Each unit TCAM or block in Tofino-3 can do a longest match on up to 512 prefixes of up to
44 bits (any of which can be the wilcard *) in a single clock cycle. For example, to fit the current IPv6
database size of 150,000 prefixes of up to 64 bits, the straightforward approach is to stitch together
2 TCAM blocks horizontally (64<88) and 300 of these pairs vertically (150, 00/512 is approximately
300).
    By contrast, MashUp builds a tree of TCAM blocks starting with a root which can fit (in other
words is “tiled”) into a TCAM block. This breaks up the bit-by-bit branching tree (trie) of prefixes into
subtrees which we can recursively tile. To pick the tree level at which to define the root TCAM, observe
that the tree has pointers, which represent “overhead” not present in a single logical CAM.
    The first idea is to reduce pointer overhead by cutting the trie into subtries at heights (which they call
lean lengths) where the number of downstream pointers are small. For example, the paper (Rios and
Varghese, 2022) shows that for a public wide area IPv6 database, the pointer overhead is only 0.41%
of total database size at height 20 but rises to 6.84% at height 32.
    The second idea is to reduce the wasted space of tiled subtrees by packing up to D subtrees in
a single TCAM block. Because the remaining prefix bits may repeat across different subtrees, this
requires adding a disambiguating tag of log2 D bits. Despite this additional cost, packing ensures that
any wasted space (which can be as large as a unit TCAM) in the last block is amortized over D subtrees.
In other words, Mashup packs subtrees into a single TCAM block to reduce internal fragmentation.
    The third idea is to do a “currency exchange” where “nearly full” subtrees are replaced by SRAM
pages in a process the authors call “RAM hybridization”. Since SRAM cannot do variable length match-
ing, this must be remedied by “expanding” variable length prefixes to the maximum length prefix in
the subtree. Hybridization allows currency “arbitrage” because SRAM pages are cheaper and more
plentiful than TCAM blocks (3 to 1 in Tofino-3).
    The Mashup paper shows results for IPv4 database sizes of 900k prefixes using all three techniques:
lean lengths, tag aggregation and RAM hybridization. A four stage tree with strides of 16-4-4-8 reduces
TCAM bits by 7× compared to the straightforward solution of using a single logical CAM, at the cost
of around 1000 SRAM pages, which is much less than the RAM required for an all RAM solution.
More details can be found in the Mashup paper (Rios and Varghese, 2022).
