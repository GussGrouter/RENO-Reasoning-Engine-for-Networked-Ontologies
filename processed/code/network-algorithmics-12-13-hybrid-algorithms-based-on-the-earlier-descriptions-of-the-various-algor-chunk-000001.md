# network-algorithmics-12-13-hybrid-algorithms-based-on-the-earlier-descriptions-of-the-various-algor (chunk 000001)

# Network Algorithmics — 12.13 Hybrid algorithms Based on the earlier descriptions of the various algorithms it should be clear that different algorithms (slice)

- Source: raw/code/pdf/Network.Algorithmics.pdf
- Full-text extraction: processed/code/network-algorithmics-full-layout.txt
- Slice start: PDF page 353
- Slice: from `12.13 Hybrid algorithms Based on the earlier descriptions of the various algorithms it should be clear that different algorithms` up to next detected section heading

---

12.13 Hybrid algorithms
Based on the earlier descriptions of the various algorithms it should be clear that different algorithms
(and even technlogies like CAMs) can do well for different databases. Thus it is natural to consider

12.14 Conclusions          327

Hybrid Schemes. For example, CAMs are fast but use a great deal of power and updates can be slow
for rules with ranges. Can TCAMs be combined with algorithmic schemes to get some of the advantages
of both schemes? We now sample a few of these ideas:
    Combining TCAMs and Algorithmic Schemes: SmartPC (Ma and Banerjee, 2012) reduces the
power consumption of TCAMs by pre-classifying a packet on two header fields, source and destination
IP addresses. The packet is only sent to TCAM if there is a match, thus only a small portion of TCAM
needs to be activated. The authors show that SmartPC reduces average power by about 90% on real
and synthetic classifiers. SAX-PAC (Kogan et al., 2014) exploits order independence to reduce the
cost (lookup time or memory) of adding additional range or prefix fields using a hybrid software and
TCAM-based approach. The order independent rules are implemented in software using linear memory
and logarithmic worst case lookup time, whereas the rest of the rules are in TCAM. The paper shows
that on real-life classifiers from Cisco Systems, about 90% of rules are handled in software and only
the remaining 10% of rules need to be stored in TCAM.
    TreeCAM (Vamanan and Vijaykumar, 2011) is a hybrid decision tree and TCAM-based approach
for improving the update complexity (not power) of decision trees without sacrificing lookup perfor-
mance. TreeCAM employs two versions of decision trees: a coarse version with a few thousand rules
per leaf achieves efficient lookups and a fine version with a few tens of rules per leaf reduces update
effort. Note that many of the papers that combine TCAM and algorithmic schemes are quite feasible to
implement with the advent of pipelined programmable hardware architectures like the Tofino-3 (Intel
Corporation, 2022) that have stages that contain both RAM and CAM.
    Other combinations: HybridCuts (Li and Li, 2013) uses a combination of decomposition and
decision-tree techniques to improve both storage and performance. HybridCuts uses memory com-
parable to EffiCuts, but outperforms EffiCuts in terms of memory accesses without the added lookup
complexity in each node. Finally, CutTSS (Li et al., 2020) combines the good update performance of
tuple space search with the quick lookup time of Decision Trees. The CutTSS paper (Li et al., 2020)
also has pointers to other more recent papers in packet classification.
