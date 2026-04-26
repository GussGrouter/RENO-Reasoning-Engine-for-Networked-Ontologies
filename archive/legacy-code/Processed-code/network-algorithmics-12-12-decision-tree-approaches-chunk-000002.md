# network-algorithmics-12-12-decision-tree-approaches (chunk 000002)

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
