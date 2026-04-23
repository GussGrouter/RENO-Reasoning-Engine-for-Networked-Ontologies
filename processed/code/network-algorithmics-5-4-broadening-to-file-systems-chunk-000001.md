# network-algorithmics-5-4-broadening-to-file-systems (chunk 000001)

# Network Algorithmics — 5.4 Broadening to file systems (slice)

- Source: raw/code/pdf/Network.Algorithmics.pdf
- Full-text extraction: processed/code/network-algorithmics-full-layout.txt
- Slice start: PDF page 158
- Slice: from `5.4 Broadening to file systems` up to next detected section heading

---

5.4 Broadening to file systems
So far this chapter has concentrated only on avoiding redundant copies that occur while sending data
between an application (such as a Web server) and the network. However, Fig. 5.1 shows that even after
removing all redundant overhead due to network copying, there are still redundant copies involving
the file system. Thus in this section, we will cast our net more widely. We leverage our intellectual
investment by extending the copy-avoidance techniques discussed so far to the file system.
    Recall from Fig. 5.1 that to process a request for File X, the server may have to read X from disk
(Copy 1) into a kernel buffer (representing the file cache) and then make a copy from the file cache to
the application buffer (Copy 2). Copy 1 goes out of the picture if the file is already in cache, a reasonable
assumption for popular files in a server with sufficient memory. The main goal is to remove Copy 2.
Note that in a Web server unnecessarily doubling the number of copies not only halves the effective bus
bandwidth but potentially halves the size of the server cache. This in turn reduces server performance
by causing a larger miss rate, which implies that a larger fraction of documents is served at disk speeds
and not bus speeds.
    This section surveys three techniques for removing the redundant file system copy (Copy 2). Sec-
tion 5.4.1 describes a technique called shared memory mapping that can reduce Copy 2 but is not well
integrated with the network subsystem. Section 5.4.2 describes IO-Lite, essentially a generalization of
fbufs to include the file system. Finally, Section 5.4.3 describes a technique called I/O splicing that is
used by many commercial Web servers.
