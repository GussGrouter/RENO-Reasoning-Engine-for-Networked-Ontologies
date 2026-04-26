# network-algorithmics-11-16-conclusions-it-is-important-to-gain-some-perspective-after-the-large-num (chunk 000001)

# Network Algorithmics — 11.16 Conclusions It is important to gain some perspective after the large number of isolated lookup variants described in (slice)

- Source: raw/code/pdf/Network.Algorithmics.pdf
- Full-text extraction: processed/code/network-algorithmics-full-layout.txt
- Slice start: PDF page 316
- Slice: from `11.16 Conclusions It is important to gain some perspective after the large number of isolated lookup variants described in` up to next detected section heading

---

11.16 Conclusions
It is important to gain some perspective after the large number of isolated lookup variants described in
this chapter. Thus we conclude with a summary of the state of the art in lookups, and a survey of the
common principles used in their design.
  State of the Art in Lookups: Lookup schemes are coming under severe pressure in core routers
as both table sizes (up to 1 million prefixes) and speed (several Terabits of aggregate throughput)
ratchet upwards. MPLS, once thought to be a way to finesse lookups, is now mostly used to avoid
packet classification for traffic engineering purposes. CAMs are nibbling away at even the core router
space with chips like Tofino-3, but still do not scale to wide area database sizes (though techniques

290      Chapter 11 Prefix-match lookups
