# network-algorithmics-7-5-hashed-wheels-the-design-of-the-first-extension-follows-a-second-common (chunk 000002)

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
