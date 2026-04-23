# network-algorithmics-2-4-2-virtual-memory (chunk 000001)

# Network Algorithmics — operating systems: virtual memory (2.4.2) (slice)

- Source: raw/code/pdf/Network.Algorithmics.pdf
- Extraction: pdftotext -f 64 -l 79 -layout
- Slice: from `2.4.2 Infinite memory via virtual memory` up to (excluding) `2.4.3 Simple I/O via system calls`

---

2.4.2 Infinite memory via virtual memory
In virtual memory (Fig. 2.13), the programmer works with an abstraction of memory that is a linear
array into which a compiler assigns variable locations. Variable X could be stored in location 1010 in
this imaginary (or virtual) array. The virtual memory abstraction is implemented using the twin mech-

FIGURE 2.13
The programmer sees the illusion of contiguous virtual memory, which is, in reality, mapped to a collection of main
memory and disk memory pages via page tables.

---

## PDF page 70

2.4 Operating systems             43
