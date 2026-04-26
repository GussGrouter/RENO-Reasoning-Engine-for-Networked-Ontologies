# network-algorithmics-16-4-maintain-active-counters-using-brick (chunk 000001)

# Network Algorithmics — 16.4 Maintain active counters using BRICK (slice)

- Source: raw/code/pdf/Network.Algorithmics.pdf
- Full-text extraction: processed/code/network-algorithmics-full-layout.txt
- Slice start: PDF page 484
- Slice: from `16.4 Maintain active counters using BRICK` up to next detected section heading

---

16.4 Maintain active counters using BRICK
In all three DRAM backing-store schemes described, namely LCF, LR, and RS, whereas incrementing
a counter can happen at the SRAM speed, reading a counter can happen only at the DRAM speed.
Therefore, they only solve the problem of so-called passive counters in which full counter values in
general do not need to be read out frequently (say not until the end of a measurement interval). Indeed,
the designs of all three schemes exploit this restricted access pattern (P7) to the fullest extent.
