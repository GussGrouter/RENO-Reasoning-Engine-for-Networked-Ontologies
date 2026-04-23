# network-algorithmics-14-12-2-augmented-data-structures (chunk 000002)

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
