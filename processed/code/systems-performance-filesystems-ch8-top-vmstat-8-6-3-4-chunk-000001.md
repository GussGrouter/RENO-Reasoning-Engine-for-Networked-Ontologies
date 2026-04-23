8.6.3

top

Some versions of the top(1) command include file system cache details. The Linux version can
echo the **buff/cache** and **available (avail Mem)** statistics also shown by free(1).

See Chapter 6, CPUs, for more about top(1).

8.6.4

vmstat

The vmstat(1) command, like top(1), also may include details on the file system cache. For more
details on vmstat(1), see Chapter 7, Memory.

Example: `vmstat 1` prints periodic rows; the **buff** column shows the buffer cache size, and
**cache** shows the page cache size, both in kilobytes.

(Omitted in this processed extract: full numeric sample grid — see PDF.)
