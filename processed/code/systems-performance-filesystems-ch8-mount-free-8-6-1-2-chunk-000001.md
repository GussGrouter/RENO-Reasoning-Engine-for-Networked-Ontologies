8.6.1 mount
The Linux mount(1) command lists mounted file systems and their mount flags:
$ mount
/dev/nvme0n1p1 on / type ext4 (rw,relatime,discard)
[... further pseudo and virtual file systems omitted ...]

The first line shows that an ext4 file system stored on /dev/nvme0n1p1 is mounted on /, with the
mount flags rw, relatime, and discard. relatime is a performance improving option that reduces
inode access time updates, and the subsequent disk I/O cost, by only updating the access time
when the modify or change times are also being updated, or if the last update was more than a
day ago.

8.6.2

free

The Linux free(1) command shows memory and swap statistics. Typical invocations include
megabyte output (`free -m`) and wide mode (`free -mw`) which splits **buffers** vs **page cache**
instead of a combined **buff/cache** column.

An important column is **available**, which shows how much memory
is available for applications without needing to swap. It takes into account memory that cannot
be reclaimed immediately.
These fields can also be read from /proc/meminfo, which provides them in kilobytes.
