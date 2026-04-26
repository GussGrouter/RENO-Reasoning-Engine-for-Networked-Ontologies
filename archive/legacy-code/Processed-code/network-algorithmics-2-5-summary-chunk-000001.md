# network-algorithmics-2-5-summary (chunk 000001)

# Network Algorithmics — summary (2.5) (slice)

- Source: raw/code/pdf/Network.Algorithmics.pdf
- Extraction: pdftotext -f 66 -l 76 -layout
- Slice: from `2.5 Summary` up to next chapter/exercises

---

2.5 Summary
This chapter is best sampled based on the reader’s needs. Structurally, the chapter works its way through
four abstraction levels that affect performance: hardware, architecture, operating systems, and proto-
cols. Viewing across abstraction levels is helpful because packet-processing speeds can be limited by
transistor paths implementing packet processing, by architectural limits such as bus speeds, by OS ab-
straction overheads such as system calls, and finally, even by protocol mechanisms. Several examples,
which look ahead to the rest of the book, were described to show that performance can be improved by
understanding each abstraction level.
    Designers that consider all four abstraction levels for each problem will soon be lost in detail.
However, there are a few important performance issues and major architectural decisions for which
simultaneous understanding of all abstraction levels is essential. For example, the simple models given
in this chapter can allow circuit designers, logic designers, architects, microcoders, and software pro-
tocol implementors to work together to craft the architecture of a world-class router. They can also
allow operating system designers, algorithm experts, and application writers to work together to design
a world-class Web server. As link speeds cross 40 Gbps, such interdisciplinary teams will become even
more important. This need is alluded to by Raymond Kurzweil in a different context (Kurzweil, 2001):
   There’s another aspect of creativity. We’ve been talking about great individual contributors, but when
   you’re creating technology it’s necessarily a group process, because technology today is so complex
   that it has to be interdisciplinary . . . And they’re all essentially speaking their own languages, even
   about the same concepts. So we will spend months establishing our common language . . . I have a
   technique to get people to think outside the box: I’ll give a signal-processing problem to the linguists,
   and vice versa, and let them apply the disciplines in which they’ve grown up to a completely different
   problem. The result is often an approach that the experts in the original field would never have thought
   of. Group process gives creativity a new dimension.
   With fields like hardware implementation and protocol design replacing signal processing and lin-
guistics, Kurzweil’s manifesto reflects the goal of this chapter.
