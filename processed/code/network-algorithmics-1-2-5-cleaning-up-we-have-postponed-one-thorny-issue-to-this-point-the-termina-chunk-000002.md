# network-algorithmics-1-2-5-cleaning-up-we-have-postponed-one-thorny-issue-to-this-point-the-termina (chunk 000002)

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
