btrfs
The B-tree file system (btrfs) is based on copy-on-write B-trees. This is a modern file system and
volume manager combined architecture, similar to ZFS, and is expected to eventually offer
a similar feature set. Current features include pooled storage, large capacity, extents, COW,
volume growth and shrinking, subvolumes, block device addition and removal, snapshots,
clones, compression, and various checksums (including crc32c, xxhash64, sha256, and blake2b).
Development was begun by Oracle in 2007.

The author then lists “key performance features” as bullets (pooled storage + RAID modes,
COW write grouping, online balancing, extents, snapshots, compression, journaling for synchronous COW).

(Omitted in this processed extract: the feature bullet list—see PDF.)

Planned performance-related features include RAID-5 and 6, object-level RAID, incremental
dumps, and data deduplication.
