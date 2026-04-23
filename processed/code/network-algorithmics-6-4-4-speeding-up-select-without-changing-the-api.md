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



    tors (e.g., newly opened sockets) must be checked. A third, subtle point is that even after network
    data has arrived for a socket (e.g., 1500 bytes), the application may read only 200 bytes. Thus a
    descriptor must be checked for readiness even after data first arrives, until there is no more data left
    (i.e., application reads all data) to signify readiness.
    To implement these ideas, besides the hints set H for each thread, the kernel implementation keeps
    two more sets. The first is an interest set I of all descriptors the thread is interested in. The second
    is a set of descriptors R that are known to be ready. The interest set I reflects long-term interest; for
    example, a socket is placed in I the first time it is mentioned in a select() call and is removed only
    when the socket is disconnected or reused. Let the set passed to select() be denoted by S. Then I
    is updated to Inew = Iold ∪ S. Note that this incorporates newly selected descriptors without losing
    previously selected descriptors.7
    Next, the kernel checks only those descriptors that are in Inew but are either (1) in the hints set H
    or (2) not in Iold or (3) in the old ready set Rold . Note that these three predicates reflect the three
    categories discussed two paragraphs back. They represent either recent activity, newly declared
    interest, or unconsumed data resulting from prior activity. The descriptors found by the check to be
    ready are recorded in Rnew . Finally, the select() call returns to the user the elements in Rnew ∩ S.
    This is because the user only cares about the readiness of descriptors specified in the selecting set S.
    As an example, socket 15 may be checked when it is first mentioned in a select() call and so enters
    I ; socket 15 may be checked next when a network packet of 500 bytes arrives, causing socket 15 to
    enter H ; finally, socket 15 may be checked repeatedly as part of R until the application consumes
    all 500 bytes, at which point socket 15 leaves R. The basis of this optimization is P12, adding state
    for speed. The optimization maintains state across calls (P12) to reduce redundant checks.
