7.1

Terminology

For reference, memory-related terminology used in this chapter includes the following:
■

■

■

■

■

■

Main memory: Also referred to as physical memory, this describes the fast data storage area
of a computer, commonly provided as DRAM.
Virtual memory: An abstraction of main memory that is (almost) infinite and noncontended. Virtual memory is not real memory.
Resident memory: Memory that currently resides in main memory.
Anonymous memory: Memory with no file system location or path name. It includes the
working data of a process address space, called the heap.
Address space: A memory context. There are virtual address spaces for each process, and
for the kernel.
Segment: An area of virtual memory flagged for a particular purpose, such as for storing
executable or writeable pages.

■

Instruction text: Refers to CPU instructions in memory, usually in a segment.

■

OOM: Out of memory, when the kernel detects low available memory.

■

■

■

■

■

Page: A unit of memory, as used by the OS and CPUs. Historically it is either 4 or 8 Kbytes.
Modern processors have multiple page size support for larger sizes.
Page fault: An invalid memory access. These are normal occurrences when using ondemand virtual memory.
Paging: The transfer of pages between main memory and the storage devices.
Swapping: Linux uses the term swapping to refer to anonymous paging to the swap device
(the transfer of swap pages). In Unix and other operating systems, swapping is the transfer
of entire processes between main memory and the swap devices. This book uses the Linux
version of the term.
Swap: An on-disk area for paged anonymous data. It may be an area on a storage device,
also called a physical swap device, or a file system file, called a swap file. Some tools use the
term swap to refer to virtual memory (which is confusing and incorrect).

Other terms are introduced throughout this chapter. The Glossary includes basic terminology
for reference if needed, including address, buffer, and DRAM. Also see the terminology sections in
Chapters 2 and 3.

