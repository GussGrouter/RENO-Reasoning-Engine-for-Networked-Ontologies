# network-algorithmics-11-15-2-ip-lookups-in-the-p4-model (chunk 000001)

# Network Algorithmics — 11.15.2 IP Lookups in the P4 Model (slice)

- Source: raw/code/pdf/Network.Algorithmics.pdf
- Full-text extraction: processed/code/network-algorithmics-full-layout.txt
- Slice start: PDF page 315
- Slice: from `11.15.2 IP Lookups in the P4 Model` up to next detected section heading

---

11.15.2 IP Lookups in the P4 Model
At first glance, chips like the Tofino-3 that use the RMT model trivialize IP lookup because they have
plenty of CAM. However, the amount of CAM in these chips do not scale to wide area databases. Could
we do better by combining algorithmic methods with TCAM?
    For instance, MashUp (Rios and Varghese, 2022) is a a “mash up” of algorithmic and hardware
techniques that uses a tree of TCAM and SRAM blocks. While a tree of CAMs has been used for
reducing power consumption or update costs (e.g., CoolCAM (Zane et al., 2003) and TreeCAM (Va-
manan and Vijaykumar, 2011)), MashUp focuses instead on reducing TCAM bits. It can also easily be
implemented in modern reconfigurable pipeline chips such as Tofino-3 (Intel Corporation). As a conse-
quence, MashUp can extend the reach of chips like Tofino-3 to the backbone IPv4 and IPv6 databases,
or to much larger data centers than is possible using today’s solution of a single logical TCAM.

11.16 Conclusions            289
