# network-algorithmics-14-12-2-augmented-data-structures (chunk 000007)

More generally, for any node and its two children, the values of these three fields in the trio satisfy
the three equations above. (The first equation corresponds to “Theorem 1” in Valente (2004) with “area”
replaced by “δW .”) These three equations are precisely the set of logic invariants to be satisfied by the
additional data fields of the augmented data structure. When “=” (equal) is replaced by “:=” in these
three equations, the three resulting assignment commands can be used for repairing any damage to
these invariants by certain “destructive” method calls to the base data structure, such as node insertions
and deletions. Such an “easy repair” explains why we should maintain areas (I), (II), and (III) instead
of areas (IV) and (V) in the augmented data structure.
    In presenting the augmented data structure (the three additional data fields) and the associated in-
variants, we pick a representation that is most convenient and provides the best possible clarity. This
representation, however, is awkward when we design and describe the “query over the staircase” algo-
rithm that runs on it. For example, with this representation, the algorithm starts at the root by checking
whether t − t0 < |L0 .range| ∗ L0 .height − L0 .area. If so, it proceeds to the left child L1 and checks
whether t − t0 < |L1 .range| ∗ L0 .height − L1 .area. If the answer is no (and equality is ruled out),
then the algorithm has to proceed to the sibling node L2 (by backtracking first to the parent node L0 )
and then to L1 s left child for the next (binary search) comparison, which is awkward (but not flawed
since the time complexity of the binary search remains O(log n)). Hence, to facilitate a clean algorithm
design, we let a parent node “lease” (cache) the values, in both its children, of these three data fields
so that the second comparison above can be performed at L0 instead of at L1 . With this “leasing,” the
binary search here can proceed in the usual way of traveling down from the root to a leaf without “going
up” (backtracking).
    The left edge of the staircase corresponds to the GPS finish time of the (last) packet whose flow
record was deleted from the shape data structure during the most recent cleanup operation. How the
logic invariant of the shape (augmented) data structure is repaired in the event of such a cleanup will be
discussed shortly. So far, we assume that v0 < v1 so that the binary search (for the V (t) line) starts from
exactly the left edge of the staircase. In practice, we almost certainly would encounter the situation of
v0 > v1 , since as explained earlier, the very purpose of the shape data structure is to allow the timeline
of the cleanup to lag far behind the V (t) line (and hence the time t0 at which the function V (·) was last
evaluated).
    We now describe the second situation of v0 > v1 (we still have v1 < v2 < ... < vm ), as shown in
Fig. 14.23. To tackle this situation, we need to make two changes to the algorithm logic. First, we
replace every occurrence of v0 in the range fields (of the tree nodes) with vc = V (tc ), where vc and
tc are the virtual and the real times of the last cleanup operation, respectively. For example, the range
of L0 is now (vc , vm ] instead of (v0 , vm ]. Second, the algorithmic logic is extended in the following

14.12 The data structure and algorithm for efficient GPS clock tracking                      417

FIGURE 14.23
Data structure (after arrival).
