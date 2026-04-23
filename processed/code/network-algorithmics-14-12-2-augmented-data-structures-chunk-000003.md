# network-algorithmics-14-12-2-augmented-data-structures (chunk 000003)

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
