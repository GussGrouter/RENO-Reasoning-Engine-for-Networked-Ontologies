8.6.6

slabtop

The Linux slabtop(1) command prints information about the kernel slab caches, some of which
are used for file system caches.

(Omitted in this processed extract: full `slabtop -o` ASCII table — see PDF.)

Some file system-related slab caches can be seen in the output: dentry, ext4_inode_cache, and
inode_cache. Without the -o (once) output mode, slabtop(1) will refresh and update the screen.

Slabs relevant to FS work include **buffer_head** (buffer cache), **dentry**, general **inode_cache**,
and **file-system–specific inode caches** (examples in the book: ext3/ext4, XFS, btrfs).

(Omitted in this processed extract: the full per-FS slab name bullet list — see PDF.)

slabtop(1) uses /proc/slabinfo, which exists if CONFIG_SLAB is enabled.
