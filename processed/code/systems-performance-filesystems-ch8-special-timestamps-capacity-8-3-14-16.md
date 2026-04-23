8.3.14

Special File Systems

The intent of a file system is usually to store data persistently, but there are special file system
types used on Linux for other purposes, including temporary files (/tmp), kernel device paths
(/dev), system statistics (/proc), and system configuration (/sys).4

8.3.15

Access Timestamps

Many file systems support access timestamps, which record the time that each file and directory
was accessed (read). This causes file metadata to be updated whenever files are read, creating a
write workload that consumes disk I/O resources. Section 8.8, Tuning, shows how to turn off
these updates.
Some file systems optimize access timestamp writes by deferring and grouping them to reduce
interference with the active workload.

8.3.16 Capacity
When file systems fill, performance may degrade for a couple of reasons. First, when writing new
data, it may take more CPU time and disk I/O to find free blocks on disk.5 Second, areas of free
space on disk are likely to be smaller and more sparsely located, degrading performance due to
smaller I/O or random I/O.
How much of a problem this is depends on the file system type, its on-disk layout, its use of
copy-on-write, and its storage devices. Various file system types are described in the next
section.

For a list of special file system types on Linux that do not use storage devices: grep '^nodev' /proc/
filesystems

4

5

ZFS, for example, switches to a different and slower free-block-finding algorithm when the pool storage exceeds a
threshold (originally 80%, later 99%). See “Pool performance can degrade when a pool is very full” [Oracle 12].

371

372

Chapter 8 File Systems

