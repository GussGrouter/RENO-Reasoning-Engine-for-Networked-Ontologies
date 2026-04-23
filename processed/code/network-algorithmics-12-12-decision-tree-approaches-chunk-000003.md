# network-algorithmics-12-12-decision-tree-approaches (chunk 000003)

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
