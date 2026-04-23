# Network Algorithmics — 1.2.5 Cleaning up We have postponed one thorny issue to this point. The terminal loop has been eliminated while leaving (slice)

- Source: raw/code/pdf/Network.Algorithmics.pdf
- Full-text extraction: processed/code/network-algorithmics-full-layout.txt
- Slice start: PDF page 38
- Slice: from `1.2.5 Cleaning up We have postponed one thorny issue to this point. The terminal loop has been eliminated while leaving` up to next detected section heading

---

1.2.5 Cleaning up
We have postponed one thorny issue to this point. The terminal loop has been eliminated while leaving
the initial initialization loop. To handle this, note that the chip has spare time for initialization after
parsing the URL of the current packet and before encountering the URL of the next packet.
    Unfortunately, packets can be as small as 50 bytes, even with an HTTP header. Thus even assuming
a slack of 40 non-URL bytes other than the 10 bytes of the URL, this still does not suffice to initialize

12        Chapter 1 Introducing network algorithmics



a 256-byte array without paying 256/40 = 6 more operations per byte than during the processing of
a URL. As in the URL processing loop, each initialization step requires a Read and Write of some
element of the coalesced array.
    A trick among lazy people is to postpone work until it is absolutely needed, in the hope that it may
never be needed. Note that, strictly speaking, the chip does not need to initialize a C[i] until character i
is accessed for the first time in a subsequent packet. But how can the chip tell that it is seeing character
i for the first time?
    To implement lazy evaluation, each memory word representing an entry in the coalesced array must
be expanded to include, say, a 3-bit generation number G[i]. The generation number can be thought of
as a value of clock time measured in terms of packets encountered so far, except that it is limited to 3
bits. Thus, the chip keeps an additional register g, besides the extra G[i] for each i, that is 3 bits long;
g is incremented mod 8 for every packet encountered. In addition, every time C[i] is updated, the chip
updates G[i] as well to reflect the current value of g.
    Given the generation numbers, the chip need not initialize the count array after the current packet has
been processed. However, consider the case of a packet whose generation number is h, which contains
a character i in its URL. When the chip encounters i while processing the packet, the chip reads C[i]
and G[i] from the Count array. If G[i] = h, this clearly indicates that entry i was last accessed by an
earlier packet and has not been subsequently initialized. Thus the logic will write back the value of C[i]
as 1 (initialization plus increment) and set G[i] to h. This is shown in Fig. 1.7.
    The careful reader will immediately object. Since the generation number is only 3 bits, once the
value of g wraps around, there can be aliasing. Thus if G[i] is 5 and entry i is not accessed until eight
more packets have gone by, g will have wrapped around to 5. If the next packet contains i, C[i] will
not be initialized and the count will (wrongly) accumulate the count of i in the current packet together
with the count that occurred eight packets in the past.
    The chip can avoid such aliasing by doing a separate “scrubbing” loop that reads the array and
initializes all counters with outdated generation numbers. For correctness, the chip must guarantee one
complete scan through the array for every eight packets processed. Given that one has a slack of (say)
40 non-URL bytes per packet, this guarantees a slack of 320 non-URL bytes after eight packets, which
suffices to initialize a 256-element array using one Read and one Write per byte, whether the byte is a




FIGURE 1.7
The final solution with generation numbers to finesse an initialization loop.

                                              1.2 The techniques: network algorithmics                  13



URL or a non-URL byte. Clearly, the designer can gain more slack, if needed, by increasing the bits in
the generation number, at the cost of slightly increased storage in the array.
    The chip, then, must have two states: one for processing URL bytes and one for processing non-
URL bytes. When the URL is completely processed, the chip switches to the “Scrub” state. The chip
maintains another register, which points to the next array entry s to be scrubbed. In the scrub state,
when a non-URL character is received, the chip reads entry s in the coalesced array. If G[s] = g, G[s]
is reset to g and C[s] is initialized to 0.
    Thus the use of 3 extra bits of generation number per array entry has reduced initialization process-
ing cycles, trading processing for storage. Altogether a coalesced array entry is now only 32 bits, 15
bits for a counter, 14 bits for a threshold shift value, and 3 bits for a generation number. Note that the
added initialization check needed during URL byte processing does not increase memory references
(the bottleneck) but adds slightly to the processing logic. In addition, it requires two more chip registers
to hold g and s, a small additional expense.
