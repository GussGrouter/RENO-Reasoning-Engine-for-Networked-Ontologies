8.4.5

Architecture

File System Types

Much of this chapter describes generic characteristics that can be applied to all file system
types. The following sections summarize specific performance features for commonly used file
systems. Their analysis and tuning are covered in later sections.

FFS
Many file systems are ultimately based on the Berkeley fast file system (FFS), which was designed
to address issues with the original Unix file system.6 Some background can help explain the
state of file systems today.
The original Unix file system on-disk layout consisted of a table of inodes, 512-byte storage
blocks, and a superblock of information used when allocating resources [Ritchie 74][Lions 77].
The inode table and storage blocks divided disk partitions into two ranges, which caused performance issues when seeking between them. Another issue was the use of the small fixed-block
size, 512 bytes, which limited throughput and increased the amount of metadata (pointers)
required to store large files. An experiment to double this to 1024 bytes, and the bottleneck then
encountered was described by [McKusick 84]:
Although the throughput had doubled, the old file system was still using only about
four percent of the disk bandwidth. The main problem was that although the free
list was initially ordered for optimal access, it quickly became scrambled as files were
created and removed. Eventually the free list became entirely random, causing files
to have their blocks allocated randomly over the disk. This forced a seek before every
block access. Although old file systems provided transfer rates of up to 175 kilobytes
per second when they were first created, this rate deteriorated to 30 kilobytes per
second after a few weeks of moderate use because of this randomization of data block
placement.
This excerpt describes free list fragmentation, which decreases performance over time as the file
system is used.

Figure 8.9 Cylinder groups

6

The original Unix file system is not to be confused with later file systems called UFS, which are based on FFS.

377

378

Chapter 8 File Systems

FFS improved performance by splitting the partition into numerous cylinder groups, shown in
Figure 8.9, each with its own inode array and data blocks. File inodes and data were kept within
one cylinder group where possible, as pictured in Figure 8.9, reducing disk seek. Other related
data was also placed nearby, including the inodes for a directory and its entries. The design of an
inode was similar, with a hierarchy of pointers and data blocks, as pictured in Figure 8.10 (triply
indirect blocks, which have three levels of pointers, are not shown here) [Bach 86].

Figure 8.10 Inode data structure
The block size was increased to a 4 Kbyte minimum, improving throughput. This reduced the
number of data blocks necessary to store a file, and therefore the number of indirect blocks
needed to refer to the data blocks. The number of required indirect pointer blocks was further
reduced because they were also larger. For space efficiency with small files, each block could be
split into 1 Kbyte fragments.
Another performance feature of FFS was block interleaving: placing sequential file blocks on disk
with a spacing between them of one or more blocks [Doeppner 10]. These extra blocks gave the
kernel and the processor time to issue the next sequential file read. Without interleaving, the next
block might pass the (rotational) disk head before it is ready to issue the read, causing latency as
it waits for a full rotation.

