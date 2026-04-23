# network-algorithmics-12-14-conclusions-this-chapter-describes-several-algorithms-for-packet-classif (chunk 000002)

the same number of rules as the Lucent scheme but perhaps can be improved to lower its memory
consumption.
    The author and his students have placed code for many of the algorithms described in this chapter
on a publicly available Web site (Singh et al., 2004a). Packet classification has stagnated because of
the lack of standard comparisons and freely available code. Readers are encouraged to experiment with
and contribute to this code base.
    Although the schemes described in this chapter require some algorithmic thinking, they make heavy
use of the other principles we have stressed. The two-dimensional scheme makes heavy use of precom-
putation; the Lucent scheme uses memory locality to turn what is essentially linear search into a fast
scheme for moderate rule sizes; all the other schemes rely on some expected-case assumption about
the structure of rules, such as the lack of general ranges and the small number of classification regions.
Table 12.1 summarizes the schemes and the principles used in them.
    Because the best-matching prefix is a special case of the lowest-cost matching rule, it is not sur-
prising that rule search schemes are generalizations of prefix search schemes. Thus, the grid of tries
and set-pruning tries generalize trie schemes for prefix matching. Multidimensional range-matching
schemes generalize prefix-matching schemes based on range matching. Tuple search generalizes binary
search on hash tables. While cross-producting is not a generalization of an existing prefix-matching
scheme, it can also be specialized for prefix lookups.
    The high-level message of this chapter is as follows. Applications such as QoS routing, firewalls,
virtual private networks, and DiffServ require a more flexible form of forwarding based on multiple
header fields. The techniques in this chapter indicate that such forwarding flexibility can go together
with high performance using algorithmic solutions without relying on ternary CAMs.
    Returning to the quote at the start of this chapter, it should be easy to see how packet classification
gets its name if the word definition is replaced with rule. Notice that classification in the sciences also
encompasses overlapping definitions: Men belong to both the mammal and Homo sapiens categories.
However, it is hard to imagine a biological analog of the concept of a lowest-cost matching rule, or the
requirement to classify species several million times a second!
