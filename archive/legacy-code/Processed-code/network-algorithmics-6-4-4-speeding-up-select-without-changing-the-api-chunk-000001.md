# network-algorithmics-6-4-4-speeding-up-select-without-changing-the-api (chunk 000001)

# Network Algorithmics — 6.4.4 Speeding up select() without changing the API (slice)

- Source: raw/code/pdf/Network.Algorithmics.pdf
- Full-text extraction: processed/code/network-algorithmics-full-layout.txt
- Slice start: PDF page 190
- Slice: from `6.4.4 Speeding up select() without changing the API` up to next detected section heading

---

6.4.4 Speeding up select() without changing the API
Banga and Mogul (Banga and Mogul, 1998) show how to eliminate the first three (of the four) elements
of waste listed earlier.
1. Avoid rebuilding bitmaps from scratch: The application code is changed to use two bitmaps of
   descriptors it is interested in. Bitmap A is used for long-term memory, and bitmap B is used as the
   actual parameter passed by reference to select(). Thus between calls to select(), only the (presumably
   few) descriptors that have changed have to be updated in bitmap A. Before calling select(), bitmap
   A is copied to bitmap B. Because copy can proceed a word at a time, the copy is more efficient
   than a laborious bit-by-bit inspection of the bitmap. In essence, the new bitmap is being computed
   incrementally (P12a).
2. Avoid rechecking all descriptors when select() wakes up: To avoid this overhead, the kernel im-
   plementation is modified such that each thread keeps a hints set H that records sockets that have
   become ready since the last time the thread called select(). The protocol or I/O modules are modified
   such that when new data arrives (network packet, disk I/O completes), the corresponding descriptor
   index is written to the hints set of all threads that are on the select queue for that descriptor. Fi-
   nally, after a thread wakes up in select(), only the descriptors in H are checked. The essence of this
   optimization is passing hints between layers (P9).
3. Avoid rechecking descriptors known not to be ready: The fundamental observation is that a descrip-
   tor that is waiting for data need not be checked until asynchronous notification occurs (e.g., the
   descriptor is placed in hints set H described earlier). Clearly, however, any newly arriving descrip-

164        Chapter 6 Transferring control
