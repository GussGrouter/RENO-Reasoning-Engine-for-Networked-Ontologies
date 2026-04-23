# Network Algorithmics — 17.8 Conclusion Returning to Marcus Ranum’s quote at the start of this chapter, hacking is probably exciting for hackers (slice)

- Source: raw/code/pdf/Network.Algorithmics.pdf
- Full-text extraction: processed/code/network-algorithmics-full-layout.txt
- Slice start: PDF page 538
- Slice: from `17.8 Conclusion Returning to Marcus Ranum’s quote at the start of this chapter, hacking is probably exciting for hackers` up to next detected section heading

---

17.8 Conclusion
Returning to Marcus Ranum’s quote at the start of this chapter, hacking is probably exciting for hackers
and scary for network administrators, who are clearly on different sides of the battlements. However,
hacking is also an exciting phenomenon for practitioners of network algorithmics, there is just so much
to do. Compared to more limited areas, such as accounting and packet lookups, where the basic tasks
have been frozen for several years, the creativity and persistence of hackers promise to produce inter-
esting problems for years to come.
    In terms of technology currently used, the set string–matching algorithms seem useful and may be
ignored by current products. However, other varieties of string matching, such as regular expression
matches, are in use. While the approximate matching techniques are somewhat speculative in terms of
current applications, past history indicates they may be useful in the future.
    Second, the traceback solutions only represent imaginative approaches to the problem. Their re-
quirements for drastic changes to router forwarding make them unlikely to be used for current deploy-
ment as compared to techniques that work in the control plane. Despite this pessimistic assessment, the
underlying techniques seem much more generally useful.
    For example, sampling with a probability inversely proportional to a rough upper bound on the
distance is useful for efficiently collecting input from each of a number of participants without explicit
coordination. Similarly, Bloom filters are useful to reduce the size of hash tables to 5 bits per entry,
at the cost of a small probability of false positives. Given their beauty and potential for high-speed
implementation, such techniques should undoubtedly be part of the designer’s bag of tricks.
    Finally, we described our approach to content-agnostic worm detection using algorithmic tech-
niques. The solution combines existing mechanisms described earlier in this book. While the exper-
imental results on our new method are still preliminary, we hope this example gives the reader some
glimpse into the possible applications of algorithmics to the scary and exciting field of network security.
Table 17.1 presents a summary of the techniques used in this chapter, together with the major principles
involved.
