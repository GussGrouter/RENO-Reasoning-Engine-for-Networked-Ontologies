# Network Algorithmics — 16.20 Conclusion This chapter was written to convince the reader that measurement is an exciting field of endeavor. (slice)

- Source: raw/code/pdf/Network.Algorithmics.pdf
- Full-text extraction: processed/code/network-algorithmics-full-layout.txt
- Slice start: PDF page 513
- Slice: from `16.20 Conclusion This chapter was written to convince the reader that measurement is an exciting field of endeavor.` up to next detected section heading

---

16.20 Conclusion
This chapter was written to convince the reader that measurement is an exciting field of endeavor.
Many years ago, the advice to an ambitious youngster was, “Go West, young man” because the East
was (supposedly) played out.

                                                                            16.21 Exercises         487



    Similarly, it may be that protocol design is played out while protocol measurement is not. After all,
TCP and IP have been cast in stone these many years; despite some confusion as to its parentage, the
Internet could only be invented once. Reinventing the Internet is even harder if one follows the fate of
the next-generation Internet proposal. But there will always be new ways to understand and measure
the Internet, especially using techniques that depend on minimal cooperation.
    The first part of the chapter focused on the problems of the most basic measurement issue at high
speeds: packet counting. This is a real problem faced by every high-speed-router vendor because they
deal, on the one hand, with increasing ISP demands for observability and, on the other hand, with hard-
ware limitations. Algorithmics can help by clever uses of memories (P5c), by changing the specification
to focus only on large counters or flow counts (P3), by unusual uses of sampling (P3a), and finally by
determining real user needs to reduce the space of counters required by aggregation for accounting or
traffic matrices (P7). Table 16.1 presents a summary of the techniques used in this chapter, together
with the major principles involved.
    The chapter concluded with an excursion into the field of passive measurement with an updated
section that describes the remarkable progress of data streaming algorithms since the first edition of
the book. Unlike all the other schemes described in this chapter, passive measurement schemes do not
require implementation or protocol changes and hence are likely to continue to be a useful source of
measurement data. Thus, it seems fitting to end this chapter with Savage’s summary of the main idea
behind Sting: “Stop thinking of a protocol as a protocol. Think of it as . . . an opportunity.”
