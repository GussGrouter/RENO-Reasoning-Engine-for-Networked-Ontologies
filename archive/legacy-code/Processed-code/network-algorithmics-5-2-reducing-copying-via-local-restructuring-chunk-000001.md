# network-algorithmics-5-2-reducing-copying-via-local-restructuring (chunk 000001)

# Network Algorithmics — 5.2 Reducing copying via local restructuring (slice)

- Source: raw/code/pdf/Network.Algorithmics.pdf
- Full-text extraction: processed/code/network-algorithmics-full-layout.txt
- Slice start: PDF page 142
- Slice: from `5.2 Reducing copying via local restructuring` up to next detected section heading

---

5.2 Reducing copying via local restructuring
Before tackling the full complexity of eliminating all redundant copies in Fig. 5.1, this section starts
by concentrating on Copy 3, the fundamental copy made from the application to kernel buffers (or
vice versa) when a network message is sent (received). This is a fundamental issue for networking,
independent of file system issues. It also turns out that general solutions that eliminate all redundant
I/O copies (Section 5.4) build on the techniques developed in this section.
    This section assumes that the protocol is fixed but the local implementation (at least the kernel) can
be restructured. The goal, of course, is to perform minimal restructuring in order to continue to lever-
age the vast amount of investment in existing kernel and application software. Section 5.2.1 describes
techniques based on exploiting adaptor memory. Section 5.2.2 describes the core idea behind copy
avoidance (by remapping shared physical pages) and its pitfalls. Section 5.2.3 shows how to optimize
page remapping using precomputation and caching based on I/O streams; however, this technique in-
volves changing the application programming interface (API). Finally, Section 5.2.4 describes another
technique, one that uses virtual memory (VM) but does not change the API.
