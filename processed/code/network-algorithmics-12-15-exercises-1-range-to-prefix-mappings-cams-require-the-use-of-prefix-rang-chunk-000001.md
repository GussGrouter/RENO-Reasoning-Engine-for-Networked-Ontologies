# network-algorithmics-12-15-exercises-1-range-to-prefix-mappings-cams-require-the-use-of-prefix-rang (chunk 000001)

# Network Algorithmics — 12.15 Exercises 1. Range to Prefix Mappings: CAMs require the use of prefix ranges, but many rules use general (slice)

- Source: raw/code/pdf/Network.Algorithmics.pdf
- Full-text extraction: processed/code/network-algorithmics-full-layout.txt
- Slice start: PDF page 355
- Slice: from `12.15 Exercises 1. Range to Prefix Mappings: CAMs require the use of prefix ranges, but many rules use general` up to next detected section heading

---

12.15 Exercises
 1. Range to Prefix Mappings: CAMs require the use of prefix ranges, but many rules use general
    ranges. Describe an algorithm that converts an arbitrary range on, say, 16-bit port number fields
    to a logarithmic number of prefix ranges. Describe the prefix ranges produced by the arbitrary but
    common range of greater than 1024. Given a rule R with arbitrary range specifications on port
    numbers, what is the worst-case number of CAM entries required to represent R? Solutions to this
    problem are discussed in Srinivasan et al. (1998, 1999).
 2. Worst-Case Storage for Set-Pruning Tries: Generalize the example of Fig. 12.5 to K fields to
    show that storage in set-pruning-trie approaches can be as bad as O(N k /k).
 3. Improvements to the Grid of Tries: In the grid of tries, the only role played by the destination trie
    is in determining the longest-matching destination prefix. Show how to use other lookup techniques
    to obtain a total search time of (log W + W ) for the destination–source rules instead of 2W .
 4. Reasoning about the Correctness of the Grid of Tries: Given any source and destination IP
    address pair (o, d), let S be the set of nodes (destination-source rules) that (o, d) matches with. A

12.15 Exercises          329
