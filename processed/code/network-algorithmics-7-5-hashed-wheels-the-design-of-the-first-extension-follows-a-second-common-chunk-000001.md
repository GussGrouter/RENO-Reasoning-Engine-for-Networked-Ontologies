# network-algorithmics-7-5-hashed-wheels-the-design-of-the-first-extension-follows-a-second-common (chunk 000001)

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
