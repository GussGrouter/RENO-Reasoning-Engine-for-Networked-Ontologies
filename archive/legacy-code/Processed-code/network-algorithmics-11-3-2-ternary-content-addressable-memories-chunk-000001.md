# network-algorithmics-11-3-2-ternary-content-addressable-memories (chunk 000001)

# Network Algorithmics — 11.3.2 Ternary content-addressable memories (slice)

- Source: raw/code/pdf/Network.Algorithmics.pdf
- Full-text extraction: processed/code/network-algorithmics-full-layout.txt
- Slice start: PDF page 285
- Slice: from `11.3.2 Ternary content-addressable memories` up to next detected section heading

---

11.3.2 Ternary content-addressable memories
Ternary content-addressable memories (CAMs) that allow “don’t care” bits provide parallel search in
one memory access. Today’s CAMs can search and update in one memory cycle (e.g., 10 nanoseconds)
and handle any combination of 100,000 prefixes. They can even be cascaded to form larger databases.
CAMs, however, have the following issues.
• Density Scaling: One bit in a TCAM requires 10–12 transistors, while an SRAM requires 4–6 tran-
  sistors. Thus TCAMs will also be less dense than SRAMs or take more area. Board area is a critical
  issue for many routers.
• Power Scaling: TCAMs take more power because of the parallel compare. CAM vendors are, how-
  ever, chipping away at this issue by finding ways to turn off parts of the CAM to reduce power.
  Power is a key issue in large core routers.
• Match Arbitration: The match logic in a CAM requires all matching rules to arbitrate so that the
  highest match wins. Older-generation CAMs took around 10 nanoseconds for an operation, but this
  is no longer as much of an issue for modern TCAMs.
• Extra Chips: Given that many routers, such as the Cisco GSR and the Juniper M160, already have
  a dedicated Application Specific Integrated Circuit (ASIC) (or network processor) doing packet

11.4 Unibit tries          259

FIGURE 11.4
Sample prefix database used for the rest of this chapter. Note that the next hops corresponding to each prefix have
been omitted for clarity.

forwarding, it is tempting to integrate the classification algorithm with the lookup without adding
  CAM interfaces and CAM chips. Note that CAMs typically require a bridge ASIC in addition to the
  basic CAM chip and sometimes require multiple CAM chips.
• Programmable Chips with built-in TCAM: By contrast to the problem of extra chips cited by the
  last bullet (that is caused by separate CAM and packet forwarding chips), a game change in recent
  years has been the emergence of programmable chips capable of performing forwarding with TCAM
  built in. For example, Intel’s Tofino-3 (Intel Corporation, 2022) contains 384 TCAM blocks of size
  44 × 512 each, enough to support a large enterprise or data center but not enough for the backbone
  without some algorithmic tricks.
    In summary, CAM technology is rapidly improving and is supplanting algorithmic methods in
smaller routers. However, for larger core routers that may wish to have databases of a million routes in
the future, it may be better to have solutions (as we describe in this chapter) that scale with standard
memory technologies such as SRAM. SRAM is likely always to be cheaper, faster, and denser than
CAMs. While it is clearly too early to predict the outcome of this war between algorithmic and TCAM
methods, even semiconductor manufacturers have hedged their bets and provide both algorithmic and
CAM-based solutions.
