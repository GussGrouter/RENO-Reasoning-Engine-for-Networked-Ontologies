# network-algorithmics-13-19-scaling-to-faster-link-speeds (chunk 000001)

# Network Algorithmics — 13.19 Scaling to faster link speeds (slice)

- Source: raw/code/pdf/Network.Algorithmics.pdf
- Full-text extraction: processed/code/network-algorithmics-full-layout.txt
- Slice start: PDF page 402
- Slice: from `13.19 Scaling to faster link speeds` up to next detected section heading

---

13.19 Scaling to faster link speeds
The preceding section focused on how switches can scale in size. This section studies how switches
can scale in speed. Now, it may be that the speeds of individual fiber channels level off at some point.
Many pundits said in the late 1990s that fundamental SRAM and optical limits would limit individual
fiber channels to OC-768 speeds. The capacity of fiber would then be used to produce more individual
channels (e.g., using multiple wavelengths) rather than higher-speed individual channels. The use of
more channels would then affect switching only in terms of increasing port count and can be handled
using the techniques of the previous section.
     This prediction has been mostly correct for the past 20 years: at the time of writing, OC-768
(40 Gbps) is still the highest link speed that is widely used, although (Ethernet) products with 100
Gbps link speeds are available. However, the lessons of history should teach us that it is certainly pos-
sible for individual applications to increase their speed needs and for technology surprisingly to keep
pace by producing faster link speeds that increase from 100 Gbps today to 1 Tbps in, say, 20 years. Thus
it is worthwhile to look for techniques to scale switches in speed. There are three common techniques:
bit slicing, the use of short links, and the use of randomized memory sharing.
