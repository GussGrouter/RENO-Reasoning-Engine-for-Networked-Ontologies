# network-algorithmics-5-4-2-io-lite-a-unified-view-of-buffering (chunk 000001)

# Network Algorithmics — 5.4.2 IO-lite: A unified view of buffering (slice)

- Source: raw/code/pdf/Network.Algorithmics.pdf
- Full-text extraction: processed/code/network-algorithmics-full-layout.txt
- Slice start: PDF page 159
- Slice: from `5.4.2 IO-lite: A unified view of buffering` up to next detected section heading

---

5.4.2 IO-lite: A unified view of buffering
While combining emulated copy with mmap() does away with all redundant copying, it still has some
missing optimizations. First, it does nothing to avoid the copying between any CGI application gener-
ating dynamic content and the Web server. Such an application is typically implemented as a separate
process7 that sends dynamic content to the server process via a UNIX pipe. But pipes and other similar
interprocess communication typically involve copying the content between two address spaces.
     Second, notice that none of our schemes so far has done anything about the TCP checksum, an ex-
pensive operation. But if the same file keeps hitting in the cache, other than the first response containing
the HTTP header, all subsequent packets that return the file contents stay the same for every request.
Why can’t the TCP checksums be cached? However, that requires a cache that can somehow map from
packet contents to checksums. This is inefficient in a conventional buffering scheme.
     This section describes a buffering scheme called IO-Lite (Pai et al., 1999b) that generalizes the fbuf
ideas to include the file system. IO-Lite not only eliminates all redundant copies in Fig. 5.1, but also
eliminates redundant copying between the CGI process and the server. It also has a specialized buffer-
numbering scheme that lets a subsystem (such as TCP) efficiently realize that it is resending an earlier
packet.
     IO-Lite is the intellectual descendant of fbufs, though integration with the file system adds sig-
nificantly more complexity. It is first worth noting that fbufs cannot be combined with mmap, unlike
TCOW, which is combined with mmap in Brustoloni (1999). This is because in mmap the application
picks the address and format of an application buffer, while in fbufs the kernel picks the address and
format of a fast buffer. Thus if the application has mapped a file using a buffer in the application virtual
address space, the buffer cannot be sent using an fbuf (kernel address space) without a physical copy.
     Since fbufs cannot be combined with mmap, IO-Lite generalizes fbufs to include the file sys-
tem, making mmap unnecessary. Also, IO-Lite is implemented in a general-purpose operating system
(UNIX), as opposed to fbufs. But setting aside these two differences, IO-Lite borrows all the main ideas
from fbufs: the notion of read-only sharing via immutable buffers (called slices in IO lite), the use of
composite buffers (called buffer aggregates), and the notion of a lazily created cache of buffers for a
path (called an I/O stream in IO-Lite).
     Despite the core similarities, IO-Lite requires solving difficult problems to integrate with the file
system. First, IO-Lite must deal with complex sharing patterns, where several applications may have
buffers pointing to the IO-Lite buffer together with the TCP code and the file server. Second, an IO-Lite
page can be both a VM page (backed up by the paging backup file on disk) and at the same time a
file page (backed up by the actual disk copy of the file). Thus IO-Lite has to implement a complex
replacement policy that integrates both the standard page replacement rules together with file cache
replacement policies (Pai et al., 1999b). Third, the goal of running over UNIX requires careful thought
to find a clean way to integrate IO-Lite without major surgery throughout UNIX.
     Fig. 5.9 shows the steps in responding to the same GET request pictured in Fig. 5.1. When the file
is first read from disk into the file system cache, the file pages are stored as IO-Lite buffers. When the
