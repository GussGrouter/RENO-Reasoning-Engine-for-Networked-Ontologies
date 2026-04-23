# network-algorithmics-12-5-1-fast-searching-using-set-pruning-tries (chunk 000002)

with D. The same idea can be extended to more than two fields, with each field value in the path pruning
the set of rules further.
    In this trie of tries, the search algorithm first matches the destination of the header in the destination
trie. This yields the longest match on the destination prefix. The search algorithm then traverses the
associated source trie to find the longest source match. While searching the source trie, the algorithms
keep track of the lowest-cost matching rule. Since all rules that have a matching destination prefix are
stored in the source trie being searched, the algorithm finds the correct least-cost rule. This is the basic
idea behind set-pruning trees (Decasper et al., 1998).
    Unfortunately, this simple extension of tries from one to two dimensions has a memory-explosion
problem. The problem arises because a source prefix can occur in multiple tries. In Fig. 12.4 for in-
stance, the source prefixes S1, S2, S3 appear in the source trie associated with D = 00∗ as well as the
trie associated with D = 0∗.
    How bad can this replication get? A worst-case example forcing roughly N 2 memory is created
using the set of rules shown in Fig. 12.5. The problem is that since the destination prefix ∗ matches any
destination header, each of the N/2 source prefixes is replicated N/2 times, one for each destination
prefix. The example (see exercises) can be extended to show a O(N K ) bound for general set-pruning
tries in K dimensions.
    While set-pruning tries do not scale to large classifiers, the natural extension to more than two fields
has been used in Decasper et al. (1998) as part of a router toolkit, and in Malan and Jahanian (1998)
as part of a flexible monitoring system. The performance of set-pruning tries is also studied in Qiu et
al. (2001). One interesting optimization introduced in Decasper et al. (1998) and Malan and Jahanian
(1998) is to avoid obvious waste (P1) when two subtries S1 and S2 have exactly the same contents. In
this case, one can replace the pointers to S1 and S2 with a pointer to a common subtrie, S. This changes
the structure from a tree to a directed acyclic graph (DAG). The DAG optimization can greatly reduce

12.5 Two-dimensional schemes                        307

FIGURE 12.5
An example forcing N 2 /2 memory for two-dimensional set-pruning trees. Similar examples, which apply to a
number of other simple schemes, can be used to show O(N K ) storage for K-dimensional rules.

storage for set-pruning tries (see Qiu et al., 2001 for other, related optimizations) and can be used to
implement small classifiers, say, up to 100 rules, in software.
