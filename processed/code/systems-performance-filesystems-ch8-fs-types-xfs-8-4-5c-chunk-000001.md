XFS
XFS was created by Silicon Graphics in 1993 for their IRIX operating system, to solve scalability
limitations in the previous IRIX file system, EFS (which was based on FFS) [Sweeney 96]. XFS
patches were merged into the Linux kernel in the early 2000s. Today, XFS is supported by most
Linux distributions and can be used for the root file system. Netflix, for example, uses XFS for its
Cassandra database instances due to its high performance for that workload (and uses ext4 for
the root file system).

The author then enumerates many named mechanisms (allocation groups, extents, separate journal
devices, stripe-aware allocation, delayed allocation, online defrag, etc.) as bullet points.

(Omitted in this processed extract: the feature bullet catalog—see PDF. Mkfs options are documented
in mkfs.xfs(8); advanced counters live under /proc/fs/xfs/stat on Linux.)

Configurable features are documented in the mkfs.xfs(8) man page. Internal performance data
for XFS can be seen via /proc/fs/xfs/stat. The data is designed for advanced analysis: for more
information see the XFS website [XFS 06][XFS 10].
