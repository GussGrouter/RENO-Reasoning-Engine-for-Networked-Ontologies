# network-algorithmics-11-3-non-algorithmic-techniques-for-prefix-matching (chunk 000001)

# Network Algorithmics — 11.3 Non-algorithmic techniques for prefix matching (slice)

- Source: raw/code/pdf/Network.Algorithmics.pdf
- Full-text extraction: processed/code/network-algorithmics-full-layout.txt
- Slice start: PDF page 285
- Slice: from `11.3 Non-algorithmic techniques for prefix matching` up to next detected section heading

---

11.3 Non-algorithmic techniques for prefix matching
In this section we consider two other systems techniques for prefix lookups that do not rely on algo-
rithmic methods: caching and ternary CAMs. Caching relies on locality in address references, while
CAMs rely on hardware parallelism.

11.3.1 Caching
Lookups can be sped up by using a cache (P11a) that maps 32-bit addresses to next hops. However,
cache hit ratios in the backbone are poor (Newman et al., 1997) because of the lack of locality exhibited
by flows in the backbone. The use of a large cache still requires the use of an exact-match algorithm for
lookup. Some researchers have advocated a clever modification of a CPU cache lookup algorithm for
this purpose (Chiueh and Pradhan, 1999). In summary, caching can help, but it does not avoid the need
for fast prefix lookups.
