8.4.4

File System Features

Additional key file system features that affect performance are described here.

Block vs. Extent
Block-based file systems store data in fixed-size blocks, referenced by pointers stored in metadata blocks. For large files, this can require many block pointers and metadata blocks, and the
placement of blocks may become scattered, leading to random I/O. Some block-based file systems attempt to place blocks contiguously to avoid this. Another approach is to use variable block
sizes, so that larger sizes can be used as the file grows, which also reduces the metadata overhead.
Extent-based file systems preallocate contiguous space for files (extents), growing them as
needed. These extents are variable in length, representing one or many contiguous blocks.

375

376

Chapter 8 File Systems

This improves streaming performance and can improve random I/O performance as file data
is localized. It also improves metadata performance as there are fewer objects to track, without
sacrificing space of unused blocks in an extent.

Journaling
A file system journal (or log) records changes to the file system so that, in the event of a system
crash or power failure, changes can be replayed atomically—either succeeding in their entirety
or failing. This allows file systems to quickly recover to a consistent state. Non-journaled file
systems can become corrupted during a system crash, if data and metadata relating to a change
were incompletely written. Recovering from such a crash requires walking all file system structures, which can take hours for large (terabytes) file systems.
The journal is written to disk synchronously, and for some file systems it can be configured
to use a separate device. Some journals record both data and metadata, which consumes more
storage I/O resources as all I/O is written twice. Others write only metadata and maintain data
integrity by employing copy-on-write.
There is a file system type that consists of only a journal: a log-structured file system, where all
data and metadata updates are written to a continuous and circular log. This optimizes write
performance, as writes are always sequential and can be merged to use larger I/O sizes.

Copy-on-Write
A copy-on-write (COW) file system does not overwrite existing blocks but instead follows these
steps:
1. Write blocks to a new location (a new copy).
2. Update references to new blocks.
3. Add old blocks to the free list.
This helps maintain file system integrity in the event of a system failure, and also improves
performance by turning random writes into sequential ones.
When a file system approaches capacity, COW can cause a file’s on-disk data layout to be fragmented, reducing performance (especially for HDDs). File system defragmentation, if available,
may help restore performance.

Scrubbing
This is a file system feature that asynchronously reads all data blocks and verifies checksums to
detect failed drives as early as possible, ideally while the failure is still recoverable due to RAID.
However, scrubbing read I/O can hurt performance, so it should be issued at a low priority or at
times of low workload.

Other Features
Other file system features that can affect performance include snapshots, compression, built-in
redundancy, deduplication, trim support, and more. The following section describes various
such features for specific file systems.

