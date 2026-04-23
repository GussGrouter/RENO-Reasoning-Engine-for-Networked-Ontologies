# Network Algorithmics — 16.18 Estimation of flow-size distribution (slice)

- Source: raw/code/pdf/Network.Algorithmics.pdf
- Full-text extraction: processed/code/network-algorithmics-full-layout.txt
- Slice start: PDF page 510
- Slice: from `16.18 Estimation of flow-size distribution` up to next detected section heading

---

16.18 Estimation of flow-size distribution
Counting the number of distinct elements or detecting heavy hitters are among the simplest and ar-
guably the easiest objectives to achieve in network data streaming. In this section we describe a
data-streaming algorithm for achieving a much more sophisticated objective: the estimation of flow
size distribution.
    The problem of estimating flow size distribution on a high-speed link is another network measure-
ment problem that has received considerable attention (Duffield et al., 2003; Hohn and Veitch, 2003;
Duffield et al., 2001, 2002; Estan and Varghese, 2002; Estan et al., 2002). In this problem, given an
arbitrary flow size s, we are interested in knowing the number of flows that contain s packets within a
monitoring interval. In other words we would like to know how the total traffic volume splits into flows
of different sizes. An estimate of the flow distribution contains knowledge about the number of flows
for all possible flow sizes, including elephants (large flows), “kangaroos/rabbits” (medium flows), and
“mice” (small flows).
