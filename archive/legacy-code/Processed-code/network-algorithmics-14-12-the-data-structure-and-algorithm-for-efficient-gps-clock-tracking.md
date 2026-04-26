# Network Algorithmics — 14.12 The data structure and algorithm for efficient GPS clock tracking (slice)

- Source: raw/code/pdf/Network.Algorithmics.pdf
- Full-text extraction: processed/code/network-algorithmics-full-layout.txt
- Slice start: PDF page 436
- Slice: from `14.12 The data structure and algorithm for efficient GPS clock tracking` up to next detected section heading

---

14.12 The data structure and algorithm for efficient GPS clock tracking
As explained earlier, the tracking of the GPS clock boils down to exactly computing the corresponding
virtual time V (t) given a real time t as input. An augmented data structure called shape data struc-
ture was proposed in Valente (2004) to perform this computation with a worst-case time complexity of
O(log n) per packet (P15). To more clearly describe the shape data structure and its companion algo-

410       Chapter 14 Scheduling packets




FIGURE 14.19
Data structure (before arrival).


rithm, we convert this problem to a much cleaner computation problem that is provably equivalent. In
the latter problem we need to answer a query concerning a staircase like the one shown in Fig. 14.19.
