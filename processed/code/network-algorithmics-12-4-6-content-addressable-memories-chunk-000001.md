# network-algorithmics-12-4-6-content-addressable-memories (chunk 000001)

# Network Algorithmics — 12.4.6 Content-addressable memories (slice)

- Source: raw/code/pdf/Network.Algorithmics.pdf
- Full-text extraction: processed/code/network-algorithmics-full-layout.txt
- Slice start: PDF page 331
- Slice: from `12.4.6 Content-addressable memories` up to next detected section heading

---

12.4.6 Content-addressable memories
Recall from Chapter 11 that a CAM is a content-addressable memory, where the first cell that matches
a data item will be returned using a parallel lookup in hardware. A ternary CAM allows each bit of data
to be either a 0, a 1, or a wildcard. Clearly, ternary CAMs can be used for rule matching as well as for
prefix matching. However, the CAMs must provide wide lengths—for example, the combination of the
IPv4 destination, source, and two port fields is 96 bits.
    Because of problems with algorithmic solutions described in the remainder of this chapter, there
is a general belief that hardware solutions such as ternary CAMs are needed for core routers, despite
the problems (Gupta and McKeown, 2001) of ternary CAMs. There are, however, several reasons to
consider algorithmic alternatives to ternary CAMs, which were presented in Chapter 11.
    Recall that these reasons include the smaller density and larger power of CAMs versus SRAMs
and the difficulty of integrating forwarding logic with the CAM. These problems remain valid when
considering CAMs for classification. An additional issue that arises is the rule multiplication caused by
ranges. In CAM solutions, each range has to be replaced by a potentially large number of prefixes, thus
causing extra entries. Some algorithmic solutions can handle ranges in rules without converting ranges
to rules.
    These arguments are strengthened by the fact that several CAM vendors have also considered algo-
rithmic solutions, motivated by some of the difficulties with CAMs. While better CAM cell designs that
reduce density and power requirements may emerge, it is still important to understand the correspond-
ing advantages and disadvantages of algorithmic solutions. The remainder of the chapter is devoted to
this topic. We will return to combinations of TCAMs and Algorithmic methods to get the best of both
worlds at the end of the chapter.
