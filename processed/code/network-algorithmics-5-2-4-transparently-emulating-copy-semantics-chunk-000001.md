# network-algorithmics-5-2-4-transparently-emulating-copy-semantics (chunk 000001)

# Network Algorithmics — 5.2.4 Transparently emulating copy semantics (slice)

- Source: raw/code/pdf/Network.Algorithmics.pdf
- Full-text extraction: processed/code/network-algorithmics-full-layout.txt
- Slice start: PDF page 150
- Slice: from `5.2.4 Transparently emulating copy semantics` up to next detected section heading

---

5.2.4 Transparently emulating copy semantics
One reaction to the new fbuf API is simply to modify applications to gain performance. It is worth
pointing out that while the changes may be simple and localized, the mental model that a programmer
has of a buffer changes in a fairly drastic way. In the standard UNIX API the application assigns
buffer addresses; in fbufs, the buffers are assigned by the kernel from the fbuf address space. In the
standard UNIX API the programmer can design the buffer layout anyway he pleases, including the use
of contiguous buffers. In fbufs data received from the network can be arbitrarily scattered into pieces

124        Chapter 5 Copying data
