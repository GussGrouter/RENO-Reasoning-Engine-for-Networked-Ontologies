# network-algorithmics-12-14-conclusions-this-chapter-describes-several-algorithms-for-packet-classif (chunk 000001)

# Network Algorithmics — 12.14 Conclusions This chapter describes several algorithms for packet classification at gigabit speeds. The grid of tries (slice)

- Source: raw/code/pdf/Network.Algorithmics.pdf
- Full-text extraction: processed/code/network-algorithmics-full-layout.txt
- Slice start: PDF page 354
- Slice: from `12.14 Conclusions This chapter describes several algorithms for packet classification at gigabit speeds. The grid of tries` up to next detected section heading

---

12.14 Conclusions
This chapter describes several algorithms for packet classification at gigabit speeds. The grid of tries
provides a two-dimensional classification algorithm that is fast and scalable. All the remaining schemes
require exploiting some assumptions about real rule databases to avoid the geometric lower bound.
While much progress has been made, it is important to reduce the number of such assumptions required
for classification and to validate these assumptions extensively.
    At the time of writing, decision tree approaches (Woo, 2000; Gupta and McKeown, 1999b; Singh
et al., 2004a; Vamanan et al., 2010) and the extended grid of tries method (Singh et al., 2004b) appear
to be the most attractive algorithmic schemes for hardware. While the latter depends on each packet’s
matching only a small number of source–destination prefixes, it is still difficult to characterize what
assumptions or parameters influence the performance of decision tree approaches. For software settings,
Tuple Space Search (Srinivasan et al., 1998) is attractive, especially when fast updates are required.
Caching and early stopping can be used to improve average lookup times (Pfaff et al., 2015).
    Of the other general schemes, the bit vector scheme is suitable for hardware implementation for a
modest number of rules (say, up to 10,000). Equivalenced cross-producting seems to scale to roughly

328      Chapter 12 Packet classification
