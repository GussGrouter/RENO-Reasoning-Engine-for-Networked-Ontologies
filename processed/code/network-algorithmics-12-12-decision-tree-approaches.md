# Network Algorithmics — 12.12 Decision tree approaches (slice)

- Source: raw/code/pdf/Network.Algorithmics.pdf
- Full-text extraction: processed/code/network-algorithmics-full-layout.txt
- Slice start: PDF page 350
- Slice: from `12.12 Decision tree approaches` up to next detected section heading

---

12.12 Decision tree approaches
This chapter ends with a description of a very simple scheme that performs well in practice, better even
than RFC and comparable to or better than the extended grid of tries. This scheme was introduced by
Woo (2000). A similar idea, with range tests replacing bit tests, was independently described by Gupta
and McKeown (1999b).
    The basic idea is extremely close to the simple set-pruning tries described in Section 12.5.1, with
the addition of some important degrees of freedom. Recall that set-pruning tries work one field at a
time; thus in Fig. 12.7, the algorithm tests all the bits for the destination address before testing all the
bits for the source address. The extension to multiple fields in Decasper et al. (1998) similarly tests all
the bits of one field before moving on to another field. The set-pruning trie can be seen as an instance
of a general decision tree.
    Clearly, an obvious degree of freedom (P13) not considered in set-pruning tries is to arbitrarily
interleave the bit tests for all fields. Thus the root of the trie could test for (say) bit 15 of the source field;
if the bit is 0, this could lead to a node that tests for, say, bit 22 of the port number field. Clearly, there
is an exponential number of such decision trees. The schemes in Woo (2000) and Gupta and McKeown
(1999b) build the final decision tree using local optimization decisions at each node to choose the next
bit to test. A simple criterion used in Gupta and McKeown (1999b) is to balance storage and time.
    A second important degree of freedom considered in Woo (2000) is to use multiple decision trees.
For example, for examples such as Fig. 12.5, it may help to place all the rules with wildcards in the
source field in one tree and the remainder in a second tree. While this can increase overall search time,
it can greatly reduce storage.
    A third degree of freedom exploited in both Woo (2000) and Gupta and McKeown (1999b) is to
allow a small amount of linear searching after traversing the decision tree. This is similar to the common
strategy of using an insert. Consider a decision tree with 10,000 leaves where each leaf is associated
with one of four rules. While it may be possible to distinguish these four rules by lengthening the
decision tree in height, this lengthened decision tree could add 40,000 extra nodes of storage.

324       Chapter 12 Packet classification




FIGURE 12.15
The HiCuts data structure is essentially a range tree that has pointers corresponding to some ranges of some dimen-
sion variable with linear search at the end.

    Thus, in balancing storage with time, it may be better to settle for a small amount of linear searching
(e.g., among one of four possible rules) at the end of tree search. Intuitively, this can help because the
storage of a tree can increase exponentially with its height. Reducing the height by employing some
linear search can greatly reduce storage.
    The hierarchical cuttings (HiCuts) scheme described in Gupta and McKeown (1999b) is similar in
spirit to that in Woo (2000) but uses range checks instead of bit tests at each node of the decision tree.
Range checks are slightly more general than bit tests because a range check such as 10 < D < 35 for a
destination address D cannot be emulated by a bit test. A range test (cut) can be viewed geometrically
in two dimensions as a line in either dimension that splits the space into half; in general, each range cut
is a hyperplane.
    In what follows, we describe HiCuts in more detail using an example. The HiCuts local optimization
criterion works well when tested on real core router classifiers.
    Fig. 12.15 shows a fragment of a HiCuts decision tree on the database of Fig. 12.2. The nodes
contain range comparisons on values of any specified fields, and the edges are labeled True or False.
Thus the root node tests whether the destination port field is less than 50. The fragment follows the case
only when this test is false. Notice in Fig. 12.2 that this branch eliminates R1 (i.e., Rule 1) and R4,
because these rules contain port numbers 25 and 23, respectively.
    The next test checks whether the source address is equal to that of the secondary name server S in
Fig. 12.2. If this test evaluates to true, then R5 is eliminated (because it contains T O), and so is R6
(because it contains N et and because S does not belong to the internal prefix N et). This leads to a
second test on the destination port field. If the value is not 53, the only possible rules that can match are
R7 and R8.

                                                          12.12 Decision tree approaches                325



    Thus on a packet header in which the destination port is 123 and the source is S, the search algorithm
takes the right branch at the root, the left branch at the next node, and a right branch at the final node. At
this point, the packet header is compared to rules R7 and R8 using linear search. Note that, unlike set
pruning trees, the HiCuts decision tree of Fig. 12.15 uses ranges, interleaves the range checks between
the destination port and source fields, and uses linear searching.
    Of course, the real trick is to find a way to build an efficient decision tree that minimizes the worst-
case height and yet has reasonable storage. Rather than consider the general optimization problem,
which is NP-complete, HiCuts (Gupta and McKeown, 1999b) uses a more restricted heuristic based on
the repeated application of the following greedy strategy.
• Pick a field: The HiCuts paper suggests first picking a field to cut on at each stage based on the
  number of distinct field values in that field. For example, in Fig. 12.15, this heuristic would pick the
  destination port field.
• Pick the number of cuts: For each field, rather than just pick one range check as in Fig. 12.15, one can
  pick k ranges or cuts. Of course, these can be implemented as separate range checks, as in Fig. 12.15.
  To choose k, the algorithm suggested in Gupta and McKeown (1999a) is to keep doubling k and to
  stop when the storage caused by the k cuts exceeds a prespecified threshold.
    Several details are needed to actually implement this somewhat general framework. Assuming the
cuts or ranges are equally spaced, the storage cost of k cuts on a field is estimated by counting the sum
of the rules assigned to each of the k cuts. Clearly, cuts that cause rule replication will have a large
storage estimate. The threshold that defines acceptable storage is a constant (called spfac, for space
factor) times the number of rules at the node. The intent is to keep the storage linear in the number of
rules up to a tunable constant factor.
    Finally, the process stops when all decision tree leaves have no more than binth (bin threshold)
rules. binth controls the amount of linear searching at the end of tree search.
    The HiCuts paper (Gupta and McKeown, 1999b) mentions the use of the DAG optimization. A more
novel optimization, described in Woo (2000) and Gupta and McKeown (1999b), is to eliminate a rule,
R, that completely overlaps another rule, R  , at a node but has a higher cost. There are also several
further degrees of freedom (P13) left unexplored in Gupta and McKeown (1999b) and Woo (2000):
unequal-size cuts at each node, more sophisticated strategies that pick more than field at a time, and
linear searching at nodes other than the leaves.
    HiCuts has inspired several follow-up papers that make improvements to the basic idea. First, in
HyperCuts (Singh et al., 2004a) the decision tree approach is taken a step further by allowing the use
of several cuts in a single step. If the cuts in each dimension are a power of two as well, lookup can be
done in a single step via multidimensional array indexing. Once again this is an extra degree of freedom
(P13) being exploited. Because each cut is now a general hypercube, the scheme is called HyperCuts.
HyperCuts works significantly faster than HiCuts on many real databases (Singh et al., 2004a).
    Finally, Efficuts (Vamanan et al., 2010) adds another degree of freedom by using what they call
“equidense cuts”: the cuts are not of equal size but instead distribute the child pointers evenly among
cuts. They do this by selectively merging equal size cuts in HyperCuts to save memory. Of course, the
tradeoff is that lookup is slightly slower because simple array indexing can no longer work. To further
reduce redundancy in the data structure, EffiCuts exploits the degree of freedom first considered in Woo
(2000) to create mutually exclusive sets of rules and creates multiple decision trees for each such set,

326      Chapter 12 Packet classification



with different heuristics to achieve a good trade-off between number of trees (lookup time) and storage
(redundancy).
     Using a publicly available benchmark of synthetic and other classifiers called ClassBench (Taylor
and Turner, 2007), the authors show that for comparable performance EffiCuts needs 57 times less
memory than HyperCuts and 4-8 times less power than a TCAM. The last experiment is notable because
unlike earlier papers that informally claimed that algorithmic schemes used less power than TCAMs,
this is one of the few papers to quantify the comparison using a hardware model called CACTI (Wilton
and Jouppi, 1996) to model CAM and RAM. However, the benchmarks used (Taylor and Turner, 2007)
are mostly synthetic ones; thus a more modern benchmark of real classifiers would be ideal to compare
all these schemes.
     HiCuts, HyperCuts, and Efficuts all use manually created heuristics to build decision trees – in other
words, to decide how to partition rules among multiple trees and how to perform cuts at each node in
a tree. A later paper, NeuroCuts (Liang et al., 2019), further advances the state-of-the-art in decision
trees by using Reinforcement Learning. First, note that using a neural network for classification, is
problematic because a neural classification network cannot guarantee correct results (the answers are
correct only with high probability). Further, neural networks are resource intensive, making it hard to
guarantee results in time to forward a packet. Instead, NeuroCuts uses deep Reinforcement Learning
to build efficient decision tree, pushing the cost of the neural network to the time when new rules are
added to the classifier.
     Thus, while previous approaches attempt to heuristically meet performance objective (e.g., reduce
storage), Reinforcement Learning explicitly maximizes the given performance objective. Fortunately,
the learning time to evaluate a large number of models, which is one of main drawbacks of RL, is
not very high for packet classification. Using synthetic workloads generated using ClassBench, the
authors (Liang et al., 2019) show that NeuroCuts outperforms existing hand-tuned decisions in both
classification time and memory footprint. More specifically, NeuroCuts improves median classification
time by 18%, and reduces both time and memory usage by up to a factor of 3.
     In conclusion, the decision tree approach described by (Woo, 2000), (Gupta and McKeown, 1999b),
(Singh et al., 2004a), (Vamanan et al., 2010) and (Liang et al., 2019) is best viewed as a framework that
encompasses a number of potential algorithms. However, experimental evidence (Singh et al., 2004a;
Vamanan et al., 2010) shows that this approach works well in practice. The performance of this scheme
can be summarized as follows.
Assumption: The scheme assumes there is a sufficient number of distinct fields to make reasonable
      cuts without much storage replication. This rather general observation needs to be sharpened.
Performance: The memory required can be kept to roughly linear in the number of rules using var-
      ious heuristics. The tree can be of relatively small height if it is reasonably balanced. Search
      can easily be pipelined to allow O(1) lookup times. Finally, the updates are likely to be slow if
      sophisticated heuristics are used to build the decision tree.
