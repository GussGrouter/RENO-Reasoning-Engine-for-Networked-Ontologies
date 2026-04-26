# Network Algorithmics — 7.5 Hashed wheels The design of the first extension follows a second common problem-solving paradigm: (slice)

- Source: raw/code/pdf/Network.Algorithmics.pdf
- Full-text extraction: processed/code/network-algorithmics-full-layout.txt
- Slice start: PDF page 212
- Slice: from `7.5 Hashed wheels The design of the first extension follows a second common problem-solving paradigm:` up to next detected section heading

---

7.5 Hashed wheels
The design of the first extension follows a second common problem-solving paradigm:
Use analogies to derive techniques for the problem at hand from solutions to a different prob-
lem.
    Many ideas first occur by analogy, even if the analogy is not always exact. The previous scheme has
an obvious analogy to inserting an element in an array using the element value as an index. If there is
insufficient memory, can we hash the element value to yield an index? For example, if the table size is
a power of 2, an arbitrary-size timer can easily be divided by the table size; the remainder (low-order
bits) is added to the current time pointer to yield the index within the array. The result of the division
(high-order bits) is stored in a list pointed to by the index.
    In Fig. 7.3 let the table size be 256 and the timer be a 32-bit timer. The remainder on division is the
last 8 bits. Let the value of the last 8 bits be 20. Then the timer index is 10 (current time pointer) +
20 (remainder) = 30. The 24 high-order bits are then inserted into a list that is pointed to by the 30th
element.
    Other methods of hashing are possible. For example, any function that maps a timer value to an
array index could be used. We will defend our choice at the end of Section 7.5. However, we now come
to a fork in the road for our design. Whatever hash function we use, there are two ways to maintain
each list.
    The most straightforward way, which seems best until we look a little closer, is to do Scheme 2
within each bucket. This clearly generalizes Scheme 2 while improving its performance because each of
the “little” lists should be smaller than a single list. Now for the details. Unfortunately, its performance
depends on the hash function because STARTTIMER can be slow because the 24-bit quantity must be
inserted into the correct place in the list. The worst-case latency for STARTTIMER is still O(n).
    Assuming that a worst-case STARTTIMER latency of O(n) is unacceptable, we can maintain each
time list as an unordered list instead of an ordered list. At first glance, this seems like a bad idea. We

186       Chapter 7 Maintaining timers




FIGURE 7.3
Array of lists used by Schemes 5 and 6 for arbitrary-size timers: basically a hash table.


have certainly made STARTTIMER faster; but if lists are unordered, then it seems that per tick we will
have to do a lot more work, seemingly a bad trade-off. Let us look a little closer, however.
    Clearly, STARTTIMER now has a worst-case and average latency of O(1). PERTICKBOOKKEEPING
now does take longer. Every timer tick, we increment the pointer (mod T ableSize); if there is a list
there, we must decrement the high-order bits for every element in the array, exactly as in Scheme
1. However, if the hash table has the property described earlier, then the average size of the list will
be O(1).
    We can make a stronger statement about the average behavior regardless of how the hash distributes.
This is perhaps not quite so obvious. Notice that every T ableSize ticks, we decrement once all timers
that are still living. Thus for n timers, we do n/T ableSize work on average per tick. If n < T ableSize,
then we do O(1) work on average per tick. If all n timers hash into the same bucket, then every
T ableSize ticks we do O(n) work, but for intermediate ticks we do O(1) work. What this means
is that if we want to keep the per-tick work small and bounded, we simply arrange that the number of
buckets is some factor larger than the maximum number of concurrent timers we support. We can even
reduce this work as much as we want by increasing the number of buckets. This is an example of a
result about amortized complexity, which is stronger than a result about average complexity.
    Thus the hash distribution in Scheme 6 controls only the “burstiness” (variance) of the latency
of PERTICKBOOKKEEPING, not the average latency. Since the worst-case latency of PERTICK-
BOOKKEEPING is always O(n) (all timers expire at the same time), we believe that the choice of
hash function for Scheme 6 is insignificant. Obtaining the remainder after dividing by a power of 2 is
cheap and, consequently, recommended. Further, using an arbitrary hash function to map a timer value
into an array index would require PERTICKBOOKKEEPING to compute the hash on each timer tick,
which would make it more expensive.

                                                                           7.6 Hierarchical wheels   187




FIGURE 7.4
Hierarchical set of arrays of lists used by Scheme 7 to “map” time more efficiently.
