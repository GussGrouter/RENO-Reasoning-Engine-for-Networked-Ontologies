# network-algorithmics-16-7-reducing-counters-using-threshold-aggregation (chunk 000001)

# Network Algorithmics — 16.7 Reducing counters using threshold aggregation (slice)

- Source: raw/code/pdf/Network.Algorithmics.pdf
- Full-text extraction: processed/code/network-algorithmics-full-layout.txt
- Slice start: PDF page 491
- Slice: from `16.7 Reducing counters using threshold aggregation` up to next detected section heading

---

16.7 Reducing counters using threshold aggregation
The last two schemes reduce the width of the SRAM counter table shown in Fig. 16.1. The next two
approaches reduce the height of the SRAM counter table. They rely on the quote from Einstein (which
opened the chapter) that not all the information in the final counter table may be useful to an application,
at least for some applications. Effectively, by relaxing the specification (P3), the number of counters
that need to be maintained can be reduced.
    One simple way to compress the counter table is shown in Fig. 16.8. The idea is to pick a threshold,
say, 0.1% of the traffic, that can possibly be sent in the measurement interval and to keep counters only
for such “large” flows. Since, by definition, there can be at most 1000 such flows, the final table reduces
to 1000 flow ID, counter pairs, which can be indexed using a CAM. Note that small CAMs are perfectly
feasible at high speed.
    This form of compression is reasonable for applications that only want counters above a threshold.
For example, just as most cell phone plans charge a fixed price up to a threshold and a usage-based fee

16.7 Reducing counters using threshold aggregation                    465

FIGURE 16.8
Using threshold compression to reduce the number of counters stored.
