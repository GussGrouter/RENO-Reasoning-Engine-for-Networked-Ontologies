# network-algorithmics-5-6-2-direct-memory-access-versus-programmed-i-o (chunk 000001)

# Network Algorithmics — 5.6.2 Direct memory access versus programmed I/O (slice)

- Source: raw/code/pdf/Network.Algorithmics.pdf
- Full-text extraction: processed/code/network-algorithmics-full-layout.txt
- Slice start: PDF page 169
- Slice: from `5.6.2 Direct memory access versus programmed I/O` up to next detected section heading

---

5.6.2 Direct memory access versus programmed I/O
Earlier sections stated that the Witless scheme uses programmed I/O, or PIO (i.e., the processor or
CPU is involved in every word transferred between memory and adaptor), while other schemes, such as
VAX Clusters, use DMA (where the adaptor copies data directly to memory). It may seem that DMA is
always better than PIO. However, comparisons between DMA and PIO are tricky because each method
has subtle implications for the overall memory bandwidth used.
    For instance, PIO has one advantage in that the data flows through the processor and thus ends up
in the processor cache. This can be useful to prevent loss of memory bandwidth for subsequent access.
Also, with PIO it is easy to integrate other functions, such as checksums, without requiring adaptor
hardware to do the same function.
    However, some studies have shown that if data arrives and is used much later (e.g., one scheduling
quantum later) by the application, then placing data in the D-cache too early is wasteful of the D-cache
and lowers rather than raises D-cache hit rate. On the other hand, DMA can steal cycles from the CPU
and also requires some careful cache invalidation when data is written into a memory location (that
could also be cached). So the jury is still out. The choice between the two is best decided on a case-by-
case basis, taking into account architectural considerations and the application at hand. A more detailed
study of the issues involved can be found in Mogul and Ramakrishnan (1997).
