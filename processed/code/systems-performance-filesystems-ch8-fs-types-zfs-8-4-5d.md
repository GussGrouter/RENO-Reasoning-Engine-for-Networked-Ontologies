ZFS
ZFS was developed by Sun Microsystems and released in 2005, combining the file system with
the volume manager and including numerous enterprise features, making it an attractive choice
for file servers (filers). ZFS was released as open source and is in use by several operating systems,
although typically as an add-on because ZFS uses the CDDL license. Most development is occurring
in the OpenZFS project, which in 2019 announced support for Linux as the primary OS
[Ahrens 19]. While it is seeing growing support and usage in Linux, there is still resistance due
to the source license, including from Linus Torvalds [Torvalds 20a].

Gregg follows with a long bullet list of ZFS subsystems (pools/RAID classes, COW, TXGs, ARC,
prefetch streams, snapshots, ZIO pipeline, compression, SLOG/L2ARC, deduplication, etc.).

(Omitted in this processed extract: the full feature grid—see PDF.)

There is a behavior of ZFS that can reduce performance in comparison with other file systems:
by default, ZFS issues cache flush commands to the storage devices, to ensure that writes have
completed in the case of a power outage. This is one of the ZFS integrity features; however, it
comes at a cost: it can induce latency for ZFS operations that must wait for the cache flush.

Gregg also warns that data deduplication can inflate device I/O badly once its hash table no longer
fits in memory (initially aimed only at workloads where the table is expected to remain RAM-resident).
