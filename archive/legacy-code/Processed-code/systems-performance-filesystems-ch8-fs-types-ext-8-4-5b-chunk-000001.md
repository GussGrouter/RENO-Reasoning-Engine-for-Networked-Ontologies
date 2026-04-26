ext3
The Linux extended file system (ext) was developed in 1992 as the first file system for Linux
and its VFS, based on the original Unix file system. The second version, ext2 (1993), included
multiple timestamps and cylinder groups from FFS. The third version, ext3 (1999), included file
system growth and journaling.

Gregg then lists “key performance features” for ext3 and ext4 as a bullet catalog (journal modes,
Orlov allocator, directory indexes, extents, delayed allocation, faster fsck, etc.), plus a `/sys/fs/ext4/features`
example listing.

(Omitted in this processed extract: the per-feature bullet grid and sysfs feature-flag sample—see PDF
for the full taxonomy. The structural themes largely repeat §8.4.4 “File System Features”—journaling tradeoffs, extents, and allocation grouping.)

ext4
The Linux ext4 file system was released in 2008, extending ext3 with new features and performance improvements: extents, large capacity, preallocation with fallocate(2), delayed allocation,
journal checksumming, faster fsck, multiblock allocator, nanosecond timestamps, and
snapshots.

Configurable features are documented in the mke2fs(8) man page. Some features, such as
extents, can also be applied to ext3 file systems.
