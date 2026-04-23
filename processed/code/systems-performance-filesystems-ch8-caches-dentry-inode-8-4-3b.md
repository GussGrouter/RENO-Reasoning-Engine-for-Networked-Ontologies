Dentry Cache
The dentry cache (Dcache) remembers mappings from directory entry (struct dentry) to VFS
inode, similar to an earlier Unix directory name lookup cache (DNLC). The Dcache improves the
performance of path name lookups (e.g., via open(2)): when a path name is traversed, each name
lookup can check the Dcache for a direct inode mapping, instead of stepping through the directory contents. The Dcache entries are stored in a hash table for fast and scalable lookup (hashed
by the parent dentry and directory entry name).
Performance has been further improved over the years, including with the read-copy-updatewalk (RCU-walk) algorithm [Corbet 10]. This attempts to walk the path name without updating
dentry reference counts, which were causing scalability issues due to cache coherency with high
rates of path name lookups on multi-CPU systems. If a dentry is encountered that isn’t in the
cache, RCU-walk reverts to the slower reference-count walk (ref-walk), since reference counts
will be necessary during file system lookup and blocking. For busy workloads, it’s expected that
the dentry data will likely be cached, and the RCU-walk approach will succeed.
The Dcache also performs negative caching, which remembers lookups for nonexistent entries.
This improves the performance of failed lookups, which commonly occur when searching for
shared libraries.
The Dcache grows dynamically, shrinking via LRU (least recently used) when the system needs
more memory. Its size can be seen via /proc.

Inode Cache
This cache contains VFS inodes (struct inodes), each describing properties of a file system object,
many of which are returned via the stat(2) system call. These properties are frequently accessed
for file system workloads, such as checking permissions when opening files, or updating timestamps during modification. These VFS inodes are stored in a hash table for fast and scalable
lookup (hashed by inode number and file system superblock), although most of the lookups will
be done via the Dentry cache.
The inode cache grows dynamically, holding at least all inodes mapped by the Dcache. When
there is system memory pressure, the inode cache will shrink, dropping inodes that do not have
associated dentries. Its size can be seen via the /proc/sys/fs/inode* files.

