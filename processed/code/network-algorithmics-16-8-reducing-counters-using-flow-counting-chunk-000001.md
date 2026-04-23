# network-algorithmics-16-8-reducing-counters-using-flow-counting (chunk 000001)

# Network Algorithmics — 16.8 Reducing counters using flow counting (slice)

- Source: raw/code/pdf/Network.Algorithmics.pdf
- Full-text extraction: processed/code/network-algorithmics-full-layout.txt
- Slice start: PDF page 493
- Slice: from `16.8 Reducing counters using flow counting` up to next detected section heading

---

16.8 Reducing counters using flow counting
A second way to reduce the number of counters even further, beyond even threshold compression, is
to realize that many applications do not even require identifying flows above a threshold. Some only
need a count of the number of flows. For example, the Snort ( www.snort.org) intrusion-detection tool
detects port scans by counting all the distinct destinations sent to by a given source and warning if this
amount is over a threshold.

16.8 Reducing counters using flow counting                  467
