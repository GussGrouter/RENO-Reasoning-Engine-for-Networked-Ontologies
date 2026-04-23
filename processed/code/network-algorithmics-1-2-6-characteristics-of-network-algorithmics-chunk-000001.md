# network-algorithmics-1-2-6-characteristics-of-network-algorithmics (chunk 000001)

# Network Algorithmics — 1.2.6 Characteristics of network algorithmics (slice)

- Source: raw/code/pdf/Network.Algorithmics.pdf
- Full-text extraction: processed/code/network-algorithmics-full-layout.txt
- Slice start: PDF page 40
- Slice: from `1.2.6 Characteristics of network algorithmics` up to next detected section heading

---

1.2.6 Characteristics of network algorithmics
The example of scenting an evil packet illustrates three important aspects of network algorithmics.
a. Network algorithmics is interdisciplinary: Given the high rates at which network processing must
   be done, a router designer would be hard pressed not to use hardware. The example exploited several
   features of hardware: It assumed that wide words of arbitrary size were easily possible; it assumed
   that shifts were easier than divides; it assumed that memory references were the bottleneck; it as-
   sumed that a 256-element array contained in fast on-chip memory was feasible; it assumed that
   adding a few extra registers was feasible; and finally it assumed that small changes to the logic to
   combine URL processing and initialization were trivial to implement.
      For the reader unfamiliar with hardware design, this is a little like jumping into a game of cards
   without knowing the rules and then finding oneself finessed and trumped in unexpected ways. A con-
   tention of this book is that mastery of a few relevant aspects of hardware design can help even a
   software designer understands at least the feasibility of different hardware designs. A further con-
   tention of this book is that such interdisciplinary thinking can help produce the best designs.
      Thus Chapter 2 presents the rules of the game. It presents simple models of hardware that point
   out opportunities for finessing and trumping troublesome implementation issues. It also presents
   simple models of operating systems. This is done because end systems such as clients and Web
   servers require tinkering with and understanding operating system issues to improve performance,
   just as routers and network devices require tinkering with hardware.
b. Network algorithmics recognizes the primacy of systems thinking: The specification was relaxed
   to allow approximate thresholds in powers of 2, which simplified the hardware. Relaxing specifica-
   tions and moving work from one subsystem to another is an extremely common systems technique,
   but it is not encouraged by current educational practice in universities, in which each area is taught
   in isolation.
      Thus today, one has separate courses in algorithms, in operating systems, and in networking.
   This tends to encourage “black box” thinking instead of holistic or systems thinking. The example
   alluded to other systems techniques, such as the use of lazy evaluation and trading memory for
   processing in order to scrub the Count array.

14         Chapter 1 Introducing network algorithmics
