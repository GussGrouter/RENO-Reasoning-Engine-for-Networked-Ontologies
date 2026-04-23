# network-algorithmics-10-5-exercise-1-arp-caches-another-example-of-an-exact-match-lookup-is-furnis (chunk 000003)

allows a set of match-action rules that can be used to implement bridge lookups, MPLS lookups, IP
  lookups, or other forms of lookup by simply changing the definition of a match.
• Multicore Processors: Processors have become faster and multicore. Thus software implementations
  of IP lookups at Gigabit speeds are feasible today.
• Network Function Virtualization (NFV): There is a growing trend among mobile carriers to replace
  complex middleboxes (that performed network functions such as longest matching prefix, firewalls,
  parental controls etc.) with flexible software realizations, a trend called Network Function Virtual-
  ization (NFV, 2022).
    Despite these changes, the underlying algorithmic ideas have remained except for small variations
that we will point out including fast software implementations such as DXR (2022) and algorithms
optimized for large amounts of DRAM and small on-chip SRAM such as SAIL (Yang et al., 2014).
    The entire chapter is organized as follows. Section 11.1 provides an introduction to prefix lookups.
Section 11.2 describes attempts to finesse the need for IP lookups. Section 11.3 presents non-
algorithmic techniques for lookup based on caching and parallel hardware. Section 11.4 describes the
simplest technique based on unibit tries.
    The chapter then transitions to describe seven more sophisticated schemes: multibit tries (Sec-
tion 11.5), level-compressed tries (Section 11.6), Lulea-compressed tries (Section 11.7), Tree bitmap
(Section 11.8), binary search on prefix ranges (Section 11.9) (with a modern manifestation called DXR),
binary search on prefix lengths (Section 11.11), and linear search on prefix lengths (Section 11.12).
    The chapter ends with Section 11.13 on memory allocation issues, Section 11.14 on fixed function
lookup chips, and Section 11.15 on programmable chips, and the P4 language to program them. The
techniques described in this chapter (and the corresponding principles) are summarized in Table 11.1.

Quick reference guide
  The most important lookup algorithms in our opinion for an implementor today are as follows. At speeds up to 100 Gbps
  in hardware or software using DRAM technology, the simplest and most effective scheme is based on binary search on
  prefix ranges (DXR) (Section 11.9) and is unencumbered by patents. At faster speeds, especially using more expensive
  SRAM technology, the most effective algorithm described in this chapter is Tree bitmap (Section 11.8). On the other
  hand, a simple scheme using small on-chip SRAM and external DRAM is SAIL (Section 11.12). Finally, Section 11.15
  describes the P4 language, and potential IP lookup implementations in programmable router chips like Tofino-3 (Intel
  Corporation, 2022) that leverage both CAM and RAM.
