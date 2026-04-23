# network-algorithmics-16-17-detection-of-heavy-hitters (chunk 000001)

# Network Algorithmics — 16.17 Detection of heavy hitters (slice)

- Source: raw/code/pdf/Network.Algorithmics.pdf
- Full-text extraction: processed/code/network-algorithmics-full-layout.txt
- Slice start: PDF page 509
- Slice: from `16.17 Detection of heavy hitters` up to next detected section heading

---

16.17 Detection of heavy hitters
In Section 16.7 we already described the problem of detecting “large” flows (those that contain many
more packets than others). Such flows are also called elephants or heavy hitters in the networking
literature. In the database literature, data items that occur frequently (e.g., merchandise that appears in
a large number of customer transactions) are called frequent items or icebergs.
    Over the years, many different heavy-hitter detection algorithms have been proposed, such as Misra
and Gries (1982); Manku and Motwani (2002); Estan and Varghese (2002); Charikar et al. (2002); and
Cormode and Muthukrishnan (2005). Most of them, however, are not suitable for measuring a high-
speed network link since, upon the arrival of each new data item, they need to update the values of a
fairly large number (say hundreds) of counters. Algorithms suitable for elephant detection and size esti-
mation in high-speed networks include (Estan and Varghese, 2002; Charikar et al., 2002; Cormode and
Muthukrishnan, 2005). Among the three, we will only describe the sample-and-hold algorithm (Estan
and Varghese, 2002) since it is conceptually the simplest. We also describe a similar technique called
ElephantTrap (Lu et al., 2007) that detects elephants but does not track their sizes.
    The objective of the sample-and-hold algorithm is to output the identities and the approximate
packet counts of the elephants, defined as the flows whose actual packet counts are at least θ (percent-
age) of the total packet count n in the packet stream. To do so, sample-and-hold requires only O(1/θ )
amount of working memory (in CAM), takes only a one-pass scan over the packet stream, and, for each
packet, searches for and updates (if at all) only a single counter. Hence, sample-and-hold can scale to
very high link speeds.
    The algorithmic logic of sample-and-hold is very simple. The algorithm maintains a small set D of
flow entries in CAM. Each flow entry contains a flow identifier and the associated packet counter. The
algorithm is, for each incoming packet, to check if its flow identifier is already included in D (which
is supported by CAM). If the answer is “yes,” then the corresponding packet counter is incremented
(“hold”). Otherwise, a new flow entry containing this flow identifier is sampled (“sample”) with proba-
bility b/(nθ ) and added to D. At the end of a measurement epoch, all items in D with high frequencies
are returned as probable heavy hitters. It was shown in Estan and Varghese (2002) that, when D contains
b/θ entries, the probability number with which an elephant is not included in D is only e−b .
    Most existing elephant-detection algorithms also produce an approximate count of the size of the
elephant flows detected. An exception to that is ElephantTrap (Lu et al., 2007). As its name suggests,
ElephantTrap is very effective at capturing and “trapping” the identities of elephant flows in a small
table. However, ElephantTrap purposefully gives up the capability of accurately tracking their packet
(or byte) counts, in exchange for a “streamlined” design that makes the algorithm extremely efficient
to implement.

16.18 Estimation of flow-size distribution            483
