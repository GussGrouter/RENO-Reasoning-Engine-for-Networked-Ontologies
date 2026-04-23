# network-algorithmics-10-3-2-using-hardware-parallelism (chunk 000001)

# Network Algorithmics — 10.3.2 Using hardware parallelism (slice)

- Source: raw/code/pdf/Network.Algorithmics.pdf
- Full-text extraction: processed/code/network-algorithmics-full-layout.txt
- Slice start: PDF page 271
- Slice: from `10.3.2 Using hardware parallelism` up to next detected section heading

---

10.3.2 Using hardware parallelism
Techniques based on perfect hashing do not completely provide worst-case guarantees. While they do
provide worst-case search times of three to four memory accesses, they cannot guarantee worst-case
update times. It is conceivable that an update takes an unpredictably long time while the software
searches for a hash function with the specified bound on the number of collisions.
   One can argue that exactly the same guarantees are provided every moment by millions of Ethernets
around the world and that nondeterministic update times are far preferable to nondeterministic search
times. However, proving that long update times are rare in practice requires either considerable exper-
imentation or good analysis. This makes some designers uncomfortable. It leads to a preference for
search schemes that have bounded worst-case search and update times.
   An alternate approach is to apply hardware parallelism (P5) to a deterministic scheme such as
binary search. Binary search has deterministic search and update times; its only problem is that search
takes a logarithmic number of memory accesses, which is too slow. We can get around this difficulty
by pipelining binary search to increase lookup throughput (number of lookups per second) without
improving lookup latency. This is illustrated in Fig. 10.4.

FIGURE 10.4
Pipeling binary search for a database with keys A through H.

10.3 Challenge 3: scaling lookups to higher speeds                   245
