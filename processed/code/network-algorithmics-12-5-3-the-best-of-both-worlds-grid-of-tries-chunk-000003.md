# network-algorithmics-12-5-3-the-best-of-both-worlds-grid-of-tries (chunk 000003)

trie. Let T (D) denote the source trie pointed to by D. Recall that T (D) contains the source fields of
exactly those rules whose destination field is D.
    Let u be a node in T (D) that fails on bit 0; that is, if u corresponds to the source prefix s, then the
trie T (D) has no string starting with s0. Let D  be the lowest ancestor of D whose source trie contains
a source string starting with prefix s0, say, at node v. Then we place a switch pointer at node u pointing
to node v. If no such node v exists, the switch pointer is nil. The switch pointer for failure on bit 1 is
defined similarly. For instance, in Fig. 12.7, the node labeled x fails on bit 0 and has a switch pointer to
the node labeled y.
    As a second example, consider the packet header (00∗, 10∗). Search starts with the first source trie,
pointed to by the destination trie node 00∗. After matching the first source bit, 1, search encounters rule
R4 . But then search fails on the second bit. Search therefore follows the switch pointer, which leads
to the node in the second trie labeled with R1 . The switch pointers at the node containing R1 are both
nil, and so search terminates. Note, however, that search has missed the rule R3 = (0∗, 1∗), which also
matches the packet header. While in this case R3 has a higher cost than R1 , in general, the overlooked
rule could have a lower cost.
    Such problems can be avoided by having each node in a source trie maintain a variable storedRule.
Specifically, a node v with destination prefix D and source prefix S stores in storedRule(v) the least-cost
rule whose destination field is a prefix of D and whose source field is a prefix of S. With this precom-
putation, the node labeled with R1 in Fig. 12.7 would store information about R3 instead of R1 if R3
had a lower cost than R1 .
    Finally, here is an argument that the search cost in the final scheme is at most 2W . The time to find
the best destination prefix is at most W . The remainder of the time is spent traversing the source tries.
However, in each step, the length of the match on the source field increases by 1—either by traversing
further down in the same trie or by following a switch pointer to an ancestral trie. Since the maximum
length of the source prefixes is W , the total time spent in searching the source tries is also W . The
memory requirement is O(N W ), since each of the N rules is stored only once, and each rule requires
O(W ) space.
    Note that k-bit tries (Chapter 11) can be used in place of 1-bit tries by expanding each destination or
source prefix to the next multiple of k. For instance, suppose k = 2. Then, in the example of Fig. 12.7,
the destination prefix 0∗ of rules R1 , R2 , R3 is expanded to 00 and 01. The source prefixes of R3 , R4 ,
R6 are expanded to 10 and 11. Using k-bit expansion, a single prefix can expand to 2k−1 prefixes. The
total memory requirement grows from 2N W to N W 2k /k, and so the memory increases by the factor
2k−1 /k. On the other hand, the depth of the trie reduces to W/k, and so the total lookup time becomes
O(W/k).
    The bottom line is that by using multibit tries, the time to search for the best matching rule in an
arbitrarily large two-dimensional database is effectively the time for two IP lookups.
    Just as the grid of tries represents a generalization of familiar trie search for prefix matching, there is
a corresponding generalization of binary search on prefix lengths (Chapter 11) that searches a database
of two field rules in 2W hashes, where W is the length of the larger of the two fields. This is a big gap
from the log W time required for prefix matching using binary search on prefix lengths. In the special
case where the rules do not overlap, the search time reduces even further to log2 W , as shown in Suri
et al. (2001). While these results are interesting theoretically, they seem to have less relevance to real
routers, mostly because of the difficulties of implementing hashing in hardware.
