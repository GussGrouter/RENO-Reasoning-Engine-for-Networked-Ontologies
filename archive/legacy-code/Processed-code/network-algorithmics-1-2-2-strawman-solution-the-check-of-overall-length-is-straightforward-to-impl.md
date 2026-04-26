# Network Algorithmics — 1.2.2 Strawman solution The check of overall length is straightforward to implement, so we concentrate on checking for a (slice)

- Source: raw/code/pdf/Network.Algorithmics.pdf
- Full-text extraction: processed/code/network-algorithmics-full-layout.txt
- Slice start: PDF page 35
- Slice: from `1.2.2 Strawman solution The check of overall length is straightforward to implement, so we concentrate on checking for a` up to next detected section heading

---

1.2.2 Strawman solution
The check of overall length is straightforward to implement, so we concentrate on checking for a
prevalence of suspicious characters. The first strawman solution is illustrated in Fig. 1.4. The chip

                                                  1.2 The techniques: network algorithmics                        9




FIGURE 1.4
Strawman solution for detecting an evil packet by counting occurrences of each character via a count array (middle)
and then comparing in a final pass with an array of acceptable thresholds (left).


maintains two arrays, T and C, with 256 elements each, one for each possible value of an 8-bit character.
The threshold array, T -, contains the acceptable percentage (as a fraction of the entire URL length) for
each character. If the occurrences of a character in an actual URL fall above this fraction, the packet
should be flagged. Each character can have a different threshold.
    The count array, C, in the middle, contains the current count C[i] for each possible character i.
When the chip reads a new character “i” in the URL, it increments C[i] by 1. C[i] is initialized to 0 for
all values of i when a new packet is encountered. The incrementing process starts only after the chip
parses the HTTP header and recognizes the start of a URL.
    In HTTP, the end of a URL is signified by two newline characters; thus one can tell the length of the
URL only after parsing the entire URL string. Thus, after the end of the URL is encountered, the chip
makes a final pass over the array C. If C[ j ] ≥ L · T [ j ] for any j , where L is the length of the URL,
the packet is flagged.
    Assume that packets are coming into the monitor at high speed and that we wish to finish processing
a packet before the next one arrives. This requirement, called wire-speed processing, is very common in
networking; it prevents processing backlogs even in the worst case. To meet wire-speed requirements,
ideally the chip should do a small constant number of operations for every URL byte. Assume the main
step of incrementing a counter can be done in the time to receive a byte.
    Unfortunately, the two passes over the array, first to initialize it and then to check for threshold
violations, make this design slow. Minimum packet sizes are often as small as 40 bytes and include
only network headers. Adding 768 more operations (1 write and 1 read to each element of C, and 1
read of T for each of 256 indices) can make this design infeasible.
