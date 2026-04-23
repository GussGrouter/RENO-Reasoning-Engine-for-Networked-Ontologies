# network-algorithmics-14-12-1-the-staircase-query-problem (chunk 000001)

# Network Algorithmics — 14.12.1 The staircase query problem (slice)

- Source: raw/code/pdf/Network.Algorithmics.pdf
- Full-text extraction: processed/code/network-algorithmics-full-layout.txt
- Slice start: PDF page 437
- Slice: from `14.12.1 The staircase query problem` up to next detected section heading

---

14.12.1 The staircase query problem
In this staircase the values of the run (width) and the rise (height) of each step are precisely known, and
the x-coordinate of the leftmost vertical line is assumed to be 0. For example, the run and the rise of
the first step are highlighted in bold in Fig. 14.19. Our computation problem is that, given any t > 0 as
input, we need to find the x-coordinate, say v, of a vertical line such that the area between the 0-line
and the v-line “under the staircase” is t, as shown in Fig. 14.19. One requirement is that the proposed
solution should have a low worst-case time complexity of O(log n) per query, where n is the number
of steps in the staircase.
    With the computation problem thus specified, we expect most readers to be able to come up with
such a solution in minutes. For example, for each vertical line along the edge of a step, say with x-
coordinate vi , we first precompute (P3b) the area between the 0-line and the vi -line and store them in a
balanced priority queue. Then, given any t, we can perform a binary search over these areas to find the
corresponding v in O(log n) time.
    This computation problem becomes much more challenging when the following three requirements
are imposed. As we will explain shortly, from time to time, a new step may be “inserted into” the
staircase based on the x-coordinate of its right edge. For example, in Fig. 14.20 a new step is inserted
between two previously consecutive steps in Fig. 14.19. The first requirement is that the proposed
solution has to be able to still answer the query in O(log n) time in the face of such insertions.
    Note the precomputation-based solution won’t work in O(log n) time any more because every pre-
computed area value changes with the insertion of the new step, and updating them all takes O(n) time.
Hence, a different data structure and algorithm is needed, and the second requirement is that the time
complexity of updating this data structure, in the event of the insertion of a step, is also O(log n). We
will also show shortly that, from time to time, the leftmost step of the staircase needs to be removed,
and this data structure needs to be updated to properly account for the removal. The third and last
requirement is that the cost of this update has to be also bounded at O(log n).

14.12 The data structure and algorithm for efficient GPS clock tracking                    411

FIGURE 14.20
Data structure (after arrival).

Standard priority-queue data structure finds it hard to satisfy all three requirements. Intuitively, the
first requirement and the two latter requirements require objects in the priority queue to be organized
(i.e., represented and sorted) in two very different ways. However, there is a family of specialized data
structures that can deal with two (but not three or more) conflicting requirements as in this case. This
family, called augmented data structures (Cormen et al., 2009, Chapter 14), is described next.
