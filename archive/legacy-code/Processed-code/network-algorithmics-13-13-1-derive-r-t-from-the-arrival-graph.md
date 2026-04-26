# Network Algorithmics — 13.13.1 Derive R(t) from the arrival graph (slice)

- Source: raw/code/pdf/Network.Algorithmics.pdf
- Full-text extraction: processed/code/network-algorithmics-full-layout.txt
- Slice start: PDF page 380
- Slice: from `13.13.1 Derive R(t) from the arrival graph` up to next detected section heading

---

13.13.1 Derive R(t) from the arrival graph
In SERENA the random matching R(t) is derived from the arrival graph A(t) defined as follows: an
edge (Ii , Oj ) belongs to A(t) if and only if there is a packet arrival to the corresponding VOQ during

354       Chapter 13 Switching




FIGURE 13.11
Illustrate MERGE procedure by an example. The three subfigures are referred to as (a), (b), and (c).


time slot t. Note that A(t) is not necessarily a matching because more than one input ports could have
a packet arrival (i.e., edge) destined for the same output port at time slot t. Hence, in this case, each
output port prunes all such edges incident upon it except the one with the heaviest weight (with ties
broken randomly). The pruned graph, denoted as A (t), is now a matching.
    This matching A (t), which is typically partial, is then randomly populated into a full matching R(t)
by pairing the yet unmatched input ports with the yet unmatched output ports in a round-robin manner.
This pairing operation clearly has O(N ) computational complexity. Deriving R(t) from A(t) in SER-
ENA is better than generating R(t) from scratch in sample-and-compare in two different ways. First, it
allows SERENA to tap into the randomness naturally contained in the packet arrival process, making it
cheaper to implement since “man-made” randomness incurs a computational cost, as explained in Sec-
tion 13.10. Second, as explained in Shah et al. (2002b); Giaccone et al. (2003), some packet arrivals
go to heavily backlogged VOQs, and hence R(t) derived from A(t) often has a larger weight than a
uniform random matching.
