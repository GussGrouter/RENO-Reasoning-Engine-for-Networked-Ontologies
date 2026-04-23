7.2.2 Paging

Paging is the movement of pages in and out of main memory, which are referred to as page-ins
and page-outs, respectively. It was first introduced by the Atlas Computer in 1962 [Corbató 68],
allowing:
■

Partially loaded programs to execute

■

Programs larger than main memory to execute

■

Efficient movement of programs between main memory and storage devices

These abilities are still true today. Unlike the earlier technique of swapping out entire programs,
paging is a fine-grained approach to managing and freeing main memory, since the page size
unit is relatively small (e.g., 4 Kbytes).
Paging with virtual memory (paged virtual memory) was introduced to Unix via BSD [Babaoglu 79]
and became the standard.
With the later addition of the page cache for sharing file system pages (see Chapter 8, File Systems),
two different types of paging became available: file system paging and anonymous paging.

File System Paging
File system paging is caused by the reading and writing of pages in memory-mapped files. This is
normal behavior for applications that use file memory mappings (mmap(2)) and on file systems
that use the page cache (most do; see Chapter 8, File Systems). It has been referred to as “good”
paging [McDougall 06a].
When needed, the kernel can free memory by paging some out. This is where the terminology
gets a bit tricky: if a file system page has been modified in main memory (called dirty), the pageout will require it to be written to disk. If, instead, the file system page has not been modified
(called clean), the page-out merely frees the memory for immediate reuse, since a copy already
exists on disk. Because of this, the term page-out means that a page was moved out of memory—
which may or may not have included a write to a storage device (you may see the term page-out
defined differently in other texts).

Anonymous Paging (Swapping)
Anonymous paging involves data that is private to processes: the process heap and stacks. It is
termed anonymous because it has no named location in the operating system (i.e., no file system
path name). Anonymous page-outs require moving the data to the physical swap devices or swap
files. Linux uses the term swapping to refer to this type of paging.
Anonymous paging hurts performance and has therefore been referred to as “bad” paging
[McDougall 06a]. When applications access memory pages that have been paged out, they block
on the disk I/O required to read them back to main memory.1 This is an anonymous page-in,

1

If faster storage devices are used as swap devices, such as 3D XPoint with sub 10 μs latency, swapping may not
be the same “bad” paging it once was, but rather become a simple way to intentionally extend main memory, one
with mature kernel support.

which introduces synchronous latency to the application. Anonymous page-outs may not affect
application performance directly, as they can be performed asynchronously by the kernel.
Performance is best when there is no anonymous paging (swapping). This can be achieved by
configuring applications to remain within the main memory available and by monitoring page
scanning, memory utilization, and anonymous paging, to ensure that there are no indicators of
a memory shortage.

