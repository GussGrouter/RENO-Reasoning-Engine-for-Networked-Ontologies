# network-algorithmics-12-7-extending-two-dimensional-schemes (chunk 000001)

# Network Algorithmics — 12.7 Extending two-dimensional schemes (slice)

- Source: raw/code/pdf/Network.Algorithmics.pdf
- Full-text extraction: processed/code/network-algorithmics-full-layout.txt
- Slice start: PDF page 340
- Slice: from `12.7 Extending two-dimensional schemes` up to next detected section heading

---

12.7 Extending two-dimensional schemes
The simplest general scheme uses observation O5 to trivially extend any efficient 2D scheme to multiple
dimensions. A number of algorithms simply use linear search to search through all possible rules. These
scales well in storage but poorly in time. The source–destination matching observation leads to a very

314      Chapter 12 Packet classification

FIGURE 12.9
Extending two-dimensional schemes.

simple idea depicted in Fig. 12.9. Use source–destination address matching to reduce linear searching
to just the rules corresponding to source–destination prefix pairs in the database that match the given
packet header. Alternately, one can use source-destination matching to reduce power in TCAMs as in
SmartPC (Ma and Banerjee, 2012) as we will see later.
    By observation O5, at most 20 rules match any packet when considering only the source and des-
tination fields. Thus pruning based on source–destination fields will reduce the number of rules to be
searched to less than 20, compared to searching the entire database. For example, Singh et al. (2004a)
describe a database with 2800 rules used by a large ISP.
    Thus in Fig. 12.9 the general idea is to use any efficient two-dimensional matching scheme to find all
distinct source–destination prefix pairs (S1 , D1 ) . . . (St , Dt ) that match a header. For each distinct pair
(Si , Di ), there is a linear array or list with all rules that contain (Si , Di ) in the source and destination
fields. Thus in the figure, the algorithm has to traverse the list at (S1 , D1 ), searching through all the
rules for R5 , R6 , R2 , and R4 . Then the algorithm moves on to consider the lists at (S2 , D2 ), and so on.
    This structure has two important advantages:
• Each rule is represented only once without replication. However, one may wish to replicate rules to
  reduce search times even further.
• The port range specifications stay as ranges in the individual lists without the associated blowup
  associated with range translation in, say, CAMs.
   Since the grid-of-tries implementation described earlier is one of the most efficient two-dimensional
schemes in the literature, it is natural to instantiate this general schema by using a grid of tries as the
two-dimensional algorithm in Fig. 12.9.

12.8 Using divide-and-conquer                315
