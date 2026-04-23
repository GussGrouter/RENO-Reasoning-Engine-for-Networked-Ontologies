# network-algorithmics-5-6-1-using-caches-effectively (chunk 000001)

# Network Algorithmics — 5.6.1 Using caches effectively (slice)

- Source: raw/code/pdf/Network.Algorithmics.pdf
- Full-text extraction: processed/code/network-algorithmics-full-layout.txt
- Slice start: PDF page 164
- Slice: from `5.6.1 Using caches effectively` up to next detected section heading

---

5.6.1 Using caches effectively
The architectural model of Fig. 5.1 avoids two important details that were described in Chapter 2.
Recall that the processor keeps one or more data caches (D-caches), and one or more instruction caches
(I-caches). The data cache is a table that maps from memory addresses to data contents; if there are
repeated reads and writes to the same location L in memory and L is cached, then these reads and writes
can be served directly out of the data cache without incurring bus or memory bandwidth. Similarly,
recall that programs are stored in memory; every line of code executed by the CPU has to be fetched
from main memory unless it is cached in the instruction cache.

138      Chapter 5 Copying data
