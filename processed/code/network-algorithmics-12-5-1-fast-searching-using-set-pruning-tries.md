# Network Algorithmics — 12.5.1 Fast searching using set-pruning tries (slice)

- Source: raw/code/pdf/Network.Algorithmics.pdf
- Full-text extraction: processed/code/network-algorithmics-full-layout.txt
- Slice start: PDF page 332
- Slice: from `12.5.1 Fast searching using set-pruning tries` up to next detected section heading

---

12.5.1 Fast searching using set-pruning tries
Consider the two-dimensional rule set in Fig. 12.3. The simplest idea is first to build a trie on the des-
tination prefixes in the database and then to hang a number of source tries off the leaves of the
destination trie. Fig. 12.4 illustrates the construction for the rules in Fig. 12.3. Each valid prefix in
the destination trie points to a trie containing some source prefixes. The question is: Which source
prefixes should be stored in the source trie corresponding to each destination prefix?
    For instance, consider D = 00∗. Both rules R4 and R5 have this destination prefix, and so the trie
at D clearly needs to store the corresponding source prefixes 1∗ and 11∗. But storing only these source
prefixes is insufficient. This is because the destination prefix 0∗ in rules R1 , R2 , and R3 also matches
any destination that D matches. In fact, the wildcard destination prefix ∗ of R7 also matches what-
ever D matches. This suggests that the source trie at D = 00 must contain the source prefixes for
{R1 , R2 , R3 , R4 , R5 , R7 }, because these are the set of rules whose destination is a prefix of D.
    Fig. 12.4 shows a schematic representation of this data structure for the database of Fig. 12.3. Note
that S1 denotes the source prefix of rule R1 , S2 of rule R2 , and so on. Thus each prefix D in the
destination trie prunes the set of rules from the entire set of rules down to the set of rules compatible

306       Chapter 12 Packet classification




FIGURE 12.4
The set-pruning trie data structure in two dimensions corresponding to the database of Fig. 12.3. Destination trie is
a trie for the destination prefixes. The nodes corresponding to a valid destination prefix in the database are shown as
filled circles; others are shown as empty circle. Each valid destination prefix D has a pointer to a trie containing the
source prefixes that belong to rules whose destination field is a prefix of D.


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
