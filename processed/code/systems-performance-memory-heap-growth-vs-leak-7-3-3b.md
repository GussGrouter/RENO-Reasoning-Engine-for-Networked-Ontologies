7.3.3 (continued) — Heap growth

Heap Growth
A common source of confusion is the endless growth of heap. Is it a memory leak? For simple
allocators, a free(3) does not return memory to the operating system; rather, memory is kept to
serve future allocations. This means that the process resident memory can only grow, which is
normal. Methods for processes to reduce system memory use include:
■

■

Re-exec: Calling execve(2) to begin from an empty address space
Memory mapping: Using mmap(2) and munmap(2), which will return memory to the
system

Memory-mapped files are described in Chapter 8, File Systems, Section 8.3.10, Memory-Mapped
Files.
Glibc, commonly used on Linux, is an advanced allocator that supports an mmap mode of operation, as well as a malloc_trim(3) function to release free memory to the system. malloc_trim(3)
is automatically called by free(3) when the top-of-heap free memory becomes large,6 and frees it
using sbrk(2) syscalls.
