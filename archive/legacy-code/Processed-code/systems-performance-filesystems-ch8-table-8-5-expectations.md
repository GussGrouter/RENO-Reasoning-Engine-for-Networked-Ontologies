Consider the general expectations for different benchmarks, which include the total size of the
files (WSS), in Table 8.5.

Gregg illustrates expectations with **128 Gbytes RAM** versus several **working set sizes** (the book table gives **10 Gbyte** vs **1000 Gbyte** file totals as contrasting cases):

- **Random read**, small WSS vs RAM → effectively **cache-resident** (hits dominate).
- **Random read + direct I/O** → bypasses caches → stresses **disk** reads.
- **Large WSS random read** → mostly disk, with **residual cache hits** (example cited: ~12% hits).
- **Sequential read**, small files → largely **cache hits**; **large** sequential reads → mix of prefetch hits and disk reads.
- **Buffered writes** → mostly buffering/cached behavior with **possible blocking** depending on FS semantics.
- **Synchronous writes** → **disk-side** writes in the modeled scenario.

(Omitted in this processed extract: the graphical **Table 8.5** grid — see PDF.)

Some file system benchmark tools do not make clear what they are testing, and may imply a
disk benchmark but use a small total file size, which returns entirely from cache and so does not
test the disks. See Section 8.3.12, Logical vs. Physical I/O, to understand the difference between
testing the file system (logical I/O) and testing the disks (physical I/O).
Some disk benchmark tools operate via the file system by using direct I/O to avoid caching and
buffering. The file system still plays a minor role, adding code path overheads and mapping
differences between file and on-disk placement.
See Chapter 12, Benchmarking, for more on this general topic.
