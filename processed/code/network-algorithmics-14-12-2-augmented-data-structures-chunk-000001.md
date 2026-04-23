# network-algorithmics-14-12-2-augmented-data-structures (chunk 000001)

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
