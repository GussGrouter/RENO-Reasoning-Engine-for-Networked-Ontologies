# Network Algorithmics — 11.1.1 Prefix notation Internet prefixes are defined using bits and not alphanumerical characters, of up to 32 bits in length. (slice)

- Source: raw/code/pdf/Network.Algorithmics.pdf
- Full-text extraction: processed/code/network-algorithmics-full-layout.txt
- Slice start: PDF page 277
- Slice: from `11.1.1 Prefix notation Internet prefixes are defined using bits and not alphanumerical characters, of up to 32 bits in length.` up to next detected section heading

---

11.1.1 Prefix notation
Internet prefixes are defined using bits and not alphanumerical characters, of up to 32 bits in length.
To confuse matters, however, IP prefixes are often written in dot-decimal notation. For example, at the

                                                                11.1 Introduction to prefix lookups                    251



                   Table 11.1 Principles involved in the various prefix-lookup schemes
                   described in this chapter.
                   Number                    Principle                         Lookup technique
                   P2a, P10    Precompute indices                       Tag switching
                   P2a, P10    Pass indices computed at run time        IP switching
                   P4a         Exploit ATM switch hardware
                   P11         Cache whole IP addresses                 Lookup caches
                   P5          Hardware parallel lookup                 CAMs
                   P4b         Expand prefixes to gain speed            Controlled expansion
                   P13         Strides as a degree of freedom           Variable-stride tries
                   P4b         Compress to gain speed                   Lulea tries
                   P12, P2a    Precomputed count of bits set
                   P15         Use efficient search                     Binary search on prefix lengths
                   P12         Add marker state
                   P2a         Precompute marker watch
                   P2a         Precompute range to prefix matching      Binary search on prefixes



time of writing UCSD has a 16-bit prefix 132.239. Each of the decimal digits between dots represents
a byte. Since in binary 132 is 10000100 and 239 is 11101111, the UCSD prefix in binary can also be
written as 1000010011101111*, where the wildcard character * is used to denote that the remaining
bits do not matter. UCSD hosts have 32-bit IP addresses beginning with these 16 bits.
    Because prefixes can be variable length, a second common way to denote a prefix is by slash notation
of the form A/L. In this case A denotes a 32-bit IP address in dot-decimal notation and L denotes the
length of the prefix. Thus the UCSD prefix can also be denoted as 132.239.0.0/16, where the length 16
indicates that only the first 16 bits (i.e., 132.239) are relevant. A third common way to describe prefixes
is to use a mask in place of an explicit prefix length. Thus the UCSD prefix can also be described as
128.239.0.0 with a mask of 255.255.0.0. Since 255.255.0.0 has 1’s in the first 16 bits, this implicitly
indicates a length of 16 bits.1
    Of these three ways to denote a prefix (binary with a wildcard at the end, slash notation, and mask
notation), the last two are more compact for writing down large prefixes. However, for pedagogical
reasons, it is much easier to use small prefixes as examples and to write them in binary. Thus in this
chapter we will use 01110* to denote a prefix that matches all 32-bit IP addresses that start with 01110.
The reader should easily be able to convert this notation to the slash or mask notation used by vendors.
Also, note that most prefixes are at least 8 bits in length; however, to keep our examples simple, this
chapter uses smaller prefixes.



1 The mask notation is actually more general because it allows noncontiguous masks where the 1’s are not necessarily consec-
utive starting from the left. Such definitions of networks actually do exist. However, they are becoming increasingly uncommon
and are nonexistent in core router prefix tables. Thus we will ignore this possibility in this chapter.

252        Chapter 11 Prefix-match lookups
