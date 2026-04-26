# network-algorithmics-12-6-2-beyond-two-dimensions-the-bad-news (chunk 000001)

# Network Algorithmics — 12.6.2 Beyond two dimensions: the bad news (slice)

- Source: raw/code/pdf/Network.Algorithmics.pdf
- Full-text extraction: processed/code/network-algorithmics-full-layout.txt
- Slice start: PDF page 339
- Slice: from `12.6.2 Beyond two dimensions: the bad news` up to next detected section heading

---

12.6.2 Beyond two dimensions: the bad news
The success of the grid of tries may make us optimistic about generalizing to larger dimensions. Unfor-
tunately, this optimism is misplaced; either the search time or the storage blows up exponentially with
the number of dimensions K for K > 2.
    Using the geometric viewpoint just described, it is easy to adapt a lower bound from computational
geometry. Thus, it is known that general multidimensional range searching over N ranges in K dimen-
sions requires ((log N )K−1 ) worst-case time if the memory is limited to about linear size (Chazelle,
1990a,b) or requires O(N K ) size memory. While log N could be reasonable (say, 10 memory accesses),
log4 N (K = 5 in the case of packet classification over source IP, destination IP, source port number,
destination port number, and protocol) will be very large (say, 10,000 memory accesses). Notice that
this lower bound is consistent with solutions for the two-dimensional cases that take linear storage but
are as fast as O(log N ).
    The lower bound implies that for perfectly general rule sets, algorithmic approaches to classification
require either a large amount of memory or a large amount of time. Unfortunately, classification at high
speeds, especially for core routers, requires the use of limited and expensive SRAM. Thus the lower
bound seems to imply that content address memories are required for reasonably sized classifiers (say,
10,000 rules) that must be searched at high speeds (e.g., OC-768 speeds).

12.7 Extending two-dimensional schemes                  313
