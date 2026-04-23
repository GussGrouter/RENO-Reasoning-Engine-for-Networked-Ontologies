# network-algorithmics-18-1-2-router-algorithmics-in-router-algorithmics-by-contrast-the-bottlenecks-a (chunk 000001)

# Network Algorithmics — 18.1.2 Router algorithmics In router algorithmics, by contrast, the bottlenecks are caused not by structuring artifacts (as in some (slice)

- Source: raw/code/pdf/Network.Algorithmics.pdf
- Full-text extraction: processed/code/network-algorithmics-full-layout.txt
- Slice start: PDF page 542
- Slice: from `18.1.2 Router algorithmics In router algorithmics, by contrast, the bottlenecks are caused not by structuring artifacts (as in some` up to next detected section heading

---

18.1.2 Router algorithmics
In router algorithmics, by contrast, the bottlenecks are caused not by structuring artifacts (as in some
problems in endnode algorithmics) but by the scaling problems caused by the need for global Internets,
together with the fast technological scaling of optical link speeds. Thus the global Internet puts pressure
on router algorithmics because of both population scaling and speed scaling.
    For example, simple caches worked fine for route lookups until address diversity and the need
for CIDR (both caused by population scaling) forced the use of a fast longest-matching prefix. Also,
simple DRAM-based schemes sufficed for prefix lookup (e.g., using expanded tries) until increasing
link speeds forced the use of limited SRAM and compressed tries. Unlike endnodes, routers do not
have protection issues, because they largely execute one code base. The only variability comes from
different packet headers. Hence protection is less of an issue.
    With the two main drivers of router algorithmics in mind, Fig. 18.2 reviews the main router bot-
tlenecks covered in this book together with causes and workarounds. This picture is a more detailed
version of the corresponding figure in Chapter 1.

516       Chapter 18 Conclusions

FIGURE 18.2
Router bottlenecks covered in this book. Associated with each bottleneck is the chapter in which the material is
reviewed, the underlying cause, and one or more sample solutions.

While we have talked about routers as the canonical switching device, many of the techniques
discussed in this book apply equally well to any switching device, such as a bridge (Chapter 10 is
devoted to lookups in bridges) or a gateway. It also applies to intrusion detection systems, firewalls, and
network monitors who do not switch packets but must still work efficiently with packet streams at high
speeds.
