# network-algorithmics-4-3-dijkstra-route-computation (chunk 000001)

# Network Algorithmics — route computation using Dijkstra (4.3) (slice)

- Source: raw/code/pdf/Network.Algorithmics.pdf
- Extraction: pdftotext -f 108 -l 126 -layout
- Slice: from `4.3 Route computation using Dijkstra’s algorithm` up to (excluding) `4.4`

---

4.3 Route computation using Dijkstra’s algorithm               81

FIGURE 4.6
Using a priority queue based on bucket sorting to speed up Dijkstra’s algorithm.

cost of a node X is c, then node X can be placed in a list pointed to by element c of the array (Fig. 4.6).
This leads to the following algorithm.
    Whenever a node X changes its cost from c to c , node X is removed from the list for c and added to
the list for c . But how is the minimum element to be found? This can be done by initializing a pointer
called CurrentMin to 0 (which corresponds to the cost of S). Each time the algorithm wishes to find the
minimum-cost node not in the tree, CurrentMin is incremented by 1 until an array location is reached
that contains a nonempty list. Any node in this list can then be added to the tree. The algorithm costs
O(N + Diam ∗ MaxLinkCost) because the work done in advancing CurrentMin can at most be the size
of the array. This can be significantly better than N log N for large N and small values of Diam and
MaxLinkCost.
    A crucial factor in being able to efficiently use a bucket sort priority queue of the kind described
earlier is that the node costs are always ahead of the value of CurrentMin. This is a monotonicity
condition. If it were not true, the algorithm would start checking for the minimum from 1 at each
iteration, instead of starting from the last value of CurrentMin and never backing up. The monotonicity
condition is fairly obvious for Dijktra’s algorithm because the costs of nodes not already in the tree
have to be larger than the costs of nodes that are already in the tree.
    Fig. 4.6 shows the state of the bucket sort priority queue after A has been added to the tree. This
corresponds to the right frame of Fig. 4.5. At this stage, CurrentMin = 2, which is the cost of A. At the
next iteration, CurrentMin will advance to 3, and D will be added to the tree. This will result in the C’s
cost being reduced to 4. We thus remove C from the list in position 5 and add it to the empty list in
position 4. CurrentMin is then advanced to 4, and C is added to the tree.

Exercises

• The algorithm requires a node to be removed from a list and added to another, earlier list. How can
  this be done efficiently?
• In Fig. 4.6 how can the algorithm know that it can terminate after adding C to the tree instead of
  advancing to the end of the long array?
• In networks that have failures, the concept of diameter is a highly suspect one because the diameter
  could change considerably after a failure. Consider a wheel topology where all N nodes have diam-

---

## PDF page 109

82       Chapter 4 Principles in action

eter 2 through a central spoke node; if the central spoke node fails, the diameter goes up to N/2. In
  actual practice the diameter is often small. Can this cause problems in sizing the array?
• Can you circumvent the problem of the diameter completely by replacing the linear array of Fig. 4.6
  with a circular array of size MaxLinkCost? Explain. The resulting solution is known as Dial’s
  algorithm (Ahuja et al., 1993).
