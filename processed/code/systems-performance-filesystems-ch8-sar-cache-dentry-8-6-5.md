8.6.5

sar

The system activity reporter, sar(1), provides various file system statistics and may be configured
to record these periodically. sar(1) is mentioned in various chapters in this book for the different
statistics it provides, and introduced in Section 4.4, sar.

(Omitted in this processed extract: `sar -v 1` sample grid — see PDF.)

The -v option provides columns including:

■ dentunusd: Directory entry cache unused count (available entries)

■ file-nr: Number of file handles in use

■ inode-nr: Number of inodes in use

■ pty-nr: Number of pseudo-terminals in use

There is also a -r option, which prints kbbuffers and kbcached columns for buffer cache and
page cache sizes, in kilobytes.
