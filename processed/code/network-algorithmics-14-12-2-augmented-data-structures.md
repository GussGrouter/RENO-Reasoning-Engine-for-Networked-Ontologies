# Network Algorithmics — 14.12.2 Augmented data structures (slice)

- Source: raw/code/pdf/Network.Algorithmics.pdf
- Full-text extraction: processed/code/network-algorithmics-full-layout.txt
- Slice start: PDF page 438
- Slice: from `14.12.2 Augmented data structures` up to next detected section heading

---

14.12.2 Augmented data structures
An augmented data structure, denoted as A, builds on a conventional data structure such as a binary
search tree, which we call a base data structure and denote as B. In B there is usually a set of logic
invariants IB associated with its data fields that need to be maintained when B is updated, using function
calls (or methods in object-oriented programming terms) of B. For example, when a new node is to be
inserted into a binary search tree, the point of insertion needs to be found (through a binary tree search),
and some other nodes may have to shifted up or down in the tree (called rotations in the algorithm
literature (Cormen et al., 2009)), so that the following invariant is maintained: when nodes are listed in
the in-order traversal order, the values of their search keys are monotonically increasing.
    An augmented data structure A usually contains several new data fields that are not a part of the
underlying base data structure B. There are logical invariants associated with these new data fields,
which we denote as IA\B , that need to be maintained when A is updated. However, since the methods
of B were programmed without the knowledge of these new data fields, they generally “have no respect
for” IA\B in the sense that, when called, these methods will likely destroy IA\B . For example, as
we will show in the next subsection, when insertions and deletions happen to an AVL tree (Adel’son-
Vel’skii and Landis, 1962) serving as the base data structure, the resulting rotations will damage the
invariants associated with the new data fields in the augmented data structure that builds on it. Hence, in
programming an augmented data structure A, we usually have to modify the implementations of some
methods inherited from B, to repair the damage to IA\B caused by these methods.

412       Chapter 14 Scheduling packets




FIGURE 14.21
Shape vis-a-vis Tree.

          14.12 The data structure and algorithm for efficient GPS clock tracking                      413




FIGURE 14.22
The “staircase” representation of the GPS graph shown in Fig. 14.16.


14.12.3 The “shape” data structure
In this section we focus on the design of the shape data structure proposed in Valente (2004) for tracking
the GPS clock. We first translate the GPS clock tracking problem into the aforementioned “binary
search-over-staircase” problem and then describe how the shape data structure solves the latter.

The staircase representation of GPS graph
The aforementioned staircase corresponds to a certain representation of the GPS graph at a certain real
time t. This representation is different than that used in Figs. 14.16–14.18 in three different ways. First,
we sort the order, from top to bottom, of the backlogged flows (at time t) according to the GPS virtual
finish time of the last packet in each flow (at time t). Second, we leave no vertical space between any
two “neighboring” flows, and hence the virtual finish times (sorted in increasing order), together with
the horizontal boundaries of these flows, form the contour of a staircase. Third, we omit all vertical
boundaries of neighboring packets in the same flow so that each flow looks like a “seamless slab” in the
graph. This omission is technically sound because these boundaries have no algorithmic significance in
the GPS clock tracking.
    We illustrate such a staircase GPS graph representation in Fig. 14.22, with the staircase (contour)
highlighted in bold. This graph corresponds to the GPS graph, at time t = 3 (after all seven packets
have arrived), of the packet arrival instance shown in Fig. 14.16. Flow F 1, whose last packet has the
earliest GPS virtual finish time of 8, is the first “slab” at the top. It is followed by F 2 and F 3, whose
GPS virtual finish times are 9 and 10, respectively.
    The staircase representation of the GPS graph allows us to “visualize” the flaw in the aforemen-
tioned timer-based O(1)-complexity solution to GPS clock tracking as follows. In any GPS graph
representation the line of current virtual time (i.e., virtual timeline) moves from left to right. The flawed
algorithm requires the leftmost step of the staircase to be removed, as a part of the aforementioned
cleanup operation, as soon as the virtual timeline has moved to the right of the vertical edge (“rise”)
of the step. In other words, the cleanup operation has to “walk down the stairs” as fast as the virtual
timeline moves. However, this requirement is problematic since a section of the staircase can be “pre-
cipitous” with as many as O(n) “tiny runs” that correspond to the aforementioned case of a tiny time
interval containing GPS finish times of the last packets of many backlogged flows.

414       Chapter 14 Scheduling packets



“Staircase query processing” by shape data structure
The shape data structure has three major design objectives. The first objective is to allow the cleanup
operation to lag far behind the progress of virtual timeline when needed, so that each cleanup can
be done, using Principle P2b, “at a convenient leisure time” (i.e., not under constant pressure by the
progress of the virtual timeline), and the overall cleanup operation incurs only O(log n) worst-case time
complexity in practice during any time interval. This objective, if achieved, would directly address the
flaw of having to “race down a precipitous staircase.” The second objective is to allow each evaluation
of V (t) (due to a “rude awakening” at time t) to incur O(log n) time complexity in the worst-case
despite that the cleanup operation may now lag far behind the virtual timeline. The third objective is
to allow a newly arrived flow (that caused a “rude awakening”) to have the GPS virtual finish time of
its first (which is at the moment also its last) packet inserted into the shape data structure in at most
O(log n) time. This operation corresponds to the aforementioned insertion of a new step (slab) into
the staircase as shown in Fig. 14.20. These three objectives correspond to the three aforementioned
requirements imposed on the “query over the staircase” computation problem, respectively.
     We are now close to finish translating the GPS clock tracking problem to the aforementioned “query
over the staircase” computation problem with the three requirements. The staircase in the latter problem
is precisely the staircase representation of the GPS graph in the former, at a real time t when the
corresponding virtual time V (t) needs to be computed. Each step in the staircase corresponds to a flow,
its height, the weight of the flow, and its x-coordinate the GPS virtual finish time of the last packet in
the flow. Those flows before the virtual timeline V (t) are no longer backlogged whereas those after are
backlogged at real time t.
     Suppose this staircase contains m steps (flows) whose x-coordinates (virtual times) in the increasing
order are v1 < v2 < · · · < vm , as shown in Fig. 14.21(a). We further assume that the previous packet
arrival (“rude awakening”) to any new flow happens at time t0 , and the corresponding virtual time
v0 = V (t0 ) is smaller than v1 , the earliest GPS finish time in the graph; this assumption will be relaxed
after we describe the shape data structure. With this assumption, v0 is the x-coordinate of the left edge
of the staircase, as shown in Fig. 14.21(a). This assumption has the following subtle implication: every
flow, say the ith flow (step) from the top in the GPS graph (staircase), was or is backlogged between v0
and vi . In other words, the entire area under the staircase is “solid” (i.e., without a gap in it). As a result,
the area under the staircase between the virtual timelines v0 and V (t) is equal to t − t0 . Therefore our
problem of computing V (t) is equivalent to the “query over the staircase” problem above (with t0 = 0
and v0 = V (t0 ) = 0).
     As mentioned earlier, the shape data structure is an augmented data structure. Its base data structure
is a balanced search tree, such as AVL (Adel’son-Vel’skii and Landis, 1962) or Red-Black (Cormen et
al., 2009), with one special stipulation: all keys are stored in the leaf nodes only. It is widely known that
this stipulation can be accommodated without increasing the asymptotic computational complexity of
(any method of) the data structure. For example, in a B+ tree (Elmasri and Navathe, 2010), all keys are
stored at the leaf nodes at the tree. For the staircase shown in Fig. 14.21(a), the tree contains exactly m
leaf nodes and the keys contained in these leaf nodes are exactly these m values. More precisely, if we
perform an in-order traversal of the tree and “print” only the keys of the leaf nodes, the output would
be exactly v1 , v2 , v3 , . . . , vm .
     In lieu of a key each internal node keeps track of the smallest and the largest key values, or in
other words, the range of the key values in the subtree rooted by it. This range of information serves
two purposes. First, in the absence of keys, internal nodes rely on this information to carry out binary

          14.12 The data structure and algorithm for efficient GPS clock tracking                          415



searches. For example, in the case of the insertion of a new leaf node with a certain key value, which
will be described in the next subsection, such range information guides the search down the tree to the
appropriate leaf position to insert. Second, the width of such a range, or more precisely the difference
between the two key values, is used for calculating an important quantity called area that is an additional
(w.r.t. the base data structure) data field of the augmented data structure. Since only leaf nodes contain
keys, the algorithmic steps for maintaining the balance of the tree, such as various rotation operations
(e.g., RR, RL, LR, LL rotations in an AVL tree), need to be suitably modified as in say B+ trees.

Detailed data structure design
We now describe the shape data structure. We do so recursively, since its base data structure, a balanced
binary search tree, is best explained recursively. The shape data structure, corresponding to the staircase
shown in Fig. 14.21(a), is shown in Fig. 14.21(b) with the details of the two top levels expanded and
the rest abbreviated. As explained earlier, the (entire) tree rooted by L0 contains m leaf nodes with
key values v1 , v2 , v3 , · · · , vm , respectively. Hence the (key) range of the root node L0 is (v0 , vm ] with
vk as the “middle” point of the range. This vk is roughly the “would-have-been” middle point in the
following sense: Had this tree been a usual binary balanced search tree in which every node, internal or
leaf, is associated with a key value, the root node L0 would have been associated with the key value vk ,
or something “close” in the rank order (e.g., vk−2 ).
     We now proceed to the next level of the tree. The range of its left child node L1 is (v0 , vk ], and
hence the left subtree contains k leaf nodes with key values v1 , v2 , ..., vk . The range of its right child
node L2 is (vk , vm ], and hence the right subtree contains m − k leaf nodes with key values vk+1 , vk+2 ,
..., vm . We do not name a middle point for either range since there are no such details in Fig. 14.21(b)
anyway. With this middle point field, the binary search over the binary search tree is straightforward:
compare the search key with the middle point (e.g., vk at L0 ), and then continue the search in either the
left or the right subtree accordingly.
     Now, we describe the three “augmentation” data fields in the shape data structure. To do so, we first
describe a specific objective we would like to achieve. The union of the solid-line-enclosed regions
(IV) and (V) corresponds to the shape information maintained at the root. We want to know if its area
is smaller or larger than t − t0 , the amount of real time that has elapsed since the last time the function
V (·) is evaluated (at time t0 ); the “equal to” case is trivial so we ignore it here and in the subsequent
discussions. The search shall continue in the left subtree in the case of “smaller than,” and in the right
subtree otherwise. While it may sound natural to include the quantity (IV) + (V) as a new data field,
from a data structure and algorithm design point of view, this quantity is hard to maintain in event
of the insertion or deletion of a leaf node. Instead, we maintain two other quantities from which this
quantity can be readily (i.e., in O(1) time) calculated. One such quantity is the area of the solid-line-
enclosed region (I), which is denoted W in the original paper (Valente, 2004). The other is the height
of the
      staircase, which is the total weight of flows F 1, F 2, ..., F k and hence is denoted as [1..m]
( m   i=1 i ) in Fig. 14.21(b). With a slight abuse of notation, we denote the area of region (IV) also
as (IV), and the area of region (I) also as (I), and so on. With this notational abuse, the relationship
between these three quantities ((I V ), [1..m], and (I )) is (I V ) = (vk − v0 ) ∗ [1..m] − (I ).
     The values of the base data structure field (key) range and the two augmented data structure fields
area and height, for the tree nodes L0 , L1 , and L2 , are shown in Fig. 14.21(b). The area associated
with the root node is L0 .area = (I ) + (I I ) + (I I I ). This area is used to calculate the area (VI) + (V),
which t − t0 should be compared against first (before it is compared against (I V ) if at all). Its (key)

416      Chapter 14 Scheduling packets



range is (v0 , vm ] (with vk as the “middle point”) as just explained, and the height of is area is clearly
                           three fields in its left child L1 are L1 .area = (I ), L1 .range = (v0 , vk ], and
[1..m]. The values of these
L1 .height = [1..k]  ki=1 i . Those in its right child L2 are L2 .area = (I I ), L2 .range = (vk , vm ],
                                     
and L2 .height = [(k + 1)..m]  m      i=k+1 i . It is not hard to check that the three fields values of L0 ,
L1 , and L2 satisfy the following three equations:

                       L0 .area = L1 .area + L2 .area + |L2 .range| ∗ L1 .height,                       (14.5)
                                           L0 .height = L1 .height + L2 .height,                        (14.6)
                                                                   
                                            L0 .range = L1 .range     L2 .range.                        (14.7)

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


manner: The algorithm shall not only map t to V (t) “upon request” but also output the value of the
area (III) + (IV) in Fig. 14.23. Hence, our “induction hypothesis” is that this logic held true at time t0 ,
i.e., the algorithm output both v0 = V (t0 ) and the value of area (III) at time t0 . Based on this “induction
hypothesis,” we now show how the revised algorithm delivers the extended logic (of outputting both
V (t) and (III) + (IV) at time t).
     Recall that we can query the shape data structure that encodes this staircase for the line V (t) such
that the area under the staircase between V (tc ) and V (t) is equal to (I) + (II). Since the staircase is
solid to the right of the V (t0 ) line (because there was no new flow arrival between t0 and t), we have
(I I ) = t − t0 . However, the area of (I) is not necessarily equal to t0 − tc because the area under the
staircase between tc and t0 is not necessarily solid. Instead, the area of (I) can be calculated as the
area of the enclosing rectangle ((v0 − vc ) ∗ [1..m]) minus (III), where (III) is known thanks to the
“induction hypothesis.” Hence, our algorithm is to query the staircase for the virtual timeline v such
that the area below the staircase between vc and v is (v0 − vc ) ∗ [1..m] − (I I I ) + t − t0 . As just
explained, the shape data structure can handle this query because it corresponds to the first situation.
This v is the value of V (t) that we are looking for. Once we obtain the value of V (t), the area of (IV)
can be calculated as (V (t) − v0 ) ∗ [1..m] − (t − t0 ). Now, we have obtained the value of (III) + (IV)
as promised, so the “induction proof” is complete.
Invariant maintenance under insertions and deletions
In this section we first describe the two method calls that would destroy the invariant of the augmented
data fields, namely an insertion or deletion of a flow record, and how to repair the invariant. We then
describe how the GPS clocking tracking operation would trigger the two method calls.

418      Chapter 14 Scheduling packets



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
