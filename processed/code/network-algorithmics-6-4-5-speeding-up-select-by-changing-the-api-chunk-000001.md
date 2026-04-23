# network-algorithmics-6-4-5-speeding-up-select-by-changing-the-api (chunk 000001)

# Network Algorithmics — 6.4.5 Speeding up select() by changing the API (slice)

- Source: raw/code/pdf/Network.Algorithmics.pdf
- Full-text extraction: processed/code/network-algorithmics-full-layout.txt
- Slice start: PDF page 191
- Slice: from `6.4.5 Speeding up select() by changing the API` up to next detected section heading

---

6.4.5 Speeding up select() by changing the API
The technique described in Section 6.4.4 improves performance considerably by eliminating the first
three (and chief) sources of overhead in select(). However, it does so by maintaining extra state (P12)
in the form of three more sets of descriptors (i.e., H , I , and R) that are also maintained as bitmaps.
This, taken together with the selection set S passed in each call, requires the scanning and updating of
four separate bitmaps.
    In a situation where a large number of connections are present but only a few are active at any
instant, this fundamentally still requires paying some small overhead, proportional to the total number
of connections as opposed to the number of active connections. This is the fourth source of “waste”
enumerated earlier, and it appears unavoidable given the present API.
    Further, as we saw earlier, even the modified fast select() potentially checks a descriptor multiple
times for each event such as a packet arrival (if the application does not consume all the data at once).
Such additional checks are unavoidable because select() provides the state of each descriptor.
    If one looks closely at the interface, what the application fundamentally requires is to be notified
of the stream of events (e.g., file I/O completed, network packet arrived) that causes changes in state.
Event-based notifications appear, on the surface, to have some obvious drawbacks that may have pre-
vented them from being used in the past.

7 The reader may wonder whether it suffices to set I = S. The exercises explore some of the issues with this alternative imple-
mentation.

6.4 Scalable I/O Notification     165
