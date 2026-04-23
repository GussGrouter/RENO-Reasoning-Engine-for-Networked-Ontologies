# network-algorithmics-12-6-3-beyond-two-dimensions-the-good-news (chunk 000001)

# Network Algorithmics — 12.6.3 Beyond two dimensions: the good news (slice)

- Source: raw/code/pdf/Network.Algorithmics.pdf
- Full-text extraction: processed/code/network-algorithmics-full-layout.txt
- Slice start: PDF page 340
- Slice: from `12.6.3 Beyond two dimensions: the good news` up to next detected section heading

---

12.6.3 Beyond two dimensions: the good news
The previous subsection may have left the reader wondering whether there is any hope left for algo-
rithmic approaches to packet classification in the general case. Fortunately, real databases have more
structure, which can be exploited to efficiently solve multidimensional packet classification using algo-
rithmic techniques.
    The good news about packet classification can be articulated using four observations. Subsequent
sections describe a series of heuristic algorithms, all of which do very badly in the worst case but quite
well on databases that satisfy one or more of the assumptions.
    The expected case can be characterized using four observations drawn from a set of firewall
databases studied in Srinivasan et al. (1998) and Gupta and McKeown (1999a) (and not from publi-
cally available lookup tables as in the previous chapter). The first is identical to an observation made in
Chapter 11 and repeated here. The observations are numbered starting from O2 to be consistent with
observation O1 made in the lookup chapter.
O2: Prefix containment is rare. It is somewhat rare to have prefixes that are prefixes of other prefixes,
    as, for example, the prefixes 00* and 0001*. In fact, the maximum number of prefixes of a given
    prefix in lookup tables and classifiers is seven.
O3: Many fields are not general ranges. For the destination and source port fields, most rules contain
    either specific port numbers (e.g., port 80 for Web traffic), the wildcard range (i.e., ∗), or the
    port ranges that separate server ports from client ports (1024 or greater and less than 1024).
    The protocol field is limited to either the wildcard or (more commonly) TCP, UDP. This field
    also rarely contains protocols such as IGMP and ICMP. While other TCP fields are sometimes
    referred to, the most common reference is to the ACK bit.
O4: The number of disjoint classification regions is small. This is perhaps the most interesting ob-
    servation. Harking back to the geometric view, the lower bounds in Chazelle (1990a) depend
    partly on the worst-case possibility of creating N K classification regions using N rules. Such
    rules require either N K space or a large search time. However, Gupta and McKeown (1999a),
    after an extensive survey of 8000 rule databases, show that the number of classification regions is
    much smaller than the worst case. Instead of being exponential in the number of dimensions, the
    number of classification regions is linear in N , with a small constant.
O5: Source–Destination matching: In Singh et al. (2004b), several core router classifiers used by real
    ISPs are analyzed and the following interesting observation is made. Almost all packets match
    at most five distinct source–destination values found in the classifier. No packet matched more
    than 20 distinct source–destination pairs. This is a somewhat more refined observation than O4
    because it says that the number of classification regions is small, even when projected only to the
    source and destination fields. By “small,” we mean that the number of regions grows much more
    slowly than N, the size of the classifier.
