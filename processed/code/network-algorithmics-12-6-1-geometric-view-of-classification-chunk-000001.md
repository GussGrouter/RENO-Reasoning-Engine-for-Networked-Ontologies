# network-algorithmics-12-6-1-geometric-view-of-classification (chunk 000001)

# Network Algorithmics — 12.6.1 Geometric view of classification (slice)

- Source: raw/code/pdf/Network.Algorithmics.pdf
- Full-text extraction: processed/code/network-algorithmics-full-layout.txt
- Slice start: PDF page 338
- Slice: from `12.6.1 Geometric view of classification` up to next detected section heading

---

12.6.1 Geometric view of classification
A second problem-solving technique that is useful is to collect different viewpoints for the same prob-
lem. This section describes a geometric view of classification that was introduced by Lakshman and
Stidialis (1998) and independently by Adisheshu (1998).
    Recall from Chapter 11 that we can view a 32-bit prefix like 00∗ as a range of addresses from
000 . . . 00 to 001 . . . 11 on the number line from 0 to 232 . If prefixes correspond to line segments geomet-
rically, two-dimensional rules correspond to rectangles (Fig. 12.8), three-dimensional rules to cubes,
and so on. A given packet header is a point. The problem of packet classification reduces to finding the
lowest-cost box that contains the given point.
    Fig. 12.8 shows the geometric view of the first three two-dimensional rules in Fig. 12.3. Destination
addresses are represented on the y-axis and source addresses on the x-axis. In the figure, some sample
prefix ranges are marked off on each axis. For example, the two halves of the y-axis are the prefix
ranges 0∗ and 1∗. Similarly, the x-axis is divided into the four prefix ranges 00∗, 01∗, 10∗, and 11∗.
To draw the box for a rule like R1 = 0∗, 10∗, draw the 0∗ range on the y-axis and the 10∗ range on the

312      Chapter 12 Packet classification

x-axis, and extend the range lines to meet, forming a box. Multiple-rule matches, such as R1 and R2 ,
correspond to overlapping boxes.
    The first advantage of the geometric view is that it enables the application of algorithms from com-
putational geometry. For example, Lakshman and Stidialis (1998) adapt a technique from computational
geometry known as fractional cascading to do binary search for two-field rule matching in O(log N )
time, where N is the number of rules. In other words, two-dimensional rule matching is asymptotically
as fast as one-dimensional rule matching using binary search. This is consistent with the results for the
grid of tries. The result also generalizes binary search on values for prefix searching as described in
Chapter 11.
    Unfortunately, the constants for fractional cascading are quite high. Perhaps this suggests that adapt-
ing existing geometric algorithms may actually not result in the most efficient algorithms. However, the
second and main advantage of the geometric viewpoint is that it is suggestive and useful.
    For example, the geometric view provides a useful metric, the number of disjoint (i.e., nonintersect-
ing) classification regions. Since rules can overlap, this is not the number of rules. In two dimensions,
for example, with N rules, one can create N 2 classification regions by having N/2 rules that correspond
geometrically to horizontal strips together with N/2 rules that correspond geometrically to vertical
strips. The intersection of the N/2 horizontal strips with the N/2 vertical strips creates O(N 2 ) disjoint
classification regions. For example, the database in Fig. 12.5 has this property. Similar constructions
can be used to generate O(N K ) regions for K-dimensional rules.
    As a second example, the database of Fig. 12.8 has four classification regions: the rule R1 , the rule
R2 , the points in R3 not contained in R1 , and all points not contained in R1 , R2 , or R3 . We will use
the number of classification regions later to characterize the complexity of a given classifier or rule
database.
