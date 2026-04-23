# network-algorithmics-14-12-2-augmented-data-structures (chunk 000009)

We describe only the insertion operation, as the deletion operation is similar. The insertion of a
node is handled first by the based data structure that is a balanced binary search tree. Note that in our
special case where all keys are stored at the leaves, the inserted node must be a leaf node. In a balanced
binary search tree such as AVL or red-black insertion of a new leaf node would trigger a series of
rotations (e.g., of types LL, LR, RL, and RR in AVL) that first travel up the tree and then possibly
travel down (but not necessarily all the way down to another leaf). This would destroy the invariants of
the augmented data fields in the set of nodes S affected by the rotations and the path from the lowest
common ancestor of nodes in S to the root of the tree. Hence we need to repair this invariant for all
nodes along this “trail of destruction.” Since it is known that, in balanced tree data structures such as
AVL or red-black, the total number of nodes in S and the height of the tree are both O(log n), the time
complexity of the invariant repair operation is O(log n).
    Finally, we describe how insertions and deletions are triggered by GPS clock tracking operations.
There are three different ways in which insertions and deletions can happen. First, each cleanup opera-
tion results in a leaf node with the smallest key value that corresponds to the lower-leftmost leaf in the
binary search tree being deleted. Second, a new flow arrival at time t, as shown in Fig. 14.20, would
result in a “staircase query” for computing V (t), the GPS virtual start time of the first packet of this
flow. Its GPS virtual finish time needs to be inserted into the shape data structure. Third, a new packet
arrival, say pi,k+1 (the (k + 1)th packet in the ith flow Fi ) to an existing (i.e., currently backlogged)
flow Fi at time t, would result in both an insertion (of the leaf node keyed by fi,k+1 , the GPS virtual
finish time of pi,k+1 ) and a deletion (of the leaf node keyed by fi,k , the GPS virtual finish time of the
previous packet pi,k ), in addition to a “staircase query” for computing V (t). Note that in this case we
must have V (t) < fi,k since otherwise Fi is not backlogged at time t.
    We note that, in real-world operations, the WFQ scheduler can usually “get away with” not perform-
ing any cleanup operation for the following reason. The utilization level of the link to be scheduled is
usually much less than 100%. In this case a busy period (of the combined queue for the link) is usually
not very long in duration, and hence the number of leaf nodes in the binary search tree is not going to
be large enough to start causing trouble (e.g., exceed the available memory or make the tree “too tall”).
Then, “throwing away” (e.g., by making “memset” + “free” systems calls) the whole augmented data
structure at the end of a busy period will do the trick. Conceivably, this “laid back” approach to cleanup
can considerably reduce cleanup time in real-world operations.
