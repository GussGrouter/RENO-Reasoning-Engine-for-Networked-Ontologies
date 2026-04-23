# network-algorithmics-1-2-5-cleaning-up-we-have-postponed-one-thorny-issue-to-this-point-the-termina (chunk 000001)

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
