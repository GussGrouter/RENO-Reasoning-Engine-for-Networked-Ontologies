# network-algorithmics-9-1-buffer-management-all-protocols-have-to-manage-buffers-in-particular-pac (chunk 000001)

# Network Algorithmics — 9.1 Buffer management All protocols have to manage buffers. In particular, packets travel up and down the protocol stack in (slice)

- Source: raw/code/pdf/Network.Algorithmics.pdf
- Full-text extraction: processed/code/network-algorithmics-full-layout.txt
- Slice start: PDF page 239
- Slice: from `9.1 Buffer management All protocols have to manage buffers. In particular, packets travel up and down the protocol stack in` up to next detected section heading

---

9.1 Buffer management
All protocols have to manage buffers. In particular, packets travel up and down the protocol stack in
buffers. The operating system must provide services to allocate and deallocate buffers. This requires
managing free memory; finding memory of the appropriate size can be challenging, especially because
buffer allocation must be done in real time. Section 9.1.1 describes a simple systems solution for doing
buffer allocation at high speeds, even for requests of variable sizes.
    If the free space must be shared between a number of connections or users, it may also be important
to provide some form of fairness so that one user cannot hog all the resources. While static limits work,
in some cases it may be preferable to allow dynamic buffer limits, where a process in isolation can get
as many buffers as it needs but relinquishes extra buffers when other processes arrive. Section 9.1.2
describes two dynamic buffer-limiting schemes that can be implemented at high speeds.
